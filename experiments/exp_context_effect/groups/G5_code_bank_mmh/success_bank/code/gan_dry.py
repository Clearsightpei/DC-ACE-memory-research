"""Bank primitive: 干 (gan, 'dry' — 3 strokes: heng + heng + shu).

Promoted from p2_radical_048_干 (G5 B1 PASS, 2026-08-08). Distinguisher
from 于/千: 干 has TWO horizontals + one vertical piercing through both.
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_gan(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    draw_heng(draw,
              _tx(92, 83, ox, oy, scale), _tx(217, 69, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(11 * scale)))
    draw_heng(draw,
              _tx(30, 169, ox, oy, scale), _tx(274, 159, ox, oy, scale),
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(12 * scale)))
    draw_shu(draw,
             _tx(136, 93, ox, oy, scale), _tx(148, 293, ox, oy, scale),
             width=max(2, int(8 * scale)))
