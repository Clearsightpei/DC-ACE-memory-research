"""饣 (shí, "food radical, simplified", 3 strokes) — B1 pass.

Strokes:
  s1 — short 撇 (upper-mid diagonal, tail in top of C).
  s2 — 横钩 (short horizontal + down-left hook flick).
  s3 — 竖提 (vertical body + rising ti-flick at bottom-right).

Joints (N-class):
  s1.mid ⇆ s2.head (~10-15 px).
  s1.mid ⇆ s3.head (~40-50 px, slightly wide but reads separate).
"""
from pie import draw_pie
from heng_gou import draw_heng_gou
from shu_ti import draw_shu_ti


def draw_shi_food(draw,
                  s1_head=('TC', 0.65, 0.45), s1_tail=('C', 0.15, 0.55),
                  s2_head=('C', 0.25, 0.55),
                  s2_shoulder=('C', 0.90, 0.60),
                  s2_tip=('C', 0.70, 0.90),
                  s3_shu_head=('C', 0.50, 0.80),
                  s3_shu_tail=('BC', 0.50, 0.55),
                  s3_ti_tail=('BC', 0.98, 0.30)):
    draw_pie(draw, s1_head, s1_tail,
             head_width=11, tail_width=2, curve=0.06, segments=48)
    draw_heng_gou(draw, s2_head, s2_shoulder, s2_tip,
                  head_w=7, mid_w=6, shoulder_w=10, tip_w=2)
    draw_shu_ti(draw, s3_shu_head, s3_shu_tail, s3_ti_tail,
                shu_head_w=10, shu_tail_w=9,
                ti_head_w=12, ti_tail_w=1)
