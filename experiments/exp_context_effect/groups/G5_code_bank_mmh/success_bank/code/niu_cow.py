"""Bank primitive: 牛 (niu, "cow" — 4 strokes: pie + short heng + long heng + shu).

Promoted from p2_radical_106_牛 (G5 B2 PASS 2026-08-08). MEDIUM-REUSE:
appears in 物/特/... Also related sibling 午 (differs by pie shape / stroke
count).
"""

from PIL import ImageDraw

from heng import draw_heng
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_niu(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 撇 (top-left)
    draw_pie(draw, _tx(92, 96.7, ox, oy, scale),
             _tx(60.6, 168.8, ox, oy, scale),
             bow_perp=max(2, int(6 * scale)),
             w_head=max(2, int(6 * scale)),
             w_tail=max(1, int(2 * scale)))
    # s2 短横
    draw_heng(draw, _tx(99.9, 137.4, ox, oy, scale),
              _tx(215.3, 120.7, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s3 长横
    draw_heng(draw, _tx(34, 207.7, ox, oy, scale),
              _tx(270.1, 190.1, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s4 丨 (central vertical piercing both hengs)
    draw_shu(draw, _tx(139.7, 57.4, ox, oy, scale),
             _tx(153.2, 296.0, ox, oy, scale),
             width=max(2, int(7 * scale)))
