"""Bank primitive: 爫 (zhao, "claw-top" — 4 strokes: pie + 2 dians + pie).

Promoted from p2_radical_131_爫 (G5 B3 PASS 2026-08-08). Top-position radical
(sits in the top ~40% of the canvas). Appears in 爱/爬/受/爵/etc.
All joints class N (no welding); the two dians sit under the top pie.
"""

from PIL import ImageDraw

from pie import draw_pie
from dian import draw_dian


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_zhao_claw_top(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 top long pie
    draw_pie(draw, _tx(189.3, 56.2, ox, oy, scale),
             _tx(97.9, 84.1, ox, oy, scale),
             bow_perp=-8, w_head=max(2, int(7 * scale)),
             w_tail=max(2, int(3 * scale)), steps=80)
    # s2 leftmost dian
    draw_dian(draw, _tx(81.2, 104.6, ox, oy, scale),
              _tx(103.4, 127.1, ox, oy, scale),
              w_head=3, w_tail=max(2, int(7 * scale)),
              bow=2, steps=40)
    # s3 middle dian
    draw_dian(draw, _tx(128.6, 97.3, ox, oy, scale),
              _tx(145.0, 116.6, ox, oy, scale),
              w_head=3, w_tail=max(2, int(7 * scale)),
              bow=2, steps=40)
    # s4 right-side medium pie
    draw_pie(draw, _tx(203.3, 71.5, ox, oy, scale),
             _tx(169.0, 114.6, ox, oy, scale),
             bow_perp=-6, w_head=max(2, int(6 * scale)),
             w_tail=max(2, int(3 * scale)), steps=80)
