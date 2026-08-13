"""于 (yú, "at / in", 3画) — Phase-3 char, B4 promotion.

Strokes:
  s1 — 短横 (top, TL→TR).
  s2 — 长横 (middle, ML→MR — crosses s3 body).
  s3 — 竖钩 (TC → BC, hook flicks LEFT).

Joints:
  s1.mid ⇆ s3.head @ TC — N (~15 px gap; s3 head lifted just below s1).
  s2.mid × s3.mid  @ C  — P (welded crossing).
"""
from heng import draw_heng
from shu_gou import draw_shu_gou


def draw_yu_at(draw,
               s1_head=('TL', 0.867, 0.888), s1_tail=('TR', 0.112, 0.806),
               s2_head=('ML', 0.328, 0.646), s2_tail=('MR', 0.678, 0.512),
               s3_head=('TC', 0.359, 0.946), s3_hook_pt=('BC', 0.359, 0.73),
               s3_tip=('BC', 0.011, 0.55)):
    # OVERRIDE anchors for this composition per TR1.
    draw_heng(draw, s1_head, s1_tail, width=9)
    draw_heng(draw, s2_head, s2_tail, width=10)
    # NOTE: shu_gou called with head as belly too (straight body — TR8).
    draw_shu_gou(draw, s3_head, s3_head, s3_hook_pt, s3_tip,
                 head_w=11, belly_w=10, hook_start_w=9, tip_w=2)
