"""Bank primitive: 王 (wang, "king" — 4 strokes: heng+heng+shu+heng).

Promoted from p2_radical_122_王 (G5 B3 PASS 2026-08-08). Structurally
土 + one extra middle heng. Very high-reuse: 玉/珠/理/球/环/瑞/王/皇/etc.
The bottom heng is the LONGEST (王 shape marker); top short; middle
short-to-medium. Position signature; reference canvas 300x300.
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_wang(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 top heng (short)
    draw_heng(draw, _tx(86.7, 105.2, ox, oy, scale),
              _tx(217.4, 94.3, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s2 middle heng
    draw_heng(draw, _tx(97.0, 184.6, ox, oy, scale),
              _tx(206.8, 174.6, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s3 central shu shaft (pierces middle heng)
    draw_shu(draw, _tx(140.3, 113.7, ox, oy, scale),
             _tx(143.6, 252.2, ox, oy, scale),
             width=max(2, int(8 * scale)))
    # s4 bottom LONG heng (王 shape marker)
    draw_heng(draw, _tx(35.7, 266.0, ox, oy, scale),
              _tx(271.3, 264.0, ox, oy, scale),
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(11 * scale)))
