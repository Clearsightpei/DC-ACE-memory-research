"""Bank primitive: 月 (yue, "moon" — 4 strokes: pie + heng_zhe_gou + heng + heng).

Promoted from p2_radical_130_月 (G5 B3 PASS 2026-08-08). VERY HIGH-REUSE:
appears in 明/朋/朝/期/服/胖/胜/朗/etc. Composed from stroke primitives
(pie + heng_zhe_gou + 2 hengs). Note the s1 pie sweeps DOWN-LEFT from
top-mid; corner and gou_tail estimated from box geometry (right wall
sits at x~=185; inner hengs end near x=172).
"""

from PIL import ImageDraw

from pie import draw_pie
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_yue_moon(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: 撇 (long left sweep)
    draw_pie(draw, _tx(99.3, 73.5, ox, oy, scale),
             _tx(52.0, 268.0, ox, oy, scale),
             bow_perp=int(18 * scale),
             w_head=max(2, int(9 * scale)),
             w_tail=max(2, int(3 * scale)))
    # s2: 横折钩 (top + right wall + hook)
    draw_heng_zhe_gou(draw, _tx(121.6, 76.2, ox, oy, scale),
                      _tx(188.0, 74.0, ox, oy, scale),
                      _tx(170.0, 278.0, ox, oy, scale),
                      _tx(157.6, 269.5, ox, oy, scale))
    # s3: upper inner heng
    draw_heng(draw, _tx(122.2, 141.2, ox, oy, scale),
              _tx(172.3, 134.8, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s4: lower inner heng
    draw_heng(draw, _tx(116.9, 192.2, ox, oy, scale),
              _tx(172.3, 185.2, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
