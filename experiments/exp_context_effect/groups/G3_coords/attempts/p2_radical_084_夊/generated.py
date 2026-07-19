# p2_radical_084_夊 (sui — walk slowly), 3 strokes.
# G3 coord format. Strokes:
#   1. Short 撇 (top-left tip, going down-left).
#   2. 横撇/折 that comes across then down-left forming the "X" cross with na.
#   3. Long 捺 stretching from upper crossing area down to lower-right.
#
# Bank use: dian/pie/na primitives don't quite fit this radical's specific
# geometry (very stretched na, short zigzag top). Following the shared_rules
# "supplementary" guidance, I inline all three strokes fresh with tapered
# beziers, matching the GT layout.

import os
import sys

from PIL import Image, ImageDraw

_CANVAS = 300


def _to_pixel_scaled(bx, by, ox, oy, scale):
    px = _CANVAS / 2 + ox + bx * scale
    py = _CANVAS / 2 - (oy + by * scale)
    return px, py


def _tapered_bezier(t, x0, y0, mx, my, x1, y1, w_head, w_tail,
                    ox, oy, scale, n=50, belly=None, w_belly=None):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel_scaled(bx, by, ox, oy, scale)
        if belly is not None and w_belly is not None:
            if u <= belly:
                w = w_head + (w_belly - w_head) * (u / belly)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly) / (1 - belly))
        else:
            w = w_head + (w_tail - w_head) * u
        w = w * scale
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_sui(t, ox=0.0, oy=0.0, scale=1.0):
    """夊 radical: 3 strokes forming an X-like shape with tail."""

    # Stroke 1: short 撇 at the top — small down-left tick.
    # Head at (~+8, +90), tapers to tip at (~-15, +55).
    _tapered_bezier(t,
                    x0=8.0, y0=90.0,
                    mx=-3.0, my=72.0,
                    x1=-15.0, y1=55.0,
                    w_head=5, w_tail=2,
                    ox=ox, oy=oy, scale=scale, n=25)

    # Stroke 2: 横撇 — small horizontal from left tip area, curving to a
    # long pie sweeping down-left to lower-left region.
    # Segment A: small horizontal-hook at top.
    _tapered_bezier(t,
                    x0=-18.0, y0=65.0,
                    mx=0.0, my=70.0,
                    x1=18.0, y1=55.0,
                    w_head=3, w_tail=6,
                    ox=ox, oy=oy, scale=scale, n=20)
    # Segment B: long pie from that head down to lower-left corner.
    _tapered_bezier(t,
                    x0=18.0, y0=55.0,
                    mx=-25.0, my=-5.0,
                    x1=-90.0, y1=-95.0,
                    w_head=7, w_tail=2,
                    ox=ox, oy=oy, scale=scale, n=60)

    # Stroke 3: 捺 — long right-falling sweep starting near the crossing
    # region, extending far to the lower right with a strong belly.
    x0, y0 = -25.0, 20.0
    x1, y1 = 110.0, -100.0
    mx = (x0 + x1) / 2.0 + 5.0
    my = (y0 + y1) / 2.0 - 18.0
    _tapered_bezier(t,
                    x0=x0, y0=y0, mx=mx, my=my, x1=x1, y1=y1,
                    w_head=3, w_tail=2,
                    ox=ox, oy=oy, scale=scale,
                    n=75, belly=0.65, w_belly=12)


def main():
    img = Image.new("RGB", (_CANVAS, _CANVAS), "white")
    draw = ImageDraw.Draw(img)
    draw_sui(draw, ox=0.0, oy=-10.0, scale=1.0)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_夊.png")
    img.save(out)


if __name__ == "__main__":
    main()
