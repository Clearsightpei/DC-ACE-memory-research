"""Bank primitive: 千 (qian, 'thousand' — 3 strokes: pie + heng + shu).

Promoted from p3_char_0075_千 (G5 B4 PASS via P-A-002 route, 2026-08-08).
Sibling of 干 / 于: 千 has pie (top-right → down-left) instead of 干's
second heng. Distinguishing feature = top-most stroke class.
"""

from PIL import ImageDraw

from pie import draw_pie
from heng import draw_heng
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_qian(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: pie — TR → ML sweep
    draw_pie(draw,
             _tx(202, 72, ox, oy, scale), _tx(84, 108, ox, oy, scale),
             bow_perp=10, w_head=max(2, int(9 * scale)),
             w_tail=max(2, int(3 * scale)), steps=90)
    # s2: long middle heng
    draw_heng(draw,
              _tx(30, 172, ox, oy, scale), _tx(272, 165, ox, oy, scale),
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(12 * scale)))
    # s3: central shu
    draw_shu(draw,
             _tx(138, 99, ox, oy, scale), _tx(150, 295, ox, oy, scale),
             width=max(2, int(8 * scale)))
