"""Bank primitive: 爻 (yao, "trigram lines" — 4 strokes = two X-groups stacked).

Promoted from p2_radical_128_爻 (G5 B3 **A verdict** 2026-08-08 — one of
first 4 A verdicts). Composition = 2 pies + 2 nas, forming a top X and a
bottom X. Same bottom-X pattern as 攵/夂/夊/父.

Low-freq as a component (appears in 爽/爾), but the encoded bottom-X
recipe is high-reuse — see draw_pu for the pattern precedent.
"""

from PIL import ImageDraw

from pie import draw_pie
from na import draw_na


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_yao_lines(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # top X
    draw_pie(draw, _tx(173.4, 60.9, ox, oy, scale),
             _tx(70.6, 162.0, ox, oy, scale),
             bow_perp=-14, w_head=max(2, int(7 * scale)),
             w_tail=2, steps=90)
    draw_na(draw, _tx(89.4, 93.2, ox, oy, scale),
            _tx(206.8, 153.5, ox, oy, scale),
            bow_perp=-8, w_head=max(2, int(3 * scale)),
            w_tail=max(2, int(9 * scale)), steps=90)
    # bottom X
    draw_pie(draw, _tx(160.8, 164.6, ox, oy, scale),
             _tx(33.7, 289.2, ox, oy, scale),
             bow_perp=-18, w_head=max(2, int(8 * scale)),
             w_tail=2, steps=100)
    draw_na(draw, _tx(83.2, 188.1, ox, oy, scale),
            _tx(267.5, 298.5, ox, oy, scale),
            bow_perp=-10, w_head=max(2, int(3 * scale)),
            w_tail=max(2, int(11 * scale)), steps=100)
