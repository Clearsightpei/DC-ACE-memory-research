"""Bank primitive: 川 (chuan, 'river' — 3 strokes: pie + shu + shu, all separated).

Promoted from p2_radical_043_川 (G5 B1 PASS, 2026-08-08).
Three separated near-vertical strokes; no joints.
"""

from PIL import ImageDraw

from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_chuan(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    draw_pie(draw,
             _tx(100, 108, ox, oy, scale), _tx(68, 258, ox, oy, scale),
             bow_perp=14 * scale, w_head=5 * scale, w_tail=2 * scale)
    draw_shu(draw,
             _tx(142, 122, ox, oy, scale), _tx(150, 218, ox, oy, scale),
             width=max(2, int(5 * scale)))
    draw_shu(draw,
             _tx(200, 108, ox, oy, scale), _tx(210, 282, ox, oy, scale),
             width=max(2, int(5 * scale)), top_curl=False)
