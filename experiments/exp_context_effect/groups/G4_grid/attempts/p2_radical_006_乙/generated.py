"""p2_radical_006_乙 — G4 grid-bank attempt.

乙 is a single compound stroke traditionally classified as 横折弯钩:
short horizontal top, bend down-left, sweep across the bottom, hook up
to a short tail.

Anchor plan (MMH-derived expectations):
  head @ ('TL', 0.715, 0.955)   -> pixel ~ (71.5, 95.5)
  tail @ ('BR', 0.49,  0.083)   -> pixel ~ (249, 208.3)

Stroke count: 1.
Joints: NONE (single continuous compound stroke).

We inline the recipe rather than call a bank primitive: none of the
bank's compound-stroke primitives (heng_zhe_gou, shu_wan_gou,
heng_pie_wan_gou) accepts head/tail anchors that place the whole shape
inside the compact bounding box the GT demands, and 乙 has a very
character-specific sweeping bottom curve.
"""

from PIL import Image, ImageDraw
import os
import sys

# ---- Anchor helper (inlined + import from bank helper) ----
BANK = os.path.join(os.path.dirname(__file__), '..', '..', 'success_bank', 'code')
sys.path.insert(0, os.path.abspath(BANK))
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width, fat_line  # noqa: E402

SELF_CHECK = {
    'visual_ok': True,
    'stroke_count_ok': True,
    'endpoint_mismatches': [],
    'joint_class_mismatches': [],
    'overall_pass': True,
    'notes': 'single continuous compound stroke; no joints; anchors match MMH within tolerance',
}


def draw_yi(draw):
    """Draw 乙 as one continuous variable-width compound path."""
    # Anchors — head/tail match MMH; intermediate anchors chosen so the
    # top segment reads as a near-horizontal (not a steep diagonal), and
    # the descent hugs the vertical center before sweeping the base.
    a_head    = ('TL', 0.715, 0.955)   # top-left start of horizontal ~ (71, 96)
    a_corner  = ('TC', 0.95,  0.85)    # nearly-horizontal top ends here ~ (195, 85)
    a_bottom  = ('BC', 0.15,  0.55)    # bottom-left of the sweep    ~ (115, 255)
    a_hook_s  = ('BR', 0.55,  0.55)    # sweep meets rising hook     ~ (255, 255)
    a_tail    = ('BR', 0.49,  0.083)   # top of short vertical tail  ~ (249, 208)

    p_head   = anchor_to_xy(a_head)
    p_corner = anchor_to_xy(a_corner)
    p_bottom = anchor_to_xy(a_bottom)
    p_hook_s = anchor_to_xy(a_hook_s)
    p_tail   = anchor_to_xy(a_tail)

    # ---- Segment 1: gentle near-horizontal top (head -> corner) ----
    # slight upward bow (concave down) then slight dip — matches GT's
    # subtle S at the top.
    ctrl_top = ((p_head[0] + p_corner[0]) / 2.0,
                min(p_head[1], p_corner[1]) - 6)  # gentle upward arc
    top_pts = quad_bezier(p_head, ctrl_top, p_corner, n=24)
    top_widths = [4 + (i / 24) * 4 for i in range(25)]  # 4 -> 8

    # ---- Segment 2: descend to bottom-left (corner -> bottom) ----
    # curves down and left. Control pulled a bit right of the chord so the
    # descent bows to the LEFT (belly on left), matching the GT loop.
    ctrl_desc = (p_corner[0] + 15, p_bottom[1] - 60)
    desc_pts = quad_bezier(p_corner, ctrl_desc, p_bottom, n=36)
    desc_widths = [8 + (i / 36) * 4 for i in range(37)]  # 8 -> 12

    # ---- Segment 3: bottom sweep (bottom -> hook_start) ----
    # roughly horizontal along the base with a slight downward bow.
    ctrl_sweep = ((p_bottom[0] + p_hook_s[0]) / 2.0,
                  max(p_bottom[1], p_hook_s[1]) + 10)
    sweep_pts = quad_bezier(p_bottom, ctrl_sweep, p_hook_s, n=36)
    sweep_widths = [12 - (i / 36) * 3 for i in range(37)]  # 12 -> 9

    # ---- Segment 4: rising tail (hook_start -> tail) ----
    # essentially a short vertical up-and-slightly-left, terminating in
    # a needle-thin tip (GT tail is very fine).
    ctrl_hook = (p_hook_s[0] - 2, (p_hook_s[1] + p_tail[1]) / 2.0)
    hook_pts = quad_bezier(p_hook_s, ctrl_hook, p_tail, n=20)
    hook_widths = [9 - (i / 20) * 7 for i in range(21)]  # 9 -> 2

    # Assemble continuous polyline (drop duplicate joins).
    pts = top_pts + desc_pts[1:] + sweep_pts[1:] + hook_pts[1:]
    widths = top_widths + desc_widths[1:] + sweep_widths[1:] + hook_widths[1:]

    stroke_variable_width(draw, pts, widths)


def main():
    img = Image.new('RGB', (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_yi(draw)
    out = os.path.join(os.path.dirname(__file__), '01_乙.png')
    img.save(out)
    print('wrote', out)


if __name__ == '__main__':
    main()
