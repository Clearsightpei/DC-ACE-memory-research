"""
横折弯钩 (heng_zhe_wan_gou) — 4-segment: heng + corner-down + curve + up-hook.

Tags: tag:compound-stroke tag:横折弯钩 tag:hook tag:multi-segment tag:corner-顿笔 tag:curved-middle
Component-of: (to fill — 力, 万, 几, 风, 凡, 飞, 九, ...)
Mastered: run_4 cycle 13, rubric 10/10

Four-segment compound (most complex Phase-2 stroke):
  Seg A short heng: (-80,+120)→(+80,+120). w 16→11→14.
  Seg B vertical drop: (+80,+120)→(+80,-60). w 14→11.
  Seg C quarter-curve: (+80,-60)→(+140,-100). Concave-up. w 11→12.
  Seg D up-hook: (+140,-100)→(+170,-50). w 12→3 taper.

Composes patterns from c7 (横折) + c10 (竖弯钩 curve+hook).
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import brushed_bezier


def _w_A(s):
    if s < 0.10: return 16.0 - (s / 0.10) * 5.0
    if s < 0.80: return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 3.0


def _w_B(s):
    if s < 0.15: return 14.0 - (s / 0.15) * 3.0
    return 11.0


def _w_C(s):
    return 11.0 + s * 1.0


def _w_D(s):
    if s < 0.15: return 12.0 - (s / 0.15) * 1.0
    return 11.0 - ((s - 0.15) / 0.85) * 8.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    A0 = (-80.0 * scale + ox, 120.0 * scale + oy)
    A3 = (80.0 * scale + ox, 120.0 * scale + oy)
    A1 = (A0[0] + (A3[0] - A0[0]) / 3.0, A0[1])
    A2 = (A0[0] + 2.0 * (A3[0] - A0[0]) / 3.0, A0[1])
    brushed_bezier(t, A0, A1, A2, A3, _w_A, samples=200)

    B0 = (80.0 * scale + ox, 120.0 * scale + oy)
    B3 = (80.0 * scale + ox, -60.0 * scale + oy)
    B1 = (B0[0], B0[1] + (B3[1] - B0[1]) / 3.0)
    B2 = (B0[0], B0[1] + 2.0 * (B3[1] - B0[1]) / 3.0)
    brushed_bezier(t, B0, B1, B2, B3, _w_B, samples=200)

    C0 = (80.0 * scale + ox, -60.0 * scale + oy)
    C3 = (140.0 * scale + ox, -100.0 * scale + oy)
    C1 = (80.0 * scale + ox, -100.0 * scale + oy)
    C2 = (120.0 * scale + ox, -100.0 * scale + oy)
    brushed_bezier(t, C0, C1, C2, C3, _w_C, samples=180)

    D0 = (140.0 * scale + ox, -100.0 * scale + oy)
    D3 = (170.0 * scale + ox, -50.0 * scale + oy)
    D1 = (155.0 * scale + ox, -100.0 * scale + oy)
    D2 = (170.0 * scale + ox, -80.0 * scale + oy)
    brushed_bezier(t, D0, D1, D2, D3, _w_D, samples=160)
