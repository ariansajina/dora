"""Shrink photos so the site stays quick to load.

Every photo in the given folder whose longer side is over MAX_SIDE pixels is
scaled down to MAX_SIDE. Photos straight from a phone are also turned the right
way up and lose their hidden camera data (including the GPS location). Colour
profiles are kept. Photos that are already small and clean are left untouched,
so running this again changes nothing.

Usage: python3 shrink_photos.py assets/img
"""
import sys
from pathlib import Path

from PIL import Image, ImageOps

MAX_SIDE = 1600
QUALITY = 82
ORIENTATION, GPS = 0x0112, 0x8825


def needs_work(img):
    exif = img.getexif()
    return max(img.size) > MAX_SIDE or exif.get(ORIENTATION, 1) != 1 or GPS in exif


def shrink(path):
    with Image.open(path) as img:
        if not needs_work(img):
            return False
        fmt, icc = img.format, img.info.get("icc_profile")
        before = img.size
        img = ImageOps.exif_transpose(img)
        img.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
        if fmt == "JPEG":
            img = img.convert("RGB")
            img.save(path, "JPEG", quality=QUALITY, optimize=True, progressive=True, icc_profile=icc)
        elif fmt == "WEBP":
            img.save(path, "WEBP", quality=QUALITY, icc_profile=icc)
        else:
            img.save(path, fmt, optimize=True, icc_profile=icc)
    print(f"{path}: {before[0]}×{before[1]} → {img.size[0]}×{img.size[1]}")
    return True


folder = Path(sys.argv[1])
photos = [p for p in sorted(folder.rglob("*")) if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}]
changed = sum(shrink(p) for p in photos)
print(f"{changed} of {len(photos)} photos changed")
