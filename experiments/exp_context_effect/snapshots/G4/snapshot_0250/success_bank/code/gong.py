"""工 (gōng, "work", 3 strokes: top 横 + 竖 + bottom 横) — B1 pass.

Strokes:
  s1 — top 横.
  s2 — 竖 (central vertical) piercing s1 near the middle.
  s3 — bottom 横 (slightly wider than s1).

Joints:
  s1 × s2 → P (weld at top of vertical).
  s2 × s3 → P (weld at bottom of vertical).
"""
from heng import draw_heng
from shu import draw_shu


def draw_gong(draw,
              s1_head=('ML', 0.867, 0.143), s1_tail=('MR', 0.253, 0.017),
              s2_head=('C', 0.421, 0.222), s2_tail=('BC', 0.441, 0.355),
              s3_head=('BL', 0.311, 0.493), s3_tail=('BR', 0.777, 0.481)):
    draw_heng(draw, s1_head, s1_tail, width=9)
    draw_shu(draw, s2_head, s2_tail, width=9)
    draw_heng(draw, s3_head, s3_tail, width=9)
