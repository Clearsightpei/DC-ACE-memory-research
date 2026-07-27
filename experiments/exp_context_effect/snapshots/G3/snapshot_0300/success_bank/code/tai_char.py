# tai_char.py — 太 (tài), 4 strokes: 一 + 丿 + ㇏ + 丶.
# PASSed at p3_char_0128_太 (B5, pos 268). 大-family X-crossing with kiss_apex
# at u_pie=0.24 (crossing on heng), plus a dian in the crotch below.
from _shared_helpers import (
    variant_pie, variant_na, variant_dian, kiss_apex, tapered_line,
)


def draw_tai_char(t, ox=0, oy=0, scale=1.0):
    """太 — 大 X-crossing + crotch dian."""
    def P(x, y):
        return (ox + x * scale, oy + y * scale)

    tapered_line(t, P(-95, +40), P(+95, +37), w0=6, w1=8, n=40)

    pie_head = P(+30, +85)
    pie_tail = P(-95, -115)
    na_tail = P(+95, -110)
    pie_h, na_h = kiss_apex(pie_head, pie_tail, na_tail,
                            u_pie=0.24, bow_pie=-6.0)
    variant_pie(t, head=pie_h, tail=pie_tail,
                bow_perp=-6.0, w_head=8.0, w_tail=1.0)
    variant_na(t, head=na_h, tail=na_tail,
               bow_perp=+8.0, w_head=2.0, w_belly=12.0,
               w_tail=2.0, belly_u=0.72)

    variant_dian(t, head=P(-8, -55), tail=P(+14, -78),
                 w_head=3.0, w_tail=9.0, bow_perp=-2.0)
