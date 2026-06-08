"""
竖 (shu) — atomic vertical stroke, 垂露 (hanging-dew) variant.

Tags: tag:atomic-stroke tag:shu tag:垂露竖
Component-of: (to fill — appears in 十, 丨, 工, 王, 中, 山, 川, 木, 林, ...)
Mastered: run_4 cycle 2, rubric 10/10
  (dunbi=2, hudu=2, taper=2, proportion=2, overall=2)

The canonical 楷书 vertical stroke in its 垂露 (rounded-bottom) form.
This is the universally-reusable variant: appears inside compound
characters as a trunk/spine. The 悬针 (needle-tip) variant is a
separate primitive to be added later if a stand-alone 竖 character
needs it.

Reuse interface:
    from shu import draw as draw_shu
    draw_shu(t)                          # centered (0,+200) → (0,-200)
    draw_shu(t, ox=100, oy=0)            # shift right 100 px (e.g. right 竖 of 工)
    draw_shu(t, ox=0, oy=0, scale=0.6)   # shorter 竖

Symmetric "barbell" width profile: top press 16 → shaft 11 →
bottom 垂露 press 18. Centerline is perfectly straight (control
points colinear with endpoints).

What this entry establishes:
- The barbell profile for symmetric strokes (top + bottom both weighted).
- Verifies the §2.1 reuse interface — this entry's `draw_shu` imports
  `brushed_bezier` from heng.py rather than duplicating it.
"""

import sys
import os
from typing import Callable

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import brushed_bezier  # reuse the mastered helper


def _w_shu_canonical(s: float) -> float:
    """垂露竖 width profile — symmetric barbell, bottom slightly heavier.

    s ∈ [0, 1] from top to bottom.
      - Top entry press (dunbi)   16 → 11 over first 10%.
      - Shaft                     ~11 over middle ~76%.
      - Bottom closing press 收笔 11 → 18 over final 14% (垂露 rounded).
    """
    if s < 0.10:
        return 16.0 - (s / 0.10) * 5.0
    if s < 0.86:
        return 11.0
    return 11.0 + ((s - 0.86) / 0.14) * 7.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0,
         w_profile: Callable[[float], float] = _w_shu_canonical):
    """Draw 竖 (垂露 variant) with optional translate (ox, oy) and uniform scale.

    Canonical endpoints (before transform):
        P0 = (0, +200),  P3 = (0, -200)  (perfectly vertical, 400 px long)
    """
    P0 = (0.0 * scale + ox, 200.0 * scale + oy)
    P3 = (0.0 * scale + ox, -200.0 * scale + oy)
    P1 = (P0[0] + (P3[0] - P0[0]) / 3.0, P0[1] + (P3[1] - P0[1]) / 3.0)
    P2 = (P0[0] + 2.0 * (P3[0] - P0[0]) / 3.0, P0[1] + 2.0 * (P3[1] - P0[1]) / 3.0)
    brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=220)
