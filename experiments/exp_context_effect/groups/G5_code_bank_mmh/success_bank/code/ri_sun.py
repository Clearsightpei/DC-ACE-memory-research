"""Bank primitive: 日 (ri, "sun" — 4 strokes: shu + heng_zhe_box + heng + heng).

Promoted from p2_radical_114_日 (G5 B2 PASS 2026-08-08). VERY HIGH-REUSE:
appears in 明/时/早/星/暗/昨/晚/... Composed from stroke primitives (not
draw_wei/draw_kou) because 日 has a MIDDLE heng inside the box.
"""

from PIL import ImageDraw

from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_ri(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 left 竖
    draw_shu(draw, _tx(83.2, 99.6, ox, oy, scale),
             _tx(88.5, 279.5, ox, oy, scale),
             width=max(2, int(8 * scale)))
    # s2 横折 box (top_left, bottom_right)
    draw_heng_zhe_box(draw, _tx(105.2, 106.6, ox, oy, scale),
                      _tx(201.6, 289.2, ox, oy, scale),
                      width=max(2, int(8 * scale)))
    # s3 middle 横 (shorter, thinner)
    draw_heng(draw, _tx(104.6, 179.0, ox, oy, scale),
              _tx(170.2, 173.7, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s4 bottom 横 (closes box)
    draw_heng(draw, _tx(99.6, 268.9, ox, oy, scale),
              _tx(185.2, 258.1, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
