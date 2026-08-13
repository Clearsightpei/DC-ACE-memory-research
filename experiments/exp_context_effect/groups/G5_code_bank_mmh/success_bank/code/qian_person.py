"""Bank primitive: 仟 (qiān, 亻+千 L-R — 5 strokes: pie + shu + pie + heng + shu).

Promoted from p3_char_0185_仟 (G5 B7 **A** verdict, 2026-08-08).
Recipe: P-A-006 — MMH anchors verbatim, stroke-primitive layer (bypasses
draw_ren_left + draw_qian_thousand double-transform). Serves as
**L-R template for 亻+X compounds** where X = 3-stroke phonetic radical.
Reuse targets: 仟 (identity), and the template pattern for 仔, 什,
仁, 化, 付, 仕, 仗, 任, ... (亻 pie head at (85, 61), 亻 shu at (67, 137)-(67, 278)).
"""

from PIL import ImageDraw

from pie import draw_pie
from shu import draw_shu
from heng import draw_heng


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_qian_person(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: 亻 pie (long TL→ML sweep, gentle bow)
    draw_pie(draw, _tx(85, 61, ox, oy, scale), _tx(14, 183, ox, oy, scale),
             bow_perp=int(13 * scale) or 1,
             w_head=max(2, int(9 * scale)),
             w_tail=max(2, int(3 * scale)), steps=90)
    # s2: 亻 shu (vertical descender)
    draw_shu(draw, _tx(67, 137, ox, oy, scale), _tx(67, 278, ox, oy, scale),
             width=max(2, int(7 * scale)))
    # s3: 千 short pie (top-right tick)
    draw_pie(draw, _tx(228, 78, ox, oy, scale), _tx(124, 114, ox, oy, scale),
             bow_perp=int(6 * scale) or 1,
             w_head=max(2, int(8 * scale)),
             w_tail=max(2, int(3 * scale)), steps=60)
    # s4: 千 long heng (crosses right-side)
    draw_heng(draw, _tx(93, 173, ox, oy, scale), _tx(276, 157, ox, oy, scale),
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(12 * scale)))
    # s5: 千 long shu (pierces heng at ~C)
    draw_shu(draw, _tx(163, 107, ox, oy, scale), _tx(178, 298, ox, oy, scale),
             width=max(2, int(8 * scale)))
