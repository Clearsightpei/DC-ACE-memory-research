"""Bank primitive: 並 (bìng, "and, together") — 8 strokes.

Promoted from p3_char_0360_並 (G5 B10 **A** 2026-08-09). A-recipe:
P-A-006 stroke-primitive layer + P-A-007-v2 hard-check on ya_asia
(stroke-count mismatch — 亚 is 6 strokes, 並 is 8; whole-radical
skipped correctly per P-A-008). Sibling of 业/亚. Reuse: rare
traditional variant, but records the 8-stroke 並-vs-6-stroke-亚 sibling
distinction for the 業/普/普 family.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_bing_and(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top-left short pie (down-right)
    draw_pie(draw, _tx(98.4, 76.8, ox, oy, scale),
             _tx(124.2, 105.2, ox, oy, scale),
             bow_perp=4, w_head=4, w_tail=3, steps=48)
    # s2: top-inner short pie (down-left)
    draw_pie(draw, _tx(189.3, 57.1, ox, oy, scale),
             _tx(156.2, 123.0, ox, oy, scale),
             bow_perp=6, w_head=4, w_tail=3, steps=56)
    # s3: middle upper crossbeam heng
    draw_heng(draw, _tx(69.7, 139.2, ox, oy, scale),
              _tx(236.4, 128.6, ox, oy, scale),
              width_head=7, width_tail=8)
    # s4: LEFT long vertical
    draw_shu(draw, _tx(111.6, 144.1, ox, oy, scale),
             _tx(119.8, 271.9, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s5: RIGHT long vertical
    draw_shu(draw, _tx(163.5, 136.5, ox, oy, scale),
             _tx(167.0, 268.1, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s6: left-outer dian
    draw_dian(draw, _tx(65.3, 192.8, ox, oy, scale),
              _tx(89.9, 230.6, ox, oy, scale),
              w_head=3, w_tail=7, bow=3, steps=40)
    # s7: right-outer dian (down-left)
    draw_dian(draw, _tx(223.5, 165.2, ox, oy, scale),
              _tx(181.1, 227.9, ox, oy, scale),
              w_head=3, w_tail=7, bow=3, steps=40)
    # s8: wide bottom heng
    draw_heng(draw, _tx(33.4, 285.1, ox, oy, scale),
              _tx(273.9, 282.7, ox, oy, scale),
              width_head=9, width_tail=10)
