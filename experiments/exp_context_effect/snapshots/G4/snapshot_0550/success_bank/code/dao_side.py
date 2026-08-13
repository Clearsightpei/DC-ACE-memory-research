"""刂 (dāo-side, "knife-radical", 2 strokes: 短竖 + 竖钩) — B1 retry-1 pass.

Bootstrap batch failed because verbatim MMH anchors put shu_gou's
head.x ≠ hook_pt.x, violating the straight-body invariant. The retry
fix (per errata + TR8): OVERRIDE hook_pt to share head's x_frac so
the body is strictly vertical, then tip goes up-and-left.

Strokes:
  s1 — 短竖 (short vertical, left column).
  s2 — 竖钩 (straight vertical body + up-left hook flick).

Joints: none (clear horizontal gap ~50 px between the two strokes).
"""
from shu import draw_shu
from shu_gou import draw_shu_gou


def draw_dao_side(draw,
                  s1_head=('C', 0.113, 0.16), s1_tail=('C', 0.113, 0.9),
                  s2_head=('TC', 0.614, 0.712),
                  s2_belly=('C', 0.614, 0.5),
                  s2_hook_pt=('BC', 0.614, 0.9),
                  s2_tip=('BC', 0.35, 0.6)):
    draw_shu(draw, s1_head, s1_tail, width=9)
    # NOTE: hook_pt shares head x_frac to satisfy shu_gou's
    # straight-body invariant. Do not "correct" back to MMH.
    draw_shu_gou(draw,
                 head=s2_head, belly=s2_belly,
                 hook_pt=s2_hook_pt, tip=s2_tip,
                 head_w=13, belly_w=12, hook_start_w=11, tip_w=2)
