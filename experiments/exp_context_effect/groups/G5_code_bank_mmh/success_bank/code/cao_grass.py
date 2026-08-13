"""Bank primitive: 艹 (cao, 'grass-top' — 3 strokes: heng + shu + shu).

Promoted from p2_radical_039_艹 (G5 B1 PASS, 2026-08-08). VERY HIGH-REUSE:
top radical in 花/草/茶/苹/... The two verticals extend both above and below
the horizontal (per GT, not MMH — MMH underspecs vertical span).
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_cao(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    h1_head = _tx(47, 185, ox, oy, scale)
    h1_tail = _tx(251, 180, ox, oy, scale)
    draw_heng(draw, h1_head, h1_tail,
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    draw_shu(draw,
             _tx(108, 115, ox, oy, scale), _tx(118, 245, ox, oy, scale),
             width=max(2, int(8 * scale)))
    draw_shu(draw,
             _tx(185, 115, ox, oy, scale), _tx(178, 245, ox, oy, scale),
             width=max(2, int(8 * scale)))
