"""Bank primitive: 佔 (zhàn, "occupy") — 7 strokes.

Promoted from p3_char_0334_佔 (G5 B10 **A** 2026-08-09). A-recipe:
P-A-006 stroke-primitive layer + BANK_DEVIATION on bu_divine (卜 top
of 占, aspect-skew) + kou_mouth (bottom 口, slant reversed). Both
DEVIATIONs used explicit P-A-007-v2 hard-check reasoning (P-A-008 +
P-A-009 quantitative aspect calc). Reuse: 亻+占 template; 占-family
extends to 沾/粘/店/贴/砧/苫 lookups.
"""

from PIL import ImageDraw

from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_zhan_occupy(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: 亻 pie
    draw_pie(draw, _tx(91.4, 75.3, ox, oy, scale),
             _tx(18.5, 214.7, ox, oy, scale),
             bow_perp=14, w_head=9, w_tail=3, steps=90)
    # s2: 亻 shu
    draw_shu(draw, _tx(80.6, 149.4, ox, oy, scale),
             _tx(80.6, 297.0, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s3: 卜 shu with top curl (compact vertical for 占-top)
    draw_shu(draw, _tx(166.7, 70.0, ox, oy, scale),
             _tx(174.6, 203.6, ox, oy, scale),
             width=max(2, int(7 * scale)), top_curl=True)
    # s4: 卜 dot (down-right)
    draw_pie(draw, _tx(190.1, 146.5, ox, oy, scale),
             _tx(246.1, 135.6, ox, oy, scale),
             bow_perp=-4, w_head=6, w_tail=2, steps=40)
    # s5: 口 left-shu (compact)
    draw_shu(draw, _tx(123.6, 210.1, ox, oy, scale),
             _tx(148.8, 295.3, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s6: 口 heng_zhe_box (top+right)
    draw_heng_zhe_box(draw, _tx(140.9, 211.5, ox, oy, scale),
                      _tx(219.7, 258.4, ox, oy, scale),
                      width=max(2, int(7 * scale)))
    # s7: 口 bottom heng
    draw_heng(draw, _tx(155.0, 280.4, ox, oy, scale),
              _tx(239.6, 271.0, ox, oy, scale),
              width_head=7, width_tail=8)
