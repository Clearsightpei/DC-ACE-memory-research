# men_char.py — 门 (mén), 3 strokes: 点 + 竖 + 横折钩. Inlined for tall/narrow.
# PASSed at p3_char_0063_门 (B4). NOTE: 门 radical still in errata (retry FAIL).
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from dian import draw_dian  # noqa: E402


def _tapered_line(D, p0, p1, w0, w1, steps=24):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = p0[0] + (p1[0] - p0[0]) * u0
        ya = p0[1] + (p1[1] - p0[1]) * u0
        xb = p0[0] + (p1[0] - p0[0]) * u1
        yb = p0[1] + (p1[1] - p0[1]) * u1
        w = max(1, int(round(w0 + (w1 - w0) * u0)))
        D.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def draw_men_char(t, ox=0, oy=0, scale=1.0):
    def X(x):
        return 150 + (x - 150) * scale + ox
    def Y(y):
        return 150 + (y - 150) * scale + oy
    draw_dian(t, ox=ox - 58 * scale, oy=oy + 68 * scale, scale=0.60 * scale)
    top = (X(80), Y(110)); bot = (X(76), Y(258))
    _tapered_line(t, top, bot, w0=int(9 * scale), w1=int(10 * scale), steps=32)
    t.ellipse([top[0] - 4, top[1] - 4, top[0] + 4, top[1] + 4], fill=(0, 0, 0))
    t.ellipse([bot[0] - 5, bot[1] - 5, bot[0] + 5, bot[1] + 5], fill=(0, 0, 0))
    h_left = (X(110), Y(75)); h_right = (X(230), Y(72))
    _tapered_line(t, h_left, h_right, w0=int(9 * scale),
                  w1=int(11 * scale), steps=24)
    t.ellipse([h_right[0] - 6, h_right[1] - 6, h_right[0] + 6,
               h_right[1] + 6], fill=(0, 0, 0))
    v_top = (X(230), Y(72)); v_bot = (X(228), Y(250))
    _tapered_line(t, v_top, v_bot, w0=int(11 * scale),
                  w1=int(10 * scale), steps=32)
    t.ellipse([v_bot[0] - 6, v_bot[1] - 6, v_bot[0] + 6,
               v_bot[1] + 6], fill=(0, 0, 0))
    hook_end = (v_bot[0] - 26 * scale, v_bot[1] - 20 * scale)
    _tapered_line(t, (v_bot[0] + 1, v_bot[1] + 2), hook_end,
                  w0=int(10 * scale), w1=max(1, int(2 * scale)), steps=16)
