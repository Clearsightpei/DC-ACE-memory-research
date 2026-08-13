"""Bank primitive: 作 (zuò, "make") — 7 strokes.

Promoted from p3_char_0301_作 (G5 B9 PASS 2026-08-09). HIGH-REUSE:
亻+乍 template — clean straight-stroke right half per P-COMP-011.
亻 (pie + shu) + 乍 (pie + heng + shu + 2 short hengs stacked).
"""

from PIL import ImageDraw

from heng import draw_heng
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_zuo_make(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 亻 pie
    draw_pie(draw, _tx(97.3, 65.3, ox, oy, scale),
             _tx(22.0, 197.2, ox, oy, scale),
             bow_perp=14, w_head=9, w_tail=3)
    # s2 亻 shu
    draw_shu(draw, _tx(81.2, 143.0, ox, oy, scale),
             _tx(87.3, 286.5, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s3 乍 top pie
    draw_pie(draw, _tx(172.9, 57.7, ox, oy, scale),
             _tx(114.0, 179.6, ox, oy, scale),
             bow_perp=8, w_head=8, w_tail=3)
    # s4 乍 top heng
    draw_heng(draw, _tx(161.7, 137.1, ox, oy, scale),
              _tx(269.5, 120.1, ox, oy, scale),
              width_head=8, width_tail=9)
    # s5 乍 long shu (extends past canvas bottom)
    draw_shu(draw, _tx(180.5, 143.3, ox, oy, scale),
             _tx(191.9, 300.0, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s6 乍 middle short heng
    draw_heng(draw, _tx(197.8, 194.5, ox, oy, scale),
              _tx(250.5, 184.0, ox, oy, scale),
              width_head=7, width_tail=8)
    # s7 乍 bottom short heng
    draw_heng(draw, _tx(199.8, 240.5, ox, oy, scale),
              _tx(256.1, 230.0, ox, oy, scale),
              width_head=7, width_tail=8)
