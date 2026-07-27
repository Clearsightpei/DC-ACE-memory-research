"""纟 (sī, "silk" radical, 3画) — B4 main promotion (finally passed as CHAR).

Compact stacked 撇折 + 撇折 + 提 following errata fix: model after 幺
(yao_small); short sweeps, tight pivots, ~11 px N-gaps between loops.
TR9 tall-thin: expand y, keep x compact.

Strokes: 2 × 撇折 (stacked loops) + 1 × 提 (rising flick).
Joints: s1.tail ⇆ s2.mid @ C  — N (~12 px);
        s2.tail ⇆ s3.mid @ BC — N (small gap).
"""
from pie_zhe import draw_pie_zhe
from ti import draw_ti


def draw_si_silk(draw,
                 s1_head=('TC', 0.354, 0.762),
                 s1_pivot=('C', 0.20, 0.68),
                 s1_tail=('C', 0.444, 0.731),
                 s2_head=('C', 0.679, 0.304),
                 s2_pivot=('BC', 0.40, 0.10),
                 s2_tail=('BC', 0.761, 0.153),
                 s3_head=('BL', 0.914, 0.795),
                 s3_tail=('BC', 0.872, 0.435)):
    draw_pie_zhe(draw, s1_head, s1_pivot, s1_tail,
                 pie_head_w=7, pie_tip_w=3, heng_w=5, shoulder=3)
    draw_pie_zhe(draw, s2_head, s2_pivot, s2_tail,
                 pie_head_w=9, pie_tip_w=4, heng_w=6, shoulder=4)
    draw_ti(draw, s3_head, s3_tail,
            head_width=11, tail_width=2, curve=0.08, segments=48)
