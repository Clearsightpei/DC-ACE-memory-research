"""Bank primitive: 国 (guó, "country") — 8 strokes = 囗 + 玉.

Promoted from p3_char_0363_国 (G5 B10 PASS 2026-08-09). VERY HIGH REUSE.
Wrapper calls draw_wei (囗 enclosure) at native then inlines 玉 = 3
hengs + shu + dian inside. Reference for any 囗+X enclosed compound
(图/困/固/圆/园) — the inner-render coords give the standard
inset spacing.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
from wei_enclose import draw_wei


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_guo_country(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # 囗 outer enclosure
    draw_wei(draw, ox=ox, oy=oy, scale=scale)
    # 玉 inner: 3 hengs + shu + dian
    draw_heng(draw, _tx(108.1, 134.5, ox, oy, scale),
              _tx(194.2, 124.5, ox, oy, scale),
              width_head=6, width_tail=7)
    draw_heng(draw, _tx(105.2, 185.7, ox, oy, scale),
              _tx(188.4, 180.2, ox, oy, scale),
              width_head=6, width_tail=7)
    draw_shu(draw, _tx(140.0, 140.0, ox, oy, scale),
             _tx(143.3, 225.6, ox, oy, scale),
             width=max(2, int(7 * scale)))
    draw_heng(draw, _tx(93.2, 239.1, ox, oy, scale),
              _tx(208.9, 232.3, ox, oy, scale),
              width_head=7, width_tail=8)
    draw_dian(draw, _tx(192.5, 190.1, ox, oy, scale),
              _tx(218.3, 211.5, ox, oy, scale),
              w_head=3, w_tail=7, bow=3, steps=40)
