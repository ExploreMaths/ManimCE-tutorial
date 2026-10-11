#!/usr/bin/env python3
"""Convert content/chapters markdown into reStructuredText sources under docs/.

The chapter content dialect (:::demo / :::params / :::compare /
:::notice / :::exercise / :::inheritance) is rewritten into native reST
directives wherever possible:

  :::demo    -> .. demo:: <example> <Scene>   (custom: build-time source
                injection + video lookup; no native equivalent)
  :::params  -> .. container:: table-scroll + .. list-table::
  :::compare -> .. container:: table-scroll + .. list-table::
  :::notice warning|tip        -> .. admonition:: with class warning/tip
  :::notice version|deprecated -> .. admonition:: with a custom class
  :::exercise / :::answer      -> nested sphinx-design .. dropdown::
  :::inheritance               -> .. manimchain:: left-to-right chain

Level-2 headings matching the section's `covers` entries are followed by
a .. manimsig:: <Cover> block (auto signature from the installed manim,
skipped for names manim does not export).

Also generates docs/index.rst, docs/api-index.rst, docs/glossary.rst,
docs/api/*.rst (per-class tutorials: Chinese notes + inheritance chain +
signature table + autodoc reference), docs/api/index.rst and
docs/inheritance-graph.rst (auto-generated via the manim_inheritance
extension).
"""

from __future__ import annotations

import argparse
import inspect
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "docs" / "source" / "_extensions"))
from manim_inheritance import (
    API_GROUPS, _normalize_link, group_api_page, load_manim_classes,
)

NOTICE_DIRECTIVES = {"warning": "warning", "tip": "tip"}
NOTICE_CLASSES = {"version": "notice-version", "deprecated": "notice-deprecated"}

HEADING_CHARS = {1: "=", 2: "-", 3: "~", 4: "^"}


# --- inline markdown -> reST -------------------------------------------------
_INLINE_CODE_RE = re.compile(r"`([^`]*)`")
_MD_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")


# docutils refuses any inline-markup end-string directly followed by a CJK
# char (letter or full-width punctuation), rendering the whole construct as
# a crimson "problematic" span. Insert a narrow no-break space (which
# docutils treats as whitespace) so the markup closes cleanly; the NNBSP is
# visually negligible in CJK text.
_MARKUP_END_CJK_RE = re.compile(
    r"(``[^`]+``|\*\*[^*]+\*\*|`[^`]+ <[^`>]+>`__"
    r"|\*[^*\s](?:[^*]*[^*\s])?\*)"
    r"(?=[\u2e80-\u9fff\uf900-\ufaff\uff00-\uffef])"
)


# The symmetric start-string problem: markup directly *preceded* by a CJK
# char is not recognized either — docutils stays silent and the asterisks
# or backticks are rendered literally ("中文**加粗**中文" never bolds).
# A narrow no-break space before the start-string fixes recognition and is
# visually negligible. (Inline links are exempt: their start-string is
# lenient and parses fine against a CJK char.)
_MARKUP_START_CJK_RE = re.compile(
    r"(?<=[\u2e80-\u9fff\uf900-\ufaff\uff00-\uffef])"
    r"(\*\*[^*]+\*\*|\*[^*\s](?:[^*]*[^*\s])?\*|``[^`]+``)"
)


def inline_md_to_rst(text: str) -> str:
    """Convert the markdown inline idioms used in chapter prose."""
    # codespans first: a generated `text <url>` link below must keep its
    # single backticks (converting links first would wrap them in ``...``).
    # GFM-style bold with padding spaces inside the delimiters
    # ("** 静态快照 **") is invalid reST — trim the inner whitespace.
    text = re.sub(r"\*\*[ \t]+([^*]*\S)[ \t]+\*\*", r"**\1**", text)
    text = _INLINE_CODE_RE.sub(r"``\1``", text)
    text = _MD_LINK_RE.sub(r"`\1 <\2>`__", text)
    text = _MARKUP_END_CJK_RE.sub(lambda m: m.group(1) + " ", text)
    text = _MARKUP_START_CJK_RE.sub(lambda m: " " + m.group(1), text)
    return text


