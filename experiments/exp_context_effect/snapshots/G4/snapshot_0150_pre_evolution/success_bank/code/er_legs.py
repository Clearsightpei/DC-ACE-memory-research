"""儿 (ér, "legs", 2 strokes: 撇 + 竖弯钩) — B1 retry-1 pass.

Bootstrap batch failed because the 竖弯钩 tip landed below-right of
the corner (long down-right tail instead of canonical up-tick). Retry
fix (per errata canonical recipe): re-anchor so body descends through
TC→C→BC, sweeps right into BR at hook_pt, then flicks UP.

Strokes:
  s1 — 撇 (left, unchanged from bootstrap — was fine).
  s2 — 竖弯钩 (right, re-anchored: TC head → C belly → BC corner →
       BR hook_pt (0.20, 0.70) → BR tip (0.25, 0.40)).

Joints: none per MMH spec.
"""
from pie import draw_pie
from shu_wan_gou import draw_shu_wan_gou


def draw_er_legs(draw,
                 s1_head=('ML', 0.929, 0.093),
                 s1_tail=('BL', 0.393, 0.827),
                 s2_head=('TC', 0.55, 0.20),
                 s2_belly=('C', 0.55, 0.50),
                 s2_corner=('BC', 0.60, 0.75),
                 s2_hook_pt=('BR', 0.20, 0.70),
                 s2_tip=('BR', 0.25, 0.40)):
    draw_pie(draw, s1_head, s1_tail,
             head_width=11, tail_width=1, curve=0.10, segments=48)
    draw_shu_wan_gou(draw, s2_head, s2_belly, s2_corner, s2_hook_pt, s2_tip,
                     head_w=8, belly_w=12, corner_w=11,
                     hook_start_w=10, tip_w=2)
