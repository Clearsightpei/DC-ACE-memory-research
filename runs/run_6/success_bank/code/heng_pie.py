"""横撇 (heng_pie) — compound stroke: horizontal + down-left taper.

Tags: tag:compound-stroke tag:heng_pie tag:two-segment
Mastered: run_6 c11 (via 又).

Reuse:
    from heng_pie import draw_heng_pie
    draw_heng_pie(t, from_anchor, corner_anchor, to_anchor)
"""
from _anchor import anchor_to_xy
from heng import brushed_bezier


def w_main(s):
    if s < 0.10: return 14.0 - (s/0.10)*3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*2.0


def w_tail(s):
    return 13.0 - s*10.0


def draw_heng_pie(t, fa, ca, ta):
    p0 = anchor_to_xy(fa); pc = anchor_to_xy(ca); p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (pc[0]-p0[0])*0.33, p0[1] + (pc[1]-p0[1])*0.33 + 4)
    a2 = (p0[0] + (pc[0]-p0[0])*0.67, p0[1] + (pc[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, a1, a2, pc, w_main, samples=180)
    b1 = (pc[0] + (p3[0]-pc[0])*0.4, pc[1] + (p3[1]-pc[1])*0.4 + 5)
    b2 = (pc[0] + (p3[0]-pc[0])*0.75, pc[1] + (p3[1]-pc[1])*0.75 + 5)
    brushed_bezier(t, pc, b1, b2, p3, w_tail, samples=160)
