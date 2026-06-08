"""
竖折 (shu_zhe) — vertical → right-turn horizontal.

Tags: tag:compound-stroke tag:竖折 tag:multi-segment tag:corner-顿笔
Component-of: (to fill — 山, 凶, 区, 匹, ...)
Mastered: run_4 cycle 12, rubric 10/10

Two-segment compound: vertical arm + bottom-corner turn + horizontal
arm. Mirror of 横折 (c7). Width 16→11→14 / 14→11→14.
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
    if s < 0.85: return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 3.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    A0 = (-80.0 * scale + ox, 100.0 * scale + oy)
    A3 = (-80.0 * scale + ox, -80.0 * scale + oy)
    A1 = (A0[0], A0[1] + (A3[1] - A0[1]) / 3.0)
    A2 = (A0[0], A0[1] + 2.0 * (A3[1] - A0[1]) / 3.0)
    brushed_bezier(t, A0, A1, A2, A3, _w_A, samples=200)

    B0 = (-80.0 * scale + ox, -80.0 * scale + oy)
    B3 = (80.0 * scale + ox, -80.0 * scale + oy)
    B1 = (B0[0] + (B3[0] - B0[0]) / 3.0, B0[1])
    B2 = (B0[0] + 2.0 * (B3[0] - B0[0]) / 3.0, B0[1])
    brushed_bezier(t, B0, B1, B2, B3, _w_B, samples=200)
