# liao.py — 了 (liǎo), 2 strokes: inline 横钩 top + wan_gou descender.
# PASSed at p3_char_0009_了 (B3 pos 166).
import os
import sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from wan_gou import draw_wan_gou  # noqa: E402


def _hengou(draw, x_left, y_left, x_right, y_right, ink=11):
    steps = 24
    w_start, w_end = 5, ink
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x_left + (x_right - x_left) * t0
        ya = y_left + (y_right - y_left) * t0
        xb = x_left + (x_right - x_left) * t1
        yb = y_left + (y_right - y_left) * t1
        w = int(w_start + (w_end - w_start) * t0)
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)
    r = 7
    draw.ellipse([x_right - r, y_right - r, x_right + r, y_right + r], fill="black")
    hx_end = x_right - 14
    hy_end = y_right + 38
    hx_ctrl = x_right + 2
    hy_ctrl = y_right + 22
    hsteps = 20
    for i in range(hsteps):
        u0 = i / hsteps
        u1 = (i + 1) / hsteps

        def bez(u):
            x = (1 - u) ** 2 * x_right + 2 * (1 - u) * u * hx_ctrl + u * u * hx_end
            y = (1 - u) ** 2 * y_right + 2 * (1 - u) * u * hy_ctrl + u * u * hy_end
            return x, y
        xa, ya = bez(u0)
        xb, yb = bez(u1)
        w = max(3, int(ink - (ink - 3) * u0))
        draw.line([(xa, ya), (xb, yb)], fill="black", width=w)


def draw_liao(draw, ox=0, oy=0, scale=1.0):
    x_l = 60 + ox
    y_l = 85 + oy
    x_r = 205 + ox
    y_r = 80 + oy
    _hengou(draw, x_l, y_l, x_r, y_r, ink=11)
    draw_wan_gou(draw, ox=ox + 26, oy=oy - 62, scale=0.85 * scale)
