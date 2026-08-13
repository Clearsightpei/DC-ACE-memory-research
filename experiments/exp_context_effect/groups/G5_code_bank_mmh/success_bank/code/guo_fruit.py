"""Bank primitive: 果 (guo, "fruit") — 8 strokes.

Promoted from p3_char_0387_果 (G5 B11 **A** 2026-08-09).

A-recipe: pure P-A-006 stroke-primitive layer with MMH anchors verbatim.
Skipped mu_wood via QUANTITATIVE P-A-009 — native mu heng band at
y[131,143] (12px mid-canvas); 果 wide-heng at y[182,192] (50px LOWER
than mu native); central 竖 pierces both 田 AND 木 (P-joint stacked)
so no scale factor s in [0.55, 1.2] recovers geometry.

The X-crossing family unlock: 果's central 竖 (s6) is 田's interior
vertical AND 木's shaft simultaneously. Whole-radical composition
(draw_ri + draw_mu) is structurally impossible; stroke-primitive
layer is the only correct route. Reuse: 巢 / 棵 / 裸 / 课 / 颗 family
(any 果-based compound).
"""

from PIL import ImageDraw

from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from na import draw_na
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_guo_fruit(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: left vertical of 田 box (slightly slanted per MMH)
    draw_shu(draw, _tx(75.3, 79.1, ox, oy, scale),
             _tx(100.28, 159.7, ox, oy, scale),
             width=max(3, int(7 * scale)))
    # s2: 横折 top+right of 田 box
    draw_heng_zhe_box(draw, _tx(84.4, 77.3, ox, oy, scale),
                      _tx(179.3, 145.6, ox, oy, scale),
                      width=max(3, int(7 * scale)))
    # s3: inner top heng
    draw_heng(draw, _tx(109.0, 17.5, ox, oy, scale),
              _tx(170.8, 9.3, ox, oy, scale),
              width_head=6, width_tail=7)
    # s4: inner bottom heng
    draw_heng(draw, _tx(108.7, 52.9, ox, oy, scale),
              _tx(176.1, 39.5, ox, oy, scale),
              width_head=6, width_tail=7)
    # s5: wide base heng of 木
    draw_heng(draw, _tx(45.1, 192.2, ox, oy, scale),
              _tx(245.8, 181.9, ox, oy, scale),
              width_head=9, width_tail=10)
    # s6: long central 竖 piercing 田 and extending below
    draw_shu(draw, _tx(136.5, 82.3, ox, oy, scale),
             _tx(143.6, 308.2, ox, oy, scale),
             width=max(3, int(8 * scale)))
    # s7: pie (bottom-left sweep)
    draw_pie(draw, _tx(135.1, 191.3, ox, oy, scale),
             _tx(37.8, 278.6, ox, oy, scale),
             bow_perp=10, w_head=6, w_tail=2)
    # s8: na (bottom-right sweep)
    draw_na(draw, _tx(152.6, 190.1, ox, oy, scale),
            _tx(279.8, 273.6, ox, oy, scale),
            bow_perp=12, w_head=4, w_tail=10)


if __name__ == '__main__':
    from PIL import Image
    img = Image.new('RGB', (300, 300), 'white')
    draw_guo_fruit(ImageDraw.Draw(img))
    img.save('/tmp/guo_fruit_preview.png')
