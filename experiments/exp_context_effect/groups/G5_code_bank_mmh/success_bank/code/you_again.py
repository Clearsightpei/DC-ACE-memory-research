"""Bank primitive: 又 (you, 'again' — 2 strokes: heng_pie + na, P-joint).

Promoted from p2_radical_037_又 (G5 B1 PASS, 2026-08-08).
Uses the new heng_pie.py stroke primitive (also promoted from this item).
"""

from PIL import ImageDraw

from heng_pie import draw_heng_pie
from na import draw_na


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_you(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    s1_head = _tx(77.9, 116.9, ox, oy, scale)
    s1_tail = _tx(42.5, 276.0, ox, oy, scale)
    s2_head = _tx(79.4, 139.7, ox, oy, scale)
    s2_tail = _tx(285.4, 278.9, ox, oy, scale)
    draw_heng_pie(draw, s1_head, s1_tail)
    draw_na(draw, s2_head, s2_tail,
            bow_perp=10 * scale, w_head=4 * scale, w_tail=12 * scale, steps=90)
