"""Bank primitive: 佟 (tóng, surname) — 7 strokes.

Promoted from p3_char_0348_佟 (G5 B10 **A** 2026-08-09). A-recipe:
P-A-006 stroke-primitive layer with MMH-verbatim anchors + P-A-008
inline reasoning trace (亻 = 2 pie+shu inline; 冬 top = 2 pies + na
X-cross with welded P-joint at center; 冬 bottom = 2 dians as 冫).
Reuse: 亻+冬 template; 冬 sub-structure extends to 终/疼/腾/图 family
where 冬 appears; also useful for any dians-below composition.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng_pie import draw_heng_pie
from na import draw_na
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_dong_person(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: 亻 pie
    draw_pie(draw, _tx(89.4, 64.7, ox, oy, scale),
             _tx(17.6, 196.0, ox, oy, scale),
             bow_perp=15, w_head=8, w_tail=2, steps=90)
    # s2: 亻 shu
    draw_shu(draw, _tx(65.9, 152.6, ox, oy, scale),
             _tx(69.7, 289.5, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s3: 冬 outer pie (top-right down-left)
    draw_pie(draw, _tx(154.1, 60.6, ox, oy, scale),
             _tx(101.7, 152.3, ox, oy, scale),
             bow_perp=8, w_head=6, w_tail=2, steps=70)
    # s4: 冬 heng_pie (X-cross helper) — welded P-joint at center
    draw_heng_pie(draw, _tx(147.7, 112.8, ox, oy, scale),
                  _tx(91.7, 221.5, ox, oy, scale),
                  apex_x=int(205 * scale + ox), corner_x=int(200 * scale + ox))
    # s5: 冬 na (X-cross partner)
    draw_na(draw, _tx(133.3, 138.0, ox, oy, scale),
            _tx(282.7, 210.4, ox, oy, scale),
            bow_perp=10, w_head=4, w_tail=12, steps=100)
    # s6: 冬 upper dian (冫 top)
    draw_dian(draw, _tx(152.6, 209.2, ox, oy, scale),
              _tx(186.9, 232.9, ox, oy, scale),
              w_head=3, w_tail=7, bow=3, steps=40)
    # s7: 冬 lower dian (冫 bottom)
    draw_dian(draw, _tx(143.6, 254.3, ox, oy, scale),
              _tx(193.7, 299.0, ox, oy, scale),
              w_head=3, w_tail=7, bow=3, steps=40)
