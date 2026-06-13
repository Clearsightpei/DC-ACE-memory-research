"""横折钩 (heng_zhe_gou) — compound stroke: horizontal + downward bend + hook.

Tags: tag:compound-stroke tag:heng_zhe_gou tag:hook tag:two-segment
Mastered: run_6 c12 (via 力).

Reuse:
    from heng_zhe_gou import draw_heng_zhe_gou
    draw_heng_zhe_gou(t, from_anchor, corner_anchor, to_anchor)
"""
from _anchor import anchor_to_xy
from heng import brushed_bezier


def w_main(s):
    if s < 0.10: return 14.0 - (s/0.10)*3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*2.0


def w_hook(s):
    return 13.0 - s*10.0


def draw_heng_zhe_gou(t, fa, ca, ta):
    p0 = anchor_to_xy(fa); pc = anchor_to_xy(ca); p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (pc[0]-p0[0])*0.33, p0[1] + (pc[1]-p0[1])*0.33 + 4)
    a2 = (p0[0] + (pc[0]-p0[0])*0.67, p0[1] + (pc[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, a1, a2, pc, w_main, samples=180)
    b1 = (pc[0] + (p3[0]-pc[0])*0.4, pc[1] + (p3[1]-pc[1])*0.4)
    b2 = (pc[0] + (p3[0]-pc[0])*0.75, pc[1] + (p3[1]-pc[1])*0.75)
    brushed_bezier(t, pc, b1, b2, p3, w_hook, samples=160)
