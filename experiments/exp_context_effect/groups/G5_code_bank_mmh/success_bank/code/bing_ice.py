"""Bank primitive: 冫 (radical — 2-dot ice, upper 点 + lower 提-ish 点).

Promoted from p2_radical_012_冫 (G5 bootstrap PASS, 2026-08-08).
Upper stroke goes UL->LR (like a small dian); lower stroke goes UR->LL
(the ti direction). Both use dian.draw_dian with head/tail placement
that preserves the vertical stacking and slight overlap.
"""

from PIL import ImageDraw

from dian import draw_dian


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_bing(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    """Draw 冫 at (ox, oy). Reference canvas 300x300."""
    s1_head = _tx(145, 100, ox, oy, scale)
    s1_tail = _tx(172, 178, ox, oy, scale)
    s2_head = _tx(158, 208, ox, oy, scale)
    s2_tail = _tx(115, 278, ox, oy, scale)

    # upper dian: standard direction (thin head UL -> thick tail LR)
    draw_dian(draw, s1_head, s1_tail,
              w_head=3 * scale, w_tail=9 * scale, bow=5 * scale)
    # lower stroke: opposite diagonal, still tapered thin->thick
    draw_dian(draw, s2_head, s2_tail,
              w_head=4 * scale, w_tail=10 * scale, bow=5 * scale)
