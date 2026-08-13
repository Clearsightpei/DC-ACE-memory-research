"""冖 (mì, "cover", 2 strokes) — B1 pass.

Strokes:
  s1 — 短撇 (short 撇, thick head, upper-left).
  s2 — 横钩 (top horizontal + short down-left hook at the right end).

Joints: s1.tail-region ⇆ s2.head → N (small gap, top-left corner of
cover); s2 has its own internal hook (not counted as a joint).
"""
from pie import draw_pie
from heng_gou import draw_heng_gou


def draw_mi_cover(draw,
                  s1_head=('TL', 0.68, 0.92), s1_tail=('ML', 0.536, 0.479),
                  s2_head=('ML', 0.779, 0.081),
                  s2_shoulder=('MR', 0.127, 0.266),
                  s2_tip=('TR', 0.20, 0.95)):
    draw_pie(draw, from_anchor=s1_head, to_anchor=s1_tail,
             head_width=8, tail_width=1, curve=0.10, segments=32)
    draw_heng_gou(draw, head=s2_head, shoulder=s2_shoulder, tip=s2_tip,
                  head_w=8, mid_w=7, shoulder_w=11, tip_w=2)
