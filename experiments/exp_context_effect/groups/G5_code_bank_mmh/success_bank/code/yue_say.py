"""Bank primitive: 曰 (yue, "say" — 4 strokes: shu + heng_zhe_box + heng + heng).

Promoted from p2_radical_129_曰 (G5 B3 PASS 2026-08-08). Sibling of 日
(narrower/taller); 曰 is WIDER/SHORTER. Same 4-stroke composition; the
inner middle heng stops SHORT of the right wall (N-joint), distinguishing
from 日 where middle heng usually touches.
"""

from PIL import ImageDraw

from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_yue_say(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    draw_shu(draw, _tx(58.0, 110.7, ox, oy, scale),
             _tx(91.4, 248.7, ox, oy, scale),
             width=max(2, int(8 * scale)))
    draw_heng_zhe_box(draw, _tx(81.2, 116.6, ox, oy, scale),
                      _tx(207.1, 264.0, ox, oy, scale),
                      width=max(2, int(8 * scale)))
    # middle heng — short, does NOT touch right wall
    draw_heng(draw, _tx(90.2, 176.7, ox, oy, scale),
              _tx(173.7, 170.8, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(7 * scale)))
    # bottom heng (closes box)
    draw_heng(draw, _tx(97.3, 243.5, ox, oy, scale),
              _tx(193.7, 230.9, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
