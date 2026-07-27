"""亼 (jí, "gather", 3画) — Phase-3 char, B4 promotion.

Same 人-family apex structure as ren.py; MMH here labels the apex meet
as N with ~22 px gap (vs T for 人). Kept as N per TR10 (≤25 px still
visually connected — do NOT weld).

Strokes:
  s1 — 撇 (TC apex → BL, down-left).
  s2 — 捺 (TC apex → MR, down-right with peak swell).
  s3 — 横 (BL→BR, lower band).

Joint: s1.head ⇆ s2.head @ TC — N (~22 px gap).
"""
from pie import draw_pie
from na import draw_na
from heng import draw_heng


def draw_ji_gather(draw,
                   s1_head=('TC', 0.48, 0.72), s1_tail=('BL', 0.26, 0.21),
                   s2_head=('TC', 0.55, 0.82), s2_tail=('MR', 0.88, 0.93),
                   s3_head=('BL', 0.45, 0.63), s3_tail=('BR', 0.63, 0.62)):
    # OVERRIDE anchors for this composition per TR1.
    # s1/s2 heads deliberately pulled together to keep apex gap ≤25 px (TR10).
    draw_pie(draw, s1_head, s1_tail,
             head_width=11, tail_width=1, curve=0.10, segments=48)
    draw_na(draw, s2_head, s2_tail,
            head_width=3, peak_width=12, tail_width=1,
            peak_t=0.85, curve=0.10, segments=48)
    draw_heng(draw, s3_head, s3_tail, width=9)
