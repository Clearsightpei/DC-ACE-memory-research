"""亻 (rén-side, "person radical", 2 strokes: 撇 + 竖) — B1 pass.

Left-side radical. Verbatim MMH anchors (Phase-2 restart used
component-style anchors that read as a left-radical shape).

Strokes:
  s1 — 撇 (curve from upper-right to lower-left).
  s2 — 竖 (short vertical dropping from mid-upper).

Joint: s2.head ⇆ s1 body → T-class (竖 head touches the 撇 body).
Sandbox observation (亻 remaining-mismatch note): the T-touch anchor
should sit slightly BELOW-LEFT of the chord midpoint to land on the
visible ink of the bowed 撇.
"""
from pie import draw_pie
from shu import draw_shu


def draw_ren_side(draw,
                  pie_head=('TC', 0.588, 0.738),
                  pie_tail=('BL', 0.806, 0.112),
                  shu_head=('C', 0.470, 0.510),
                  shu_tail=('BC', 0.470, 0.927)):
    draw_pie(draw, pie_head, pie_tail,
             head_width=12, tail_width=1, curve=0.10, segments=48)
    draw_shu(draw, shu_head, shu_tail, width=9)
