#!/usr/bin/env python3
"""Convert a supplied, approved homepage PNG into a website WebP at quality 80."""

import argparse
import hashlib
from pathlib import Path

from PIL import Image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="Approved raster PNG master")
    parser.add_argument("--output", type=Path, default=Path("images/heroes/earthrise_hero_q80.webp"))
    args = parser.parse_args()

    if not args.source.is_file() or args.source.suffix.lower() != ".png":
        parser.error("source must be an existing PNG file")

    with Image.open(args.source) as original:
        original.load()
        if original.format != "PNG":
            parser.error("source is not a PNG image")
        width, height = original.size
        if width < 500 or height < 300:
            parser.error("source is too small for the homepage hero")
        image = original.convert("RGB")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.output, format="WEBP", quality=80, method=6, exact=True)

    with Image.open(args.output) as checked:
        assert checked.format == "WEBP"
        assert checked.size == (width, height)

    content = args.output.read_bytes()
    digest = hashlib.sha256(content).hexdigest()
    print(f"source: {args.source} ({width}x{height})")
    print(f"WebP quality: 80")
    print(f"output: {args.output} ({len(content):,} bytes)")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
