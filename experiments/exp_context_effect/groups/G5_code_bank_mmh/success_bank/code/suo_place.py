"""Bank primitive: 所 (suǒ, "place") — 8 strokes = 户 top-left + 斤 right.

Promoted from p3_char_0371_所 (G5 B10 PASS 2026-08-09). VERY HIGH REUSE:
extends to 房/扇/雇 (户-family top) and 斤-family (析/新/斧/欣).
Composition: 户 = dian + pie + heng + heng (4 strokes); 斤 = pie + heng
+ heng + shu (4 strokes). All strokes at MMH-verbatim anchors.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu


CELL_BASE = {
    'TL': (0, 0),    'TC': (100, 0),   'TR': (200, 0),
    'ML': (0, 100),  'C':  (100, 100), 'MR': (200, 100),
    'BL': (0, 200),  'BC': (100, 200), 'BR': (200, 200),
}


def _cell(name, xf, yf, ox, oy, scale):
    cx, cy = CELL_BASE[name]
    return (ox + (cx + xf * 100.0) * scale,
            oy + (cy + yf * 100.0) * scale)


def draw_suo_place(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: top dian (户)
    draw_dian(draw, _cell('TC', 0.143, 0.653, ox, oy, scale),
              _cell('ML', 0.776, 0.025, ox, oy, scale),
              w_head=3, w_tail=7, bow=2)
    # s2: 户 pie
    draw_pie(draw, _cell('TL', 0.557, 0.99, ox, oy, scale),
             _cell('BL', 0.246, 0.804, ox, oy, scale),
             bow_perp=-8, w_head=8, w_tail=2)
    # s4: 户 upper heng (inside)
    draw_heng(draw, _cell('ML', 0.706, 0.989, ox, oy, scale),
              _cell('C', 0.274, 0.89, ox, oy, scale),
              width_head=7, width_tail=8)
    # s5: 户 lower heng
    draw_pie(draw, _cell('C', 0.755, 0.005, ox, oy, scale),
             _cell('TR', 0.438, 0.741, ox, oy, scale),
             bow_perp=3, w_head=5, w_tail=3)
    # s6: 斤 left pie
    draw_pie(draw, _cell('TC', 0.515, 0.94, ox, oy, scale),
             _cell('BC', 0.069, 0.622, ox, oy, scale),
             bow_perp=-15, w_head=8, w_tail=2)
    # s7: 斤 upper heng
    draw_heng(draw, _cell('C', 0.731, 0.5, ox, oy, scale),
              _cell('MR', 0.748, 0.395, ox, oy, scale),
              width_head=7, width_tail=8)
    # s8: 斤 shu (right vertical)
    draw_shu(draw, _cell('MR', 0.054, 0.509, ox, oy, scale),
             _cell('BR', 0.054, 0.95, ox, oy, scale),
             width=max(2, int(7 * scale)))
