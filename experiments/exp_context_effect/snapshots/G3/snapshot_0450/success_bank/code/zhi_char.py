# zhi_char.py — 之 (zhī), 3 strokes: 点 + 横撇 + 平捺.
# PASSed at p3_char_0039_之 (B4). Uses variant helpers.
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from _shared_helpers import (
    variant_dian, variant_na, tapered_line, tapered_bezier, to_px,
)  # noqa: E402


def draw_zhi_char(t, ox=0, oy=0, scale=1.0):
    def P(x, y):
        return (ox + x * scale, oy + y * scale)
    variant_dian(t, head=P(+2, +112), tail=P(+22, +92),
                 w_head=2.5, w_tail=9.0, bow_perp=-2.0)
    heng_left = P(-80, +40)
    corner = P(+40, +50)
    pie_tail = P(-30, -35)
    tapered_line(t, heng_left, corner, w0=4.0, w1=8.0, n=32)
    cx, cy = to_px(*corner)
    r = 5.0
    t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    mid = ((corner[0] + pie_tail[0]) / 2 - 4,
           (corner[1] + pie_tail[1]) / 2 + 4)
    tapered_bezier(t, corner, mid, pie_tail, w_head=8.0, w_tail=2.0, n=48)
    tapered_line(t, P(-105, -55), P(-70, -70), w0=2.0, w1=6.0, n=16)
    variant_na(t, head=P(-70, -70), tail=P(+120, -55),
               bow_perp=-10.0, w_head=3.0, w_belly=13.0,
               w_tail=2.0, belly_u=0.75, n=72)
