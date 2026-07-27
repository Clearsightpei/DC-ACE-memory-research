# p3_char_0077_习 — 习 (xí, "to practice"), 3 strokes.
# Composition:
#   Stroke 1: 横折钩 — top-horizontal, corner, descending, small hook toward lower-left.
#   Stroke 2: 点 — small dot inside upper-left area (angled).
#   Stroke 3: 提 — short rising stroke inside lower area (from lower-left up to right).
#
# GT shows a compact 3-stroke character: an outer 横折钩 envelope with two
# small internal strokes clustered in the lower-left of the enclosure.
# Rendering: use bank heng_zhe_gou at a tuned (ox, oy, scale) for the envelope;
# inline the two small internal strokes as tapered segments (they are too small
# and too custom-positioned to justify a bank primitive call).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                     "..", "..", "success_bank", "code")
_BANK = os.path.abspath(_BANK)
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from heng_zhe_gou import draw_heng_zhe_gou  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_segment(draw, p0, p1, w0, w1, steps=20):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(w0 + (w1 - w0) * u0))
        pa = _to_pixel(xa, ya)
        pb = _to_pixel(xb, yb)
        draw.line([pa, pb], fill=(0, 0, 0), width=w)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)

    # Stroke 1: 横折钩 envelope. Bank primitive spans ~ x[-90,+80], y[+60,-70]
    # at scale 1.0. We want the envelope shifted slightly up-left to leave room
    # for the internal strokes at lower-left of the enclosure. Scale ~0.85 to
    # keep it within a 3-stroke compact character silhouette.
    draw_heng_zhe_gou(draw, ox=-5, oy=+15, scale=0.85)

    # Stroke 2: short 撇 — inside upper-left; small down-left curl.
    # GT shows a short arc-like mark angled from upper-right to lower-left.
    _tapered_segment(draw, (-25, 35), (-55, 15), w0=7, w1=2, steps=14)

    # Stroke 3: longer descending 撇 — from upper-mid-interior down to lower-left.
    # This is the character's dominant internal stroke.
    _tapered_segment(draw, (-5, 20), (-55, -35), w0=8, w1=2, steps=24)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_习.png")
    img.save(out_path)
    print(f"saved {out_path}")


if __name__ == "__main__":
    main()
