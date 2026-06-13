"""捺 (na) — atomic right-down diagonal stroke with kick-release tail.

Tags: tag:atomic-stroke tag:na tag:flat-kick tag:楷书
Mastered: run_6 c5 (introduced via 八). Structural ✓ (count=2 for 八, na anchors from=1.0 to=6.4 px).

Width profile (s ∈ [0,1]) — REVERSED from 撇:
  - [0.00, 0.30] head thin: 5 → 14
  - [0.30, 0.75] body:      14 → 18
  - [0.75, 1.00] kick:      18 → 3   (rapid release)

The MIDDLE-BODY is the heaviest. Head is the thinnest entry. Tail
releases to a fine kick. This is the right-down companion to 撇 and
its dynamics are inverted at every level.

Reuse:
    from na import draw_na
    draw_na(t, from_anchor, to_anchor)
"""
from _anchor import anchor_to_xy
from heng import brushed_bezier


def w_na(s):
    if s < 0.30: return 5.0 + (s / 0.30) * 9.0
    if s < 0.75: return 14.0 + ((s - 0.30) / 0.45) * 4.0
    return 18.0 - ((s - 0.75) / 0.25) * 15.0


def draw_na(t, from_anchor, to_anchor):
    p0 = anchor_to_xy(from_anchor)
    p3 = anchor_to_xy(to_anchor)
    p1 = (p0[0] + (p3[0] - p0[0]) * 0.33, p0[1] + (p3[1] - p0[1]) * 0.33 - 10)
    p2 = (p0[0] + (p3[0] - p0[0]) * 0.67, p0[1] + (p3[1] - p0[1]) * 0.67 - 10)
    brushed_bezier(t, p0, p1, p2, p3, w_na, samples=240)
