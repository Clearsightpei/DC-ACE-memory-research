"""竖 (shu) — atomic vertical stroke (垂露 variant).

Tags: tag:atomic-stroke tag:shu tag:垂露 tag:楷书
Mastered: run_6 c2.
Gates: structural ✓ (count=1, from_dist=5.8, to_dist=13.3 px). v=0.83. Curator vision ✓.

Width profile (s ∈ [0, 1]):
  - [0.00, 0.10] entry press: 16 → 11
  - [0.10, 0.80] shaft:        11
  - [0.80, 1.00] 垂露 closing:  11 → 18 (bottom heaviest)

Reuse:
    from shu import draw_shu
    draw_shu(t, from_anchor, to_anchor)
"""
from _anchor import anchor_to_xy
from heng import brushed_bezier


def w_shu(s):
    if s < 0.10: return 16.0 - (s / 0.10) * 5.0
    if s < 0.80: return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 7.0


def draw_shu(t, from_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor)
    p3 = anchor_to_xy(to_anchor)
    p1 = (p0[0] + (p3[0] - p0[0]) * 0.33, p0[1] + (p3[1] - p0[1]) * 0.33)
    p2 = (p0[0] + (p3[0] - p0[0]) * 0.67, p0[1] + (p3[1] - p0[1]) * 0.67)
    brushed_bezier(t, p0, p1, p2, p3, w_shu, samples=220)
