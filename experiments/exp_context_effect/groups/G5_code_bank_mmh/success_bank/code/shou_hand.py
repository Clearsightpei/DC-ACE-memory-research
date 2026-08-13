"""Bank primitive: 扌 (shou, 'hand-radical' left position — 3 strokes: heng + shu_gou + ti).

Promoted from p2_radical_068_扌 (G5 B1 PASS, 2026-08-08). VERY HIGH-REUSE:
left-position hand radical in 打/找/把/接/拿/挂/... The 提 ti stroke rises
diagonally from lower-left to upper-right, crossing the vertical.

Uses the new ti.py stroke primitive.
"""

from PIL import ImageDraw

from heng import draw_heng
from shu_gou import draw_shu_gou
from ti import draw_ti


def _tx(x, y, ox, oy, scale):
    return (ox + x * scale, oy + y * scale)


def draw_shou(draw: ImageDraw.ImageDraw, ox=0, oy=0, scale=1.0):
    s1_head = _tx(102, 138, ox, oy, scale)
    s1_tail = _tx(187, 126, ox, oy, scale)
    s2_head = _tx(143, 67, ox, oy, scale)
    s2_tail = _tx(115, 263, ox, oy, scale)
    s3_head = _tx(85, 220, ox, oy, scale)
    s3_tail = _tx(189, 172, ox, oy, scale)
    draw_heng(draw, s1_head, s1_tail,
              width_head=max(2, int(8 * scale)),
              width_tail=max(2, int(9 * scale)))
    draw_shu_gou(draw, s2_head, s2_tail,
                 width=max(2, int(7 * scale)),
                 hook_start_offset=max(10, int(25 * scale)))
    draw_ti(draw, s3_head, s3_tail,
            w_head=max(3, int(9 * scale)), w_tail=max(1, int(2 * scale)))
