"""横 (heng) — atomic horizontal stroke.

Tags: tag:atomic-stroke tag:heng tag:楷书
Mastered: run_6 c1.
Gates passed:
  - Stroke count: 1 (matches MMH for 一).
  - Anchor placement: from (V_left, H_mid) dist 6.7 px; to (V_right, H_mid) dist 12.4 px. Both ≤ 15 px.
  - Visual score: 0.832 (informational).
  - OCR: returned no character — RapidOCR is unreliable on isolated 一 (run_5 lesson). Not gated on.
  - Judge panel: 3/3 YES.

Width profile (s ∈ [0, 1]):
  - [0.00, 0.10] entry dunbi:    16 → 11
  - [0.10, 0.85] shaft:          11
  - [0.85, 1.00] closing press:  11 → 19  (heaviest — the 楷书 diagnostic)

Reuse interface:
    from heng import draw_heng, brushed_bezier, w_heng
    draw_heng(t, from_anchor, to_anchor)

`from_anchor` / `to_anchor` are anchors resolvable by `_anchor.anchor_to_xy`
(either `(cell, x_frac, y_frac)` tuples or axis-intersection tuples like
`(V_left, H_mid)`).

The function is immutable per the Success Bank rule — DO NOT modify
this file. If a different profile is needed, create a new entry (e.g.
`heng_short.py`).
"""

from _anchor import anchor_to_xy


def brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=220):
    """Cubic Bezier from P0..P3 with per-sample pensize. Min pensize 3
    floor enforced (run_3 c17 lesson — hairlines lose readability)."""
    t.penup(); t.goto(P0); t.pendown()
    for i in range(samples + 1):
        s = i / samples
        x = ((1 - s) ** 3 * P0[0] + 3 * (1 - s) ** 2 * s * P1[0]
             + 3 * (1 - s) * s * s * P2[0] + s ** 3 * P3[0])
        y = ((1 - s) ** 3 * P0[1] + 3 * (1 - s) ** 2 * s * P1[1]
             + 3 * (1 - s) * s * s * P2[1] + s ** 3 * P3[1])
        t.pensize(max(3, w_profile(s)))
        t.goto(x, y)
    t.penup()


def w_heng(s):
    """Canonical 楷书 横 width profile.

    s ∈ [0, 1]. Closing press at the right end is the heaviest point.
    """
    if s < 0.10:
        return 16.0 - (s / 0.10) * 5.0
    if s < 0.85:
        return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 8.0


def draw_heng(t, from_anchor, to_anchor):
    """Draw a 横 from `from_anchor` to `to_anchor`.

    Both anchors are resolved via `_anchor.anchor_to_xy`. Control points
    sit at the 1/3 and 2/3 marks with a small +4 y-bow for the 楷书 arc.
    """
    p0 = anchor_to_xy(from_anchor)
    p3 = anchor_to_xy(to_anchor)
    p1 = (p0[0] + (p3[0] - p0[0]) * 0.33,
          p0[1] + (p3[1] - p0[1]) * 0.33 + 4)
    p2 = (p0[0] + (p3[0] - p0[0]) * 0.67,
          p0[1] + (p3[1] - p0[1]) * 0.67 + 4)
    brushed_bezier(t, p0, p1, p2, p3, w_heng, samples=220)
