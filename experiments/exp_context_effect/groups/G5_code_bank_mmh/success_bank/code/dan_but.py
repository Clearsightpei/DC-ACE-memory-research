"""Bank primitive: 但 (dàn, "but") — 7 strokes.

Promoted from p3_char_0324_但 (G5 B9 PASS 2026-08-09). HIGH-REUSE:
亻+旦 template. 旦 sub-structure (日 box + long bottom heng) also
useful for 旦/亘/宣 family lookups.
"""

from PIL import ImageDraw

from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_dan_but(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 亻 pie
    draw_pie(draw, _tx(91, 61, ox, oy, scale),
             _tx(18, 195, ox, oy, scale),
             bow_perp=13, w_head=9, w_tail=3, steps=90)
    # s2 亻 shu
    draw_shu(draw, _tx(76, 141, ox, oy, scale),
             _tx(76, 289, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s3 left shu of 日
    draw_shu(draw, _tx(130, 110, ox, oy, scale),
             _tx(151, 204, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s4 heng_zhe_box of 日
    draw_heng_zhe_box(draw, _tx(149, 122, ox, oy, scale),
                      _tx(218, 195, ox, oy, scale),
                      width=max(2, int(7 * scale)))
    # s5 middle heng inside 日
    draw_heng(draw, _tx(152, 157, ox, oy, scale),
              _tx(202, 147, ox, oy, scale),
              width_head=6, width_tail=7)
    # s6 bottom heng of 日
    draw_heng(draw, _tx(158, 197, ox, oy, scale),
              _tx(208, 192, ox, oy, scale),
              width_head=7, width_tail=8)
    # s7 long bottom heng of 旦
    draw_heng(draw, _tx(104, 250, ox, oy, scale),
              _tx(278, 247, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
