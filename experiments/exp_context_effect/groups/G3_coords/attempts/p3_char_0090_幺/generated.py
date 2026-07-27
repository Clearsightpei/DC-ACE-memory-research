# p3_char_0090_幺 (yāo) — revised.
# 3 strokes: (1) upper 撇折 (小), (2) lower 撇折 (小), (3) 点.
# Rev1: enlarge, centre better, make 折 arc-like (single bezier) so
# the 撇 sweeps into the 折 smoothly rather than a sharp V. Keep
# lines relatively thin per MMH GT style.

import os, sys, math
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
BANK_CODE = os.path.abspath(os.path.join(HERE, "..", "..", "success_bank", "code"))
sys.path.insert(0, BANK_CODE)

from _shared_helpers import tapered_bezier, tapered_line, to_px  # noqa: E402


def _bow_bezier(draw, p0, p2, bow_perp, w_head, w_tail, n=48):
    """Quadratic bezier with control offset perpendicular to chord."""
    x0, y0 = p0
    x1, y1 = p2
    mx = (x0 + x1) / 2.0
    my = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    p1 = (mx + perp_x * bow_perp, my + perp_y * bow_perp)
    tapered_bezier(draw, p0, p1, p2, w_head, w_tail, n=n)


def draw_yao(t=None, ox=0, oy=0, scale=1.0):
    img = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(img)

    # ---- Upper 撇折 ----
    # Curved 撇 down-left, sweeping into a rightward折.
    # Head upper-right, tail mid-lower-left; then 折 curves right.
    up_head = (25 + ox, 100 + oy)
    up_pivot = (-25 + ox, 45 + oy)
    up_end = (25 + ox, 25 + oy)
    _bow_bezier(draw, up_head, up_pivot, bow_perp=-6.0,
                w_head=5.5, w_tail=3.0, n=40)
    _bow_bezier(draw, up_pivot, up_end, bow_perp=-5.0,
                w_head=3.0, w_tail=2.5, n=32)

    # ---- Lower 撇折 ----
    # Larger. Head just below upper, slight right shift.
    lo_head = (25 + ox, 5 + oy)
    lo_pivot = (-45 + ox, -55 + oy)
    lo_end = (30 + ox, -70 + oy)
    _bow_bezier(draw, lo_head, lo_pivot, bow_perp=-8.0,
                w_head=6.0, w_tail=3.0, n=48)
    _bow_bezier(draw, lo_pivot, lo_end, bow_perp=-7.0,
                w_head=3.0, w_tail=2.5, n=36)

    # ---- 点 ---- bottom-right of the whole char, small teardrop.
    tapered_line(
        draw,
        (35 + ox, -85 + oy),
        (55 + ox, -110 + oy),
        1.5, 6.5, n=20,
    )

    return img


if __name__ == "__main__":
    img = draw_yao()
    out = os.path.join(HERE, "01_幺.png")
    img.save(out)
    print("wrote", out)
