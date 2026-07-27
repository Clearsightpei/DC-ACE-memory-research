# 心 (xin, heart) — radical.
# Structure per GT:
#   1. 左点  — small dot on the lower-left, angling down-left (head upper-right, tail lower-left)
#   2. 卧钩 — lying hook: shallow arc dipping down from left to right, tiny hook back up-left
#   3. 中点 — small dot above the middle of the bowl, angled
#   4. 右点 — dot on the upper-right, standard head-upper-left → tail-lower-right
#
# G3 approach: use the wo_gou bank primitive for the bowl; inline
# three custom dot strokes tuned per form_catalog (all short dots with
# distinct orientations). Numbers are chosen deliberately per TR1-TR3.

import os, sys
from PIL import Image, ImageDraw

# Add success_bank/code to path so we can import bank primitives.
BANK = os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
sys.path.insert(0, os.path.abspath(BANK))

from wo_gou import draw_wo_gou  # noqa: E402


CANVAS = 300


def to_pixel(ox, oy):
    """Math coords (center origin, +y up) -> PIL pixel."""
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def tapered_bezier(draw, p0, p1, p2, w0, w1, n=32):
    """Quadratic Bezier with linearly interpolated width."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = to_pixel(bx, by)
        if prev is not None:
            w = w0 * (1 - u) + w1 * u
            w_int = max(1, int(round(w)))
            draw.line([prev, pt], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))
        prev = pt


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ------------------------------------------------------------------
    # Stroke 2: 卧钩 — the bowl. Use wo_gou primitive.
    # Bowl center at ~ math (0, -20), scale 0.85 (radical size, not full canvas).
    # ------------------------------------------------------------------
    draw_wo_gou(d, ox=-5, oy=-20, scale=0.85)

    # ------------------------------------------------------------------
    # Stroke 1: 左点 — small dot on lower-left of bowl.
    # In GT the left dot sits down-left of the bowl's start.
    # Head at upper-right, tail lower-left — mirrored variant.
    # ------------------------------------------------------------------
    # head: math (-75, +5); tail: math (-90, -25)
    tapered_bezier(
        d,
        p0=(-75, 5),          # thin head upper-right
        p1=(-82, -8),         # slight bow
        p2=(-92, -28),        # heavier tail lower-left
        w0=2, w1=8,
    )

    # ------------------------------------------------------------------
    # Stroke 3: 中点 — small dot above the middle of the bowl.
    # In GT it sits just above the bowl arc, tilted slightly right.
    # Re-centered and shortened per self-check.
    # ------------------------------------------------------------------
    tapered_bezier(
        d,
        p0=(-15, 25),
        p1=(-10, 18),
        p2=(-2, 8),
        w0=2, w1=7,
    )

    # ------------------------------------------------------------------
    # Stroke 4: 右点 — dot on upper-right of the bowl.
    # In GT it curves like a short 撇 (thin toward lower-left).
    # Head thick upper-right, tail thin lower-left — mirrored orientation
    # per form_catalog note on 心-family right stroke.
    # ------------------------------------------------------------------
    tapered_bezier(
        d,
        p0=(55, 40),           # thick head upper-right
        p1=(50, 25),
        p2=(42, 8),            # thin tail lower-left
        w0=8, w1=2,
    )

    out = os.path.join(os.path.dirname(__file__), "01_心.png")
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
