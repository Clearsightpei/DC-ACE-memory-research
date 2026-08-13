"""Bank primitive: 白 (bái, 'white' — 5 strokes: pie + shu + heng_zhe_box + 2 hengs).

Promoted from p3_char_0206_白 (G5 B7 PASS, 2026-08-08). Close cousin
of 日 (`ri_sun.py`) but with an added top 撇.
Reuse targets: 白, 百, 伯, 柏, 怕, 拍, 泊, 珀, 迫, 皂, 皇, 皆, 泉 (top),
的 (left).
"""

from PIL import ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_bai_white(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top pie (diagonal, sweeps down-left)
    draw_pie(draw, _tx(131.5, 63.0, ox, oy, scale), _tx(91.4, 143.0, ox, oy, scale),
             bow_perp=int(10 * scale) or 1,
             w_head=max(2, int(9 * scale)),
             w_tail=max(2, int(3 * scale)), steps=80)
    # s2: left 竖 of box
    draw_shu(draw, _tx(53.9, 143.6, ox, oy, scale), _tx(85.5, 274.2, ox, oy, scale),
             width=max(2, int(8 * scale)))
    # s3: 横折 box (top + right)
    draw_heng_zhe_box(draw,
                      _tx(68.8, 145.3, ox, oy, scale),
                      _tx(203.6, 286.2, ox, oy, scale),
                      width=max(2, int(8 * scale)))
    # s4: middle heng (thinner)
    draw_heng(draw, _tx(84.1, 201.9, ox, oy, scale), _tx(181.6, 196.0, ox, oy, scale),
              width_head=max(2, int(6 * scale)),
              width_tail=max(2, int(7 * scale)))
    # s5: bottom-inner heng (closes box)
    draw_heng(draw, _tx(91.1, 256.1, ox, oy, scale), _tx(191.9, 252.8, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
