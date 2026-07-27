"""习 (xí, "practice", 3画) — B4 main promotion.

Strokes:
  s1 — 横折钩 (outer bracket: top bar + right descent + up-left hook flick).
  s2 — 点 (short slanted dot inside the upper-left region).
  s3 — 提 (rising diagonal inside the middle region).

Joints: NONE (MMH declares 0; strokes visually separate).

The heng_zhe_gou corner + pre-hook tail are inferred from the GT since
MMH only reports the outer head+tail of a compound stroke.
"""
from heng_zhe_gou import draw_heng_zhe_gou
from dian import draw_dian
from ti import draw_ti


def draw_xi_practice(draw,
                     s1_head=('TL', 0.773, 0.94),
                     s1_corner=('TR', 0.02, 0.10),
                     s1_tail=('MR', 0.02, 0.85),
                     s1_tip=('BC', 0.295, 0.50),
                     s2_head=('ML', 0.917, 0.251),
                     s2_tail=('C', 0.225, 0.494),
                     s3_head=('BL', 0.630, 0.188),
                     s3_tail=('C', 0.567, 0.682)):
    draw_heng_zhe_gou(draw, s1_head, s1_corner, s1_tail, s1_tip,
                      h_width=9, v_width=10, shoulder=13, tip_w=2)
    draw_dian(draw, from_anchor=s2_head, to_anchor=s2_tail)
    draw_ti(draw, from_anchor=s3_head, to_anchor=s3_tail,
            head_width=11, tail_width=1, curve=0.08)
