"""横折提 (heng_zhe_ti) — compound stroke: horizontal + corner-down + rising upper-right tail.

Tags: tag:compound-stroke tag:heng_zhe_ti tag:three-segment
Mastered: run_6 c31 (panel 3/3 YES, isolated render).

Used as the third stroke of the 讠 radical (计, 论). Shape: ─┐↗ — the
descender meets the rising tail at a heavy dunbi pivot.

Four-anchor interface: from, c1 (corner after heng), c2 (dunbi pivot
at the base, where ti begins), to (ti tip).

Reuse:
    from heng_zhe_ti import draw_heng_zhe_ti
    draw_heng_zhe_ti(t, from_anchor, c1_anchor, c2_anchor, to_anchor)
"""
from _anchor import anchor_to_xy
from heng import brushed_bezier


def w_heng_seg(s):
    if s < 0.10: return 14.0 - (s / 0.10) * 3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 2.0


def w_zhe_seg(s):
    if s < 0.10: return 13.0
    if s < 0.85: return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 8.0  # ends at 19 — dunbi press


def w_ti_seg(s):
    if s < 0.15: return 19.0 - (s / 0.15) * 4.0  # starts at dunbi width (19→15)
    return 15.0 - ((s - 0.15) / 0.85) * 12.0  # tapers to 3 tip


def draw_heng_zhe_ti(t, fa, c1a, c2a, ta):
    p0 = anchor_to_xy(fa); p1 = anchor_to_xy(c1a)
    p2 = anchor_to_xy(c2a); p3 = anchor_to_xy(ta)
    a1 = (p0[0] + (p1[0] - p0[0]) * 0.33, p0[1] + (p1[1] - p0[1]) * 0.33 + 4)
    a2 = (p0[0] + (p1[0] - p0[0]) * 0.67, p0[1] + (p1[1] - p0[1]) * 0.67 + 4)
    brushed_bezier(t, p0, a1, a2, p1, w_heng_seg, samples=160)
    b1 = (p1[0] + (p2[0] - p1[0]) * 0.33, p1[1] + (p2[1] - p1[1]) * 0.33)
    b2 = (p1[0] + (p2[0] - p1[0]) * 0.67, p1[1] + (p2[1] - p1[1]) * 0.67)
    brushed_bezier(t, p1, b1, b2, p2, w_zhe_seg, samples=160)
    c1 = (p2[0] + (p3[0] - p2[0]) * 0.33, p2[1] + (p3[1] - p2[1]) * 0.33)
    c2 = (p2[0] + (p3[0] - p2[0]) * 0.67, p2[1] + (p3[1] - p2[1]) * 0.67)
    brushed_bezier(t, p2, c1, c2, p3, w_ti_seg, samples=140)
