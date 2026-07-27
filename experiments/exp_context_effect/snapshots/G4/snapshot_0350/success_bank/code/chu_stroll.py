"""亍 (chù, "step / stroll", 3画) — Phase-3 char, B4 promotion.

Strokes:
  s1 — 短横 (top, TL→TR, thin, near y_frac 0.85).
  s2 — 长横 (middle, ML→MR, mild up-right slant).
  s3 — 竖钩 (C → BC, hook flicks up-and-left).

Joint: s2.mid ⇆ s3.head @ C — N (small natural writing gap, s3 head
just below s2 body; do NOT weld per TR10).
"""
from heng import draw_heng
from shu_gou import draw_shu_gou


def draw_chu_stroll(draw,
                    s1_head=('TL', 0.55, 0.85), s1_tail=('TR', 0.15, 0.80),
                    s2_head=('ML', 0.10, 0.60), s2_tail=('MR', 0.90, 0.50),
                    s3_head=('C', 0.42, 0.60), s3_belly=('C', 0.42, 0.90),
                    s3_hook_pt=('BC', 0.42, 0.65),
                    s3_tip=('BC', 0.10, 0.80)):
    # OVERRIDE anchors for this composition per TR1.
    draw_heng(draw, s1_head, s1_tail, width=7)
    draw_heng(draw, s2_head, s2_tail, width=8)
    draw_shu_gou(draw,
                 head=s3_head, belly=s3_belly,
                 hook_pt=s3_hook_pt, tip=s3_tip,
                 head_w=10, belly_w=9, hook_start_w=9, tip_w=2)
