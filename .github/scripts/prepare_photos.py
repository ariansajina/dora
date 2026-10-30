"""Get uploaded photos ready for the site.

- HEIC/HEIF photos (the iPhone format, which most browsers can't show) are
  converted to JPEG, the original is deleted, and the content files that point
  at it are updated to the new name.
- Every photo whose longer side is over MAX_SIDE pixels is scaled down to MAX_SIDE.
- Photos straight from a phone are turned the right way up and lose their
  hidden camera data (including the GPS location). Colour profiles are kept.

Photos that are already fine are left untouched, so running this again changes
nothing.

Usage: python3 prepare_photos.py assets/img
"""
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageOps
from pillow_heif import register_heif_opener

register_heif_opener()

MAX_SIDE = 1600
QUALITY = 82
ORIENTATION, GPS = 0x0112, 0x8825
PHOTOS = {".jpg", ".jpeg", ".png", ".webp"}
HEIC = {".heic", ".heif"}
# content files that can point at photos
CONTENT = re.compile(r"\.(md|markdown|html|yml|yaml)$")


def needs_work(img):
    exif = img.getexif()
    return max(img.size) > MAX_SIDE or exif.get(ORIENTATION, 1) != 1 or GPS in exif


def save(img, path, fmt, icc):
    if fmt == "JPEG":
        img.convert("RGB").save(path, "JPEG", quality=QUALITY, optimize=True, progressive=True, icc_profile=icc)
    elif fmt == "WEBP":
        img.save(path, "WEBP", quality=QUALITY, icc_profile=icc)
    else:
        img.save(path, fmt, optimize=True, icc_profile=icc)


def prepare(path, out=None, fmt=None):
    """Shrink/clean `path` in place, or write it to `out` as `fmt`."""
    with Image.open(path) as img:
        if out is None and not needs_work(img):
            return False
        fmt, icc = fmt or img.format, img.info.get("icc_profile")
        before = img.size
        img = ImageOps.exif_transpose(img)
        img.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
        save(img, out or path, fmt, icc)
    print(f"{path}: {before[0]}×{before[1]} → {out or path}: {img.size[0]}×{img.size[1]}")
    return True


def jpeg_for(heic):
    """The name a HEIC photo gets as a JPEG: the same, unless another photo has it."""
    jpg = heic.with_suffix(".jpg")
    return jpg.with_stem(jpg.stem + "-heic") if jpg.exists() else jpg


def converted(heic):
    """The JPEG a HEIC photo was converted to (maybe in an earlier run), if any."""
    for jpg in (heic.with_stem(heic.stem + "-heic").with_suffix(".jpg"), heic.with_suffix(".jpg")):
        if jpg.exists():
            return jpg
    return None


def to_jpeg(m):
    jpg = converted(Path(m.group(0)))
    return jpg.as_posix() if jpg else m.group(0)


def update_references(folder):
    """Point content files at the JPEG versions of converted HEIC photos.

    The upload and the save that uses it are separate commits, so the photo may
    have been converted by an earlier run: this looks at what's in the folder.
    """
    pattern = re.compile(re.escape(folder.as_posix()) + r"/[^\s\"'()\]]+?\.(?:heic|heif)\b", re.I)
    files = subprocess.run(["git", "ls-files"], capture_output=True, text=True, check=True).stdout.split()
    for name in files:
        if not CONTENT.search(name) or name.startswith((".github/", "vendor/")):
            continue
        path = Path(name)
        text = path.read_text()
        new = pattern.sub(to_jpeg, text)
        if new != text:
            path.write_text(new)
            print(f"{path}: now points at the JPEG version")


folder = Path(sys.argv[1])
changed = 0
for heic in sorted(p for p in folder.rglob("*") if p.suffix.lower() in HEIC):
    prepare(heic, out=jpeg_for(heic), fmt="JPEG")
    heic.unlink()
    changed += 1
update_references(folder)
photos = [p for p in sorted(folder.rglob("*")) if p.suffix.lower() in PHOTOS]
changed += sum(prepare(p) for p in photos)
print(f"{changed} photos changed")
