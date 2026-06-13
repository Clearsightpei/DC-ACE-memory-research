"""点 (dian) — atomic short brushed dab with symmetric bell width.

Tags: tag:atomic-stroke tag:dian tag:bell-width tag:楷书
Mastered: run_6 c4. Structural ✓ (count=1, from=2.0 to=6.4 px).

Width profile (s ∈ [0,1]): 3 → 14 → 3 (symmetric).

Reuse:
    from dian import draw_dian
    draw_dian(t, from_anchor, to_anchor)
"""
from _anchor import anchor_to_xy
from heng import brushed_bezier


def w_dian(s):
    if s < 0.5:
        return 3.0 + (s / 0.5) * 11.0
    return 14.0 - ((s - 0.5) / 0.5) * 11.0


def draw_dian(t, from_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor); p3 = anchor_to_xy(to_anchor)
    p1 = (p0[0] + (p3[0] - p0[0]) * 0.33, p0[1] + (p3[1] - p0[1]) * 0.33 + 5)
    p2 = (p0[0] + (p3[0] - p0[0]) * 0.67, p0[1] + (p3[1] - p0[1]) * 0.67 + 5)
    brushed_bezier(t, p0, p1, p2, p3, w_dian, samples=120)
