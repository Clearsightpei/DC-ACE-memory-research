"""Bank primitive: 自 (zì, 'self' — 6 strokes: pie + shu + heng_zhe_box + 3 hengs).

Promoted from p3_char_0229_自 (G5 B7 PASS, 2026-08-08). Very close cousin
of 白 (`bai_white.py`) but with an extra interior heng. Phonetic radical.
Reuse targets: 自, 息, 鼻, 臭, 嗅, 洎, 咱, 皋 (bottom).
"""

from PIL import ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_zi_self(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top pie (short, negative bow — arcs to right)
    draw_pie(draw, _tx(135.9, 56.5, ox, oy, scale), _tx(118.4, 116.6, ox, oy, scale),
             bow_perp=int(-8 * scale) or -1,
             w_head=max(2, int(7 * scale)),
             w_tail=max(2, int(3 * scale)))
    # s2: left vertical of box
    draw_shu(draw, _tx(88.8, 114.6, ox, oy, scale), _tx(96.1, 278.3, ox, oy, scale),
             width=max(2, int(8 * scale)))
    # s3: 横折 (top + right of box)
    draw_heng_zhe_box(draw,
                      _tx(107.5, 121.6, ox, oy, scale),
                      _tx(183.7, 269.5, ox, oy, scale),
                      width=max(2, int(8 * scale)))
    # s4: top-inside heng
    draw_heng(draw, _tx(106.9, 176.7, ox, oy, scale), _tx(171.7, 164.9, ox, oy, scale),
              width_head=max(2, int(6 * scale)),
              width_tail=max(2, int(7 * scale)))
    # s5: middle heng
    draw_heng(draw, _tx(106.9, 220.3, ox, oy, scale), _tx(172.9, 210.9, ox, oy, scale),
              width_head=max(2, int(6 * scale)),
              width_tail=max(2, int(7 * scale)))
    # s6: bottom heng (closes box)
    draw_heng(draw, _tx(103.7, 272.8, ox, oy, scale), _tx(190.1, 263.4, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
