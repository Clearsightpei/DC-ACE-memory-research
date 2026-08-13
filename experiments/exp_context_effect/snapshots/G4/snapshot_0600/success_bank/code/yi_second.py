"""乙 (yǐ) — Phase-2 radical, 1画 (compound stroke 横折弯钩).

Inlined recipe (not a bank primitive wrapper) — 乙's shape is
character-specific and no bank compound-stroke primitive maps 1:1
onto its top-horizontal → wrap → bottom-sweep → tail geometry.

Anchor plan (米字格, PIL-native):
  head    @ ('TL', 0.715, 0.955)   — top-left start of horizontal
  corner  @ ('TC', 0.95,  0.85)    — top ends here (nearly-horizontal)
  bottom  @ ('BC', 0.15,  0.55)    — bottom-left of the sweep
  hook_s  @ ('BR', 0.55,  0.55)    — sweep meets rising hook base
  tail    @ ('BR', 0.49,  0.083)   — top of short vertical tail

Stroke count: 1 (single continuous variable-width path).
Joints: NONE.

Human PASS (bootstrap batch, 2026-07-17).
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width  # noqa: E402


def draw_yi_second(draw,
                   head=('TL', 0.715, 0.955),
                   corner=('TC', 0.95, 0.85),
                   bottom=('BC', 0.15, 0.55),
                   hook_s=('BR', 0.55, 0.55),
                   tail=('BR', 0.49, 0.083)):
    """Render 乙 as one continuous variable-width compound path."""
    p_head   = anchor_to_xy(head)
    p_corner = anchor_to_xy(corner)
    p_bottom = anchor_to_xy(bottom)
    p_hook_s = anchor_to_xy(hook_s)
    p_tail   = anchor_to_xy(tail)

    # Segment 1: near-horizontal top (head -> corner) with gentle upward arc.
    ctrl_top = ((p_head[0] + p_corner[0]) / 2.0,
                min(p_head[1], p_corner[1]) - 6)
    top_pts = quad_bezier(p_head, ctrl_top, p_corner, n=24)
    top_widths = [4 + (i / 24) * 4 for i in range(25)]

    # Segment 2: descend to bottom-left (corner -> bottom), left-bowed belly.
    ctrl_desc = (p_corner[0] + 15, p_bottom[1] - 60)
    desc_pts = quad_bezier(p_corner, ctrl_desc, p_bottom, n=36)
    desc_widths = [8 + (i / 36) * 4 for i in range(37)]

    # Segment 3: bottom sweep (bottom -> hook_s) roughly horizontal.
    ctrl_sweep = ((p_bottom[0] + p_hook_s[0]) / 2.0,
                  max(p_bottom[1], p_hook_s[1]) + 10)
    sweep_pts = quad_bezier(p_bottom, ctrl_sweep, p_hook_s, n=36)
    sweep_widths = [12 - (i / 36) * 3 for i in range(37)]

    # Segment 4: rising tail (hook_s -> tail) — short vertical needle.
    ctrl_hook = (p_hook_s[0] - 2, (p_hook_s[1] + p_tail[1]) / 2.0)
    hook_pts = quad_bezier(p_hook_s, ctrl_hook, p_tail, n=20)
    hook_widths = [9 - (i / 20) * 7 for i in range(21)]

    pts = top_pts + desc_pts[1:] + sweep_pts[1:] + hook_pts[1:]
    widths = top_widths + desc_widths[1:] + sweep_widths[1:] + hook_widths[1:]
    stroke_variable_width(draw, pts, widths)
