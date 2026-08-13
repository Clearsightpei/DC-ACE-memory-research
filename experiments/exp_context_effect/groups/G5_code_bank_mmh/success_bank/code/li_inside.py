"""Bank primitive: 里 (lǐ, "inside") — 7 strokes.

Promoted from p3_char_0299_里 (G5 B9 PASS 2026-08-09 via BANK_DEVIATION;
whole-radical draw_ri/draw_tu skipped for compressed-aspect reasons).
HIGH-REUSE: 日+土 stack template (里/量/重/野/黑). Central 竖 (s5)
pierces s3/s4/s6 (three P-welds); s7 long bottom heng closes.
"""

from PIL import ImageDraw

from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_li_inside(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 left shu of 日
    draw_shu(draw, _tx(70.6, 90.2, ox, oy, scale),
             _tx(106.1, 186.6, ox, oy, scale),
             width=max(2, int(8 * scale)))
    # s2 heng_zhe_box top+right of 日
    draw_heng_zhe_box(draw,
                      _tx(85.5, 91.1, ox, oy, scale),
                      _tx(196.9, 183.4, ox, oy, scale),
                      width=max(2, int(8 * scale)))
    # s3 middle heng inside 日
    draw_heng(draw, _tx(116.6, 135.9, ox, oy, scale),
              _tx(183.4, 128.3, ox, oy, scale),
              width_head=7, width_tail=8)
    # s4 bottom heng of 日 (closes box)
    draw_heng(draw, _tx(111.3, 173.4, ox, oy, scale),
              _tx(186.0, 165.8, ox, oy, scale),
              width_head=8, width_tail=9)
    # s5 central 竖 (pierces s3/s4/s6)
    draw_shu(draw, _tx(135.1, 95.5, ox, oy, scale),
             _tx(140.0, 264.6, ox, oy, scale),
             width=max(2, int(8 * scale)))
    # s6 middle heng of 土 half
    draw_heng(draw, _tx(95.8, 224.7, ox, oy, scale),
              _tx(202.4, 215.6, ox, oy, scale),
              width_head=8, width_tail=9)
    # s7 long bottom heng
    draw_heng(draw, _tx(84.3, 280.4, ox, oy, scale),
              _tx(276.0, 271.6, ox, oy, scale),
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(11 * scale)))
