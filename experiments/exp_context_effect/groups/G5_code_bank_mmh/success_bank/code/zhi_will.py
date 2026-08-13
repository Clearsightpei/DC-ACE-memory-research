"""Bank primitive: 志 (zhì, "will/aspiration") — 7 strokes = 士 top + 心 bottom.

Promoted from p3_char_0345_志 (G5 B10 PASS 2026-08-09). HIGH REUSE:
extends to 忠/念/思/急/怒/怎/怨/恨/悲 family (any 心-bottom compound).
士 = heng + shu + heng (3 strokes). 心 = 卧钩 wo_gou + 3 dians
(4 strokes). Central 卧钩 uses default wo_gou params (belly, hook_up,
hook_back) — reference for 心-bottom family calibration.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
from wo_gou import draw_wo_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_zhi_will(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # --- 士 top ---
    # s1: top heng (士 top is longer than 土 top)
    draw_heng(draw, _tx(73.5, 126, ox, oy, scale),
              _tx(227.6, 108.7, ox, oy, scale),
              width_head=9, width_tail=10)
    # s2: central shu
    draw_shu(draw, _tx(137.1, 61.2, ox, oy, scale),
             _tx(144.1, 168.5, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s3: bottom heng of 士 (shorter than top)
    draw_heng(draw, _tx(94, 180.5, ox, oy, scale),
              _tx(208.9, 175.8, ox, oy, scale),
              width_head=9, width_tail=10)
    # --- 心 bottom ---
    # s4: left dian
    draw_dian(draw, _tx(68.6, 219.4, ox, oy, scale),
              _tx(49.5, 276.6, ox, oy, scale),
              w_head=3, w_tail=7, bow=-3)
    # s5: 卧钩
    draw_wo_gou(draw, _tx(98.1, 216.5, ox, oy, scale),
                _tx(202.4, 239.6, ox, oy, scale))
    # s6: middle dian
    draw_dian(draw, _tx(135.9, 253.3, ox, oy, scale),
              _tx(164.1, 281.4, ox, oy, scale),
              w_head=3, w_tail=7, bow=2)
    # s7: right dian
    draw_dian(draw, _tx(214.7, 196.3, ox, oy, scale),
              _tx(266, 232.9, ox, oy, scale),
              w_head=3, w_tail=8, bow=3)
