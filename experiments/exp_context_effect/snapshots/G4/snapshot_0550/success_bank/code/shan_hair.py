"""彡 (shān, "hair", 3 strokes: 3 parallel 撇) — B1 pass.

Three stacked 撇 sweeping upper-right to lower-left, no joints (S).
"""
from pie import draw_pie


def draw_shan_hair(draw,
                   s1_head=('TC', 0.696, 0.653), s1_tail=('C', 0.113, 0.532),
                   s2_head=('C', 0.734, 0.345), s2_tail=('BC', 0.166, 0.095),
                   s3_head=('C', 0.928, 0.887), s3_tail=('BL', 0.779, 1.103)):
    draw_pie(draw, from_anchor=s1_head, to_anchor=s1_tail,
             head_width=9, tail_width=1, curve=0.10)
    draw_pie(draw, from_anchor=s2_head, to_anchor=s2_tail,
             head_width=9, tail_width=1, curve=0.10)
    draw_pie(draw, from_anchor=s3_head, to_anchor=s3_tail,
             head_width=9, tail_width=1, curve=0.10)
