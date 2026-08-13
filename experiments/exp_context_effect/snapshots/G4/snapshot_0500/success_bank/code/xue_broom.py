"""彐 (jì, "pig snout", 3 strokes) — B2 retry pass (graduated from B1 fail).

RETRY FIX vs B1: every 横's head and tail sit in the SAME cell ROW.
Prior failure had s3 head in BL (row=2) with tail in C (row=1),
tilting the "horizontal" by 100 px.

Strokes:
  s1 — 横折 (top bracket).
  s2 — 横 (middle bar).
  s3 — 横 (bottom bar).

Joints:
  s2.tail ⇆ s1 vertical body — N (~32 px horizontal gap).
  s1.tail ⇆ s3 body vertical — N (~16 px).
"""
from _anchor import anchor_to_xy, fat_line


def draw_xue_broom(draw,
                   s1_head=('TL', 0.35, 0.90),
                   s1_corner=('TC', 0.90, 0.90),
                   s1_tail=('C', 0.90, 0.95),
                   s2_head=('ML', 0.40, 0.55), s2_tail=('C', 0.65, 0.55),
                   s3_head=('BL', 0.25, 0.30), s3_tail=('BR', 0.05, 0.30)):
    color = (0, 0, 0)
    p_s1h = anchor_to_xy(s1_head)
    p_s1c = anchor_to_xy(s1_corner)
    p_s1t = anchor_to_xy(s1_tail)
    fat_line(draw, p_s1h, p_s1c, width=9)
    fat_line(draw, p_s1c, p_s1t, width=9)
    r = 6
    draw.ellipse([p_s1c[0]-r, p_s1c[1]-r, p_s1c[0]+r, p_s1c[1]+r], fill=color)

    fat_line(draw, anchor_to_xy(s2_head), anchor_to_xy(s2_tail), width=8)
    fat_line(draw, anchor_to_xy(s3_head), anchor_to_xy(s3_tail), width=9)
