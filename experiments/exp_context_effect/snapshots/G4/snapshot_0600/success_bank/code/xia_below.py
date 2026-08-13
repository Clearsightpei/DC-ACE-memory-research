"""下 (xià, "below", 3画) — Phase-3 char, B4 promotion.

Strokes:
  s1 — 横 across top (ML→TR).
  s2 — 竖 vertical (C→BC, mid-column).
  s3 — 点 diagonal dot (C→MR, short down-right stroke).

Joints:
  s1.mid ⇆ s2.head @ TC — N (natural gap where 点-of-横 meets top of vertical).
  s2.mid ⇆ s3.head @ C  — N (dot starts near vertical body, small gap).
"""
from heng import draw_heng
from shu import draw_shu
from dian import draw_dian


def draw_xia_below(draw,
                   s1_head=('ML', 0.331, 0.002), s1_tail=('TR', 0.707, 0.92),
                   s2_head=('C', 0.427, 0.005), s2_tail=('BC', 0.494, 1.006),
                   s3_head=('C', 0.626, 0.479), s3_tail=('MR', 0.191, 0.896)):
    # OVERRIDE anchors for this composition per TR1.
    draw_heng(draw, s1_head, s1_tail, width=9)
    draw_shu(draw, s2_head, s2_tail, width=9)
    draw_dian(draw, s3_head, s3_tail,
              head_width=2, peak_width=10, curve=0.05, segments=24)
