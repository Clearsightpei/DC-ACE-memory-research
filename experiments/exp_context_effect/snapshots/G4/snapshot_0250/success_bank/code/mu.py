"""木 (mù, "tree", 4 strokes) — B2 pass.

Canonical 十-with-arms shape.

Strokes:
  s1 — 横 (full-width bar).
  s2 — 竖 (spine, x=0.5 fixed for P-weld guarantee).
  s3 — 撇 (left arm, sweeps down-left; curve NEGATIVE = concave-right).
  s4 — 捺 (right arm, sweeps down-right).

Joints:
  s1 × s2 @ C — P.
  s3 head + s4 head both at y_frac=0.45 (aligned to heng) — N connections
    to horizontal/vertical crossing per TR10 (all gaps ≤16 px).
"""
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie
from na import draw_na


def draw_mu(draw,
            s1_head=('ML', 0.10, 0.45), s1_tail=('MR', 0.90, 0.45),
            s2_head=('TC', 0.50, 0.15), s2_tail=('BC', 0.50, 0.90),
            s3_head=('C', 0.42, 0.45),  s3_tail=('BL', 0.10, 0.95),
            s4_head=('C', 0.55, 0.45),  s4_tail=('BR', 0.90, 0.90)):
    draw_heng(draw, s1_head, s1_tail, width=9)
    draw_shu(draw, s2_head, s2_tail, width=10)
    draw_pie(draw, s3_head, s3_tail, head_width=8, tail_width=1, curve=-0.08)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=10, tail_width=1,
            peak_t=0.75, curve=0.08)
