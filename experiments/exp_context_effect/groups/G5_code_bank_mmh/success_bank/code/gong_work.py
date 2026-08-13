"""Bank primitive: 工 (gong, 'work' — 3 strokes: heng + shu + heng).

Promoted from p2_radical_049_工 (G5 B1 PASS, 2026-08-08). HIGH-REUSE:
component of 左/式/巧/项/... The vertical sits between the two horizontals
with N-gaps on both ends (no piercing).
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_gong_work(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    s1_head = _tx(87, 114, ox, oy, scale)
    s1_tail = _tx(225, 102, ox, oy, scale)
    s2_head = _tx(142, 122, ox, oy, scale)
    s2_tail = _tx(144, 236, ox, oy, scale)
    s3_head = _tx(31, 249, ox, oy, scale)
    s3_tail = _tx(278, 248, ox, oy, scale)
    draw_heng(draw, s1_head, s1_tail,
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    draw_shu(draw, s2_head, s2_tail, width=max(2, int(7 * scale)))
    draw_heng(draw, s3_head, s3_tail,
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
