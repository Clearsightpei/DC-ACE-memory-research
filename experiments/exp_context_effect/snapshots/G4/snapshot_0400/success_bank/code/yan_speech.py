"""讠 (yán, "speech radical", 2 strokes) — B1 pass.

Left-side radical. TR11-compliant self-check documented two
GT-agreement features on the pass.

Strokes:
  s1 — 点 (small dot upper-left).
  s2 — 横折提 compound: horizontal opening, vertical drop, then a
       tí up-flick at the bottom.

Joints: none between s1 and s2 (S-class — dot is separate from the
compound stroke).
"""
from dian import draw_dian
from heng_zhe_ti import draw_heng_zhe_ti


def draw_yan_speech(draw,
                    s1_head=('C', 0.061, 0.014),
                    s1_tail=('ML', 0.164, 0.734),
                    s2_head_h=('ML', 0.20, 0.75),
                    s2_corner=('ML', 0.85, 0.80),
                    s2_knee=('BL', 0.75, 0.65),
                    s2_tail=('BC', 0.45, 0.35)):
    draw_dian(draw, s1_head, s1_tail,
              head_width=2, peak_width=9, curve=0.10, segments=24)
    draw_heng_zhe_ti(draw, s2_head_h, s2_corner, s2_knee, s2_tail,
                     h_width=9, v_head_w=9, v_knee_w=11,
                     shoulder=12, knee_shoulder=13,
                     ti_head_w=12, ti_tail_w=1, ti_curve=0.06)
