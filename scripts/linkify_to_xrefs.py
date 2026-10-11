"""Rewrite hand-written manim.community doc URLs as :class: cross-references.

Frozen chapter .rst files (and any other hand-written source) link to the
official v0.21.0 API with anonymous inline references::

    `Point3DLike <https://docs.manim.community/en/v0.21.0/reference/...>`__

This script rewrites them into Python-domain roles so Sphinx + intersphinx
emits proper ``<code class="xref py py-class">`` links::

    :class:`Point3DLike <manim.typing.Point3DLike>`

Links without an anchor (the predefined color swatches page) resolve to
``<page module>.<link text>``. Local (non docs.manim.community) links are
left untouched.

Usage: py -3 scripts/linkify_to_xrefs.py [--dry-run] [paths...]
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

BASE = "https://docs.manim.community/en/v0.21.0"
LINK_RE = re.compile(
    r"`([^`<]+?)\s*<" + re.escape(BASE) + r"/([^`>\s]+)>`__?"
)
REF_PAGE_RE = re.compile(r"^reference/([A-Za-z0-9_.]+)\.html(?:#([A-Za-z0-9_.]+))?$")


def convert(text: str) -> tuple[str, int]:
    count = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal count
        text_part, url = m.group(1).strip(), m.group(2)
        pm = REF_PAGE_RE.match(url)
        if not pm:
            return m.group(0)  # not an API reference page — leave as-is
        page, anchor = pm.group(1), pm.group(2)
        target = anchor if anchor else f"{page}.{text_part}"
        # Constants and predefined colors have no entries in the official
        # Sphinx inventory (only classes/functions/methods do), so an
        # intersphinx role can never resolve them — keep the deep URL link.
        if target.startswith((
            "manim.constants.",
            "manim.utils.color.manim_colors.",
        )):
            return m.group(0)
        last = target.rsplit(".", 1)[-1]
        count += 1
        if text_part == last:
            return f":class:`{target}`"
        return f":class:`{text_part} <{target}>`"

    return LINK_RE.sub(repl, text), count


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="report only")
    ap.add_argument(
        "paths",
        nargs="*",
        default=["docs/source/chapters"],
        help="rst files or directories to rewrite",
    )
    args = ap.parse_args()

    files: list[pathlib.Path] = []
    for raw in args.paths:
        p = pathlib.Path(raw)
        files.extend(p.rglob("*.rst") if p.is_dir() else [p])

    total = 0
    changed = []
    for f in sorted(files):
        old = f.read_text(encoding="utf-8")
        new, n = convert(old)
        if n:
            changed.append((f, n))
            total += n
            if not args.dry_run:
                f.write_text(new, encoding="utf-8")
                print(f"  {f}: {n} link(s) -> :class: role")
    mode = "DRY-RUN " if args.dry_run else ""
    print(f"{mode}{total} link(s) across {len(changed)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
