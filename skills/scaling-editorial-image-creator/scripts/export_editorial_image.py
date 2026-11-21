#!/usr/bin/env python3
"""Export an editorial PNG, adding the supplied Frontify AI label after cropping."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil

from PIL import Image, ImageOps, ImageStat

ASSETS = Path(__file__).resolve().parents[1] / "assets" / "ai-labels"


def _luminance(rgb):
    channels = [v / 255 for v in rgb]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in channels]
    return sum(v * w for v, w in zip(linear, (0.2126, 0.7152, 0.0722)))


def _contrast(a, b):
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def _apply_label(image, label, style, corner, label_width, margin):
    """Composite the original artwork; never synthesize lettering or recolor it."""
    asset = ASSETS / f"ai-{label}-positive.png"
    with Image.open(asset) as original:
        label_height = round(label_width * original.height / original.width)
    width, height = image.size
    if label_width < 1 or label_height < 1 or margin < 0:
        raise ValueError("Label width must be positive and margin must be nonnegative.")
    if label_width + 2 * margin > width or label_height + 2 * margin > height:
        raise ValueError("Label and margins do not fit inside the final image.")
    x = margin if corner == "bottom-left" else width - margin - label_width
    y = height - margin - label_height
    # Only sample the destination beneath visible artwork, not its empty viewBox.
    with Image.open(asset) as original:
        mask = original.convert("RGBA").getchannel("A").resize(
            (label_width, label_height), Image.Resampling.LANCZOS
        ).point(lambda v: 255 if v >= 64 else 0)
    base = image.convert("RGBA")
    patch = base.crop((x, y, x + label_width, y + label_height))
    matte = Image.new("RGBA", patch.size, "white")
    matte.alpha_composite(patch)
    mean = ImageStat.Stat(matte.convert("RGB"), mask=mask).mean
    background = _luminance(mean)
    scores = {"positive": _contrast(background, _luminance((51, 51, 51))),
              "negative": _contrast(background, 1.0)}
    selected_style = max(scores, key=scores.get) if style == "auto" else style
    asset = ASSETS / f"ai-{label}-{selected_style}.png"
    with Image.open(asset) as original:
        artwork = original.convert("RGBA").resize(
            (label_width, label_height), Image.Resampling.LANCZOS
        )
    base.alpha_composite(artwork, (x, y))
    return base, {
        "type": f"AI {label}",
        "style": selected_style,
        "asset": asset.name,
        "corner": corner,
        "box": [x, y, x + label_width, y + label_height],
        "margin": margin,
        "estimated_contrast": round(scores[selected_style], 2) if selected_style in scores else None,
        "visual_legibility_verified": False,
        "downstream_crops_verified": False,
    }


def export_image(source: Path, destination: Path, kind: str, label: str = "created",
                 label_style: str = "auto", corner: str = "bottom-right",
                 label_width: int | None = None, margin: int | None = None,
                 label_reason: str | None = None) -> dict:
    sizes = {"title": (1920, 1080), "avatar": (240, 240)}
    ratios = {"title": (16, 9), "avatar": (1, 1)}
    target = sizes[kind]
    if label not in ("created", "modified", "none"):
        raise ValueError("Unknown label type.")
    if label_style not in ("auto", "positive", "negative", "negative-transparent"):
        raise ValueError("Unknown label style.")
    if corner not in ("bottom-left", "bottom-right"):
        raise ValueError("Use a bottom corner for the label.")
    if label in ("modified", "none") and not (label_reason and label_reason.strip()):
        raise ValueError("Document the source/edit classification with --label-reason.")
    if source.resolve() == destination.resolve():
        raise ValueError("Keep the source file; choose a separate output path.")
    if destination.exists():
        raise FileExistsError("Output exists; choose a new version instead of overwriting.")
    if destination.suffix.lower() != ".png":
        raise ValueError("The output filename must end in .png.")
    if not destination.parent.is_dir():
        raise ValueError("Create the output directory before exporting.")

    with Image.open(source) as original:
        original.load()
        original_size = original.size
        original_format = original.format
        orientation = original.getexif().get(274, 1)
        image = ImageOps.exif_transpose(original)
        width, height = image.size
        rw, rh = ratios[kind]
        unit = min(width // rw, height // rh)
        if unit < 1:
            raise ValueError("Source is too small for the required crop ratio.")
        crop_width, crop_height = rw * unit, rh * unit
        left = (width - crop_width) // 2
        top = (height - crop_height) // 2
        box = (left, top, left + crop_width, top + crop_height)
        unchanged = (label == "none" and original_format == "PNG"
                     and orientation == 1 and image.size == target)
        label_info = {"type": "none", "reason": label_reason}
        if unchanged:
            with source.open("rb") as incoming, destination.open("xb") as outgoing:
                shutil.copyfileobj(incoming, outgoing)
        else:
            result = image.crop(box)
            if result.size != target:
                result = result.resize(target, Image.Resampling.LANCZOS)
            if result.mode not in ("RGB", "RGBA"):
                result = result.convert("RGBA" if "transparency" in result.info else "RGB")
            if label != "none":
                result, label_info = _apply_label(
                    result, label, label_style, corner,
                    label_width if label_width is not None else (192 if kind == "title" else 88),
                    margin if margin is not None else (24 if kind == "title" else 8),
                )
                label_info["reason"] = label_reason or "Newly AI-created image."
            with destination.open("xb") as outgoing:
                result.save(outgoing, format="PNG")

    with Image.open(destination) as check:
        check.load()
        if check.format != "PNG" or check.size != target:
            raise ValueError("Export verification failed.")

    return {
        "filename": destination.name,
        "source_dimensions": list(original_size),
        "oriented_dimensions": [width, height],
        "crop_box": list(box),
        "dimensions": list(target),
        "format": "PNG",
        "bytes": destination.stat().st_size,
        "sha256": hashlib.sha256(destination.read_bytes()).hexdigest(),
        "source_copied_unchanged": unchanged,
        "ai_label": label_info,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--kind", choices=("title", "avatar"), default="title")
    parser.add_argument("--label", choices=("created", "modified", "none"), default="created")
    parser.add_argument("--label-reason", help="Required for modified or none; record actual provenance/edit.")
    parser.add_argument("--label-style", choices=("auto", "positive", "negative", "negative-transparent"), default="auto")
    parser.add_argument("--corner", choices=("bottom-left", "bottom-right"), default="bottom-right")
    parser.add_argument("--label-width", type=int, help="Width of the complete original artwork in output pixels.")
    parser.add_argument("--margin", type=int, help="Inset from the bottom and side in output pixels.")
    args = parser.parse_args()
    try:
        print(json.dumps(export_image(
            args.source, args.destination, args.kind, args.label, args.label_style,
            args.corner, args.label_width, args.margin, args.label_reason,
        ), ensure_ascii=False))
    except (ValueError, OSError) as error:
        parser.exit(1, f"Export failed: {error}\n")
