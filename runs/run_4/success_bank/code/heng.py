"""
横 (heng) — atomic horizontal stroke.

Mastered in run_4 cycle 1 at rubric 10/10.
Source: attempts/cycle_1/generated.py (preserved verbatim from the
mastered render — DO NOT modify parameters).

To reuse this stroke at a different location/scale, call
draw(t, ox, oy, scale) — internally translates the canonical (-200,
0) → (+200, 0) endpoints by (ox, oy) and multiplies coordinates by
scale. Width profile widths are NOT scaled (use update_widths to
override if needed).
"""

from typing import Callable


def _w_heng_canonical(s: float) -> float:
    """Canonical 楷书 horizontal-stroke width profile.

    s ∈ [0, 1]. Returns pensize.
      - Entry press (dunbi) 16 → 11 over the first 10%.
      - Shaft  ~11           over the middle ~78%.
      - Closing press 收笔   10.5 → 19 over the final 12%.
    """
    if s < 0.10:
        return 16.0 - (s / 0.10) * 5.0
    if s < 0.88:
        return 11.0 - ((s - 0.10) / 0.78) * 0.5
    return 10.5 + ((s - 0.88) / 0.12) * 8.5


def brushed_bezier(t, P0, P1, P2, P3, w_profile: Callable[[float], float], samples: int = 220):
    """Cubic Bézier with per-sample pensize. Min pensize 3 floor enforced."""
    t.penup(); t.goto(P0); t.pendown()
    for i in range(samples + 1):
        s = i / samples
        x = (1 - s) ** 3 * P0[0] + 3 * (1 - s) ** 2 * s * P1[0] + 3 * (1 - s) * s * s * P2[0] + s ** 3 * P3[0]
        y = (1 - s) ** 3 * P0[1] + 3 * (1 - s) ** 2 * s * P1[1] + 3 * (1 - s) * s * s * P2[1] + s ** 3 * P3[1]
        t.pensize(max(3, w_profile(s)))
        t.goto(x, y)
    t.penup()


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0,
         w_profile: Callable[[float], float] = _w_heng_canonical):
    """Draw 横 with optional translate (ox, oy) and uniform scale.

    Canonical endpoints (before transform):
        P0 = (-200, -3),  P3 = (+200, +3)  (gentle ~6 px upward tilt)
    """
    P0 = (-200.0 * scale + ox, -3.0 * scale + oy)
    P3 = (200.0 * scale + ox, 3.0 * scale + oy)
    P1 = (P0[0] + (P3[0] - P0[0]) / 3.0, P0[1] + (P3[1] - P0[1]) / 3.0)
    P2 = (P0[0] + 2.0 * (P3[0] - P0[0]) / 3.0, P0[1] + 2.0 * (P3[1] - P0[1]) / 3.0)
    brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=220)
