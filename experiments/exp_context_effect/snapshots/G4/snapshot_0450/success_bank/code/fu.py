"""父 (fù, "father", 4 strokes) — B2 pass.

X-crossing composite with two upper strokes above the crossing.

Strokes:
  s1 — 撇 (short upper-left).
  s2 — 点 (upper-right, tilted).
  s3 — 撇 (long down-left).
  s4 — 捺 (long down-right — sweeps DOWN through the pie mid, hence
       head placed ABOVE-LEFT of s3.head to avoid the inverted-V bug
       described in the 攴 lesson).

Joints:
  s3.mid ⇆ s4.mid @ BC — P (natural X-crossing at ~(116, 187)).
"""
from pie import draw_pie
from dian import draw_dian
from na import draw_na


def draw_fu(draw,
            s1_head=('TL', 0.95, 0.75), s1_tail=('ML', 0.55, 0.65),
            s2_head=('TC', 0.55, 0.75), s2_tail=('TR', 0.35, 0.95),
            s3_head=('C', 0.58, 0.36),  s3_tail=('BL', 0.36, 0.82),
            s4_head=('ML', 0.84, 0.66), s4_tail=('BR', 0.76, 0.90)):
    draw_pie(draw, s1_head, s1_tail, head_width=9, tail_width=1, curve=0.08)
    draw_dian(draw, s2_head, s2_tail, head_width=3, peak_width=10, curve=0.08)
    draw_pie(draw, s3_head, s3_tail, head_width=11, tail_width=1, curve=0.10)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.82, curve=0.10)
