"""Bank primitive: 冖 (mi, 'cover' — 2 strokes: dian + heng_zhe_short).

Promoted from p2_radical_026_冖 (G5 B1 PASS, 2026-08-08).
Similar to 宀 without the left dot — bare horizontal-hook roof.
"""

from PIL import ImageDraw

from dian import draw_dian
from heng_zhe_short import draw_heng_zhe_short


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_mi_cover(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    s1_head = _tx(68, 92, ox, oy, scale)
    s1_tail = _tx(54, 148, ox, oy, scale)
    s2_head = _tx(78, 108, ox, oy, scale)
    s2_tail = _tx(213, 140, ox, oy, scale)
    draw_dian(draw, s1_head, s1_tail,
              w_head=3 * scale, w_tail=7 * scale, bow=3 * scale, steps=48)
    draw_heng_zhe_short(draw, s2_head, s2_tail,
                        corner_offset=(-2 * scale, -6 * scale))
