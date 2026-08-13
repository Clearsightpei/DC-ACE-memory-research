"""Bank primitive: 的 (de/dí, particle/target) — 8 strokes.

Promoted from p3_char_0359_的 (G5 B10 **A** 2026-08-09). A-recipe:
P-A-006 stroke-primitive layer + 2 BANK_DEVIATIONs (bai_white for
compressed 白, bao_wrap for 3-stroke 勺 with interior dian) — both
with quantitative aspect calc (P-A-009): bai_white aspect 0.36 vs
bank 0.67 = 2x compressed; bao_wrap fails on stroke-count (2 vs 3).
Reuse: HIGHEST-frequency character in modern Chinese; also reuse
template for 白-compressed-L + 勺-with-interior-dian family.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from heng_zhe_box import draw_heng_zhe_box
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_de_target(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # --- 白 (compressed L, 5 strokes) ---
    # s1: 撇
    draw_pie(draw, _tx(81.4, 71.5, ox, oy, scale),
             _tx(57.4, 143.8, ox, oy, scale),
             bow_perp=8, w_head=7, w_tail=3)
    # s2: 竖
    draw_shu(draw, _tx(39.6, 141.8, ox, oy, scale),
             _tx(57.4, 251.4, ox, oy, scale),
             width=max(2, int(6 * scale)))
    # s3: 横折(box)
    draw_heng_zhe_box(draw, _tx(55.1, 148.2, ox, oy, scale),
                      _tx(108.1, 261.9, ox, oy, scale),
                      width=max(2, int(6 * scale)))
    # s4: middle 横
    draw_heng(draw, _tx(60.9, 193.4, ox, oy, scale),
              _tx(95.2, 188.1, ox, oy, scale),
              width_head=5, width_tail=5)
    # s5: bottom 横 (closes box)
    draw_heng(draw, _tx(63.0, 248.1, ox, oy, scale),
              _tx(94.6, 237.3, ox, oy, scale),
              width_head=5, width_tail=6)
    # --- 勺 (right, 3 strokes) ---
    # s6: 撇
    draw_pie(draw, _tx(184.6, 54.2, ox, oy, scale),
             _tx(137.7, 169.9, ox, oy, scale),
             bow_perp=12, w_head=8, w_tail=3)
    # s7: 横折钩 wrap
    draw_heng_zhe_gou(draw,
                      heng_head=_tx(169.0, 142.7, ox, oy, scale),
                      corner=_tx(232.0, 138.0, ox, oy, scale),
                      gou_tail=_tx(215.0, 268.7, ox, oy, scale),
                      hook_tip=_tx(177.0, 260.0, ox, oy, scale))
    # s8: interior 点
    draw_dian(draw, _tx(151.5, 186.9, ox, oy, scale),
              _tx(181.3, 218.3, ox, oy, scale),
              w_head=3, w_tail=7, bow=4, steps=40)
