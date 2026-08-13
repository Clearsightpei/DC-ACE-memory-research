"""Bank primitive: 入 (ru, 'enter' — 2 strokes, pie + na with N-joint at top).

Promoted from p2_radical_030_入 (G5 B1 PASS, 2026-08-08).
Differs from 人: 入's pie head sits at cell C (rather than TC), and the na
starts at TC — the two strokes visually meet near the TOP with the na
extending upward past the pie head.
"""

from PIL import ImageDraw

from pie import draw_pie
from na import draw_na


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_ru(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    s1_head = _tx(146.2, 150.6, ox, oy, scale)
    s1_tail = _tx(33.7, 274.2, ox, oy, scale)
    s2_head = _tx(100.2, 99.9, ox, oy, scale)
    s2_tail = _tx(284.2, 273.0, ox, oy, scale)
    draw_pie(draw, s1_head, s1_tail,
             bow_perp=10 * scale, w_head=6 * scale, w_tail=2 * scale)
    draw_na(draw, s2_head, s2_tail,
            bow_perp=10 * scale, w_head=3 * scale, w_tail=9 * scale)
