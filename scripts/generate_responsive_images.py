#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
JPEG_QUALITY = 85
WEBP_QUALITY = 86


@dataclass(frozen=True)
class Batch:
    source_dir: Path
    output_dir: Path
    widths: tuple[int, ...]


BATCHES = (
    Batch(
        source_dir=ROOT / "Photos-3-001",
        output_dir=ROOT / "optimized" / "gallery",
        widths=(1280, 1920),
    ),
    Batch(
        source_dir=ROOT / "material",
        output_dir=ROOT / "optimized" / "material",
        widths=(640, 1024),
    ),
)

VALID_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".avif"}


def ensure_rgb(image: Image.Image) -> Image.Image:
    if image.mode in {"RGB", "L"}:
        return image.convert("RGB")
    if image.mode in {"RGBA", "LA"}:
        background = Image.new("RGB", image.size, (255, 255, 255))
        background.paste(image, mask=image.getchannel("A"))
        return background
    return image.convert("RGB")


def resized_copy(image: Image.Image, target_width: int) -> Image.Image:
    if image.width <= target_width:
        return image.copy()
    ratio = target_width / image.width
    target_height = round(image.height * ratio)
    return image.resize((target_width, target_height), Image.Resampling.LANCZOS)


def save_variants(source_path: Path, output_dir: Path, widths: tuple[int, ...]) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)

    with Image.open(source_path) as source_image:
        normalized = ensure_rgb(ImageOps.exif_transpose(source_image))

        written: list[Path] = []
        for width in widths:
            target_width = min(width, normalized.width)
            resized = resized_copy(normalized, target_width)
            stem = f"{source_path.stem}-{target_width}"

            jpg_path = output_dir / f"{stem}.jpg"
            resized.save(
                jpg_path,
                format="JPEG",
                quality=JPEG_QUALITY,
                optimize=True,
                progressive=True,
            )
            written.append(jpg_path)

            webp_path = output_dir / f"{stem}.webp"
            resized.save(
                webp_path,
                format="WEBP",
                quality=WEBP_QUALITY,
                method=6,
            )
            written.append(webp_path)

            resized.close()

    return written


def main() -> None:
    total_outputs = 0
    for batch in BATCHES:
        source_paths = sorted(
            path
            for path in batch.source_dir.iterdir()
            if path.is_file() and path.suffix.lower() in VALID_SUFFIXES
        )
        for source_path in source_paths:
            written = save_variants(source_path, batch.output_dir, batch.widths)
            total_outputs += len(written)
            print(f"{source_path.relative_to(ROOT)} -> {len(written)} files")
    print(f"done: wrote {total_outputs} responsive assets")


if __name__ == "__main__":
    main()
