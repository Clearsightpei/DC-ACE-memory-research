"""Bank primitive: 时 (shí, "time") — 7 strokes.

Promoted from p3_char_0295_时 (G5 B9 PASS 2026-08-09). HIGH-REUSE:
日+寸 template (时/村/衬/时/耐-like). Records the 日-compressed-left +
寸 shu_gou with hook_start_offset=32 pattern.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from shu import draw_shu
from shu_gou import draw_shu_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_shi_time(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 日 left shu
    draw_shu(draw, _tx(41.3, 98.1, ox, oy, scale),
             _tx(49.2, 253.1, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s2 日 heng_zhe_box
    draw_heng_zhe_box(draw, _tx(59.8, 104.6, ox, oy, scale),
                      _tx(103.1, 254.6, ox, oy, scale),
                      width=max(2, int(7 * scale)))
    # s3 日 middle heng
    draw_heng(draw, _tx(59.8, 174.9, ox, oy, scale),
              _tx(87.0, 167.9, ox, oy, scale),
              width_head=6, width_tail=7)
    # s4 日 bottom heng
    draw_heng(draw, _tx(57.4, 243.2, ox, oy, scale),
              _tx(88.8, 235.0, ox, oy, scale),
              width_head=7, width_tail=8)
    # s5 寸 top heng
    draw_heng(draw, _tx(122.8, 146.5, ox, oy, scale),
              _tx(268.4, 133.3, ox, oy, scale),
              width_head=7, width_tail=8)
    # s6 寸 shu_gou (hook_start_offset=32)
    draw_shu_gou(draw, _tx(199.5, 64.2, ox, oy, scale),
                 _tx(169.3, 273.3, ox, oy, scale),
                 width=max(2, int(7 * scale)),
                 hook_start_offset=32)
    # s7 寸 dian
    draw_dian(draw, _tx(135.9, 185.2, ox, oy, scale),
              _tx(167.3, 216.2, ox, oy, scale),
              w_head=3, w_tail=7, bow=3)
