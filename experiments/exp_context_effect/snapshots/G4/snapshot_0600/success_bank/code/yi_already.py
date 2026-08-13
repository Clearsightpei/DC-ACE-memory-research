"""已 (yǐ, "already", 3画) — B4 main promotion.

Distinguishes 己/已/巳: 已 has s2 touching s1 at C (right side, sealing
the top box near-closed).

Strokes:
  s1 — 横折 (top bracket): TL head → TC corner → C tail.
  s2 — 短横 (small middle horizontal): ML head → C tail.
  s3 — 竖弯钩 (bottom sweep with rising hook): ML head → BL bend →
       BC sweep → BR hook base → BR hook tip.

Joints (both N, ~16 px gaps):
  s1.tail ⇆ s2.mid  @ C
  s2.head ⇆ s3.head @ ML
"""
from _anchor import anchor_to_xy, quad_bezier, stroke_variable_width


def draw_yi_already(draw):
    # s1 — 横折
    s1_head = anchor_to_xy(('TL', 0.832, 0.961))
    s1_corner = anchor_to_xy(('TC', 0.90, 0.90))
    s1_tail = anchor_to_xy(('C', 0.576, 0.427))
    ctrl_top = ((s1_head[0] + s1_corner[0]) / 2.0, min(s1_head[1], s1_corner[1]) - 4)
    top_pts = quad_bezier(s1_head, ctrl_top, s1_corner, n=28)
    ctrl_fold = (s1_corner[0] - 6, (s1_corner[1] + s1_tail[1]) / 2.0)
    fold_pts = quad_bezier(s1_corner, ctrl_fold, s1_tail, n=18)
    stroke_variable_width(draw, top_pts + fold_pts[1:],
                          [5 + i / 28 * 2 for i in range(29)] +
                          [7 - i / 18 * 2 for i in range(1, 19)])

    # s2 — 短横
    s2_head = anchor_to_xy(('ML', 0.861, 0.717))
    s2_tail = anchor_to_xy(('C', 0.787, 0.544))
    ctrl_s2 = ((s2_head[0] + s2_tail[0]) / 2.0, (s2_head[1] + s2_tail[1]) / 2.0 - 2)
    s2_pts = quad_bezier(s2_head, ctrl_s2, s2_tail, n=20)
    stroke_variable_width(draw, s2_pts, [5 + i / 20 * 1 for i in range(21)])

    # s3 — 竖弯钩
    s3_head = anchor_to_xy(('ML', 0.677, 0.315))
    s3_bend = anchor_to_xy(('BL', 0.55, 0.85))
    s3_sweep = anchor_to_xy(('BC', 0.80, 0.88))
    s3_hook_s = anchor_to_xy(('BR', 0.60, 0.80))
    s3_tail = anchor_to_xy(('BR', 0.505, 0.083))
    desc = quad_bezier(s3_head, (s3_head[0] - 6, (s3_head[1] + s3_bend[1]) / 2.0), s3_bend, n=32)
    sweep = quad_bezier(s3_bend, ((s3_bend[0] + s3_sweep[0]) / 2.0, max(s3_bend[1], s3_sweep[1]) + 6), s3_sweep, n=32)
    rnd = quad_bezier(s3_sweep, (s3_sweep[0] + 25, s3_sweep[1]), s3_hook_s, n=20)
    hook = quad_bezier(s3_hook_s, (s3_hook_s[0] + 2, (s3_hook_s[1] + s3_tail[1]) / 2.0), s3_tail, n=18)
    stroke_variable_width(draw, desc + sweep[1:] + rnd[1:] + hook[1:],
                          [6 + i / 32 * 3 for i in range(33)] +
                          [9 + i / 32 * 1 for i in range(1, 33)] +
                          [10 - i / 20 * 2 for i in range(1, 21)] +
                          [8 - i / 18 * 6 for i in range(1, 19)])
