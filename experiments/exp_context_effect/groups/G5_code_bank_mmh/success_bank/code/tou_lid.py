"""Bank primitive: 亠 (tou, 'lid' — 2 strokes: dian + heng).

Promoted from p2_radical_033_亠 (G5 B1 PASS, 2026-08-08). VERY HIGH-REUSE:
top radical in 六/亡/交/京/亦/... — dot sitting above a long horizontal.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_tou(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    s1_head = _tx(120.4, 128.0, ox, oy, scale)
    s1_tail = _tx(160.8, 155.9, ox, oy, scale)
    s2_head = _tx(46.3, 193.1, ox, oy, scale)
    s2_tail = _tx(258.4, 185.7, ox, oy, scale)
    draw_dian(draw, s1_head, s1_tail,
              w_head=3 * scale, w_tail=8 * scale, bow=5 * scale, steps=48)
    draw_heng(draw, s2_head, s2_tail,
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
