"""p1_stroke_31_竖折折钩 attempt.

竖折折钩 (shù zhé zhé gōu) — 竖折折 with a hook flick at the end.

Structure (extension of p1_stroke_28_竖折折):
  1. shu1  : head    (TL 0.40, 0.25)  →  corner1 (ML 0.40, 0.70)  (vertical descent)
  2. heng  : corner1                  →  corner2 (C  0.85, 0.70)  (horizontal right)
  3. shu2  : corner2                  →  hook_pt (BC 0.85, 0.75)  (final descent, vertical)
  4. gou   : hook_pt                  →  tip     (BC 0.55, 0.55)  (short up-left flick)

Joints:
  - corner1: P (welded), 竖→横
  - corner2: P (welded), 横→竖
  - hook is internal to the final 竖 segment (see principle_bank:
    "hook is treated as an internal segment of the same primitive, NOT
    a separate joint").

Reuses `fat_line`, `quad_bezier`, `stroke_variable_width` from
`_anchor.py`. Base pattern derived from `shu_zhe.py` (batch1 pass) and
`p1_stroke_28_竖折折` (structural precedent). Hook technique borrowed
from `shu_gou.py` (small curl before rising up-left).
"""
import sys
import os

_SB_CODE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..', 'success_bank', 'code'
))
if _SB_CODE not in sys.path:
    sys.path.insert(0, _SB_CODE)

from PIL import Image, ImageDraw
from _anchor import (anchor_to_xy, fat_line, quad_bezier,
                     stroke_variable_width)


def draw_shu_zhe_zhe_gou(draw,
                         head, corner1, corner2, hook_pt, tip,
                         v_width=10, h_width=10, shoulder=13,
                         hook_start_w=10, tip_w=1,
                         color=(0, 0, 0)):
    p_head = anchor_to_xy(head)
    p_c1 = anchor_to_xy(corner1)
    p_c2 = anchor_to_xy(corner2)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)

    # Sanity assertions (principle_bank: catch silent geometric bugs).
    assert p_c1[1] > p_head[1], "shu1 must drop downward"
    assert p_c2[0] > p_c1[0], "heng must go rightward"
    assert p_hook[1] > p_c2[1], "shu2 must drop downward"
    assert p_tip[1] < p_hook[1], "hook flick must go upward"
    assert p_tip[0] < p_hook[0], "hook flick must go leftward"

    # Three body segments.
    fat_line(draw, p_head, p_c1, v_width, color)   # 竖
    fat_line(draw, p_c1, p_c2, h_width, color)     # 折 → 横
    fat_line(draw, p_c2, p_hook, v_width, color)   # 折 → 竖

    # 顿笔 discs at every welded corner.
    r = shoulder / 2.0
    for (cx, cy) in (p_c1, p_c2):
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=color)

    # Hook: short curved flick up-and-left from p_hook to p_tip.
    ctrl = (p_hook[0] - (p_hook[0] - p_tip[0]) * 0.25,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.10)
    hook_pts = quad_bezier(p_hook, ctrl, p_tip, n=25)
    n = len(hook_pts)
    hook_widths = [hook_start_w * (1 - i / (n - 1)) + tip_w * (i / (n - 1))
                   for i in range(n)]
    stroke_variable_width(draw, hook_pts, hook_widths, color)


def main():
    img = Image.new('RGB', (300, 300), 'white')
    draw = ImageDraw.Draw(img)

    draw_shu_zhe_zhe_gou(
        draw,
        head    =('TL', 0.40, 0.25),
        corner1 =('ML', 0.40, 0.70),
        corner2 =('C',  0.85, 0.70),
        hook_pt =('BC', 0.85, 0.75),
        tip     =('BC', 0.55, 0.55),
        v_width=10, h_width=10, shoulder=13,
        hook_start_w=10, tip_w=1,
    )

    out = os.path.join(os.path.dirname(__file__), '01_竖折折钩.png')
    img.save(out)
    print(f"wrote {out} size={img.size}")


if __name__ == '__main__':
    main()
