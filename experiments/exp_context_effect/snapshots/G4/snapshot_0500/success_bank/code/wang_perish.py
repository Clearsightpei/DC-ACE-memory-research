"""亡 (wáng, "perish", 3画) — Phase-3 char, B4 promotion.

Related mastered: tou.py (亠 = 点+横) covers top half pattern.

Strokes:
  s1 — 点 (top dot, thin head upper-left → heavier tail lower-right).
  s2 — 横 (top horizontal, ML→MR, near-flat with small tilt).
  s3 — 竖折 (bottom L: down from under s2 → right along baseline).

Joint: s2.mid(~22%) ⇆ s3.head @ ML — N (~10-15 px gap, TR10 ≤25 px).
"""
from dian import draw_dian
from heng import draw_heng
from shu_zhe import draw_shu_zhe


def draw_wang_perish(draw,
                     s1_head=('TC', 0.307, 0.691), s1_tail=('C', 0.734, 0.043),
                     s2_head=('ML', 0.30, 0.65), s2_tail=('MR', 0.75, 0.60),
                     s3_head=('ML', 0.84, 0.78),
                     s3_corner=('BL', 0.30, 0.55),
                     s3_tail=('BR', 0.70, 0.55)):
    # OVERRIDE anchors for this composition per TR1.
    draw_dian(draw,
              from_anchor=s1_head, to_anchor=s1_tail,
              head_width=2, peak_width=11, curve=0.08, segments=24)
    draw_heng(draw, from_anchor=s2_head, to_anchor=s2_tail, width=10)
    draw_shu_zhe(draw,
                 head=s3_head, corner=s3_corner, tail=s3_tail,
                 v_width=10, h_width=10, shoulder=13)
