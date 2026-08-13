"""Bank primitive: 些 (xiē, "some") — 8 strokes.

Promoted from p3_char_0383_些 (G5 B10 **A** 2026-08-09). A-recipe:
P-A-006 stroke-primitive layer with TRIPLE BANK_DEVIATION
(zhi_stop for 止 top, bi_dagger for 匕 top-right, er_two for bottom
二) — each with quantitative aspect/scale calc per P-A-009. Reuse:
some (some literary chars); 此-top pattern (止+匕) also relevant to
柴/紫/呰 family.
"""

from PIL import ImageDraw

from heng import draw_heng
from pie import draw_pie
from shu import draw_shu
from shu_wan_gou import draw_shu_wan_gou
from ti import draw_ti


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_xie_some(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # ---- 止 (top-left, 4 strokes) ----
    # s1: top-center 竖
    draw_shu(draw, _tx(96.7, 77.9, ox, oy, scale),
             _tx(109.0, 189.8, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s2: middle-right 短横
    draw_heng(draw, _tx(120.7, 138.3, ox, oy, scale),
              _tx(152.1, 128.3, ox, oy, scale),
              width_head=6, width_tail=7)
    # s3: left 短竖
    draw_shu(draw, _tx(60.6, 133.3, ox, oy, scale),
             _tx(75.9, 196.9, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s4: 提 (rising)
    draw_ti(draw, _tx(40.7, 210.4, ox, oy, scale),
            _tx(155.9, 181.1, ox, oy, scale),
            w_head=9, w_tail=3)
    # ---- 匕 (top-right, 2 strokes) ----
    # s5: 撇 (into 匕)
    draw_pie(draw, _tx(231.4, 97.6, ox, oy, scale),
             _tx(179.3, 142.4, ox, oy, scale),
             bow_perp=-6, w_head=7, w_tail=3)
    # s6: 竖弯钩 (匕 body)
    draw_shu_wan_gou(draw, _tx(164.6, 61.8, ox, oy, scale),
                     _tx(262.2, 157.9, ox, oy, scale),
                     width=max(2, int(7 * scale)),
                     bottom_extra=35, knee_ratio=0.75)
    # ---- 二 (bottom, 2 strokes) ----
    # s7: upper heng of 二
    draw_heng(draw, _tx(108.4, 235.3, ox, oy, scale),
              _tx(188.4, 228.5, ox, oy, scale),
              width_head=7, width_tail=8)
    # s8: lower heng of 二 (heaviest)
    draw_heng(draw, _tx(58.3, 286.8, ox, oy, scale),
              _tx(250.2, 279.2, ox, oy, scale),
              width_head=10, width_tail=12)
