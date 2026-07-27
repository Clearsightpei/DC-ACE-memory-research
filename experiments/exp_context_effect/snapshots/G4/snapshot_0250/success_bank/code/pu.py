"""攵 (pū, "rap", 4 strokes) — B2 pass.

Right-side radical (as in 政, 教, 敬). Composite of two upper marks
(short 撇 + short 横) followed by a 撇 + 捺 X-crossing at bottom.

The s3/s4 tails are OVERRIDDEN from MMH's BL/BR to BC/BC so the
crossing is a true P-weld, not a splayed inverted-V (lesson from
p2_radical_109_攴 bootstrap failure).

Strokes:
  s1 — 撇 (top-right down-left sweep).
  s2 — 横 (short bar upper-left area).
  s3 — 撇 (down-left crossing).
  s4 — 捺 (down-right crossing).

Joints:
  s1.mid(0.42) ⇆ s2.head @ C  — N (~25 px).
  s1.mid(0.75) ⇆ s4.head @ ML — N (~18 px).
  s2.mid(0.31) ⇆ s3.head @ C  — N (~14 px).
  s3.mid(0.48) ⇆ s4.mid(0.38) @ BC — P (welded X).
"""
from _anchor import anchor_to_xy
from pie import draw_pie
from heng import draw_heng
from na import draw_na


def draw_pu(draw,
            s1_head=('TC', 0.172, 0.756), s1_tail=('BL', 0.639, 0.039),
            s2_head=('C', 0.16, 0.436),  s2_tail=('MR', 0.188, 0.26),
            s3_head=('C', 0.582, 0.471), s3_tail=('BC', 0.38, 0.81),
            s4_head=('ML', 0.952, 0.758), s4_tail=('BC', 0.97, 0.9)):
    draw_pie(draw, s1_head, s1_tail, head_width=10, tail_width=2, curve=0.14)
    draw_heng(draw, s2_head, s2_tail, width=8)
    draw_pie(draw, s3_head, s3_tail, head_width=11, tail_width=2, curve=0.09)
    draw_na(draw, s4_head, s4_tail,
            head_width=3, peak_width=13, tail_width=1,
            peak_t=0.78, curve=0.08)
    # P-weld disc at approximate s3×s4 crossing.
    p3h = anchor_to_xy(s3_head); p3t = anchor_to_xy(s3_tail)
    p4h = anchor_to_xy(s4_head); p4t = anchor_to_xy(s4_tail)
    p3_mid = (p3h[0]*0.52 + p3t[0]*0.48, p3h[1]*0.52 + p3t[1]*0.48)
    r = 4
    draw.ellipse([p3_mid[0]-r, p3_mid[1]-r, p3_mid[0]+r, p3_mid[1]+r],
                 fill=(0, 0, 0))
