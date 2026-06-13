"""竖钩 (shu_gou) — compound stroke: vertical drop + hook tail.

Tags: tag:compound-stroke tag:shu_gou tag:hook tag:two-segment
Mastered: run_6 c6 (via 亅). Structural ✓ (count=1, from=10.0 to=5.1 px).

Three-anchor interface: from, corner, to.
- Segment A (head → corner): vertical drop, width 16 → 11 → 13.
- Segment B (corner → tail): hook taper, width 13 → 3.

Reuse:
    from shu_gou import draw_shu_gou
    draw_shu_gou(t, from_anchor, corner_anchor, to_anchor)
"""
from _anchor import anchor_to_xy
from heng import brushed_bezier


def w_shu_main(s):
    if s < 0.10: return 16.0 - (s / 0.10) * 5.0
    if s < 0.85: return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 2.0


def w_hook(s):
    return 13.0 - s * 10.0


def draw_shu_gou(t, from_anchor, corner_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor)
    pc = anchor_to_xy(corner_anchor)
    p3 = anchor_to_xy(to_anchor)
    p1 = (p0[0] + (pc[0]-p0[0]) * 0.33, p0[1] + (pc[1]-p0[1]) * 0.33)
    p2 = (p0[0] + (pc[0]-p0[0]) * 0.67, p0[1] + (pc[1]-p0[1]) * 0.67)
    brushed_bezier(t, p0, p1, p2, pc, w_shu_main, samples=200)
    p1b = (pc[0] + (p3[0]-pc[0]) * 0.5, pc[1] + (p3[1]-pc[1]) * 0.5 + 5)
    p2b = (pc[0] + (p3[0]-pc[0]) * 0.8, pc[1] + (p3[1]-pc[1]) * 0.8 + 3)
    brushed_bezier(t, pc, p1b, p2b, p3, w_hook, samples=80)
