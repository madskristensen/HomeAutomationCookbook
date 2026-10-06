#!/usr/bin/env python3
"""Build the fixed AVIF and JPEG names during the Pages deploy.

Card masters get name-400.avif, name-640.avif, and name-640.jpg.
Hero masters (stem "hero") also get name-800.avif, name-1200.avif, and
name-1600.avif. Oversized masters are capped in the cache (content
<=1600px long side, heroes <=2000px) and published into _site without
changing the repo original. Nothing here is committed. Actions can
cache .image-cache on a hash of the masters and this encoder.

    python3 script/render-image-variants.py --fingerprint
    python3 script/render-image-variants.py --check-cache
    python3 script/render-image-variants.py --from-cache
    python3 script/render-image-variants.py
    python3 script/render-image-variants.py --publish-site

Run from the repo root. Masters live under docs/assets/img.
A referenced photo that cannot be encoded fails the build.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import sys

IMAGE_ROOT = os.path.join("docs", "assets", "img")
CACHE_ROOT = ".image-cache"
CACHE_OUT = os.path.join(CACHE_ROOT, "out")
CACHE_META = os.path.join(CACHE_ROOT, "meta")
CACHE_MASTERS = os.path.join(CACHE_ROOT, "masters")
SKIP_TOP = {"logos", "social", "diagrams"}
SKIP_NAMES = {
    "apple-touch-icon.png",
    "favicon-96x96.png",
    "favicon.png",
}
SOURCE_EXT = {".jpg", ".jpeg", ".png", ".webp"}
CARD_AVIF = (400, 640)
HERO_AVIF = (400, 640, 800, 1200, 1600)
JPEG_WIDTH = 640
AVIF_QUALITY = 60
JPEG_QUALITY = 75
CARD_MASTER_CAP = 1600
HERO_MASTER_CAP = 2000
MASTER_WEBP_QUALITY = 82
MASTER_JPEG_QUALITY = 85
ENCODER_ID = "hac-fixed-card-400-640-jpg640-hero-800-1200-1600"
VARIANT_RE = re.compile(r"-(?:400|640|800|960|1200|1280|1600)$")
HERO_STEMS = {"hero"}
# Markup that must resolve to generated variants after encode.
REQUIRED_STEMS = {
    "hero": "hero",
}


def is_hero(path: str) -> bool:
    stem = os.path.splitext(os.path.basename(path))[0]
    return stem in HERO_STEMS


def avif_widths(path: str):
    if is_hero(path):
        return HERO_AVIF
    return CARD_AVIF


def source_files():
    found = []
    if not os.path.isdir(IMAGE_ROOT):
        return found
    for dirpath, dirnames, filenames in os.walk(IMAGE_ROOT):
        dirnames[:] = [name for name in dirnames if name not in SKIP_TOP]
        for name in filenames:
            if name in SKIP_NAMES or name.startswith("icon-"):
                continue
            stem, ext = os.path.splitext(name)
            if ext.lower() not in SOURCE_EXT:
                continue
            if VARIANT_RE.search(stem):
                continue
            found.append(os.path.join(dirpath, name))
    found.sort()
    return found


def file_sha256(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fingerprint() -> str:
    lines = [
        "encoder %s avif %s jpeg %s"
        % (ENCODER_ID, AVIF_QUALITY, JPEG_QUALITY)
    ]
    for path in source_files():
        lines.append("%s %s" % (path.replace(os.sep, "/"), file_sha256(path)))
    payload = "\n".join(lines).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def rel_key(path: str) -> str:
    rel = os.path.relpath(path, IMAGE_ROOT).replace(os.sep, "/")
    return os.path.splitext(rel)[0]


def meta_path(key: str) -> str:
    return os.path.join(CACHE_META, key + ".json")


def variant_name(stem: str, width: int, ext: str) -> str:
    return "%s-%d%s" % (stem, width, ext)


def read_record(path: str):
    key = rel_key(path)
    meta = meta_path(key)
    if not os.path.exists(meta):
        return None
    try:
        with open(meta, encoding="utf-8") as handle:
            record = json.load(handle)
    except (OSError, ValueError):
        return None
    if record.get("hash") != file_sha256(path):
        return None
    if record.get("encoder") != ENCODER_ID:
        return None
    stem = os.path.splitext(os.path.basename(path))[0]
    folder = os.path.dirname(path)
    for fmt, ext in (("avif", ".avif"), ("jpeg", ".jpg")):
        for width in record.get(fmt) or []:
            cached = os.path.join(
                CACHE_OUT, folder, variant_name(stem, int(width), ext)
            )
            if not os.path.exists(cached):
                return None
    return record


def widths_complete(path: str, record) -> bool:
    avif = [int(width) for width in (record.get("avif") or [])]
    jpeg = [int(width) for width in (record.get("jpeg") or [])]
    return avif == list(avif_widths(path)) and jpeg == [JPEG_WIDTH]


def cached_record(path: str):
    record = read_record(path)
    if not record or not widths_complete(path, record):
        return None
    return record


def cache_complete() -> bool:
    files = source_files()
    if not files:
        return True
    return all(cached_record(path) for path in files)


def copy_record(path: str, record) -> None:
    stem = os.path.splitext(os.path.basename(path))[0]
    folder = os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)
    for fmt, ext in (("avif", ".avif"), ("jpeg", ".jpg")):
        for width in record.get(fmt) or []:
            name = variant_name(stem, int(width), ext)
            src = os.path.join(CACHE_OUT, folder, name)
            dest = os.path.join(folder, name)
            if os.path.exists(src):
                shutil.copy2(src, dest)


def open_image(path: str):
    from PIL import Image, ImageOps

    image = ImageOps.exif_transpose(Image.open(path))
    image.load()
    if image.mode not in ("RGB", "RGBA"):
        image = image.convert("RGB")
    return image


def frame_at(image, width: int):
    from PIL import Image

    if width == image.width:
        return image
    height = max(1, round(image.height * width / image.width))
    return image.resize((width, height), Image.Resampling.LANCZOS)


def save_variant(image, dest: str, kind: str) -> None:
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if kind == "jpeg":
        image.convert("RGB").save(
            dest, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True
        )
        return
    image.convert("RGB").save(dest, "AVIF", quality=AVIF_QUALITY)


def encode(path: str):
    key = rel_key(path)
    stem = os.path.splitext(os.path.basename(path))[0]
    folder = os.path.dirname(path)
    image = open_image(path)
    widths = list(avif_widths(path))
    record = {
        "hash": file_sha256(path),
        "encoder": ENCODER_ID,
        "width": image.width,
        "height": image.height,
        "avif": [],
        "jpeg": [],
    }
    built = []
    for width in widths:
        name = variant_name(stem, width, ".avif")
        cached = os.path.join(CACHE_OUT, folder, name)
        dest = os.path.join(folder, name)
        save_variant(frame_at(image, width), cached, "avif")
        os.makedirs(folder, exist_ok=True)
        shutil.copy2(cached, dest)
        built.append(width)
        print("  %s (%dK)" % (dest, os.path.getsize(dest) // 1024))
    record["avif"] = built
    name = variant_name(stem, JPEG_WIDTH, ".jpg")
    cached = os.path.join(CACHE_OUT, folder, name)
    dest = os.path.join(folder, name)
    save_variant(frame_at(image, JPEG_WIDTH), cached, "jpeg")
    shutil.copy2(cached, dest)
    record["jpeg"] = [JPEG_WIDTH]
    print("  %s (%dK)" % (dest, os.path.getsize(dest) // 1024))
    os.makedirs(os.path.dirname(meta_path(key)), exist_ok=True)
    with open(meta_path(key), "w", encoding="utf-8") as handle:
        json.dump(record, handle)
    return record


def master_cap(path: str) -> int:
    if is_hero(path):
        return HERO_MASTER_CAP
    return CARD_MASTER_CAP


def capped_cache_path(path: str) -> str:
    return os.path.join(CACHE_MASTERS, path)


def master_long_side(path: str) -> int:
    from PIL import Image, ImageOps

    with Image.open(path) as image:
        exif = image.getexif()
        orientation = exif.get(274) if exif else None
        if orientation and orientation != 1:
            image = ImageOps.exif_transpose(image)
        return max(image.width, image.height)


def oriented_image(path: str):
    from PIL import Image, ImageOps

    image = ImageOps.exif_transpose(Image.open(path))
    image.load()
    return image


def frame_within(image, cap: int):
    from PIL import Image

    long_side = max(image.width, image.height)
    if long_side <= cap:
        return image
    if image.width >= image.height:
        width = cap
        height = max(1, round(image.height * cap / image.width))
    else:
        height = cap
        width = max(1, round(image.width * cap / image.height))
    return image.resize((width, height), Image.Resampling.LANCZOS)


def save_master(image, dest: str, ext: str) -> None:
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if ext in {".jpg", ".jpeg"}:
        image.convert("RGB").save(
            dest,
            "JPEG",
            quality=MASTER_JPEG_QUALITY,
            optimize=True,
            progressive=True,
        )
        return
    if ext == ".webp":
        if image.mode not in ("RGB", "RGBA"):
            bands = image.getbands()
            image = image.convert("RGBA" if bands and "A" in bands else "RGB")
        image.save(dest, "WEBP", quality=MASTER_WEBP_QUALITY, method=6)
        return
    if image.mode == "P":
        image = image.convert(
            "RGBA" if "transparency" in image.info else "RGB"
        )
    elif image.mode not in ("RGB", "RGBA"):
        bands = image.getbands()
        image = image.convert("RGBA" if bands and "A" in bands else "RGB")
    image.save(dest, "PNG", optimize=True)


def drop_capped(path: str) -> None:
    cached = capped_cache_path(path)
    for extra in (cached, cached + ".sha256"):
        if os.path.exists(extra):
            os.remove(extra)


def capped_stamp(path: str, cap: int) -> str:
    return "%s %d" % (file_sha256(path), cap)


def capped_current(path: str, cap: int) -> bool:
    cached = capped_cache_path(path)
    stamp = cached + ".sha256"
    if not os.path.exists(cached) or not os.path.exists(stamp):
        return False
    with open(stamp, encoding="utf-8") as handle:
        return handle.read().strip() == capped_stamp(path, cap)


def write_capped(path: str) -> None:
    cap = master_cap(path)
    ext = os.path.splitext(path)[1].lower()
    dest = capped_cache_path(path)
    tmp = dest + ".tmp"
    try:
        image = oriented_image(path)
        try:
            resized = frame_within(image, cap)
            long_side = max(resized.width, resized.height)
            save_master(resized, tmp, ext)
        finally:
            image.close()
        os.replace(tmp, dest)
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)
    with open(dest + ".sha256", "w", encoding="utf-8") as handle:
        handle.write(capped_stamp(path, cap))
    print("capped master %s -> cache (%dpx, cap %d)" % (path, long_side, cap))


def ensure_capped_masters() -> int:
    capped = 0
    for path in source_files():
        cap = master_cap(path)
        long_side = master_long_side(path)
        if long_side <= cap:
            drop_capped(path)
            continue
        if not capped_current(path, cap):
            write_capped(path)
        capped += 1
    if capped:
        print("%d capped master(s) in cache." % capped)
    else:
        print("no oversized masters")
    return capped


def publish_site() -> None:
    # Jekyll with working-directory docs writes to docs/_site.
    candidates = [
        os.path.join("docs", "_site"),
        "_site",
    ]
    site_root = next((path for path in candidates if os.path.isdir(path)), None)
    if not site_root:
        sys.exit("_site is missing, so capped masters were not published")
    ensure_capped_masters()
    copied = 0
    for path in source_files():
        cached = capped_cache_path(path)
        if not os.path.exists(cached):
            continue
        dest = os.path.join(
            site_root, "assets", "img", os.path.relpath(path, IMAGE_ROOT)
        )
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(cached, dest)
        source_hash = file_sha256(path)
        published_hash = file_sha256(dest)
        if published_hash == source_hash:
            sys.exit("capped master matches the repo file for %s" % path)
        copied += 1
        print("published %s" % dest)
    print("Published %d capped master(s) to _site." % copied)


def publish_from_cache() -> None:
    for path in source_files():
        record = cached_record(path)
        if not record:
            sys.exit("image cache is missing %s" % path)
        copy_record(path, record)
    print("Restored %d image(s) from cache." % len(source_files()))
    ensure_capped_masters()
    require_variants()


def required_variant_paths(path: str):
    stem = os.path.splitext(os.path.basename(path))[0]
    folder = os.path.dirname(path)
    paths = []
    for width in avif_widths(path):
        paths.append(os.path.join(folder, variant_name(stem, width, ".avif")))
    paths.append(os.path.join(folder, variant_name(stem, JPEG_WIDTH, ".jpg")))
    return paths


def require_variants() -> None:
    missing = []
    files = source_files()
    by_stem = {
        os.path.splitext(os.path.basename(path))[0]: path for path in files
    }
    for stem in REQUIRED_STEMS:
        if stem not in by_stem:
            missing.append("required master stem missing: %s" % stem)
            continue
        path = by_stem[stem]
        for variant in required_variant_paths(path):
            if not os.path.exists(variant):
                missing.append(variant)
    for path in files:
        for variant in required_variant_paths(path):
            if not os.path.exists(variant):
                missing.append(variant)
    if missing:
        for item in missing:
            print("missing %s" % item)
        sys.exit("image variants incomplete (%d)" % len(missing))
    print("image variants ok (%d master(s))" % len(files))


def generate() -> None:
    try:
        import PIL  # noqa: F401
        import pillow_avif  # noqa: F401
    except ImportError:
        sys.exit("Pillow and pillow-avif-plugin are required")
    failed = []
    for path in source_files():
        existing = cached_record(path)
        if existing:
            copy_record(path, existing)
            print("cached %s" % path)
            continue
        print(path)
        try:
            encode(path)
        except Exception as exc:
            print("  failed %s: %s" % (path, exc))
            failed.append(path)
    if failed:
        sys.exit("could not encode %d photo(s)" % len(failed))
    try:
        ensure_capped_masters()
    except Exception as exc:
        sys.exit("could not cap masters: %s" % exc)
    require_variants()


def main() -> None:
    if "--fingerprint" in sys.argv:
        print(fingerprint())
        return
    if "--check-cache" in sys.argv:
        sys.exit(0 if cache_complete() else 1)
    if "--from-cache" in sys.argv:
        publish_from_cache()
        return
    if "--publish-site" in sys.argv:
        publish_site()
        return
    generate()


if __name__ == "__main__":
    main()
