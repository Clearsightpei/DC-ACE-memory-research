"""入 (rù, "enter", 2 strokes: 撇 + 捺) — B1 pass.

Similar to 人 but the 撇 head starts lower (below the 捺 head), and the
strokes meet with an N-class small gap at the top, not welded.

Strokes:
  s1 — 撇 from C center down-left to BL.
  s2 — 捺 from apex TC(0.00,1.00) down-right to BR foot.

Joint: s1.head ⇆ s2.head → N (~12 px gap).
"""
from pie import draw_pie
from na import draw_na


def draw_ru(draw,
            pie_head=('C', 0.42, 0.50), pie_tail=('BL', 0.34, 0.74),
            na_head=('TC', 0.00, 1.00), na_tail=('BR', 0.84, 0.73)):
    draw_pie(draw, pie_head, pie_tail,
             head_width=11, tail_width=2, curve=0.10, segments=48)
    draw_na(draw, na_head, na_tail,
            head_width=3, peak_width=14, tail_width=1,
            peak_t=0.85, curve=0.08, segments=48)
