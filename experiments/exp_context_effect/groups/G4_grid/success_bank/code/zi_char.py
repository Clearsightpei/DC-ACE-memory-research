"""子 (zǐ, "child", 3画) — Phase-3 char, B4 promotion.

Errata p2_082_子 fix applied: s2 belly biased RIGHT, hook_pt right-lower,
tip up-and-LEFT so wan_gou reads as 子's characteristic bulge. s1 corner
lowered so 横 opening reads FLAT (level, not hat-sloped).

Strokes:
  s1 — 横撇 (TL → TC-corner nearly level → C tip).
  s2 — 弯钩 (C → belly rightward → BC hook tip up-left).
  s3 — 横 (ML→MR, welds through s2 body).

Joints:
  s1.tail ⇆ s2.head @ C — N (~13 px gap, do NOT weld).
  s2.mid  × s3.mid  @ C — P (welded crossing).
"""
from heng import draw_heng
from heng_pie import draw_heng_pie
from wan_gou import draw_wan_gou


def draw_zi_char(draw,
                 s1_head=('TL', 0.86, 0.92), s1_corner=('TC', 0.90, 0.85),
                 s1_tip=('C', 0.57, 0.32),
                 s2_head=('C', 0.38, 0.28), s2_belly=('C', 0.70, 0.62),
                 s2_hook_pt=('BC', 0.35, 0.92), s2_tip=('BC', 0.03, 0.73),
                 s3_head=('ML', 0.35, 0.81), s3_tail=('MR', 0.75, 0.76)):
    # OVERRIDE anchors for this composition per TR1.
    draw_heng_pie(draw, s1_head, s1_corner, s1_tip,
                  head_w=7, corner_w=10, tip_w=4)
    draw_wan_gou(draw, s2_head, s2_belly, s2_hook_pt, s2_tip,
                 head_w=8, belly_w=12, hook_start_w=10, tip_w=2)
    draw_heng(draw, s3_head, s3_tail, width=9)
