"""扌 (hand-side radical, 3 strokes: 横 + 竖钩 + 提) — B1 pass.

The 竖钩 primitive is inlined (custom shu_gou) so the body follows a
head→hook_pt line even when hook_pt.x ≠ head.x — the standard shu_gou
demands equal x, which doesn't fit this radical's slight lean.

Strokes:
  s1 — 横 (short horizontal upper area, slightly rising).
  s2 — 竖钩 with up-left hook (custom inline, hook tip at MMH tail).
  s3 — 提 (rising diagonal crossing s2 body in cell C).

Joints (both P by construction — 提 crosses 竖钩 body, 横 crosses 竖钩
body near top):
  s1 × s2 → P (weld at top).
  s2 × s3 → P (weld at mid-body).
"""
from _anchor import anchor_to_xy, sample_line, stroke_variable_width, quad_bezier
from heng import draw_heng
from ti import draw_ti


def _draw_shu_gou_custom(draw, head, hook_pt, tip,
                         head_w=11, mid_w=10, hook_start_w=9, tip_w=2):
    p_head = anchor_to_xy(head)
    p_hook = anchor_to_xy(hook_pt)
    p_tip = anchor_to_xy(tip)
    body_pts = sample_line(p_head, p_hook, n=60)
    n = len(body_pts) - 1
    body_widths = []
    for i in range(n + 1):
        t = i / n
        if t <= 0.55:
            u = t / 0.55
            w = head_w + (mid_w - head_w) * u
        else:
            u = (t - 0.55) / 0.45
            w = mid_w + (hook_start_w - mid_w) * u
        body_widths.append(w)
    stroke_variable_width(draw, body_pts, body_widths)
    ctrl = (p_hook[0] + (p_tip[0] - p_hook[0]) * 0.25,
            p_hook[1] + (p_tip[1] - p_hook[1]) * 0.1)
    hook_pts = quad_bezier(p_hook, ctrl, p_tip, n=25)
    m = len(hook_pts) - 1
    hook_widths = [hook_start_w + (tip_w - hook_start_w) * (i / m)
                   for i in range(m + 1)]
    stroke_variable_width(draw, hook_pts, hook_widths)


def draw_shou_side(draw,
                   s1_head=('C', 0.02, 0.383), s1_tail=('C', 0.866, 0.263),
                   s2_head=('TC', 0.433, 0.674),
                   s2_hook_pt=('BC', 0.43, 0.63),
                   s2_tip=('BC', 0.151, 0.631),
                   s3_head=('BL', 0.85, 0.203),
                   s3_tail=('C', 0.887, 0.717)):
    draw_heng(draw, s1_head, s1_tail, width=8)
    _draw_shu_gou_custom(draw, s2_head, s2_hook_pt, s2_tip,
                         head_w=11, mid_w=10, hook_start_w=9, tip_w=2)
    draw_ti(draw, s3_head, s3_tail, head_width=11, tail_width=1,
            curve=0.05, segments=48)
