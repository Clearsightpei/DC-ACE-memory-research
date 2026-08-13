"""Bank primitive: 攵 (pu, "rap/action" radical — 4 strokes: pie + heng + pie + na).

Promoted from p2_radical_110_攵 (G5 B2 PASS 2026-08-08). HIGH-REUSE
right-side radical: appears in 收/教/散/敌/放/敬/故/救... s3 and s4 form
the bottom X (P joint at BC); s1 and s2 have a natural N-gap.
"""

from PIL import ImageDraw

from pie import draw_pie
from heng import draw_heng
from na import draw_na


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_pu(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 long upper pie
    draw_pie(draw, _tx(117.2, 75.6, ox, oy, scale),
             _tx(63.9, 207.9, ox, oy, scale),
             bow_perp=max(2, int(14 * scale)),
             w_head=max(2, int(8 * scale)),
             w_tail=max(1, int(3 * scale)))
    # s2 short heng
    draw_heng(draw, _tx(116.0, 143.6, ox, oy, scale),
              _tx(218.8, 126.0, ox, oy, scale),
              width_head=max(2, int(7 * scale)),
              width_tail=max(2, int(8 * scale)))
    # s3 lower pie (crosses s4 at BC — P joint)
    draw_pie(draw, _tx(158.2, 147.1, ox, oy, scale),
             _tx(56.5, 281.0, ox, oy, scale),
             bow_perp=max(2, int(10 * scale)),
             w_head=max(2, int(8 * scale)),
             w_tail=max(1, int(3 * scale)))
    # s4 na (bottom X with s3)
    draw_na(draw, _tx(95.2, 175.8, ox, oy, scale),
            _tx(251.7, 290.0, ox, oy, scale),
            bow_perp=max(2, int(10 * scale)),
            w_head=max(2, int(4 * scale)),
            w_tail=max(3, int(12 * scale)))
