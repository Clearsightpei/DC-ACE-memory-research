"""Bank primitive: 止 (zhi, "stop" — 4 strokes: shu + heng + shu + heng).

Promoted from p2_radical_133_止 (G5 B3 PASS 2026-08-08). High-reuse
whole-glyph radical (企/正/此/歧/步/etc.). All 3 joints class N (natural
gap). Composition: top center 竖 + short middle 横 (right) + left short
竖 (drops) + long bottom 横 (baseline).
"""

from PIL import ImageDraw

from shu import draw_shu
from heng import draw_heng


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_zhi_stop(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 top-center shu
    draw_shu(draw, _tx(138.9, 78.5, ox, oy, scale),
             _tx(146.5, 259.3, ox, oy, scale),
             width=max(2, int(8 * scale)))
    # s2 short middle heng (right of center)
    draw_heng(draw, _tx(163.2, 169.9, ox, oy, scale),
              _tx(236.4, 161.7, ox, oy, scale),
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s3 left short shu
    draw_shu(draw, _tx(74.4, 166.1, ox, oy, scale),
             _tx(99.3, 262.8, ox, oy, scale),
             width=max(2, int(8 * scale)))
    # s4 long bottom heng (baseline)
    draw_heng(draw, _tx(36.3, 274.8, ox, oy, scale),
              _tx(269.8, 267.2, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
