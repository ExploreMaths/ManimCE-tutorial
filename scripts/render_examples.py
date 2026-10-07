#!/usr/bin/env python3
"""Incrementally render examples/**.py into media/ videos.

Cache design (a REAL cache, not a fake):
  * Scan key: posix relative path of the example without extension, e.g.
    "ch02/circle_intro". Keys are immutable — they are the cache identity.
  * Cache validity: manifest entry sha256 == sha256(file_bytes + version salt)
    AND status == "ok" AND the recorded video file exists under media-dir.
  * Anything invalid/missing is queued and rendered in a subprocess:
      manim render --media_dir <tmpdir> -q<quality> --format mp4 <file> <Scene>
The scene class is discovered by AST: the first top-level class whose base
class name ends with "Scene". Files under examples/_shared/ are skipped.

Outputs media/manifest.json and media/render-summary.json. Exit code is 0
even when individual examples fail (CI reads render-summary.json); exit 1
only on internal errors (e.g. manifest unwritable).
"""

from __future__ import annotations

import argparse
import ast
import concurrent.futures
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

MANIM_VERSION = "0.21.0"
VERSION_SALT = f"\nmanim=={MANIM_VERSION}".encode()
SIZE_WARNING_BYTES = 25 * 1024 * 1024
ERROR_TAIL_LINES = 20


def example_key(path: Path, root: Path) -> str:
    """Posix relative path without extension, e.g. ch02/circle_intro."""
    return path.relative_to(root).with_suffix("").as_posix()


