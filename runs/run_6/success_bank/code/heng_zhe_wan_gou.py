"""横折弯钩 (heng_zhe_wan_gou) — complex compound stroke: horizontal + down-turn + curve + hook tail.

Tags: tag:compound-stroke tag:heng_zhe_wan_gou tag:hook tag:three-segment
Mastered: run_6 c8 (via 乙). Count ✓, anchor from=4.1 to=18.0 px (tol=40).

Four-anchor interface: from, corner1, corner2, to.

Reuse:
    from heng_zhe_wan_gou import draw_heng_zhe_wan_gou
    draw_heng_zhe_wan_gou(t, from_anchor, c1_anchor, c2_anchor, to_anchor)
"""
from _anchor import anchor_to_xy
from heng import brushed_bezier


def w_main(s):
    if s < 0.10: return 14.0 - (s / 0.10) * 3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 2.0


def w_tail(s):
    return 13.0 - s * 9.0


def draw_heng_zhe_wan_gou(t, fa, c1a, c2a, ta):
    p0 = anchor_to_xy(fa); pc1 = anchor_to_xy(c1a); pc2 = anchor_to_xy(c2a); p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (pc1[0]-p0[0])*0.33, p0[1] + (pc1[1]-p0[1])*0.33 + 4)
    a2 = (p0[0] + (pc1[0]-p0[0])*0.67, p0[1] + (pc1[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, a1, a2, pc1, w_main, samples=120)
    b1 = (pc1[0] + (pc2[0]-pc1[0])*0.33 + 20, pc1[1] + (pc2[1]-pc1[1])*0.33)
    b2 = (pc1[0] + (pc2[0]-pc1[0])*0.67 + 10, pc1[1] + (pc2[1]-pc1[1])*0.67)
    brushed_bezier(t, pc1, b1, b2, pc2, w_main, samples=180)
    c1 = (pc2[0] + (p3[0]-pc2[0])*0.33, pc2[1] + (p3[1]-pc2[1])*0.33 + 10)
    c2 = (pc2[0] + (p3[0]-pc2[0])*0.67, pc2[1] + (p3[1]-pc2[1])*0.67 + 10)
    brushed_bezier(t, pc2, c1, c2, p3, w_tail, samples=120)
