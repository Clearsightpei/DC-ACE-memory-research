# ji_meet_char.py — 亼 (jí, "meet/gather"), 3 strokes: 人-roof + 一 base.
# PASSed at p3_char_0054_亼 (B4). Uses kiss_apex — SUCCESS EXAMPLE of B3 helper.
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
from _shared_helpers import (variant_pie, variant_na, kiss_apex,
                             tapered_line)  # noqa: E402


def draw_ji_meet_char(t, ox=0, oy=0, scale=1.0):
    def P(x, y):
        return (ox + x * scale, oy + y * scale)
    pie_head = P(-2, +75)
    pie_tail = P(-90, -50)
    na_tail = P(+90, -45)
    pie_h, na_h = kiss_apex(pie_head, pie_tail, na_tail,
                            u_pie=0.0, bow_pie=-6.0)
    variant_pie(t, head=pie_h, tail=pie_tail,
                bow_perp=-6.0, w_head=4.0, w_tail=2.0)
    variant_na(t, head=na_h, tail=na_tail,
               bow_perp=+6.0, w_head=3.0, w_belly=4.0,
               w_tail=2.0, belly_u=0.7)
    tapered_line(t, P(-70, -95), P(+70, -93), w0=3, w1=3, n=32)
