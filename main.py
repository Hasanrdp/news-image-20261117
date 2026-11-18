#!/usr/bin/env python3
"""news-image-20261117 entry: "The Daily World", a one-page newspaper
front page summing up the world's news of Tuesday 17 November 2026.

The image is entry.png beside this file (drawn by draw_image.py with
Pillow during the build; the drawing is flat vector art with real rendered
text, so nothing in it is garbled). This program only copies it to the
grader's output directory, which keeps the entry byte-identical on every
run: standard library only, no network, no clock, no randomness.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    size = os.path.getsize(dest)
    if size == 0 or size > 1048576:
        print(f"entry.png has unexpected size {size}", file=sys.stderr)
        return 1
    if sha256(SOURCE) != sha256(dest):
        print("copy mismatch: destination differs from entry.png",
              file=sys.stderr)
        return 1
    print(f"wrote {dest} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
