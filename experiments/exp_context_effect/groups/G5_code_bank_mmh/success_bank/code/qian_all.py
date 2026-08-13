"""Bank primitive: 佥 (qiān, "all") — 7 strokes.

Promoted from p3_char_0352_佥 (G5 B10 **A** 2026-08-09). A-recipe:
P-A-006 stroke-primitive layer + BANK_DEVIATION-style inlined pie
variants for s4 and s6 (short pie-family curves at unusual direction
not covered by canonical bank primitives). Rare char; retained
primarily as a record of the "small pie/dian variant" A recipe.
Reuse: 亼 top + wide-heng bottom pattern is uncommon; retain as
reference more than for reuse.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from na import draw_na
from pie import draw_pie


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_qian_all(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: 人 pie (wide-spread top)
    draw_pie(draw, _tx(138.0, 64.7, ox, oy, scale),
             _tx(29.3, 203.3, ox, oy, scale),
             bow_perp=14, w_head=9, w_tail=3, steps=90)
    # s2: 人 na (wide-spread top)
    draw_na(draw, _tx(153.2, 92.3, ox, oy, scale),
            _tx(285.6, 169.6, ox, oy, scale),
            bow_perp=14, w_head=4, w_tail=11, steps=90)
    # s3: short heng under 人 (亼 flat)
    draw_heng(draw, _tx(109.6, 170.5, ox, oy, scale),
              _tx(185.4, 163.2, ox, oy, scale),
              width_head=6, width_tail=7)
    # s4: small down-right stroke (dian-like)
    draw_dian(draw, _tx(128.6, 202.7, ox, oy, scale),
              _tx(147.9, 234.1, ox, oy, scale),
              w_head=3, w_tail=6, bow=2, steps=30)
    # s5: dian variant in cluster
    draw_dian(draw, _tx(148.6, 202.7, ox, oy, scale),
              _tx(167.9, 234.1, ox, oy, scale),
              w_head=3, w_tail=6, bow=2, steps=30)
    # s6: pie-direction stroke (short)
    draw_pie(draw, _tx(191.9, 189.0, ox, oy, scale),
             _tx(155.6, 270.7, ox, oy, scale),
             bow_perp=6, w_head=6, w_tail=3, steps=60)
    # s7: wide bottom heng
    draw_heng(draw, _tx(57.4, 282.7, ox, oy, scale),
              _tx(249.6, 281.2, ox, oy, scale),
              width_head=9, width_tail=10)
