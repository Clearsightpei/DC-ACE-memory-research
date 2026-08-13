"""Bank primitive: 伾 (pī) — 7 strokes.

Promoted from p3_char_0320_伾 (G5 B9 A verdict 2026-08-09). 亻 (2 strokes)
inline + 丕 (5 strokes) inline; both refused whole-radical primitives
(draw_ren_left rejected because MMH pie head at TL(0.87, 0.656) sits
higher than baked geometry — P-A-007 clause 2). 丕 has no bank primitive.

MEDIUM-REUSE: template for 亻+X where X = 不-family (丕/否). Also validates
the "reject bank primitive for anchor-mismatch" branch of P-A-007.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_pi_flourish(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 亻 pie
    draw_pie(draw, _tx(87, 65.6, ox, oy, scale),
             _tx(19.6, 203, ox, oy, scale),
             bow_perp=max(1, int(13 * scale)),
             w_head=max(2, int(9 * scale)),
             w_tail=max(2, int(3 * scale)), steps=90)
    # s2 亻 shu
    draw_shu(draw, _tx(69.7, 151.8, ox, oy, scale),
             _tx(73.2, 296.5, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s3 丕 top heng
    draw_heng(draw, _tx(119.8, 119.5, ox, oy, scale),
              _tx(250.8, 102.2, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s4 丕 left pie
    draw_pie(draw, _tx(184.3, 115.7, ox, oy, scale),
             _tx(108.4, 230.6, ox, oy, scale),
             bow_perp=max(1, int(10 * scale)),
             w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(3 * scale)), steps=80)
    # s5 丕 short middle shu
    draw_shu(draw, _tx(162, 147.9, ox, oy, scale),
             _tx(172, 256.3, ox, oy, scale),
             width=max(2, int(6 * scale)))
    # s6 丕 right dian
    draw_dian(draw, _tx(206.2, 182.2, ox, oy, scale),
              _tx(264, 225.9, ox, oy, scale),
              w_head=3, w_tail=9, bow=4, steps=48)
    # s7 丕 bottom heng
    draw_heng(draw, _tx(112.2, 280.7, ox, oy, scale),
              _tx(267.5, 279.2, ox, oy, scale),
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(11 * scale)))
