"""廾 (gǒng, "two hands", 3 strokes: 横 + 撇 + 竖) — B1 pass.

Strokes:
  s1 — 横 spanning the middle row.
  s2 — 撇 crossing the heng (upper-mid to lower-left).
  s3 — 竖 (or shu) crossing the heng (upper-right to bottom).

Joints: both s2 and s3 cross s1 → P (welded by construction, since
both descend past the heng's y-line).
"""
from heng import draw_heng
from pie import draw_pie
from shu import draw_shu


def draw_gong_join(draw,
                   s1_head=('ML', 0.35, 0.60), s1_tail=('MR', 0.65, 0.60),
                   s2_head=('C', 0.10, 0.20), s2_tail=('BL', 0.30, 0.85),
                   s3_head=('C', 0.75, 0.10), s3_tail=('BC', 0.85, 0.90)):
    draw_heng(draw, s1_head, s1_tail, width=8)
    draw_pie(draw, s2_head, s2_tail, head_width=11, tail_width=1, curve=0.10)
    draw_shu(draw, s3_head, s3_tail, width=9)
