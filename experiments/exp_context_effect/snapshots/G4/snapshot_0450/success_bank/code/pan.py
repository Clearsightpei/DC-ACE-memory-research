"""丬 (pán, "left-爿", 3 strokes) — B2 pass.

Strokes:
  s1 — 撇 (short, upper — anchors intentionally swapped for curve
       orientation).
  s2 — 提 (rising, from BL upward to center).
  s3 — 竖 (short center-bottom vertical).

Joints:
  s2.tail ⇆ s3.mid @ C — N (~10 px measured, target ~27 px per MMH).
"""
from pie import draw_pie
from ti import draw_ti
from shu import draw_shu


def draw_pan(draw,
             s1_head=('C', 0.342, 0.424), s1_tail=('C', 0.046, 0.081),
             s2_head=('BL', 0.87, 0.306), s2_tail=('C', 0.576, 0.749),
             s3_head=('TC', 0.538, 0.7),  s3_tail=('BC', 0.638, 1.026)):
    # Anchors for s1 intentionally reversed from MMH order so the
    # pie primitive's curve bows in the correct direction.
    draw_pie(draw, s1_head, s1_tail, head_width=8, tail_width=2, curve=0.12)
    draw_ti(draw, s2_head, s2_tail, head_width=11, tail_width=1, curve=0.08)
    draw_shu(draw, s3_head, s3_tail, width=9)
