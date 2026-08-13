"""Bank primitive: 土 (tu, "earth" — 3 strokes: heng + shu + heng, BOTTOM heng LONGER).

Promoted from p2_radical_072_土 (G5 B2 PASS 2026-08-08). HIGH-REUSE:
appears in 地/坐/城/块/坑/场/... Distinguishes from 士 (shi_scholar) by
having the BOTTOM heng LONGER than the top (士 is inverse).
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_tu(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 top short heng
    draw_heng(draw, _tx(82.9, 171.7, ox, oy, scale),
              _tx(217.1, 157.9, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s2 central shu; tail short of s3 for N-gap
    draw_shu(draw, _tx(135.1, 77.3, ox, oy, scale),
             _tx(139.5, 246.0, ox, oy, scale),
             width=max(2, int(8 * scale)))
    # s3 bottom LONG heng (土 vs 士 distinguisher)
    draw_heng(draw, _tx(37.8, 271.0, ox, oy, scale),
              _tx(270.1, 262.2, ox, oy, scale),
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(11 * scale)))
