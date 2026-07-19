"""人 (rén, "person", 2 strokes: 撇 + 捺) — B1 pass.

Strokes:
  s1 — 撇 sweeping from upper-mid to lower-left.
  s2 — 捺 sweeping from upper-mid to lower-right, with a broadened
       foot (顿笔) at the tail.

Joint: s1.head ⇆ s2.head → T-class (welded, near the apex).
"""
from pie import draw_pie
from na import draw_na


def draw_ren(draw,
             s1_head=('TC', 0.45, 0.25), s1_tail=('BL', 0.15, 0.85),
             s2_head=('C', 0.15, 0.25), s2_tail=('BR', 0.85, 0.85)):
    draw_pie(draw, s1_head, s1_tail,
             head_width=12, tail_width=1, curve=0.10, segments=48)
    draw_na(draw, s2_head, s2_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.85, curve=0.10, segments=48)
