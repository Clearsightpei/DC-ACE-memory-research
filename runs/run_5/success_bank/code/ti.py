"""
提 (ti) — atomic upward flick.

Tags: tag:atomic-stroke tag:提 tag:tapered-tip
Component-of: (to fill — appears in 习, 河, 江, 沙, 三point-water radical, ...)
Mastered: run_4 cycle 5, rubric 10/10

The upward flick: weighted base lower-left, fine point upper-right.
Same tapered-tip family as 撇 but shorter (~250 px) and lighter
(peak 14 not 18). Width profile 14 → 11 → 9 → 3.

Reuse:
    from ti import draw as draw_ti
    draw_ti(t)                          # base (-100,-80) → tip (+150,+60)
    draw_ti(t, ox=-200, oy=0)           # shift left (e.g. inside 习)
"""

import sys, os
from typing import Callable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import brushed_bezier


def _w_ti_canonical(s: float) -> float:
    if s < 0.12:
        return 14.0 - (s / 0.12) * 3.0
    if s < 0.88:
        return 11.0 - ((s - 0.12) / 0.76) * 2.0
    return 9.0 - ((s - 0.88) / 0.12) * 6.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0,
         w_profile: Callable[[float], float] = _w_ti_canonical):
    P0 = (-100.0 * scale + ox, -80.0 * scale + oy)
    P3 = (150.0 * scale + ox, 60.0 * scale + oy)
    P1 = (-20.0 * scale + ox, -20.0 * scale + oy)
    P2 = (75.0 * scale + ox, 30.0 * scale + oy)
    brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=220)
