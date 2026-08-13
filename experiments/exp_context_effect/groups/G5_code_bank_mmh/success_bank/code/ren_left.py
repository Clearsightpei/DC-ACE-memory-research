"""Bank primitive: 亻 (ren-left, 'person-radical' left position — 2 strokes: pie + shu).

Promoted from p2_radical_029_亻 (G5 B1 PASS, 2026-08-08). HIGH-REUSE:
this is the left-position 人 radical, appearing in 你/他/什/们/作/...

Reference layout preserves the PASSing 300x300 render. Callers translate/
scale via (ox, oy, scale). N-joint between s1.mid and s2.head emerges from
MMH anchor spacing.
"""

from PIL import ImageDraw

from pie import draw_pie
from shu import draw_shu


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_ren_left(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    s1_head = _tx(158.8, 73.8, ox, oy, scale)
    s1_tail = _tx(80.6, 211.2, ox, oy, scale)
    s2_head = _tx(138.9, 158.2, ox, oy, scale)
    s2_tail = _tx(144.1, 292.7, ox, oy, scale)
    draw_pie(draw, s1_head, s1_tail,
             bow_perp=16 * scale, w_head=9 * scale, w_tail=3 * scale, steps=80)
    draw_shu(draw, s2_head, s2_tail, width=max(2, int(7 * scale)), top_curl=True)