def content_hash(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    h.update(VERSION_SALT)
    return h.hexdigest()


def discover_scene(path: Path) -> str | None:
    """First top-level class subclassing something named *Scene (AST only)."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError):
        return None
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        for base in node.bases:
            if isinstance(base, ast.Name):
                name = base.id
            elif isinstance(base, ast.Attribute):
                name = base.attr
            else:
                continue
            if name.endswith("Scene"):
                return node.name
    return None


def load_manifest(media_dir: Path) -> dict:
    path = media_dir / "manifest.json"
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict) and isinstance(data.get("examples"), dict):
                data.setdefault("version", MANIM_VERSION)
                return data
        except json.JSONDecodeError:
            print(f"WARNING: {path} is corrupt, starting fresh", file=sys.stderr)
    return {"version": MANIM_VERSION, "examples": {}}


def render_one(
    key: str, py_file: Path, digest: str, media_dir: Path, quality: str
) -> tuple[str, dict, str | None]:
    """Render a single example. Returns (key, manifest_entry, error|None)."""
    scene = discover_scene(py_file)
    if scene is None:
        entry = {"sha256": digest, "status": "failed", "error": "no Scene class found (AST)"}
        return key, entry, "no Scene class found"

    tmp = Path(tempfile.mkdtemp(prefix=f"manim-{key.replace('/', '-')}-"))
    try:
        cmd = [
            "manim", "render",
            "--media_dir", str(tmp),
            f"-q{quality}",
            "--format", "mp4",
            str(py_file),
            scene,
        ]
        proc = subprocess.run(
            cmd, capture_output=True, text=True,
            encoding="utf-8", errors="replace",
        )
        mp4s = sorted(tmp.rglob(f"{scene}.mp4"))
        if not mp4s:
            mp4s = sorted(tmp.rglob("*.mp4"))
        if proc.returncode != 0:
            tail = "\n".join((proc.stderr or "").splitlines()[-ERROR_TAIL_LINES:])
            entry = {"sha256": digest, "status": "failed", "scene": scene, "error": tail}
            return key, entry, f"manim exited {proc.returncode}"
        if not mp4s:
            tail = "\n".join((proc.stderr or "").splitlines()[-ERROR_TAIL_LINES:])
            entry = {"sha256": digest, "status": "failed", "scene": scene,
                     "error": (tail or "no mp4 produced").strip() or "no mp4 produced"}
            return key, entry, "no mp4 produced"

        dest = media_dir / f"{key}__{scene}.mp4"
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(mp4s[0], dest)
        entry = {
            "sha256": digest,
            "video": f"{key}__{scene}.mp4",
            "scene": scene,
            "status": "ok",
            "duration": None,
        }
        if dest.stat().st_size > SIZE_WARNING_BYTES:
            entry["sizeWarning"] = True
        return key, entry, None
    except OSError as exc:
        entry = {"sha256": digest, "status": "failed", "scene": scene, "error": str(exc)}
        return key, entry, str(exc)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def normalize_only(raw: str) -> str:
    """Normalize --only input to a key (no extension, no examples/ prefix)."""
    key = raw.replace("\\", "/")
    if key.startswith("examples/"):
        key = key[len("examples/"):]
    if key.endswith(".py"):
        key = key[:-3]
    return key


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--media-dir", required=True, help="media output/cache directory")
    ap.add_argument("--workers", type=int, default=min(4, os.cpu_count() or 4),
                    help="parallel render workers (default: min(4, cpu_count))")
    ap.add_argument("--dry-run", action="store_true",
                    help="compute cache state, write manifest, do not render")
    ap.add_argument("--quality", default="m", help="manim quality flag: l/m/h/p/k (default m)")
    ap.add_argument("--only", help="restrict to one example path/key")
    args = ap.parse_args()

    try:
        media_dir = Path(args.media_dir)
        media_dir.mkdir(parents=True, exist_ok=True)
        examples_root = Path("examples")
        if not examples_root.is_dir():
            print("ERROR: examples/ directory not found", file=sys.stderr)
            return 1

        files = sorted(
            p for p in examples_root.rglob("*.py")
            if "_shared" not in p.relative_to(examples_root).parts
        )
        on_disk = {example_key(p, examples_root): p for p in files}

        only_key = normalize_only(args.only) if args.only else None
        if only_key and only_key not in on_disk:
            print(f"ERROR: --only '{args.only}' matches no example", file=sys.stderr)
            return 1

        manifest = load_manifest(media_dir)
        examples = manifest["examples"]

        # Drop entries whose example file no longer exists.
        for stale in [k for k in examples if k not in on_disk]:
            del examples[stale]

        to_render: list[tuple[str, Path, str]] = []
        reused: list[str] = []
        for key, py_file in on_disk.items():
            if only_key and key != only_key:
                continue
            digest = content_hash(py_file)
            entry = examples.get(key)
            video_ok = (
                entry
                and entry.get("sha256") == digest
                and entry.get("status") == "ok"
                and entry.get("video")
                and (media_dir / entry["video"]).is_file()
            )
            if video_ok:
                reused.append(key)
            else:
                to_render.append((key, py_file, digest))

        if args.dry_run:
            print(f"total examples : {len(on_disk)}")
            print(f"would reuse    : {len(reused)}")
            for key in reused:
                print(f"  reuse  {key}")
            print(f"would render   : {len(to_render)}")
            for key, _, _ in to_render:
                print(f"  render {key}")
            (media_dir / "manifest.json").write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            return 0

        rendered: list[str] = []
        failed: list[dict] = []
        if to_render:
            workers = max(1, args.workers)
            with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
                futures = {
                    pool.submit(render_one, key, py_file, digest, media_dir, args.quality): key
                    for key, py_file, digest in to_render
                }
                for fut in concurrent.futures.as_completed(futures):
                    key = futures[fut]
                    try:
                        rkey, entry, error = fut.result()
                    except Exception as exc:  # defensive: never abort the batch
                        rkey, entry, error = key, {
                            "sha256": "", "status": "failed", "error": str(exc),
                        }, str(exc)
                    examples[rkey] = entry
                    if error is None:
                        rendered.append(rkey)
                        print(f"ok      {rkey}")
                    else:
                        failed.append({"key": rkey, "error": error})
                        print(f"FAILED  {rkey}: {error}", file=sys.stderr)

        summary = {"rendered": sorted(rendered), "reused": sorted(reused),
                   "failed": sorted(failed, key=lambda f: f["key"])}
        (media_dir / "render-summary.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        (media_dir / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        print("=== render summary ===")
        print(f"total   : {len(on_disk)}")
        print(f"reused  : {len(reused)}")
        print(f"rendered: {len(rendered)}")
        print(f"failed  : {len(failed)}")
        for f in summary["failed"]:
            print(f"  {f['key']}: {f['error']}")
        return 0
    except Exception as exc:  # internal error only
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
