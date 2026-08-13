"""Bank primitive: 会 (huì, 'meet' — 6 strokes: pie + na + 2 hengs + pie_zhe + dian).

Promoted from p3_char_0231_会 (G5 B7 PASS, 2026-08-08). Composition:
人-top (2 strokes) + 云-body (2 hengs) + 厶-bottom (pie_zhe + dian).
Very high-freq char.
Reuse targets: 会, 绘, 桧, 侩, 烩, 荟.
"""

from PIL import ImageDraw

from pie import draw_pie
from na import draw_na
from heng import draw_heng
from dian import draw_dian
from pie_zhe import draw_pie_zhe


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_hui_meet(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: 人-pie (big sweep)
    draw_pie(draw, _tx(134.2, 63.3, ox, oy, scale), _tx(27.8, 209.5, ox, oy, scale),
             bow_perp=int(16 * scale) or 1,
             w_head=max(2, int(10 * scale)),
             w_tail=max(2, int(3 * scale)), steps=90)
    # s2: 人-na (right sweep, thickens to tail)
    draw_na(draw, _tx(149.4, 93.8, ox, oy, scale), _tx(290.0, 186.3, ox, oy, scale),
            bow_perp=int(14 * scale) or 1,
            w_head=max(2, int(4 * scale)),
            w_tail=max(2, int(12 * scale)), steps=90)
    # s3: short heng under 人's belly
    draw_heng(draw, _tx(103.7, 177.8, ox, oy, scale), _tx(184.0, 169.6, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s4: wider heng (top of 云 body)
    draw_heng(draw, _tx(60.6, 221.2, ox, oy, scale), _tx(229.7, 210.9, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s5: 厶 left stroke (撇折) — MMH head/tail plus low-left corner
    draw_pie_zhe(draw,
                 _tx(145.6, 226.8, ox, oy, scale),
                 _tx(135, 268, ox, oy, scale),
                 _tx(193.4, 268.7, ox, oy, scale),
                 pie_bow=int(6 * scale) or 1, zhe_bow=0,
                 w_head=max(2, int(8 * scale)),
                 w_corner=max(2, int(6 * scale)),
                 w_tail=max(2, int(5 * scale)), steps=70)
    # s6: 厶 right dot
    draw_dian(draw, _tx(180.2, 242.9, ox, oy, scale), _tx(221.5, 296.8, ox, oy, scale),
              w_head=max(2, int(4 * scale)),
              w_tail=max(2, int(9 * scale)),
              bow=max(2, int(4 * scale)), steps=60)
