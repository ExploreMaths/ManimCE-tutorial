# /// script
# requires-python = ">=3.10"
# ///
"""Insert a blank line after list-table blocks when missing.

Some generated sections place the next section title (or directive) directly
after the last table row without a blank line, which docutils reports as
"Explicit markup ends without a blank line; unexpected unindent".
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CHAPTERS = Path(__file__).resolve().parent.parent / "docs" / "chapters"
CHAPTERS = Path(__file__).resolve().parent.parent / "docs" / "source" / "chapters"

ROW_RE = re.compile(r"^\s+\* - ")
CONT_RE = re.compile(r"^\s+- ")
DIRECTIVE_RE = re.compile(r"^\s*\.\. ")


def fix_file(path: Path) -> int:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out: list[str] = []
    inserted = 0
    for idx, line in enumerate(lines):
        out.append(line)
        nxt = lines[idx + 1] if idx + 1 < len(lines) else None
        if nxt is None:
            break
        # Any indented non-blank line followed directly by a column-0 line
        # (section title, directive, or plain paragraph) needs a separating
        # blank line; RST never allows that transition without one.
        needs_blank = (
            line.startswith((" ", "\t"))
            and line.strip() != ""
            and nxt.strip() != ""
            and not nxt.startswith((" ", "\t"))
        )
        if needs_blank:
            out.append("\n")
            inserted += 1
    if inserted:
        path.write_text("".join(out), encoding="utf-8")
    return inserted


def main() -> int:
    total = 0
    for path in sorted(CHAPTERS.rglob("*.rst")):
        n = fix_file(path)
        if n:
            print(f"{path.relative_to(CHAPTERS)}: +{n} blank line(s)")
            total += n
    print(f"\nTotal blank lines inserted: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
