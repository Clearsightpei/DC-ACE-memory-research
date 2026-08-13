"""Bank primitive: 忄 (xin-left, heart-side radical — 3 strokes: dian + dian + shu_gou).

Promoted from p2_radical_077_忄 (G5 B2 PASS 2026-08-08). HIGH-REUSE
left-position radical: appears in 快/性/情/怕/怀/悟/... Left dian is long,
right dian short, central shu_gou pierces down through the middle with a
LEFT-curling hook at the bottom.
"""

from PIL import ImageDraw

from dian import draw_dian
from shu_gou import draw_shu_gou


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_xin_left(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 — left dian (long taper, slight rightward bow)
    draw_dian(draw, head=_tx(112, 147, ox, oy, scale),
              tail=_tx(101, 205, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(3, int(7 * scale)),
              bow=max(2, int(3 * scale)))
    # s2 — right dian (short, thick tail)
    draw_dian(draw, head=_tx(160, 137, ox, oy, scale),
              tail=_tx(189, 163, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(3, int(8 * scale)),
              bow=max(2, int(3 * scale)))
    # s3 — vertical shu-gou (hook curls LEFT at bottom)
    draw_shu_gou(draw, head=_tx(137, 70, ox, oy, scale),
                 tail=_tx(125, 290, ox, oy, scale),
                 width=max(2, int(7 * scale)),
                 hook_start_offset=max(10, int(25 * scale)))
