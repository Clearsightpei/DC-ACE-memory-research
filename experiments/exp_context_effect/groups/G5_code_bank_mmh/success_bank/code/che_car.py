"""Bank primitive: 车 (che, "vehicle" — 4 strokes: heng + shu_zhe compound + heng + shu).

Promoted from p2_radical_089_车 (G5 B2 PASS 2026-08-08 via BANK_DEVIATION;
draw_shu_zhe repurposed as generic bent stroke for s2). MEDIUM-REUSE:
appears in 转/软/连/轻/较/... Three P (welded) joints stack the composition
around the central shu.
"""

from PIL import ImageDraw

from heng import draw_heng
from shu import draw_shu
from shu_zhe import draw_shu_zhe


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_che(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    # s1 top short heng
    draw_heng(draw, _tx(81, 113, ox, oy, scale),
              _tx(217, 103, ox, oy, scale),
              width_head=max(2, int(9 * scale)),
              width_tail=max(2, int(10 * scale)))
    # s2 撇折 compound via draw_shu_zhe (slanted first segment then horizontal)
    draw_shu_zhe(draw, head=_tx(139, 57, ox, oy, scale),
                 corner=_tx(96, 172, ox, oy, scale),
                 tail=_tx(218, 176, ox, oy, scale),
                 width=max(2, int(7 * scale)))
    # s3 long middle heng
    draw_heng(draw, _tx(33, 239, ox, oy, scale),
              _tx(267, 235, ox, oy, scale),
              width_head=max(2, int(10 * scale)),
              width_tail=max(2, int(12 * scale)))
    # s4 central 竖 (piercing) — tail clipped at 295 to stay on canvas
    draw_shu(draw, _tx(142, 148, ox, oy, scale),
             _tx(153, 295, ox, oy, scale),
             width=max(2, int(8 * scale)))
