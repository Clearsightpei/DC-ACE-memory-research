"""
点 (dian) — atomic dot, 右点 (right-leaning) variant.

Tags: tag:atomic-stroke tag:点 tag:右点
Component-of: (to fill — 火, 寸, 之, 主, 永, 心, ...)
Mastered: run_4 cycle 6, rubric 10/10

Short teardrop dot. Both ends thin (3), belly heavy (14) at s≈0.30
(asymmetric — heavier toward the entry, lighter toward the tail).
Tilted ~45° down-right. About 60 px.

Reuse:
    from dian import draw as draw_dian
    draw_dian(t)                        # entry (-25,+20) → tail (+30,-25)
    draw_dian(t, ox=100, oy=200)        # decorative dot at upper area (e.g. inside 火)
"""

import sys, os
from typing import Callable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import brushed_bezier


def _w_dian_canonical(s: float) -> float:
    if s < 0.30:
        return 3.0 + (s / 0.30) * 11.0
    return 14.0 - ((s - 0.30) / 0.70) * 11.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0,
         w_profile: Callable[[float], float] = _w_dian_canonical):
    P0 = (-25.0 * scale + ox, 20.0 * scale + oy)
    P3 = (30.0 * scale + ox, -25.0 * scale + oy)
    P1 = (-8.0 * scale + ox, 8.0 * scale + oy)
    P2 = (15.0 * scale + ox, -10.0 * scale + oy)
    brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=120)
