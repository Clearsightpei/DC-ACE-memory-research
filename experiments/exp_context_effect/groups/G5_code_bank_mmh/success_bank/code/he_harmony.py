"""Bank primitive: 和 (hé, "harmony/and") — 8 strokes.

Promoted from p3_char_0365_和 (G5 B10 **A** 2026-08-09). A-recipe:
P-A-006 stroke-primitive layer + BANK_DEVIATION on kou_mouth
(near-square inner 口, aspect-skew 1.21 at edge of P-A-007-v2 window
per P-A-009 quantitative calc). 禾 half inlined (no bank primitive).
Reuse: EXTREMELY high-freq char; 禾 sub-template extends to
秋/秒/科/秤/秘/税/秃 family; 口 rendered compact-inline for right-half
compound context (contrast with kou_mouth landscape default).
"""

from PIL import ImageDraw

from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from na import draw_na
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_he_harmony(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # --- 禾 (left, 5 strokes) ---
    # s1: 撇 (flat top pie)
    draw_pie(draw, _tx(150.0, 74.1, ox, oy, scale),
             _tx(48.3, 108.4, ox, oy, scale),
             bow_perp=6, w_head=8, w_tail=4)
    # s2: 横
    draw_heng(draw, _tx(22.6, 157.6, ox, oy, scale),
              _tx(152.1, 138.6, ox, oy, scale),
              width_head=6, width_tail=7)
    # s3: 竖 (long central; note s2/s3 P-cross)
    draw_shu(draw, _tx(92.9, 99.6, ox, oy, scale),
             _tx(99.6, 297.0, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s4: 撇 (禾 bottom left leg)
    draw_pie(draw, _tx(96.4, 154.4, ox, oy, scale),
             _tx(20.2, 258.1, ox, oy, scale),
             bow_perp=8, w_head=7, w_tail=3)
    # s5: 捺 (禾 bottom right leg)
    draw_na(draw, _tx(112.8, 287.2, ox, oy, scale),
            _tx(145.0, 209.5, ox, oy, scale),
            bow_perp=10, w_head=4, w_tail=10, steps=80)
    # --- 口 (right, 3 strokes, compact near-square) ---
    # s6: 竖
    draw_shu(draw, _tx(157.0, 153.2, ox, oy, scale),
             _tx(179.6, 244.6, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s7: 横折(box) top+right
    draw_heng_zhe_box(draw, _tx(170.0, 153.0, ox, oy, scale),
                      _tx(255.0, 246.0, ox, oy, scale),
                      width=max(2, int(7 * scale)))
    # s8: bottom heng
    draw_heng(draw, _tx(184.9, 226.2, ox, oy, scale),
              _tx(254.9, 215.3, ox, oy, scale),
              width_head=7, width_tail=8)
