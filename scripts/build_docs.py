#!/usr/bin/env python3
"""Convert content/chapters markdown into MyST sources under docs/.

Reads the same content dialect as build_content.py (:::demo / :::params /
:::compare / :::notice / :::exercise / :::inheritance) and rewrites it into
MyST + the custom directives provided by docs/_ext/manim_tutorial.py:

  :::demo    -> ```{demo} <example> <Scene>```
  :::params  -> ```{params}```   (pipe table kept as directive content)
  :::compare -> ```{compare}```
  :::notice warning|tip        -> ```{warning} / {tip}```
  :::notice version|deprecated -> ```{admonition}``` with a custom class
  :::exercise / :::answer      -> nested sphinx-design ```{dropdown}```
  :::inheritance               -> ```{inheritance}```

Level-2 headings matching the section's `covers` entries get an explicit
MyST target ``(CoverName)=`` above them so API links have stable anchors.

Also generates docs/index.md, docs/api-index.md, docs/glossary.md,
docs/inheritance-graph.md and docs/_extra/_redirects (old-route redirects).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

NOTICE_DIRECTIVES = {"warning": "warning", "tip": "tip"}
NOTICE_CLASSES = {"version": "notice-version", "deprecated": "notice-deprecated"}


def strip_first_codespan(text: str) -> str:
    return re.sub(r"`[^`]*`", "", text, count=1).strip()


def myst_slug(text: str) -> str:
    """MyST auto heading anchor: lowercase, drop punctuation, spaces -> hyphens."""
    t = re.sub(r"`([^`]*)`", r"\1", text.strip()).lower()
    t = re.sub(r"[^\w\u4e00-\u9fff\- ]", "", t, flags=re.UNICODE)
    t = re.sub(r"[\s_]+", "-", t)
    return t.strip("-")


def collect_until_close(lines: list[str], start: int) -> tuple[list[str], int]:
    body: list[str] = []
    i = start
    while i < len(lines):
        if lines[i].strip() == ":::":
            return body, i + 1
        body.append(lines[i])
        i += 1
    return body, i


def parse_exercise(lines: list[str], start: int) -> tuple[list[str], list[str], int]:
    question: list[str] = []
    answer: list[str] = []
    i = start
    in_answer = False
    closed = False
    while i < len(lines):
        s = lines[i].strip()
        if not in_answer and s == ":::answer":
            in_answer = True
            i += 1
            continue
        if in_answer and s == ":::":
            closed = True
            i += 1
            break
        (answer if in_answer else question).append(lines[i])
        i += 1
    if closed and i < len(lines) and lines[i].strip() == ":::":
        i += 1
    return question, answer, i


def convert_section(text: str, covers: list[str]) -> tuple[str, set[str]]:
    lines = text.split("\n")
    matched: set[str] = set()
    out: list[str] = []
    i = 0
    if lines and lines[0].strip() == "---":
        j = 1
        while j < len(lines) and lines[j].strip() != "---":
            j += 1
        i = j + 1

    def blank() -> None:
        if out and out[-1].strip():
            out.append("")

    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if s.startswith("```"):
            out.append(line)
            i += 1
            while i < len(lines):
                out.append(lines[i])
                if lines[i].strip().startswith("```"):
                    i += 1
                    break
                i += 1
            continue
        if s.startswith(":::"):
            kind, _, rest = s[3:].partition(" ")
            kind = kind.strip()
            rest = rest.strip()
            if kind in ("params", "compare"):
                body, i = collect_until_close(lines, i + 1)
                blank()
                out.append(f"```{{{kind}}}")
                out.extend(body)
                out.append("```")
                blank()
                continue
            if kind == "demo":
                body, i = collect_until_close(lines, i + 1)
                blank()
                out.append(f"```{{demo}} {rest}")
                out.extend(body)
                out.append("```")
                blank()
                continue
            if kind == "notice":
                body, i = collect_until_close(lines, i + 1)
                title = body[0].strip() if body else ""
                content_lines = body[1:] if len(body) > 1 else []
                blank()
                cls = NOTICE_DIRECTIVES.get(rest) or NOTICE_CLASSES.get(rest) or f"notice-{rest}"
                out.append(f"```{{admonition}} {title or rest}")
                out.append(f":class: {cls}")
                out.append("")
                out.extend(content_lines)
                out.append("```")
                blank()
                continue
            if kind == "exercise":
                question, answer, i = parse_exercise(lines, i + 1)
                blank()
                # Colon fences: nested ``` code blocks inside answers cannot
                # close a colon-fence dropdown early.
                out.append('::::{dropdown} ✏️ 练习')
                out.extend(question)
                if any(l.strip() for l in answer):
                    out.append("")
                    out.append(":::{dropdown} ✅ 参考答案")
                    out.extend(answer)
                    out.append(":::")
                out.append("::::")
                blank()
                continue
            if kind == "inheritance":
                body, i = collect_until_close(lines, i + 1)
                blank()
                out.append("```{inheritance}")
                out.extend(body)
                out.append("```")
                blank()
                continue
            out.append(line)
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.+?)\s*$", line)
        if m:
            level = len(m.group(1))
            text_ = m.group(2).strip()
            if level == 2:
                stripped = strip_first_codespan(text_)
                if stripped in covers:
                    matched.add(stripped)
                    if myst_slug(text_) != stripped.lower():
                        # auto heading anchor would not match the cover name:
                        # pin an explicit target with the exact id.
                        blank()
                        out.append(f"({stripped})=")
                    out.append(line)
                    # auto-generated signature line (skipped by the directive
                    # for names manim does not export: methods, flags, ...).
                    out.append("")
                    out.append(f"```{{manimsig}} {stripped}")
                    out.append("```")
                    i += 1
                    continue
        out.append(line)
        i += 1

    while out and not out[-1].strip():
        out.pop()
    return "\n".join(out) + "\n", matched


def ref(part: str, section: str, anchor: str | None = None) -> str:
    base = f"chapters/{part}/{section}.md"
    return f"{base}#{anchor}" if anchor else base


def build_index(config: dict, flat: list[tuple[dict, dict]]) -> str:
    total = len(flat)
    parts = config["parts"]
    L: list[str] = [
        "# ManimCE 中文教程",
        "",
        "基于 **Manim Community v0.21.0** 的系统性中文教程：从安装到进阶，"
        "每个 API 配中文讲解、可交互示例视频与源码，全部例子可一键复现。",
        "",
        '<div id="home-progress" data-total="%d"></div>' % total,
        "",
        "::::{grid} 1 2 2 2",
        ":gutter: 2",
        "",
    ]
    cards = [
        ("🚀 开始学习",
         ref(flat[0][0]['id'], flat[0][1]['id'])[:-3],
         f"**{parts[0]['title']}**：{flat[0][1]['title']}"),
        ("📚 API 索引", "api-index",
         "全部 259 个类与函数，按字母分组，直达中文讲解。"),
        ("🧬 继承关系图", "inheritance-graph",
         "教程涉及的核心类继承全景图，可筛选、可折叠、可点击跳转。"),
        ("📖 术语表", "glossary",
         "Mobject、VMobject 等核心术语的中文释义。"),
    ]
    for title, link, body in cards:
        L += [
            ":::{grid-item-card} " + title,
            f":link: {link}",
            ":link-type: doc",
            "",
            body,
            ":::",
            "",
        ]
    L += [
        "::::",
        "",
    ]
    for part in parts:
        L.append("```{toctree}")
        L.append(":maxdepth: 1")
        L.append(":hidden:")
        L.append(f":caption: {part['title']}")
        L.append("")
        for s in part["sections"]:
            L.append(f"chapters/{part['id']}/{s['id']}")
        L.append("```")
        L.append("")
    L.append("```{toctree}")
    L.append(":maxdepth: 1")
    L.append(":hidden:")
    L.append(":caption: 站内")
    L.append("")
    L.extend(["api-index", "inheritance-graph", "glossary"])
    L.append("```")
    L.append("")
    return "\n".join(L)


def build_api_index(config: dict) -> str:
    items: list[tuple[str, str]] = []  # (name, link)
    for part in config["parts"]:
        for s in part["sections"]:
            for c in s.get("covers", []):
                items.append((c, f"{part['id']}/{s['id']}"))
    groups: dict[str, list[tuple[str, str]]] = {}
    for name, sec in items:
        groups.setdefault(name[:1].upper(), []).append((name, sec))
    L = ["# API 索引", "", "按字母分组，点击进入对应章节的中文讲解。", ""]
    for letter in sorted(groups):
        L.append(f"## {letter}")
        L.append("")
        for name, sec in sorted(groups[letter]):
            kind = "class" if name[:1].isupper() else "函数"
            L.append(f"- [`{name}`]({ref_from_root(sec, name)})（{kind}）")
        L.append("")
    return "\n".join(L)


def ref_from_root(section_path: str, anchor: str) -> str:
    part, sec = section_path.split("/")
    # MyST/docutils normalizes explicit target names to lowercase ids.
    return f"chapters/{part}/{sec}.md#{anchor.lower()}"


def build_glossary(glossary: list[dict]) -> str:
    L = ["# 术语表", "", "| 术语 | 中文 | 说明 |", "| --- | --- | --- |"]
    for it in glossary:
        L.append(f"| `{it['term']}` | {it['zh']} | {it['desc']} |")
    L.append("")
    return "\n".join(L)


OLD_LINK_RE = re.compile(r"^/ch/([a-z0-9]+)/([a-z0-9-]+)#(.+)$")


def build_inheritance_graph_page(inheritance: dict) -> str:
    nodes = inheritance.get("nodes", [])
    for n in nodes:
        m = OLD_LINK_RE.match(n.get("link") or "")
        if m:
            part, sec, anchor = m.groups()
            n["link"] = f"/chapters/{part}/{sec}.html#{anchor.lower()}"
    data = json.dumps(nodes, ensure_ascii=False)
    L = [
        "# 继承关系图",
        "",
        "教程涉及的核心类继承全景图。节点可点击跳转到对应章节；"
        "带 `+` 角标的节点可以折叠/展开其子树。",
        "",
        "```{inheritance-graph}",
        f":nodes: {data}",
        "```",
        "",
    ]
    return "\n".join(L)


def build_redirects(flat: list[tuple[dict, dict]]) -> str:
    L = [
        "# Old Vue-router paths -> new Sphinx paths.",
        "/ch/*  /chapters/:splat.html  301",
        "/api  /api-index.html  301",
        "/glossary  /glossary.html  301",
        "",
    ]
    return "\n".join(L)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--content", default="content")
    ap.add_argument("--docs", default="docs")
    args = ap.parse_args()

    content_dir = Path(args.content)
    docs = Path(args.docs)
    config = json.loads((content_dir / "site.config.json").read_text(encoding="utf-8"))

    flat = [(p, s) for p in config["parts"] for s in p["sections"]]
    part_ids = {p["id"] for p in config["parts"]}

    chapters_root = content_dir / "chapters"
    out_root = docs / "chapters"
    warnings: list[str] = []
    converted = 0
    for part, section in flat:
        md_path = chapters_root / part["id"] / f"{section['id']}.md"
        dest = out_root / part["id"] / f"{section['id']}.md"
        if not md_path.is_file():
            warnings.append(f"missing md: {part['id']}/{section['id']}")
            continue
        covers = section.get("covers", [])
        text, matched = convert_section(md_path.read_text(encoding="utf-8"), covers)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        converted += 1
        missing = [c for c in covers if c not in matched]
        if missing:
            warnings.append(f"MISSING covers {part['id']}/{section['id']}: {', '.join(missing)}")

    (docs / "index.md").write_text(build_index(config, flat), encoding="utf-8")
    (docs / "api-index.md").write_text(build_api_index(config), encoding="utf-8")
    glossary = json.loads((content_dir / "glossary.json").read_text(encoding="utf-8"))
    (docs / "glossary.md").write_text(build_glossary(glossary), encoding="utf-8")
    inheritance = json.loads((content_dir / "inheritance.json").read_text(encoding="utf-8"))
    (docs / "inheritance-graph.md").write_text(
        build_inheritance_graph_page(inheritance), encoding="utf-8"
    )
    extra = docs / "_extra"
    extra.mkdir(parents=True, exist_ok=True)
    (extra / "_redirects").write_text(build_redirects(flat), encoding="utf-8")

    print(f"converted {converted}/{len(flat)} sections -> {out_root}")
    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)
    return 1 if any(w.startswith("MISSING") for w in warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
