"""
横撇 (heng_pie) — short heng + 撇 tail.

Tags: tag:compound-stroke tag:横撇 tag:tapered-tip tag:multi-segment tag:corner-顿笔
Component-of: (to fill — 又, 友, 反, 灰, ...)
Mastered: run_4 cycle 11, rubric 10/10

Two-segment compound: short horizontal heng + concave-down 撇 tail
tapering to a fine point. Width 16→11→15 / 15→11→3, continuous
across the junction.

Reuse:
    from heng_pie import draw as draw_heng_pie
    draw_heng_pie(t)                          # heng base (-100,+100)→(+30,+100), tail to (-150,-130)
    draw_heng_pie(t, ox=0, oy=0, scale=0.7)   # smaller variant for inset use
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import brushed_bezier


def _w_A(s):
    if s < 0.12: return 16.0 - (s / 0.12) * 5.0
    if s < 0.80: return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 4.0


def _w_B(s):
    if s < 0.18: return 15.0 - (s / 0.18) * 4.0
    if s < 0.88: return 11.0
    return 11.0 - ((s - 0.88) / 0.12) * 8.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    # Seg A: short heng
    A0 = (-100.0 * scale + ox, 100.0 * scale + oy)
    A3 = (30.0 * scale + ox, 100.0 * scale + oy)
    A1 = (A0[0] + (A3[0] - A0[0]) / 3.0, A0[1])
    A2 = (A0[0] + 2.0 * (A3[0] - A0[0]) / 3.0, A0[1] - 10.0 * scale)
    brushed_bezier(t, A0, A1, A2, A3, _w_A, samples=200)

    # Seg B: 撇 tail (concave-down)
    B0 = (30.0 * scale + ox, 100.0 * scale + oy)
    B3 = (-150.0 * scale + ox, -130.0 * scale + oy)
    B1 = (-10.0 * scale + ox, 60.0 * scale + oy)
    B2 = (-100.0 * scale + ox, -30.0 * scale + oy)
    brushed_bezier(t, B0, B1, B2, B3, _w_B, samples=220)
