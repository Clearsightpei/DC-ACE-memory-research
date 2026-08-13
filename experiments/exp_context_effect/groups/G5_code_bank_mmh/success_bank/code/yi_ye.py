"""Bank primitive: 业 (yè, 'industry' — 5 strokes: 2 shu + 2 dian + heng).

Promoted from p3_char_0184_业 (G5 B7 **A** verdict, 2026-08-08).
Recipe: MMH anchors verbatim + stroke-primitive layer (P-A-006).
Reuse targets: 业, 邺, 亚 (sibling family with top-block + baseline heng).
Two tall central verticals stop ~11-14 px above baseline heng (N joints).
"""

from PIL import ImageDraw

from shu import draw_shu
from heng import draw_heng
from dian import draw_dian


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_yi_ye(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: left tall vertical
    draw_shu(draw, _tx(103, 107, ox, oy, scale), _tx(114, 268, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s2: right tall vertical
    draw_shu(draw, _tx(161, 84, ox, oy, scale), _tx(166, 266, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s3: left outer short slanted dian (upper-left → lower-right toward left shu)
    draw_dian(draw, _tx(57, 178, ox, oy, scale), _tx(88, 212, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(2, int(7 * scale)),
              bow=max(2, int(3 * scale)), steps=40)
    # s4: right outer short slanted dian (pie-like, upper-right → lower-left)
    draw_dian(draw, _tx(232, 147, ox, oy, scale), _tx(197, 205, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(2, int(7 * scale)),
              bow=max(2, int(3 * scale)), steps=40)
    # s5: long baseline heng
    draw_heng(draw, _tx(38, 279, ox, oy, scale), _tx(268, 280, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(11 * scale)))
