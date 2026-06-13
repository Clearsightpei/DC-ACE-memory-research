"""竖弯钩 (shu_wan_gou) — compound stroke: vertical drop, curve right, closing kick.

Tags: tag:compound-stroke tag:shu_wan_gou tag:hook tag:two-segment
Mastered: run_6 c10 (via 七).

Three-anchor: from, corner, to.

Reuse:
    from shu_wan_gou import draw_shu_wan_gou
    draw_shu_wan_gou(t, from_anchor, corner_anchor, to_anchor)
"""
from _anchor import anchor_to_xy
from heng import brushed_bezier


def w_vert(s):
    if s < 0.10: return 14.0 - (s/0.10)*3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15)*2.0


def w_curve(s):
    if s < 0.20: return 13.0
    if s < 0.80: return 11.0
    return 11.0 + ((s-0.80)/0.20)*7.0


def draw_shu_wan_gou(t, fa, ca, ta):
    p0 = anchor_to_xy(fa); pc = anchor_to_xy(ca); p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (pc[0]-p0[0])*0.33, p0[1] + (pc[1]-p0[1])*0.33)
    a2 = (p0[0] + (pc[0]-p0[0])*0.67, p0[1] + (pc[1]-p0[1])*0.67)
    brushed_bezier(t, p0, a1, a2, pc, w_vert, samples=180)
    b1 = (pc[0] + (p3[0]-pc[0])*0.4, pc[1] + (p3[1]-pc[1])*0.3 - 10)
    b2 = (pc[0] + (p3[0]-pc[0])*0.85, pc[1] + (p3[1]-pc[1])*0.85 - 5)
    brushed_bezier(t, pc, b1, b2, p3, w_curve, samples=160)
