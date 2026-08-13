"""Bank primitive: 十 (shi, 'ten' — 2 strokes, heng + shu with P-joint at center).

Promoted from p2_radical_031_十 (G5 B1 PASS, 2026-08-08). HIGH-REUSE:
十 appears as a component in 古/克/直/... and as its own character.

Piercing joint welds naturally where the two stroke bodies cross.
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_shi_ten(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    s1_head = _tx(32, 170, ox, oy, scale)
    s1_tail = _tx(273, 160, ox, oy, scale)
    s2_head = _tx(134, 62, ox, oy, scale)
    s2_tail = _tx(149, 292, ox, oy, scale)
    draw_heng(draw, s1_head, s1_tail,
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    draw_shu(draw, s2_head, s2_tail,
             width=max(2, int(8 * scale)), top_curl=True)
