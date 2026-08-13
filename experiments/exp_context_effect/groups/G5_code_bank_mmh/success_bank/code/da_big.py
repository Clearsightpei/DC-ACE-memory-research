"""Bank primitive: 大 (da, 'big' — 3 strokes: heng + pie + na).

Promoted from p2_radical_046_大 (G5 B1 PASS, 2026-08-08).
Composition: heng crosses pie mid (P-joint); na starts below heng (N-gap).
"""

from PIL import ImageDraw

from heng import draw_heng
from pie import draw_pie
from na import draw_na


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_da(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    s1_head = _tx(61.5, 165.8, ox, oy, scale)
    s1_tail = _tx(237.3, 148.5, ox, oy, scale)
    s2_head = _tx(121.9, 62.7, ox, oy, scale)
    s2_tail = _tx(40.4, 288.0, ox, oy, scale)
    s3_head = _tx(142.4, 174.0, ox, oy, scale)
    s3_tail = _tx(279.2, 287.7, ox, oy, scale)
    draw_heng(draw, s1_head, s1_tail,
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(7 * scale)))
    draw_pie(draw, s2_head, s2_tail,
             bow_perp=-22 * scale, w_head=8 * scale, w_tail=2 * scale, steps=100)
    draw_na(draw, s3_head, s3_tail,
            bow_perp=-6 * scale, w_head=3 * scale, w_tail=10 * scale, steps=100)
