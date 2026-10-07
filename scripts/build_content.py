#!/usr/bin/env python3
"""Build JSON content blocks from markdown chapter sources.

Reads content/chapters/<part>/<section>.md, parses the directive syntax
described in the repo docs, and emits one JSON file per section into
public/data/chapters/<part>/<section>.json, plus chapters.json,
search-index.json and api-index.json. Copies glossary.json and
inheritance.json verbatim from the content directory. The output lives
in public/ so both `vite dev` and `vite build` serve it at /data/.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

import markdown
import yaml

MD_EXTENSIONS = ["extra", "sane_lists"]

EXIT_OK = 0
EXIT_STRICT = 1
EXIT_ERROR = 2


# ---------------------------------------------------------------------------
# markdown helpers
# ---------------------------------------------------------------------------

def md_html(text: str) -> str:
    """Render a markdown fragment to HTML (block level)."""
    md = markdown.Markdown(extensions=MD_EXTENSIONS)
    return md.convert(text).strip()


def md_inline(text: str) -> str:
    """Render a markdown fragment to inline HTML (strips the <p> wrapper)."""
    html = md_html(text)
    m = re.fullmatch(r"<p>(.*)</p>", html, re.DOTALL)
    return m.group(1) if m else html


def slugify(text: str) -> str:
    """Slugify a heading: lowercase, keep CJK chars, spaces/underscores -> hyphens."""
    t = re.sub(r"`([^`]*)`", r"\1", text.strip()).lower()
    t = re.sub(r"[^\w\u4e00-\u9fff\- ]", "", t, flags=re.UNICODE)
    t = re.sub(r"[\s_]+", "-", t)
    return t.strip("-") or "section"


def strip_first_codespan(text: str) -> str:
    """Heading text with the first `code span` removed (used for covers matching)."""
    return re.sub(r"`[^`]*`", "", text, count=1).strip()


# ---------------------------------------------------------------------------
# table parsing
# ---------------------------------------------------------------------------

def parse_pipe_table(lines: list[str]) -> list[list[str]]:
    """Extract the first GFM pipe table from a list of lines."""
    rows: list[list[str]] = []
    for line in lines:
        s = line.strip()
        if s.startswith("|") and s.endswith("|"):
            rows.append([c.strip() for c in s.strip("|").split("|")])
        elif rows:
            break
    if len(rows) >= 2 and all(re.fullmatch(r":?-{2,}:?", c or "---") for c in rows[1]):
        rows.pop(1)
    return rows


# ---------------------------------------------------------------------------
# block parser
# ---------------------------------------------------------------------------

def collect_until_close(lines: list[str], start: int) -> tuple[list[str], int]:
    """Collect lines until a line that is exactly ':::'. Returns (body, next_index)."""
    body: list[str] = []
    i = start
    while i < len(lines):
        if lines[i].strip() == ":::":
            return body, i + 1
        body.append(lines[i])
        i += 1
    return body, i


def parse_demo_args(rest: str) -> tuple[str, str] | None:
    """Parse 'examples/ch02/circle_intro.py CircleIntro' -> ('ch02/circle_intro', 'CircleIntro')."""
    parts = rest.split()
    if len(parts) < 2:
        return None
    example = parts[0].replace("\\", "/")
    if example.startswith("examples/"):
        example = example[len("examples/"):]
    if example.endswith(".py"):
        example = example[:-3]
    return example, parts[1]


class SectionParser:
    def __init__(self, part: str, section: dict, examples_dir: Path, media_dir: Path):
        self.part = part
        self.section = section
        self.examples_dir = examples_dir
        self.media_dir = media_dir
        self.errors: list[str] = []
        self.matched_covers: set[str] = set()

    def parse(self, text: str) -> tuple[str | None, str | None, list[dict]]:
        lines = text.split("\n")
        i = 0
        fm_title: str | None = None
        if lines and lines[0].strip() == "---":
            j = 1
            while j < len(lines) and lines[j].strip() != "---":
                j += 1
            fm = yaml.safe_load("\n".join(lines[1:j])) or {}
            if isinstance(fm, dict) and fm.get("title"):
                fm_title = str(fm["title"])
            i = j + 1

        blocks: list[dict] = []
        buf: list[str] = []

        def flush() -> None:
            if buf:
                src = "\n".join(buf).strip("\n")
                if src.strip():
                    blocks.append({"type": "html", "html": md_html(src)})
                buf.clear()

        while i < len(lines):
            line = lines[i]
            s = line.strip()
            if s.startswith("```"):
                # Fenced code block: pass through verbatim (may contain '#' or ':::' lines).
                fence_marker = s
                buf.append(line)
                i += 1
                while i < len(lines):
                    buf.append(lines[i])
                    if lines[i].strip().startswith("```"):
                        i += 1
                        break
                    i += 1
                continue
            if s.startswith(":::"):
                flush()
                kind, _, rest = s[3:].partition(" ")
                kind = kind.strip()
                rest = rest.strip()
                if kind in ("params", "compare"):
                    body, i = collect_until_close(lines, i + 1)
                    block = self._parse_table_block(kind, body)
                    if block:
                        blocks.append(block)
                elif kind == "demo":
                    body, i = collect_until_close(lines, i + 1)
                    block = self._parse_demo(rest, body)
                    if block:
                        blocks.append(block)
                elif kind == "notice":
                    body, i = collect_until_close(lines, i + 1)
                    block = self._parse_notice(rest, body)
                    if block:
                        blocks.append(block)
                elif kind == "exercise":
                    block, i = self._parse_exercise(lines, i + 1)
                    if block:
                        blocks.append(block)
                elif kind == "inheritance":
                    body, i = collect_until_close(lines, i + 1)
                    blocks.append(self._parse_inheritance(body))
                else:
                    # Unknown container: keep the source line as plain text.
                    buf.append(line)
                    i += 1
                continue
            m = re.match(r"^(#{1,4})\s+(.+?)\s*$", line)
            if m:
                flush()
                level = len(m.group(1))
                text_ = m.group(2).strip()
                if level == 1:
                    self.heading_title = text_
                else:
                    blocks.append(self._parse_heading(level, text_))
                i += 1
                continue
            buf.append(line)
            i += 1
        flush()
        return fm_title, getattr(self, "heading_title", None), blocks

    def _parse_heading(self, level: int, text: str) -> dict:
        stripped = strip_first_codespan(text)
        covers = self.section.get("covers", [])
        if level == 2 and stripped in covers:
            hid = stripped
            self.matched_covers.add(stripped)
        else:
            hid = slugify(text)
        return {"type": "heading", "level": level, "id": hid, "text": text}

    def _parse_table_block(self, kind: str, body: list[str]) -> dict | None:
        rows = parse_pipe_table(body)
        if not rows:
            self.errors.append(
                f"{self.part}/{self.section['id']}: :::{kind} has no pipe table"
            )
            return None
        if kind == "params":
            header = [c.lower() for c in rows[0]]
            if header != ["name", "type", "default", "desc"]:
                self.errors.append(
                    f"{self.part}/{self.section['id']}: :::params header must be "
                    "| name | type | default | desc |"
                )
                return None
            parsed = [
                {
                    "name": md_inline(r[0]) if len(r) > 0 else "",
                    "type": md_inline(r[1]) if len(r) > 1 else "",
                    "default": md_inline(r[2]) if len(r) > 2 else "",
                    "desc": md_inline(r[3]) if len(r) > 3 else "",
                }
                for r in rows[1:]
            ]
            return {"type": "params", "rows": parsed}
        headers = [md_inline(c) for c in rows[0]]
        parsed_rows = [
            [md_inline(c) for c in r] for r in rows[1:]
        ]
        return {"type": "compare", "headers": headers, "rows": parsed_rows}

    def _parse_demo(self, rest: str, body: list[str]) -> dict | None:
        parsed = parse_demo_args(rest)
        if parsed is None:
            self.errors.append(
                f"{self.part}/{self.section['id']}: :::demo needs '<example.py> <SceneName>'"
            )
            return None
        example, scene = parsed
        src_path = self.examples_dir / f"{example}.py"
        if not src_path.is_file():
            self.errors.append(
                f"{self.part}/{self.section['id']}: demo references missing example "
                f"examples/{example}.py"
            )
            return None
        code = src_path.read_text(encoding="utf-8")
        basename = example.rsplit("/", 1)[-1]
        video_rel = f"{self.part}/{basename}__{scene}.mp4"
        video = (
            f"media/{video_rel}"
            if (self.media_dir / video_rel).is_file()
            else None
        )
        caption = md_html("\n".join(body)) if any(l.strip() for l in body) else ""
        return {
            "type": "demo",
            "example": example,
            "scene": scene,
            "caption": caption,
            "code": code,
            "video": video,
        }

    def _parse_notice(self, level: str, body: list[str]) -> dict | None:
        if level not in ("version", "deprecated", "warning", "tip"):
            self.errors.append(
                f"{self.part}/{self.section['id']}: unknown notice level '{level}'"
            )
            return None
        title = body[0].strip() if body else ""
        rest = "\n".join(body[1:]) if len(body) > 1 else ""
        return {
            "type": "notice",
            "level": level,
            "title": title,
            "html": md_html(rest) if rest.strip() else "",
        }

    def _parse_exercise(self, lines: list[str], start: int) -> tuple[dict | None, int]:
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
        # The answer container is nested: consume the exercise-closing ':::' too.
        if closed and i < len(lines) and lines[i].strip() == ":::":
            i += 1
        if not closed:
            self.errors.append(
                f"{self.part}/{self.section['id']}: :::answer / ::: not closed in exercise"
            )
        return (
            {
                "type": "exercise",
                "questionHtml": md_html("\n".join(question)) if any(
                    l.strip() for l in question
                ) else "",
                "answerHtml": md_html("\n".join(answer)) if any(
                    l.strip() for l in answer
                ) else "",
            },
            i,
        )

    def _parse_inheritance(self, body: list[str]) -> dict:
        chain: list[str] = []
        for line in body:
            for piece in re.split(r"→|->", line):
                piece = piece.strip()
                if piece:
                    chain.append(piece)
        return {"type": "inheritance", "chain": chain}


# ---------------------------------------------------------------------------
# build
# ---------------------------------------------------------------------------

def build(args: argparse.Namespace) -> int:
    content_dir = Path(args.content)
    config_path = content_dir / "site.config.json"
    config = json.loads(config_path.read_text(encoding="utf-8"))
    examples_dir = Path("examples")
    media_dir = Path(args.media_dir)
    out_dir = Path(args.out)
    chapters_out = out_dir / "chapters"

    errors: list[str] = []
    warnings: list[str] = []
    strict_warnings: list[str] = []
    search_items: dict[tuple[str, str], dict] = {}

    # Flatten section order for prev/next navigation.
    flat: list[tuple[dict, dict]] = []  # (part, section)
    for part in config["parts"]:
        for section in part["sections"]:
            flat.append((part, section))

    part_ids = {p["id"] for p in config["parts"]}

    # Unknown part dirs on disk (not listed in the config).
    chapters_root = content_dir / "chapters"
    if chapters_root.is_dir():
        for d in sorted(chapters_root.iterdir()):
            if d.is_dir() and d.name not in part_ids:
                errors.append(f"unknown part directory: chapters/{d.name}")

    total_sections = 0
    for idx, (part, section) in enumerate(flat):
        total_sections += 1
        part_id, section_id = part["id"], section["id"]
        md_path = chapters_root / part_id / f"{section_id}.md"
        path = f"/ch/{part_id}/{section_id}"

        if not md_path.is_file():
            # Unwritten chapters are expected during ramp-up: report, but only
            # genuinely inconsistent content (unknown part dirs, demos pointing
            # at missing examples, MISSING covers under --strict) is fatal.
            warnings.append(f"missing md file for config section: {part_id}/{section_id}")
            continue

        parser = SectionParser(part_id, section, examples_dir, media_dir)
        fm_title, heading_title, blocks = parser.parse(
            md_path.read_text(encoding="utf-8")
        )
        errors.extend(parser.errors)

        title = fm_title or heading_title or section["title"]

        prev = flat[idx - 1] if idx > 0 else None
        nxt = flat[idx + 1] if idx < len(flat) - 1 else None

        def nav_item(ps: tuple[dict, dict] | None) -> dict | None:
            if ps is None:
                return None
            p_, s_ = ps
            return {
                "part": p_["id"],
                "id": s_["id"],
                "title": s_["title"],
                "path": f"/ch/{p_['id']}/{s_['id']}",
            }

        doc = {
            "part": part_id,
            "id": section_id,
            "title": title,
            "partTitle": part["title"],
            "prev": nav_item(prev),
            "next": nav_item(nxt),
            "blocks": blocks,
        }
        dest = chapters_out / part_id / f"{section_id}.json"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(
            json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        # Coverage: covers entries with no matching '## heading'.
        # Only these count toward the strict exit code (exit 1).
        missing = [c for c in section.get("covers", []) if c not in parser.matched_covers]
        if missing:
            strict_warnings.append(
                f"MISSING covers in {part_id}/{section_id}: {', '.join(missing)}"
            )

        # Search index: covered headings + section titles.
        for block in blocks:
            if (
                block["type"] == "heading"
                and block["level"] == 2
                and block["id"] in section.get("covers", [])
            ):
                kind = "class" if block["id"][:1].isupper() else "function"
                key = (block["id"], f"{path}#{block['id']}")
                search_items[key] = {
                    "name": block["id"],
                    "kind": kind,
                    "path": f"{path}#{block['id']}",
                }
        search_items[(title, path)] = {"name": title, "kind": "section", "path": path}

    # chapters.json
    chapters_json = {
        "parts": [
            {
                "id": p["id"],
                "title": p["title"],
                "sections": [
                    {
                        "part": p["id"],
                        "id": s["id"],
                        "title": s["title"],
                        "path": f"/ch/{p['id']}/{s['id']}",
                    }
                    for s in p["sections"]
                ],
            }
            for p in config["parts"]
        ],
        "totalSections": total_sections,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "chapters.json").write_text(
        json.dumps(chapters_json, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # search-index.json (unique by name+path)
    search_list = sorted(search_items.values(), key=lambda x: (x["path"], x["name"]))
    (out_dir / "search-index.json").write_text(
        json.dumps(search_list, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # api-index.json: cover-derived items grouped alphabetically.
    api_items = [it for it in search_list if it["kind"] in ("class", "function")]
    groups: dict[str, list[dict]] = {}
    for it in api_items:
        letter = it["name"][:1].upper()
        groups.setdefault(letter, []).append(it)
    api_index = [
        {"letter": letter, "items": sorted(groups[letter], key=lambda x: x["name"])}
        for letter in sorted(groups)
    ]
    (out_dir / "api-index.json").write_text(
        json.dumps(api_index, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Copy glossary + inheritance verbatim.
    for name in ("glossary.json", "inheritance.json"):
        src = content_dir / name
        if src.is_file():
            shutil.copyfile(src, out_dir / name)

    # Coverage report.
    print("=== coverage report ===")
    for w in warnings + strict_warnings:
        print(f"WARNING: {w}")
    if not strict_warnings:
        print("all covers matched.")
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)

    if errors:
        return EXIT_ERROR
    if strict_warnings and args.strict:
        return EXIT_STRICT
    return EXIT_OK


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--content", default="content", help="content directory")
    ap.add_argument("--media-dir", default="media", help="media directory (for demo videos)")
    ap.add_argument("--out", default="public/data", help="output directory")
    ap.add_argument("--strict", action="store_true", help="exit 1 on MISSING covers")
    args = ap.parse_args()
    sys.exit(build(args))


if __name__ == "__main__":
    main()
