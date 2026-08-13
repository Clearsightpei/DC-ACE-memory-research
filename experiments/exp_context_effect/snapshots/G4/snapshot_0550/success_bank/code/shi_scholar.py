"""士 (shì, "scholar", 3 strokes: 横 + 竖 + 横) — B1 pass.

Distinguishing feature: top 横 is LONGER than bottom 横 (opposite of
土 which has bottom-longer). Uses different filename `shi_scholar.py`
to avoid collision with `shi_ten.py`.

Joints:
  s1 × s2 → P (welded crossing at C by construction).
  s2.tail ⇆ s3.mid → N (~12 px gap).
"""
from heng import draw_heng
from shu import draw_shu


def draw_shi_scholar(draw,
                     s1_head=('ML', 0.384, 0.816), s1_tail=('MR', 0.607, 0.714),
                     s2_head=('TC', 0.365, 0.788), s2_tail=('BC', 0.427, 0.528),
                     s3_head=('BL', 0.794, 0.657), s3_tail=('BR', 0.186, 0.64)):
    draw_heng(draw, s1_head, s1_tail, width=9)
    draw_shu(draw, s2_head, s2_tail, width=10)
    draw_heng(draw, s3_head, s3_tail, width=9)
