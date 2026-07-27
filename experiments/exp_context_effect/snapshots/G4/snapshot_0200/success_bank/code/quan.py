"""犬 (quǎn, "dog", 4 strokes) — B2 pass.

Composition: 大 (heng+pie+na) + upper-right dian.

Strokes:
  s1 — 横 (full-width bar; TR9 span-expanded).
  s2 — 撇 (upper-mid down-left, concave-right — curve=-0.12).
  s3 — 捺 (down-right from center-below-heng).
  s4 — 点 (small dot in upper-right area).

Joints:
  s1 × s2 near C — P (natural crossing).
  s1 × s3 — N-tangent at s3.head (just below heng).
  s2 × s3 — N (X arms diverge from apex just below heng).
"""
from heng import draw_heng
from pie import draw_pie
from na import draw_na
from dian import draw_dian


def draw_quan(draw,
              s1_head=('ML', 0.15, 0.55), s1_tail=('MR', 0.90, 0.55),
              s2_head=('TC', 0.60, 0.35), s2_tail=('BL', 0.30, 0.92),
              s3_head=('C', 0.40, 0.60),  s3_tail=('BR', 0.85, 0.92),
              s4_head=('TR', 0.20, 0.55), s4_tail=('TR', 0.55, 0.80)):
    draw_heng(draw, s1_head, s1_tail, width=8)
    draw_pie(draw, s2_head, s2_tail, head_width=10, tail_width=1, curve=-0.12)
    draw_na(draw, s3_head, s3_tail,
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.8, curve=0.10)
    draw_dian(draw, s4_head, s4_tail, head_width=2, peak_width=11, curve=0.08)
