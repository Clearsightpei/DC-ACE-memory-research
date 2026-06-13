"""撇 (pie) — atomic down-left diagonal stroke with tapered tip.

Tags: tag:atomic-stroke tag:pie tag:tapered-tip tag:楷书
Mastered: run_6 c3. Structural ✓ (count=1, from=9.8, to=5.1 px).

Width profile (s ∈ [0,1]):
  - [0.00, 0.10] head dunbi: 18 → 14   (heaviest)
  - [0.10, 0.85] shaft:      14 → 11
  - [0.85, 1.00] tail taper: 11 → 3    (fine tip)

OPPOSITE direction from heng/shu — head is heaviest, tail is finest.

Reuse:
    from pie import draw_pie
    draw_pie(t, from_anchor, to_anchor)
"""
from _anchor import anchor_to_xy
from heng import brushed_bezier


def w_pie(s):
    if s < 0.10: return 18.0 - (s / 0.10) * 4.0
    if s < 0.85: return 14.0 - ((s - 0.10) / 0.75) * 3.0
    return 11.0 - ((s - 0.85) / 0.15) * 8.0


def draw_pie(t, from_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor)
    p3 = anchor_to_xy(to_anchor)
    p1 = (p0[0] + (p3[0] - p0[0]) * 0.33, p0[1] + (p3[1] - p0[1]) * 0.33 + 10)
    p2 = (p0[0] + (p3[0] - p0[0]) * 0.67, p0[1] + (p3[1] - p0[1]) * 0.67 + 10)
    brushed_bezier(t, p0, p1, p2, p3, w_pie, samples=240)
