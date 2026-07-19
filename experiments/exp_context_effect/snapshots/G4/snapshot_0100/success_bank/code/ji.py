"""几 (jī, 2 strokes: 撇 + 横折弯钩) — B1 pass.

The 横折弯钩 (top-bar + descent + round sweep + up-flick) has NO clean
bank primitive that fits without extreme transformation, so it is
inlined as a 4-segment variable-width path.

Anchors (per successful drawer attempt):
  s1 撇: head TL(0.90, 0.40) → tail BL(0.30, 0.90).  (TR9 override — the
    standalone radical's 撇 starts at the top, not near the bottom.)
  s2 横折弯钩 (inlined):
    head @ TL(0.98, 0.35), corner @ TR(0.10, 0.40), knee @ BR(0.05, 0.75),
    hook_start @ BR(0.45, 0.60), tip @ BR(0.55, 0.30).

Joint: s1.head ⇆ s2.head → N-class (~15-20 px gap at top of the
  character).
"""
from PIL import ImageDraw  # noqa: F401
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width
from pie import draw_pie


def draw_ji(draw,
            s1_head=('TL', 0.90, 0.40),
            s1_tail=('BL', 0.30, 0.90),
            s2_head=('TL', 0.98, 0.35),
            s2_corner=('TR', 0.10, 0.40),
            s2_knee=('BR', 0.05, 0.75),
            s2_hook_s=('BR', 0.45, 0.60),
            s2_tip=('BR', 0.55, 0.30)):
    # s1 — 撇
    draw_pie(draw, s1_head, s1_tail,
             head_width=9, tail_width=1, curve=0.13, segments=48)

    # s2 — 横折弯钩 inlined
    p_head = anchor_to_xy(s2_head)
    p_corner = anchor_to_xy(s2_corner)
    p_knee = anchor_to_xy(s2_knee)
    p_hs = anchor_to_xy(s2_hook_s)
    p_tip = anchor_to_xy(s2_tip)

    ctrl_top = ((p_head[0] + p_corner[0]) / 2.0,
                min(p_head[1], p_corner[1]) - 2)
    top_pts = quad_bezier(p_head, ctrl_top, p_corner, n=24)
    top_widths = [6 + (i / 24) * 4 for i in range(25)]

    ctrl_desc = (p_corner[0] - 6, (p_corner[1] + p_knee[1]) / 2.0)
    desc_pts = quad_bezier(p_corner, ctrl_desc, p_knee, n=32)
    desc_widths = [10 - (i / 32) * 2 for i in range(33)]

    ctrl_sweep = ((p_knee[0] + p_hs[0]) / 2.0,
                  max(p_knee[1], p_hs[1]) + 8)
    sweep_pts = quad_bezier(p_knee, ctrl_sweep, p_hs, n=28)
    sweep_widths = [8 + (i / 28) * 1 for i in range(29)]

    ctrl_hook = ((p_hs[0] + p_tip[0]) / 2.0 - 2,
                 (p_hs[1] + p_tip[1]) / 2.0)
    hook_pts = quad_bezier(p_hs, ctrl_hook, p_tip, n=18)
    hook_widths = [9 - (i / 18) * 8 for i in range(19)]

    pts = top_pts + desc_pts[1:] + sweep_pts[1:] + hook_pts[1:]
    widths = top_widths + desc_widths[1:] + sweep_widths[1:] + hook_widths[1:]
    stroke_variable_width(draw, pts, widths)
