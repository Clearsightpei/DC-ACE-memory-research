"""宀 (mián, "roof", 3 strokes: 点 + 点 + 横钩) — B1 pass.

Strokes:
  s1 — top 点 (rounded press above the roof).
  s2 — short left 点 (vertical-leaning dot at the left corner).
  s3 — 横钩 (horizontal top + down-left hook at the right end).

Joints: s1 sits above the roof (N-gap ~7-12 px); s2 & s3 near the
top-left corner (N-gap).
"""
from dian import draw_dian
from heng_gou import draw_heng_gou


def draw_mian(draw,
              s1_head=('TC', 0.35, 0.55), s1_tail=('C', 0.55, 0.20),
              s2_head=('ML', 0.55, 0.60), s2_tail=('BL', 0.42, 0.15),
              s3_head=('ML', 0.55, 0.75),
              s3_shoulder=('MR', 0.60, 0.75),
              s3_tip=('MR', 0.30, 1.00)):
    draw_dian(draw, s1_head, s1_tail,
              head_width=2, peak_width=8, curve=0.08, segments=24)
    draw_dian(draw, s2_head, s2_tail,
              head_width=2, peak_width=8, curve=0.06, segments=24)
    draw_heng_gou(draw, s3_head, s3_shoulder, s3_tip,
                  head_w=8, mid_w=7, shoulder_w=12, tip_w=2)
