"""十 (shí, "ten", 2 strokes: 横 + 竖 crossing at center) — B1 pass.

Canonical P-class crossing at C(0.5, 0.5). Both strokes share the
CROSS anchor by construction, guaranteeing the weld.

Strokes:
  s1 — 横 spanning ML→MR through center.
  s2 — 竖 spanning TC→BC through center.

Joint: P at C(0.5, 0.5) — welded crossing.
"""
from heng import draw_heng
from shu import draw_shu


def draw_shi_ten(draw,
                 s1_head=('ML', 0.15, 0.5), s1_tail=('MR', 0.85, 0.5),
                 s2_head=('TC', 0.5, 0.30), s2_tail=('BC', 0.5, 0.90)):
    draw_heng(draw, s1_head, s1_tail, width=10)
    draw_shu(draw, s2_head, s2_tail, width=10)
