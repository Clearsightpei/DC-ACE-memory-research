"""Bank primitive: 士 (shi, 'scholar' — 3 strokes: heng + shu + heng, TOP heng LONGER).

Promoted from p2_radical_067_士 (G5 B1 PASS, 2026-08-08).
Distinguisher from 土: 士 has top-heng LONGER than bottom-heng. Enforced
in the reference layout (top span ≈ 223 px, bottom span ≈ 140 px).
Central shu pierces the top heng (P-joint); bottom heng sits below with N-gap.
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_shi_scholar(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    s1_head = _tx(38.4, 181.6, ox, oy, scale)
    s1_tail = _tx(260.7, 171.4, ox, oy, scale)
    s2_head = _tx(136.5, 78.8, ox, oy, scale)
    s2_tail = _tx(142.7, 252.8, ox, oy, scale)
    s3_head = _tx(79.4, 265.7, ox, oy, scale)
    s3_tail = _tx(218.6, 264.0, ox, oy, scale)
    draw_heng(draw, s1_head, s1_tail,
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    draw_shu(draw, s2_head, s2_tail, width=max(2, int(8 * scale)))
    draw_heng(draw, s3_head, s3_tail,
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(11 * scale)))