def convert_body(
    body: list[str],
    link_maps: dict[str, str] | None = None,
    const_urls: dict[str, str] | None = None,
) -> list[str]:
    """Convert fenced code blocks and md pipe tables inside a block body
    (:::demo / :::notice / :::exercise); everything else goes inline."""
    out: list[str] = []
    i = 0
    while i < len(body):
        s = body[i].strip()
        if s.startswith("```"):
            lang = s[3:].strip() or "text"
            code: list[str] = []
            i += 1
            while i < len(body) and body[i].strip() != "```":
                code.append(body[i])
                i += 1
            i += 1  # closing fence
            if out and out[-1].strip():
                out.append("")
            out.append(f".. code-block:: {lang}")
            out.append("")
            out.extend(indent(code))
            continue
        if s.startswith("|"):
            tbl: list[str] = []
            while i < len(body) and body[i].strip().startswith("|"):
                tbl.append(body[i])
                i += 1
            if out and out[-1].strip():
                out.append("")
            out.extend(emit_table(tbl, link_maps, const_urls))
            continue
        out.append(inline_md_to_rst(body[i]))
        i += 1
    return out


def strip_first_codespan(text: str) -> str:
    return re.sub(r"`[^`]*`", "", text, count=1).strip()


def rst_section_id(text: str) -> str:
    """Approximate docutils' section id (used to detect covers whose heading
    text would not already produce the cover's anchor)."""
    t = re.sub(r"`([^`]*)`", r"\1", text.strip()).lower()
    t = re.sub(r"[^\w\u4e00-\u9fff\- ]", "", t, flags=re.UNICODE)
    t = re.sub(r"[\s_]+", "-", t)
    return t.strip("-")


def display_width(text: str) -> int:
    """docutils counts CJK/full-width characters as width 2 for title rules."""
    return sum(2 if ord(c) > 0x2E7F else 1 for c in text)


def rst_heading(level: int, text: str) -> list[str]:
    t = inline_md_to_rst(text)
    ch = HEADING_CHARS[level]
    return [t, ch * max(display_width(t), 3)]


def indent(lines: list[str], spaces: int = 3) -> list[str]:
    pad = " " * spaces
    return [pad + l if l.strip() else l for l in lines]


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


def parse_pipe_table(body: list[str]) -> list[list[str]]:
    """Split single-line pipe-table rows into cells (unescaping \\|)."""
    rows: list[list[str]] = []
    for line in body:
        s = line.strip()
        if not s.startswith("|"):
            continue
        if re.match(r"^\|[\s\-|:]+\|$", s):  # separator row
            continue
        cells = re.split(r"(?<!\\)\|", s)
        cells = [c.strip().replace("\\|", "|") for c in cells]
        rows.append(cells[1:-1] if cells and not cells[0] and not cells[-1] else cells)
    return rows


# --- table-cell cross references ----------------------------------------------
# Official v0.21.0 API pages that document constants and predefined colors.
_OFFICIAL_BASE = "https://docs.manim.community/en/v0.21.0"
_CONST_PAGE = f"{_OFFICIAL_BASE}/reference/manim.constants.html"
_COLOR_PAGE = f"{_OFFICIAL_BASE}/reference/manim.utils.color.manim_colors.html"

_TOKEN_RE = re.compile(r"[A-Za-z_]\w*")
# reST literals and inline references already emitted by inline_md_to_rst:
# tokens inside them must not be linkified a second time.
_RST_SPAN_RE = re.compile(r"``[^`\n]*``|`[^`\n]+`__?")


