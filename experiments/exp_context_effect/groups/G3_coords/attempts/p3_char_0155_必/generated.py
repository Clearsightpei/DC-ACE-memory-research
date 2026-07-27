# p3_char_0155_必 (bì, "must")
# Composition: 心 (wo_gou bowl + 3 dots) + diagonal 撇 (pie) crossing bowl.
# Uses xin.py's dot pattern; adds a tapered 撇 that starts upper-right
# and swings down-left through the middle of the bowl.

import os
import sys

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from PIL import Image, ImageDraw  # noqa: E402
from wo_gou import draw_wo_gou  # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def _tb(draw, p0, p1, p2, w0, w1, n=32):
    """Tapered quadratic Bezier."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = _to_pixel(bx, by)
        if prev is not None:
            w = w0 * (1 - u) + w1 * u
            wi = max(1, int(round(w)))
            draw.line([prev, pt], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))
        prev = pt


def draw_bi(d, ox=0, oy=0, scale=1.0):
    """Draw 必. Bowl (卧钩) + central 撇 crossing + 3 dots (left, top-mid, right)."""
    # Bowl — centered lower on canvas
    draw_wo_gou(d, ox=ox - 5, oy=oy - 30, scale=0.85 * scale)

    # Central 撇 (piě) — starts high middle-top, sweeps down-left through
    # the bowl center. This is the tall diagonal stroke defining 必.
    _tb(d,
        (ox + 15, oy + 70),    # start upper (slightly right of center)
        (ox + -5, oy + 10),    # middle (through bowl)
        (ox + -50, oy + -55),  # tail lower-left
        w0=4, w1=2, n=40)

    # Top-mid dot — small dian to right of 撇 top, angled down-right
    _tb(d, (ox + 30, oy + 50), (ox + 35, oy + 38), (ox + 42, oy + 25), 2, 7)

    # Left dot (long down-left dian outside bowl on left)
    _tb(d, (ox + -68, oy + 8), (ox + -75, oy + -8), (ox + -85, oy + -28), 2, 7)

    # Right dot (long down-right dian outside bowl on right)
    _tb(d, (ox + 58, oy + 15), (ox + 65, oy + 2), (ox + 75, oy + -15), 7, 2)


if __name__ == "__main__":
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_bi(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(__file__), "01_必.png")
    img.save(out)
    print(f"Wrote {out}")
