"""Bank primitive: 人 (ren, 'person' — 2 strokes, pie + na with N-joint at top).

Promoted from p2_radical_028_人 (G5 B1 PASS, 2026-08-08).
Reference layout preserves the PASSing 300x300 render.

Differs from 八 (which has clean separation): 人's two strokes meet near
the top with a small N-gap (~20 px on reference scale).
"""

from PIL import ImageDraw

from pie import draw_pie
from na import draw_na


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_ren(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    pie_head = _tx(141.5, 84.4, ox, oy, scale)
    pie_tail = _tx(21.1, 272.2, ox, oy, scale)
    na_head = _tx(138.9, 160.3, ox, oy, scale)
    na_tail = _tx(288.9, 273.6, ox, oy, scale)
    draw_pie(draw, pie_head, pie_tail,
             bow_perp=14 * scale, w_head=9 * scale, w_tail=3 * scale)
    draw_na(draw, na_head, na_tail,
            bow_perp=12 * scale, w_head=4 * scale, w_tail=11 * scale)
