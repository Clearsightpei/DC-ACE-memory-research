"""Bank primitive: 小 (xiao, "small" — 3 strokes: shu_gou + pie + dian).

Promoted from p2_radical_076_小 (G5 B2 PASS 2026-08-08). HIGH-REUSE:
appears as bottom-radical in 尔/示/京/常/... and as compound 少. Center
shu-gou anchors the composition; left pie and right dian are separated
from the shaft (no joints).
"""

from PIL import ImageDraw

from shu_gou import draw_shu_gou
from pie import draw_pie
from dian import draw_dian


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_xiao(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1: center 竖钩 (small hook to lower-left)
    draw_shu_gou(draw, head=_tx(142, 74, ox, oy, scale),
                 tail=_tx(105, 267, ox, oy, scale),
                 width=max(2, int(7 * scale)),
                 hook_start_offset=max(10, int(35 * scale)))
    # s2: left 撇
    draw_pie(draw, head=_tx(82, 161, ox, oy, scale),
             tail=_tx(50, 220, ox, oy, scale),
             bow_perp=max(2, int(6 * scale)),
             w_head=max(2, int(8 * scale)),
             w_tail=max(1, int(3 * scale)))
    # s3: right 点
    draw_dian(draw, head=_tx(208, 155, ox, oy, scale),
              tail=_tx(258, 209, ox, oy, scale),
              w_head=max(2, int(3 * scale)),
              w_tail=max(3, int(8 * scale)),
              bow=max(2, int(4 * scale)))
