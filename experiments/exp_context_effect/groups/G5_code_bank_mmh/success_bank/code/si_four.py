"""Bank primitive: 四 (sì, 'four' — 5 strokes: shu + heng_zhe_box + pie + shu_zhe + heng).

Promoted from p3_char_0210_四 (G5 B7 PASS, 2026-08-08). Very high-freq
numeral + phonetic (e.g., 泗/驷). Distinct from 田/由/甲: inside marks
are pie (left) + shu_zhe (right L), NOT two straight verticals.
Reuse targets: 四, 泗, 驷.
"""

from PIL import ImageDraw

from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from pie import draw_pie
from shu_zhe import draw_shu_zhe


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_si_four(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: 丨 left vertical
    draw_shu(draw, _tx(58, 92, ox, oy, scale), _tx(72, 260, ox, oy, scale),
             width=max(2, int(8 * scale)))
    # s2: 横折 box (top-left to bottom-right)
    draw_heng_zhe_box(draw, _tx(72, 88, ox, oy, scale), _tx(232, 268, ox, oy, scale),
                      width=max(2, int(8 * scale)))
    # s3: inner-left short 撇
    draw_pie(draw, _tx(118, 122, ox, oy, scale), _tx(95, 218, ox, oy, scale),
             bow_perp=int(4 * scale) or 1,
             w_head=max(2, int(7 * scale)),
             w_tail=max(2, int(4 * scale)))
    # s4: inner-right 竖折 (small L)
    draw_shu_zhe(draw,
                 _tx(162, 122, ox, oy, scale),
                 _tx(162, 218, ox, oy, scale),
                 _tx(222, 218, ox, oy, scale),
                 width=max(2, int(7 * scale)))
    # s5: bottom sealing heng
    draw_heng(draw, _tx(60, 268, ox, oy, scale), _tx(232, 262, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
