"""Bank primitive: 定 (dìng, "fix/settle") — 8 strokes = 宀 + 疋.

Promoted from p3_char_0381_定 (G5 B10 PASS 2026-08-09). VERY HIGH REUSE:
extends to 宿/宁/它/宅/守/宇 family for 宀-top calibration + 是/走/足/建
family for 疋-like footer. P-A-006 stroke-primitive layer; 宀 inlined
via dian + pie + heng_zhe_short (matches MMH anchors better than
draw_mian_roof at this compression).
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from heng_zhe_short import draw_heng_zhe_short
from na import draw_na
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_ding_fix(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # --- 宀 top (3 strokes) ---
    draw_dian(draw, _tx(127.7, 53.0, ox, oy, scale),
              _tx(159.1, 79.4, ox, oy, scale),
              w_head=3, w_tail=8, bow=3, steps=48)
    draw_pie(draw, _tx(67.1, 105.8, ox, oy, scale),
             _tx(57.1, 164.4, ox, oy, scale),
             bow_perp=4, w_head=6, w_tail=3, steps=60)
    draw_heng_zhe_short(draw, _tx(79.7, 123.6, ox, oy, scale),
                        _tx(203.3, 155.0, ox, oy, scale),
                        corner_offset=(-6, -4))
    # --- 疋 bottom (5 strokes) ---
    draw_heng(draw, _tx(99.0, 161.1, ox, oy, scale),
              _tx(184.0, 150.0, ox, oy, scale),
              width_head=7, width_tail=8)
    draw_shu(draw, _tx(133.3, 169.3, ox, oy, scale),
             _tx(148.5, 255.5, ox, oy, scale),
             width=max(2, int(7 * scale)))
    draw_heng(draw, _tx(153.8, 211.2, ox, oy, scale),
              _tx(200.1, 202.1, ox, oy, scale),
              width_head=7, width_tail=8)
    draw_pie(draw, _tx(87.6, 198.3, ox, oy, scale),
             _tx(37.5, 289.5, ox, oy, scale),
             bow_perp=10, w_head=8, w_tail=3, steps=90)
    draw_na(draw, _tx(100.8, 227.6, ox, oy, scale),
            _tx(277.4, 294.7, ox, oy, scale),
            bow_perp=14, w_head=4, w_tail=11, steps=90)
