"""Bank primitive: 父 (fu, "father" — 4 strokes: small pie + dian + big pie + na).

Promoted from p2_radical_095_父 (G5 B2 PASS 2026-08-08). MEDIUM-REUSE:
sub-component in 爸/爷/爹/... s3 and s4 form the main X (P joint at BC);
s1 and s2 are small top decorations.
"""

from PIL import ImageDraw

from pie import draw_pie
from na import draw_na
from dian import draw_dian


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_fu(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 — small pie top-left
    draw_pie(draw, _tx(94, 87, ox, oy, scale),
             _tx(49, 157, ox, oy, scale),
             bow_perp=max(2, int(6 * scale)),
             w_head=max(2, int(6 * scale)),
             w_tail=max(1, int(2 * scale)))
    # s2 — small dian top-right (tapered short stroke)
    draw_dian(draw, _tx(172, 77, ox, oy, scale),
              _tx(230, 116, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(3, int(7 * scale)),
              bow=max(2, int(3 * scale)))
    # s3 — main pie (from center down-left)
    draw_pie(draw, _tx(158, 136, ox, oy, scale),
             _tx(36, 282, ox, oy, scale),
             bow_perp=max(2, int(12 * scale)),
             w_head=max(2, int(9 * scale)),
             w_tail=max(1, int(3 * scale)))
    # s4 — main na (from upper-left down-right to BR)
    draw_na(draw, _tx(84, 166, ox, oy, scale),
            _tx(276, 290, ox, oy, scale),
            bow_perp=max(2, int(14 * scale)),
            w_head=max(2, int(4 * scale)),
            w_tail=max(3, int(12 * scale)))
