# /// script
# requires-python = ">=3.10"
# ///
"""Fix broken generated parameter list-tables.

A previous generator emitted parameter tables with a single ``* -`` row
marker followed by continuation ``- `` cells, so Nx4 tables collapsed into
one row of 4N cells.  This script finds every ``.. list-table::`` block that

  * declares ``:header-rows: 1``,
  * contains exactly one ``* - `` marker line, and
  * holds a cell count that is a positive multiple of 4 (>= 8),

and rewrites it as a header row (``name / type / default / desc``) followed
by one ``* -`` row per parameter (4 cells each).  All other blocks are left
untouched.  Blocks whose cells are not single-line or not a multiple of 4
are reported and skipped.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CHAPTERS = Path(__file__).resolve().parent.parent / "docs" / "source" / "chapters"

HEADER = ["name", "type", "default", "desc"]

ROW_RE = re.compile(r"^(\s*)\* - (.*)$")
CONT_RE = re.compile(r"^(\s*)- (.*)$")
OPT_RE = re.compile(r"^\s*:header-rows:")


def fix_file(path: Path) -> tuple[int, list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out: list[str] = []
    i = 0
    fixed = 0
    reports: list[str] = []
    n = len(lines)
    while i < n:
        line = lines[i]
        m = re.match(r"^(\s*)\.\. list-table::", line)
        if not m:
            out.append(line)
            i += 1
            continue
        # Collect the whole block: directive + options + blank + rows.
        block = [line]
        j = i + 1
        has_header_opt = False
        while j < n and re.match(r"^\s{3,}:\w", lines[j]):
            has_header_opt |= bool(OPT_RE.match(lines[j]))
            block.append(lines[j])
            j += 1
        # blank line(s) between options and first row stay in the block
        while j < n and lines[j].strip() == "":
            block.append(lines[j])
            j += 1
        # rows until a line that is not part of the table
        rows: list[tuple[str, str]] = []  # (marker '*'/ '-', text incl. newline)
        row_indent = None
        k = j
        while k < n:
            lm = ROW_RE.match(lines[k])
            lc = CONT_RE.match(lines[k])
            if lm and (row_indent is None or len(lm.group(1)) == row_indent):
                row_indent = len(lm.group(1))
                rows.append(("*", lines[k]))
                k += 1
            elif lc and row_indent is not None and len(lc.group(1)) == row_indent + 2:
                rows.append(("-", lines[k]))
                k += 1
            elif lines[k].strip() == "" and rows and k + 1 < n and (
                ROW_RE.match(lines[k + 1]) or CONT_RE.match(lines[k + 1])
            ):
                k += 1  # tolerate blank line between rows
            else:
                break
        star_rows = [r for r in rows if r[0] == "*"]
        if (
            has_header_opt
            and len(star_rows) == 1
            and len(rows) >= 4
            and len(rows) % 4 == 0
            and row_indent is not None
        ):
            pad = " " * row_indent
            cont_pad = " " * (row_indent + 2)
            new_rows: list[str] = []
            for ci, h in enumerate(HEADER):
                if ci == 0:
                    new_rows.append(f"{pad}* - {h}\n")
                else:
                    new_rows.append(f"{cont_pad}- {h}\n")
            for r, (marker, text) in enumerate(rows):
                if r % 4 == 0:
                    new_rows.append(f"{pad}* - {text.split('- ', 1)[1].lstrip()}")
                else:
                    new_rows.append(f"{cont_pad}- {text.split('- ', 1)[1].lstrip()}")
            block.extend(new_rows)
            fixed += 1
            reports.append(f"  fixed table at line {i + 1} ({len(rows) // 4} params)")
        else:
            block.extend(t for _, t in rows)
        out.extend(block)
        i = k
    if fixed:
        path.write_text("".join(out), encoding="utf-8")
    return fixed, reports


def main() -> int:
    total = 0
    for path in sorted(CHAPTERS.rglob("*.rst")):
        fixed, reports = fix_file(path)
        if reports:
            print(path.relative_to(CHAPTERS))
            for r in reports:
                print(r)
            total += fixed
    print(f"\nTotal tables fixed: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
