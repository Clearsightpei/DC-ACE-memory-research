"""Bank primitive: 来 (lái, "come") — 7 strokes.

Promoted from p3_char_0293_来 (G5 B9 PASS 2026-08-09). HIGH-REUSE:
central-spine template for 未/末/朱/木-family compounds. Pattern:
horizontal + 2 mirror dians + horizontal + central vertical spine +
long pie + long na.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from na import draw_na
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_lai_come(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 short top heng
    draw_heng(draw, _tx(87.9, 110.4, ox, oy, scale),
              _tx(210.6, 100.2, ox, oy, scale),
              width_head=7, width_tail=8)
    # s2 mirror dian left
    draw_dian(draw, _tx(89.1, 137.7, ox, oy, scale),
              _tx(116.3, 163.8, ox, oy, scale),
              w_head=3, w_tail=6, bow=-4)
    # s3 mirror dian right
    draw_dian(draw, _tx(193.4, 121.6, ox, oy, scale),
              _tx(168.5, 158.8, ox, oy, scale),
              w_head=3, w_tail=6, bow=4)
    # s4 long middle heng
    draw_heng(draw, _tx(47.8, 191.9, ox, oy, scale),
              _tx(252.5, 185.2, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s5 central spine (full height)
    draw_shu(draw, _tx(133.6, 58.6, ox, oy, scale),
             _tx(143.8, 212.0, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s6 long left descending pie
    draw_pie(draw, _tx(139.5, 193.4, ox, oy, scale),
             _tx(40.1, 276.3, ox, oy, scale),
             bow_perp=14, w_head=6, w_tail=2)
    # s7 long right na
    draw_na(draw, _tx(156.7, 191.6, ox, oy, scale),
            _tx(277.4, 281.0, ox, oy, scale),
            bow_perp=16, w_head=4, w_tail=11)
