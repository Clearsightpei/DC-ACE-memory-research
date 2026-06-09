"""
竖钩 (shu_gou) — compound vertical with leftward hook.

Tags: tag:compound-stroke tag:竖钩 tag:hook tag:multi-segment
Component-of: (to fill — 寸, 守, 子, 字, 小, 才, 水, 永, ...)
Mastered: run_4 cycle 8, rubric 10/10

Vertical shaft + small upward-left hook (钩) at the bottom. Two
Bézier segments per §1.5, with the junction's A2 nudged ~3 px
left so the shaft tangent points down-and-left into the hook —
this eliminates the angular notch at the junction.

Reuse:
    from shu_gou import draw as draw_shu_gou
    draw_shu_gou(t)                          # shaft 180→-150, hook to (-60,-110)
    draw_shu_gou(t, ox=-100, oy=0)           # shift left (e.g. inside 寸)
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import brushed_bezier


def _w_shugou_A(s: float) -> float:
    if s < 0.10: return 16.0 - (s / 0.10) * 5.0
    if s < 0.80: return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 4.0


def _w_shugou_B(s: float) -> float:
    if s < 0.20: return 15.0 - (s / 0.20) * 2.0
    return 13.0 - ((s - 0.20) / 0.80) * 10.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    # Shaft
    A0 = (0.0 * scale + ox, 180.0 * scale + oy)
    A3 = (0.0 * scale + ox, -150.0 * scale + oy)
    A1 = (A0[0], A0[1] + (A3[1] - A0[1]) / 3.0)
    A2 = (-3.0 * scale + ox, A0[1] + 2.0 * (A3[1] - A0[1]) / 3.0)
    brushed_bezier(t, A0, A1, A2, A3, _w_shugou_A, samples=220)

    # Hook
    B0 = (0.0 * scale + ox, -150.0 * scale + oy)
    B3 = (-60.0 * scale + ox, -110.0 * scale + oy)
    B1 = (-12.0 * scale + ox, -150.0 * scale + oy)
    B2 = (-45.0 * scale + ox, -118.0 * scale + oy)
    brushed_bezier(t, B0, B1, B2, B3, _w_shugou_B, samples=180)
