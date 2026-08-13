"""Bank primitive: 者 (zhě, "one who") — 8 strokes = 耂 top + 日 bottom.

Promoted from p3_char_0373_者 (G5 B10 PASS 2026-08-09). VERY HIGH REUSE:
extends to 都/都/署/著/煮/暑 family (all share 者 sub-component).
Composition: 4 inline strokes (heng + shu + heng + long pie) forming
耂 + `draw_ri` at (ox=+70, oy=+150, scale=0.52) for bottom 日.
"""

from PIL import ImageDraw

from heng import draw_heng
from pie import draw_pie
from ri_sun import draw_ri
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_zhe_person(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top heng of 耂
    draw_heng(draw, _tx(96, 118, ox, oy, scale),
              _tx(189, 108, ox, oy, scale),
              width_head=7, width_tail=8)
    # s2: short shu (top of 耂)
    draw_shu(draw, _tx(134, 54, ox, oy, scale),
             _tx(141, 156, ox, oy, scale),
             width=max(2, int(6 * scale)))
    # s3: main wide heng
    draw_heng(draw, _tx(34, 173, ox, oy, scale),
              _tx(274, 157, ox, oy, scale),
              width_head=8, width_tail=9)
    # s4: long pie descender
    draw_pie(draw, _tx(211, 82, ox, oy, scale),
             _tx(25, 275, ox, oy, scale),
             bow_perp=18, w_head=9, w_tail=3, steps=100)
    # s5-s8: 日 (bottom, via wrapper)
    draw_ri(draw, ox=ox + 70 * scale, oy=oy + 150 * scale, scale=0.52 * scale)