def _const_urls() -> dict[str, str]:
    """UPPER_CASE manim namespace values -> official docs URL (lazy, cached)."""
    global _CONST_URLS
    if _CONST_URLS is not None:
        return _CONST_URLS
    urls: dict[str, str] = {}
    try:
        import manim
        import manim.constants as _mc
        from manim.utils.color import manim_colors as _colors
    except Exception:  # noqa: BLE001 - manim optional at build time
        _CONST_URLS = {}
        return _CONST_URLS
    for name in dir(manim):
        if not re.fullmatch(r"[A-Z][A-Z0-9_]*", name):
            continue
        value = getattr(manim, name)
        if callable(value) or isinstance(value, type):
            continue
        if hasattr(_colors, name):
            urls[name] = _COLOR_PAGE
        elif hasattr(_mc, name):
            urls[name] = f"{_CONST_PAGE}#manim.constants.{name}"
    # Typing aliases (Point3DLike, Vector3D, ...) and the color type aliases
    # (ParsableManimColor, ...): documented on their own official module
    # pages. Imported utility names (np, Callable, ...) are excluded.
    try:
        import manim.typing as _mt
        import manim.utils.color.core as _mcc
    except Exception:  # noqa: BLE001
        pass
    else:
        imported = {
            "Any", "Callable", "ClassVar", "Final", "Hashable", "Iterable",
            "Literal", "Mapping", "MutableMapping", "NamedTuple", "NewType",
            "Optional", "PathLike", "Protocol", "Sequence", "TYPE_CHECKING",
            "TypeAlias", "TypeVar", "Union", "annotations", "cast", "np",
            "npt", "overload", "runtime_checkable",
        }
        for name in dir(_mt):
            if not name.startswith("_") and name not in imported:
                urls.setdefault(
                    name,
                    f"{_OFFICIAL_BASE}/reference/manim.typing.html"
                    f"#manim.typing.{name}",
                )
        for name in ("HSV", "ManimColor", "ParsableManimColor", "RGBA",
                     "RandomColorGenerator"):
            if hasattr(_mcc, name):
                urls.setdefault(
                    name,
                    f"{_OFFICIAL_BASE}/reference/manim.utils.color.core.html"
                    f"#manim.utils.color.core.{name}",
                )
    _CONST_URLS = urls
    return urls


_CONST_URLS: dict[str, str] | None = None


def linkify_rst(
    text: str,
    link_maps: dict[str, str] | None = None,
    const_urls: dict[str, str] | None = None,
) -> str:
    """Turn known class names / manim constants into reference links.

    Classes resolve to the local docs (chapter tutorial preferred, api/
    page fallback — same targets as the inheritance graphs); constants
    resolve to the official v0.21.0 reference. Existing reST literals are
    linked whole when their content is a single known name; other tokens
    are linked only outside literals and existing inline references.
    """
    link_maps = link_maps or {}

    def link_token(tok: str) -> str:
        url = link_maps.get(tok) or const_urls.get(tok)
        return f"`{tok} <{url}>`__" if url else tok

    out: list[str] = []
    pos = 0
    for m in _RST_SPAN_RE.finditer(text):
        seg = text[pos:m.start()]
        out.append(_TOKEN_RE.sub(lambda t: link_token(t.group(0)), seg))
        span = m.group(0)
        if span.startswith("``"):
            inner = span[2:-2]
            url = link_maps.get(inner) or const_urls.get(inner)
            out.append(f"`{inner} <{url}>`__" if url else span)
        else:  # inline reference from inline_md_to_rst — leave untouched
            out.append(span)
        pos = m.end()
    out.append(_TOKEN_RE.sub(lambda t: link_token(t.group(0)), text[pos:]))
    result = "".join(out)
    # docutils rejects an inline-reference end-string directly followed by
    # an ASCII word char or a markup-sensitive char ("Inline interpreted
    # text or phrase reference start-string without end-string" -> a
    # crimson .problematic span). A narrow no-break space (treated as
    # whitespace, visually negligible) after `__ keeps the reference
    # parseable, e.g. `ManimColor </...>`__('#000000').
    return re.sub(r"`__(?=[A-Za-z0-9_(<*=%])", "`__\u202f", result)


