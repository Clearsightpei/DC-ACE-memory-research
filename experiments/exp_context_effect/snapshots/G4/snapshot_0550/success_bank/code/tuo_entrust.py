"""乇 (tuō, "entrust", 3画) — Phase-3 char, B4 promotion.

Strokes:
  s1 — 短撇 (upper-right → mid-left).
  s2 — 横 (main crossbar, ML→MR with mild up-right slant).
  s3 — 竖弯钩 (top C → down C-column → bend at BC → sweep to BR, hook
       flick up-right).

Joints:
  s1 ⇆ s3    @ C  — N (~20 px gap).
  s2 × s3    @ mid — P (welded body crossing).
"""
from pie import draw_pie
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou


def draw_tuo_entrust(draw,
                     s1_head=('TC', 0.89, 0.82), s1_tail=('ML', 0.668, 0.327),
                     s2_head=('ML', 0.281, 0.898), s2_tail=('MR', 0.479, 0.688),
                     s3_head=('C', 0.122, 0.225), s3_belly=('C', 0.15, 0.85),
                     s3_corner=('BC', 0.12, 0.75),
                     s3_hook_pt=('BR', 0.55, 0.75),
                     s3_tip=('BR', 0.572, 0.241)):
    # OVERRIDE anchors for this composition per TR1.
    draw_pie(draw, s1_head, s1_tail,
             head_width=10, tail_width=1, curve=0.10)
    draw_heng(draw, s2_head, s2_tail, width=9)
    draw_shu_wan_gou(draw,
                     head=s3_head, belly=s3_belly, corner=s3_corner,
                     hook_pt=s3_hook_pt, tip=s3_tip,
                     head_w=8, belly_w=11, corner_w=11,
                     hook_start_w=10, tip_w=2)
