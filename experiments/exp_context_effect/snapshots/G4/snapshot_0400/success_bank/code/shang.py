"""上 (shàng, "above", 3画) — Phase-3 char, B4 promotion.

Strokes:
  s1 — 竖 (short vertical, near center-top going down).
  s2 — 短横 (short crossbar right of s1's mid).
  s3 — 长横 (long baseline at bottom).

Joints: two N-class (natural gaps ~14-17 px; do NOT weld per TR10).
"""
from heng import draw_heng
from shu import draw_shu


def draw_shang(draw,
               s1_head=('TC', 0.307, 0.712), s1_tail=('BC', 0.383, 0.602),
               s2_head=('C', 0.556, 0.688), s2_tail=('MR', 0.25, 0.547),
               s3_head=('BL', 0.393, 0.73), s3_tail=('BR', 0.73, 0.71)):
    # OVERRIDE anchors for this composition per TR1.
    draw_shu(draw, s1_head, s1_tail, width=10)
    draw_heng(draw, s2_head, s2_tail, width=8)
    draw_heng(draw, s3_head, s3_tail, width=11)
