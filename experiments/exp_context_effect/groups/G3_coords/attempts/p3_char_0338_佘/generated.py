# p3_char_0338_佘 (shé, surname) — 7 strokes.
# Structure (from GT):
#   1) 人-roof at top: pie + na kissing at apex (~ +115) with legs
#      splaying out over top ~55% of canvas.
#   2) 一 short heng in middle (~y=-5).
#   3) bottom 示-like group: a centered vertical (shu), a left short
#      pie-dot, a right dot.
#
# Bank use: pie + na (like tong_same / ji_meet_char) for the 人-roof.
# Bottom hand-inlined (thin uniform, MMH-style).

import os
import sys
from PIL import Image, ImageDraw

_BANK = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code"
))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from pie import draw_pie   # noqa: E402
from na import draw_na     # noqa: E402

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_line(t, p0, p1, w0=3.0, w1=3.0, n=32):
    x0, y0 = p0
    x1, y1 = p1
    prev = None
    for i in range(n + 1):
        u = i / n
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        px, py = _to_pixel(x, y)
        w = w0 + (w1 - w0) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_she(t, ox=0.0, oy=0.0, scale=1.0):
    # ---- 人-roof ----
    # pie canonical head (65, 90), tail (-45, -85). scale ~0.85.
    # Place apex near (0, +115): ox_pie = 0 - 65*0.85 = -55; oy_pie = 115 - 90*0.85 = 38.5
    draw_pie(t, ox=ox + -55 * scale, oy=oy + 38 * scale, scale=0.85 * scale)
    # na canonical head (-70, 80), tail (80, -90). scale ~0.85.
    # Place apex near (0, +115): ox_na = 0 - (-70)*0.85 = 59; oy_na = 115 - 80*0.85 = 47
    draw_na(t, ox=ox + 59 * scale, oy=oy + 47 * scale, scale=0.85 * scale)

    # ---- middle 一 (short heng) ----
    _tapered_line(t,
                  (ox + -30 * scale, oy + -5 * scale),
                  (ox + +30 * scale, oy + -5 * scale),
                  w0=3.0, w1=3.0, n=24)

    # ---- bottom 示-like: shu + left dot + right dot ----
    # centered shu from (0, -20) to (0, -115)
    _tapered_line(t,
                  (ox + 0 * scale, oy + -20 * scale),
                  (ox + 0 * scale, oy + -115 * scale),
                  w0=3.5, w1=3.5, n=28)
    # left dot: short pie-like from (-15, -45) to (-40, -100)
    _tapered_line(t,
                  (ox + -15 * scale, oy + -45 * scale),
                  (ox + -42 * scale, oy + -100 * scale),
                  w0=4.0, w1=2.0, n=20)
    # right dot: short na-like from (+15, -45) to (+40, -100)
    _tapered_line(t,
                  (ox + 15 * scale, oy + -45 * scale),
                  (ox + 42 * scale, oy + -100 * scale),
                  w0=2.5, w1=4.5, n=20)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_she(d, ox=0, oy=0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佘.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
