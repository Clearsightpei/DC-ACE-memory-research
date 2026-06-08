"""
横 (heng) — atomic horizontal stroke.

Tags: tag:atomic-stroke tag:heng
Component-of: (to be filled in as 横 appears inside mastered chars — 一, 二, 三, 十, 工, 王, ...)
Mastered: run_4 cycle 1, rubric 10/10
  (dunbi=2, hudu=2, taper=2, proportion=2, overall=2)

The canonical 楷书 horizontal stroke. Used as the top/middle/bottom
bar in dozens of simple characters and as a constituent inside
hundreds of compound ones. This is the first Phase-1 primitive
mastered in run_4.

Reuse interface:
    from heng import draw as draw_heng
    draw_heng(t)                          # centered at origin
    draw_heng(t, ox=0, oy=100)            # shift up 100 px (e.g. top heng of 二)
    draw_heng(t, ox=0, oy=-100)           # shift down 100 px (e.g. bottom heng of 二)
    draw_heng(t, ox=0, oy=0, scale=0.6)   # shrink to 60% (e.g. short top heng of 王)

The function preserves all mastered parameters verbatim — DO NOT modify
this file (Success Bank immutability rule). If a different profile is
needed, create a new entry (e.g. heng_short.py) that supersedes.

What this entry establishes for the project:
- The brushed-Bézier-with-per-sample-pensize pattern (brushed_bezier helper).
- The min-pensize-3 floor (run_3 c17 lesson).
- The 楷书 weighted-entry / lighter-shaft / heavier-closing-press width profile.
- The Success Bank's draw(t, ox=0, oy=0, scale=1.0) interface convention.
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
