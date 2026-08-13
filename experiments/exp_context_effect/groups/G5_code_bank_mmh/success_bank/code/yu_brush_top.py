"""Bank primitive: 肀 (yu, "brush-top" — 4 strokes: heng_zhe_short + heng + heng + shu).

Promoted from p2_radical_105_肀__retry_1 (G5 B3 R1 PASS 2026-08-08).
Low-freq radical, but the shape appears in 事/建/律-related families.
Central vertical PIERCES all three horizontals; s1 is a short 横折-like
top-piece, NOT a pure diagonal.
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu
from heng_zhe_short import draw_heng_zhe_short


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_yu_brush_top(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 top-piece: 短横折
    draw_heng_zhe_short(draw, _tx(89.6, 114.6, ox, oy, scale),
                        _tx(184.3, 170.2, ox, oy, scale),
                        corner_offset=(15, -2))
    # s2 dominant middle heng
    draw_heng(draw, _tx(36.0, 158.8, ox, oy, scale),
              _tx(274.2, 147.1, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s3 lower shorter heng
    draw_heng(draw, _tx(87.6, 188.7, ox, oy, scale),
              _tx(201.9, 182.2, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s4 central shu (pierces all hengs, extends below baseline)
    draw_shu(draw, _tx(131.0, 57.1, ox, oy, scale),
             _tx(143.8, 304.1, ox, oy, scale),
             width=max(2, int(7 * scale)))
