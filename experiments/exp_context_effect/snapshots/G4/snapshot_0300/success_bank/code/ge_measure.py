"""个 (gè, "measure word / individual", 3画) — Phase-3 char, B4 promotion.

Strokes:
  s1 — 撇 (TC apex → BL, gentle bow).
  s2 — 捺 (TC apex → MR, broadened foot).
  s3 — 竖 (C → BC, clipped near bottom edge).

Joint: s1.mid ⇆ s2.head @ C — N (~18 px gap, do NOT weld per TR10).
"""
from pie import draw_pie
from na import draw_na
from shu import draw_shu


def draw_ge_measure(draw,
                    s1_head=('TC', 0.40, 0.656), s1_tail=('BL', 0.34, 0.083),
                    s2_head=('TC', 0.529, 0.979), s2_tail=('MR', 0.859, 0.863),
                    s3_head=('C', 0.403, 0.553), s3_tail=('BC', 0.509, 0.98)):
    # OVERRIDE anchors for this composition per TR1.
    draw_pie(draw, s1_head, s1_tail,
             head_width=11, tail_width=1, curve=0.10, segments=48)
    draw_na(draw, s2_head, s2_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.85, curve=0.10, segments=48)
    draw_shu(draw, s3_head, s3_tail, width=8)