def emit_table(
    body: list[str],
    link_maps: dict[str, str] | None = None,
    const_urls: dict[str, str] | None = None,
) -> list[str]:
    rows = parse_pipe_table(body)
    out = [".. container:: table-scroll", "", "   .. list-table::", "      :header-rows: 1", ""]
    for row in rows:
        for idx, cell in enumerate(row):
            prefix = "      * - " if idx == 0 else "        - "
            out.append(prefix + linkify_rst(inline_md_to_rst(cell), link_maps, const_urls))
    return out


def emit_graphviz(dot: list[str]) -> list[str]:
    return [".. graphviz::", ""] + indent(dot)


def emit_chain(dot: list[str]) -> list[str]:
    """Chain diagram rendered like the full inheritance graph: inline SVG,
    clickable links, official Manim style (no <object> frame / double border)."""
    return [".. manimchain::", ""] + indent(dot)


def _dot_quote(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def build_link_maps(classes: dict[str, type], content_dir: Path) -> dict[str, str]:
    """Class name -> absolute doc URL, chapter tutorial preferred over the
    api/ page (same resolution as the full inheritance graph)."""
    links: dict[str, str] = {}
    for n, obj in classes.items():
        gid = group_api_page(getattr(obj, "__module__", ""))
        links[n] = f"/api/{gid}.html#{n.lower()}"
    inheritance = content_dir / "inheritance.json"
    if inheritance.is_file():
        data = json.loads(inheritance.read_text(encoding="utf-8"))
        for node in data.get("nodes", []):
            if node.get("name") and node.get("link"):
                links[node["name"]] = _normalize_link(node["link"])
    return links


def chain_dot(chain: list[str], links: dict[str, str]) -> list[str]:
    dot = ["digraph G {", *_CHAIN_DOT_ATTRS]
    for name in chain:
        link = links.get(name)
        url = f', URL="{_dot_quote(link)}"' if link else ""
        dot.append(f'  "{_dot_quote(name)}" [label="{_dot_quote(name)}"{url}];')
    dot += [f'  "{_dot_quote(chain[i-1])}" -> "{_dot_quote(chain[i])}";'
            for i in range(1, len(chain))]
    dot.append("}")
    return dot


def convert_section(
    text: str, covers: list[str], link_maps: dict[str, str] | None = None,
    class_names: set[str] | None = None,
    const_urls: dict[str, str] | None = None,
) -> tuple[str, set[str]]:
    link_maps = link_maps or {}
    class_names = class_names or set()
    current_cover: str | None = None  # last seen cover heading
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
            lang = s[3:].strip() or "text"
            code: list[str] = []
            i += 1
            while i < len(lines) and lines[i].strip() != "```":
                code.append(lines[i])
                i += 1
            i += 1  # closing fence
            # a handwritten "Name(" signature fence right under a cover
            # heading duplicates the autoclass signature — drop it
            if (current_cover and current_cover in class_names
                    and len(code) > 1 and code[0].strip() == f"{current_cover}("):
                blank()
                continue
            blank()
            out.append(f".. code-block:: {lang}")
            out.append("")
            out.extend(indent(code))
            blank()
            continue
        if s.startswith(":::"):
            kind, _, rest = s[3:].partition(" ")
            kind = kind.strip()
            rest = rest.strip()
            if kind in ("params", "compare"):
                body, i = collect_until_close(lines, i + 1)
                blank()
                out.extend(emit_table(body, link_maps, const_urls))
                blank()
                continue
            if kind == "demo":
                body, i = collect_until_close(lines, i + 1)
                blank()
                out.append(f".. demo:: {rest}")
                out.append("")
                out.extend(indent(convert_body(body, link_maps, const_urls)))
                blank()
                continue
            if kind == "notice":
                body, i = collect_until_close(lines, i + 1)
                title = body[0].strip() if body else ""
                content_lines = body[1:] if len(body) > 1 else []
                blank()
                cls = NOTICE_DIRECTIVES.get(rest) or NOTICE_CLASSES.get(rest) or f"notice-{rest}"
                out.append(f".. admonition:: {inline_md_to_rst(title) or rest}")
                out.append(f"   :class: {cls}")
                out.append("")
                out.extend(indent(convert_body(content_lines, link_maps, const_urls)))
                blank()
                continue
            if kind == "exercise":
                question, answer, i = parse_exercise(lines, i + 1)
                blank()
                out.append(".. dropdown:: ✏️ 练习")
                out.append("")
                out.extend(indent(convert_body(question, link_maps, const_urls)))
                if any(l.strip() for l in answer):
                    out.append("")
                    out.append("   .. dropdown:: ✅ 参考答案")
                    out.append("")
                    out.extend(indent(convert_body(answer, link_maps, const_urls), 6))
                blank()
                continue
            if kind == "inheritance":
                body, i = collect_until_close(lines, i + 1)
                chain: list[str] = []
                for bline in body:
                    for piece in re.split(r"→|->", bline):
                        piece = piece.strip()
                        if piece:
                            chain.append(piece)
                blank()
                # Homepage inheritance-graph style: inline SVG, linked nodes.
                out.extend(emit_chain(chain_dot(chain, link_maps)))
                blank()
                continue
            out.append(line)
            i += 1
            continue
        if s.startswith("|"):
            tbl: list[str] = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                tbl.append(lines[i])
                i += 1
            blank()
            out.extend(emit_table(tbl, link_maps, const_urls))
            blank()
            continue
        m = re.match(r"^(#{1,4})\s+(.+?)\s*$", line)
        if m:
            level = len(m.group(1))
            text_ = m.group(2).strip()
            if level == 2:
                stripped = strip_first_codespan(text_)
                if stripped in covers:
                    matched.add(stripped)
                    if rst_section_id(text_) != stripped.lower():
                        # section id would not match the cover name:
                        # pin an explicit target with the exact id.
                        blank()
                        out.append(f".. _{stripped}:")
                        out.append("")
                    blank()
                    out.extend(rst_heading(2, text_))
                    out.append("")
                    current_cover = stripped
                    if stripped in class_names:
                        # autodoc-style signature (class docstring is dropped
                        # by the autodoc handler; no :members: so methods
                        # stay undocumented here — they live on api/ pages).
                        out.append(f".. autoclass:: manim.{stripped}")
                        out.append("   :noindex:")
                        out.append("")
                    else:
                        # auto-generated signature line (skipped by the
                        # directive for names manim does not export:
                        # methods, flags, ...).
                        out.append(f".. manimsig:: {stripped}")
                        out.append("")
                    i += 1
                    continue
            blank()
            out.extend(rst_heading(level, text_))
            out.append("")
            current_cover = None
            i += 1
            continue
        if s:
            out.append(inline_md_to_rst(line))
        else:
            out.append("")
        i += 1

    while out and not out[-1].strip():
        out.pop()
    return "\n".join(out) + "\n", matched


def ref(part: str, section: str, anchor: str | None = None) -> str:
    base = f"chapters/{part}/{section}.rst"
    return f"{base}#{anchor}" if anchor else base


def rst_title(title: str, ch: str = "=") -> list[str]:
    w = max(display_width(title), 3)
    return [ch * w, title, ch * w]


def build_index(config: dict, flat: list[tuple[dict, dict]], class_count: int) -> str:
    total = len(flat)
    parts = config["parts"]
    L: list[str] = rst_title("ManimCE 中文教程") + [
        "",
        "基于 **Manim Community v0.21.0** 的系统性中文教程：从安装到进阶，"
        "每个 API 配中文讲解、可交互示例视频与源码，全部例子可一键复现。",
        "",
        ".. raw:: html",
        "",
        f'   <div id="home-progress" data-total="{total}"></div>',
        "",
        ".. grid:: 1 2 2 2",
        "   :gutter: 2",
        "",
    ]
    cards = [
        ("🚀 开始学习",
         f"chapters/{flat[0][0]['id']}/{flat[0][1]['id']}",
         f"**{parts[0]['title']}**：{flat[0][1]['title']}"),
        ("📚 API 索引", "api-index",
         "全部 259 个类与函数，按字母分组，直达中文讲解。"),
        ("🧪 API 参考（全类）", "api/index",
         f"{class_count} 个公开类逐一精讲：中文说明、继承链、参数表、上手示例与 autodoc 参考。"),
        ("🧬 继承关系图", "inheritance-graph",
         f"全部 {class_count} 个公开类的继承全景图，构建时自动遍历生成，节点可点击跳转。"),
        ("📖 术语表", "glossary",
         "Mobject、VMobject 等核心术语的中文释义。"),
    ]
    for title, link, body in cards:
        L += [
            f"   .. grid-item-card:: {title}",
            f"      :link: {link}",
            "      :link-type: doc",
            "",
            "      " + body,
            "",
        ]
    for part in parts:
        L += [
            ".. toctree::",
            "   :maxdepth: 1",
            "   :hidden:",
            f"   :caption: {part['title']}",
            "",
        ]
        for s in part["sections"]:
            L.append(f"   chapters/{part['id']}/{s['id']}")
        L.append("")
    L += [
        ".. toctree::",
        "   :maxdepth: 1",
        "   :hidden:",
        "   :caption: 站内",
        "",
        "   api-index",
        "   inheritance-graph",
        "   glossary",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   :hidden:",
        "   :caption: API 参考（全类）",
        "",
        "   api/index",
        "",
    ]
    return "\n".join(L)


def build_api_index(config: dict) -> str:
    items: list[tuple[str, str]] = []  # (name, section path)
    for part in config["parts"]:
        for s in part["sections"]:
            for c in s.get("covers", []):
                items.append((c, f"{part['id']}/{s['id']}"))
    groups: dict[str, list[tuple[str, str]]] = {}
    for name, sec in items:
        groups.setdefault(name[:1].upper(), []).append((name, sec))
    L = rst_title("API 索引") + [
        "",
        "按字母分组，点击进入对应章节的中文讲解。",
        "",
    ]
    for letter in sorted(groups):
        L += [letter, "-" * len(letter), ""]
        for name, sec in sorted(groups[letter]):
            kind = "class" if name[:1].isupper() else "函数"
            L.append(f"- `{name} <chapters/{sec}.html#{name.lower()}>`__\u202f（{kind}）")
        L.append("")
    return "\n".join(L)


def build_glossary(
    glossary: list[dict],
    link_maps: dict[str, str] | None = None,
    const_urls: dict[str, str] | None = None,
) -> str:
    L = rst_title("术语表") + ["", ".. container:: table-scroll", "",
                               "   .. list-table::", "      :header-rows: 1", ""]
    # explicit header row — without it the first entry would be rendered
    # as the table head (bold, centered) instead of a body row
    L += ["      * - 术语", "        - 中文", "        - 说明"]
    for it in glossary:
        term = linkify_rst(f"``{it['term']}``", link_maps, const_urls)
        L.append(f"      * - {term}")
        L.append(f"        - {it['zh']}")
        L.append(f"        - {it['desc']}")
    L.append("")
    return "\n".join(L)


# --- per-class tutorial pages ------------------------------------------------
def _signature_params(obj: type) -> list[tuple[str, str]]:
    """(name, default-or-annotation text) for __init__, skipping self/*args."""
    try:
        sig = inspect.signature(obj.__init__)
    except (TypeError, ValueError):
        return []
    rows: list[tuple[str, str]] = []
    for p in sig.parameters.values():
        if p.name == "self" or p.kind in (p.VAR_POSITIONAL, p.VAR_KEYWORD):
            continue
        if p.default is p.empty:
            default = "—"
        else:
            r = repr(p.default)
            default = r if len(r) <= 30 else r[:27] + "…"
        if p.annotation is not p.empty:
            ann = getattr(p.annotation, "__name__", str(p.annotation))
            if len(ann) <= 24:
                default += f"，{ann}"
        # repr'd defaults may contain <class 'manim.camera.x_y.Y'> whose
        # angle brackets/underscores docutils would parse as inline markup;
        # wrap such defaults in a literal.
        if re.search(r"[<>`*_]", default):
            default = "``" + default.replace("\\", "\\\\") + "``"
        rows.append((p.name, default))
    return rows


def _inheritance_chain(name: str, classes: dict[str, type]) -> list[str]:
    """Base -> ... -> class chain through documented manim ancestors."""
    if name not in classes:
        return []
    chain = [n for n in (c.__name__ for c in inspect.getmro(classes[name])) if n in classes]
    return list(reversed(chain))


# Same look as the manim_extensions docs inheritance diagrams
# (ExploreMaths/manim_extensions conf.py: sphinx.ext.inheritance_diagram
# attrs mapped to raw DOT, plus its manim-class node colors).
_CHAIN_DOT_ATTRS = (
    '  graph [rankdir=LR, bgcolor="transparent", splines=spline, concentrate=true, '
    'size="", nodesep="0.15", ranksep="0.3"];',
    '  node  [shape=box, style="filled", penwidth=0, width=0.05, height=0.05, '
    'margin=0.05, fillcolor="#EBF5FB", fontcolor="#1A5276"];',
    '  edge  [penwidth=1];',
)


def build_class_tutorial(
    name: str, classes: dict[str, type], notes: dict,
    link_maps: dict[str, str] | None = None,
    const_urls: dict[str, str] | None = None,
) -> list[str]:
    """One class entry: Chinese notes + chain + params + example + autodoc."""
    obj = classes[name]
    note = notes.get(name, {})
    L: list[str] = [name, "-" * max(len(name), 3), ""]
    if note.get("zh"):
        L += [note["zh"], ""]
    chain = _inheritance_chain(name, classes)
    if len(chain) > 1:
        L += ["继承关系", "~~~~~~~~", ""]
        L += emit_chain(chain_dot(chain, link_maps or {}))
        L.append("")
    params = _signature_params(obj)
    if params:
        L += ["参数", "~~~~", "", ".. container:: table-scroll", "",
              "   .. list-table::", "      :header-rows: 1", ""]
        # explicit header row — without it the first parameter would be
        # rendered as the table head instead of a body row
        L += ["      * - 参数", "        - 默认值"]
        for pname, default in params:
            L.append(f"      * - ``{pname}``")
            L.append(f"        - {linkify_rst(default, link_maps, const_urls)}")
        L.append("")
    if note.get("ex"):
        L += ["快速上手", "~~~~~~~~", "", ".. code-block:: python", ""]
        L += indent(note["ex"].split("\n"))
        L.append("")
    L += ["API 文档", "~~~~~~~~", "", f".. autoclass:: manim.{name}", "   :members:", ""]
    return L


def build_api_pages(
    classes: dict[str, type], notes: dict, docs: Path,
    link_maps: dict[str, str] | None = None,
    const_urls: dict[str, str] | None = None,
) -> dict[str, str]:
    """Write docs/api/<group>.rst (per-class tutorials), docs/api/index.rst
    and docs/_api_map.json (class name -> api page anchor) used by the
    manim-inheritance directive for node links. Returns the api map."""
    groups: dict[str, list[str]] = {gid: [] for gid, _t, _p in API_GROUPS}
    for name, obj in sorted(classes.items()):
        groups[group_api_page(getattr(obj, "__module__", ""))].append(name)

    api_map: dict[str, str] = {}
    used: list[tuple[str, str, int]] = []  # (gid, title, count)
    for gid, title, _pred in API_GROUPS:
        names = groups[gid]
        if not names:
            continue
        used.append((gid, title, len(names)))
        L = rst_title(f"API 参考：{title}") + [
            "",
            f"共 **{len(names)}** 个类，按字母排序。每个类含中文说明、继承链、"
            "参数表与上手示例，API 文档由 autodoc 从 manim v0.21.0 源码自动生成；"
            "带完整中文精讲的类见 `API 索引 <../api-index.html>`__。",
            "",
        ]
        for n in names:
            api_map[n] = f"/api/{gid}.html#{n.lower()}"
            L += build_class_tutorial(n, classes, notes, link_maps, const_urls)
        page = docs / "api" / f"{gid}.rst"
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text("\n".join(L), encoding="utf-8")

    total = sum(c for _g, _t, c in used)
    L = rst_title("API 参考（全类）") + [
        "",
        f"Manim Community v0.21.0 全部 **{total}** 个公开类，按模块分组。"
        "每个类一页式教程：中文说明、继承关系、参数表、快速上手示例，"
        "并附 autodoc 自动生成的完整 API 文档。",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "",
    ]
    L += [f"   {gid}" for gid, _t, _c in used]
    L += ["", ""]
    (docs / "api" / "index.rst").write_text("\n".join(L), encoding="utf-8")
    (docs / "_api_map.json").write_text(
        json.dumps(api_map, ensure_ascii=False, indent=1), encoding="utf-8"
    )
    return api_map


def build_inheritance_graph_page(class_count: int) -> str:
    # The DOT itself is produced at Sphinx build time by the
    # manim-inheritance directive (docs/source/_extensions/manim_inheritance.py), which
    # auto-enumerates the installed manim and resolves node links to
    # chapter anchors / api pages.
    return "\n".join(rst_title("继承关系图") + [
        "",
        f"Manim Community v0.21.0 全部 **{class_count}** 个公开类的继承全景图，"
        "构建时自动遍历生成。点击节点：有中文精讲的类跳转到对应教程章节，"
        "其余跳转到 `API 参考 <api/index.html>`__ 中的教程条目。",
        "",
        ".. manim-inheritance::",
        "",
    ])


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--content", default="content")
    ap.add_argument("--docs", default="docs/source")
    args = ap.parse_args()

    content_dir = Path(args.content)
    docs = Path(args.docs)
    config = json.loads((content_dir / "site.config.json").read_text(encoding="utf-8"))

    flat = [(p, s) for p in config["parts"] for s in p["sections"]]
    classes = load_manim_classes()
    if not classes:
        print("WARNING: manim not importable; api pages and full graph skipped",
              file=sys.stderr)

    notes_path = content_dir / "class-notes.json"
    notes = (json.loads(notes_path.read_text(encoding="utf-8"))
             if notes_path.is_file() else {})

    link_maps = build_link_maps(classes, content_dir)
    const_urls = _const_urls()
    chapters_root = content_dir / "chapters"
    out_root = docs / "chapters"
    warnings: list[str] = []
    converted = 0
    for part, section in flat:
        md_path = chapters_root / part["id"] / f"{section['id']}.md"
        dest = out_root / part["id"] / f"{section['id']}.rst"
        if not md_path.is_file():
            warnings.append(f"missing md: {part['id']}/{section['id']}")
            continue
        covers = section.get("covers", [])
        text, matched = convert_section(
            md_path.read_text(encoding="utf-8"), covers, link_maps,
            set(classes), const_urls)
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")
        converted += 1
        missing = [c for c in covers if c not in matched]
        if missing:
            warnings.append(f"MISSING covers {part['id']}/{section['id']}: {', '.join(missing)}")

    (docs / "index.rst").write_text(build_index(config, flat, len(classes)), encoding="utf-8")
    (docs / "api-index.rst").write_text(build_api_index(config), encoding="utf-8")
    glossary = json.loads((content_dir / "glossary.json").read_text(encoding="utf-8"))
    (docs / "glossary.rst").write_text(
        build_glossary(glossary, link_maps, const_urls), encoding="utf-8")
    build_api_pages(classes, notes, docs, link_maps, const_urls)
    (docs / "inheritance-graph.rst").write_text(
        build_inheritance_graph_page(len(classes)), encoding="utf-8"
    )

    print(f"converted {converted}/{len(flat)} sections -> {out_root}")
    for w in warnings:
        print(f"WARNING: {w}", file=sys.stderr)
    return 1 if any(w.startswith("MISSING") for w in warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
