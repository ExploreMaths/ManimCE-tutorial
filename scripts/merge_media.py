#!/usr/bin/env python3
"""Copy rendered videos from media/ into dist/media/ for deployment.

Preserves relative paths below media/ (videos live in media/chXX/*.mp4).
Skips manifest.json and render-summary.json (they are not videos).
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--media-dir", default="media")
    ap.add_argument("--dist", default="dist")
    args = ap.parse_args()

    media_dir = Path(args.media_dir)
    dest_root = Path(args.dist) / "media"
    if not media_dir.is_dir():
        print(f"media dir {media_dir} not found, nothing to merge")
        return 0

    count = 0
    total_bytes = 0
    for mp4 in sorted(media_dir.rglob("*.mp4")):
        rel = mp4.relative_to(media_dir)
        dest = dest_root / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(mp4, dest)
        count += 1
        total_bytes += mp4.stat().st_size

    print(f"merged {count} video(s), {total_bytes} bytes total into {dest_root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
