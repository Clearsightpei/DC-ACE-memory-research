"""横钩 (heng_gou) — compound stroke: horizontal + short downward hook.

Tags: tag:compound-stroke tag:heng_gou tag:hook tag:two-segment
Mastered: run_6 c7 (via 乛). Structural count ✓ (1 stroke). Anchor measurement
imprecise for L-shapes via bbox-corner detector (90+ px on tail) but the rendered
shape is visually correct per Curator vision review.

Three-anchor interface: from, corner, to.
- Segment A (head → corner): horizontal, width 16 → 11 → 13.
- Segment B (corner → tail): hook, width 13 → 3.

Reuse:
    from heng_gou import draw_heng_gou
    draw_heng_gou(t, from_anchor, corner_anchor, to_anchor)
"""
from _anchor import anchor_to_xy
from heng import brushed_bezier


def w_heng_main(s):
    if s < 0.10: return 16.0 - (s / 0.10) * 5.0
    if s < 0.85: return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 2.0


def w_hook(s):
    return 13.0 - s * 10.0


def draw_heng_gou(t, from_anchor, corner_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor)
    pc = anchor_to_xy(corner_anchor)
    p3 = anchor_to_xy(to_anchor)
    p1 = (p0[0] + (pc[0]-p0[0])*0.33, p0[1] + (pc[1]-p0[1])*0.33 + 4)
    p2 = (p0[0] + (pc[0]-p0[0])*0.67, p0[1] + (pc[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, p1, p2, pc, w_heng_main, samples=200)
    p1b = (pc[0] + (p3[0]-pc[0])*0.4, pc[1] + (p3[1]-pc[1])*0.5)
    p2b = (pc[0] + (p3[0]-pc[0])*0.75, pc[1] + (p3[1]-pc[1])*0.8)
    brushed_bezier(t, pc, p1b, p2b, p3, w_hook, samples=80)
