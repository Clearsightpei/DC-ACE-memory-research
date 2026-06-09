"""
竖弯钩 (shu_wan_gou) — vertical drop, curve right, up-right hook.

Tags: tag:compound-stroke tag:竖弯钩 tag:hook tag:multi-segment tag:curved-middle
Component-of: (to fill — 也, 已, 巴, 七, 元, 见, ...)
Mastered: run_4 cycle 10, rubric 10/10

Three-segment compound: vertical drop + smooth quarter-arc + up-right
hook. The middle segment is a TRUE curved Bézier (not two straight
arms with a sharp turn). Width 16→11 drop, 11→13 thickening through
the curve, 13→3 taper on the hook.

Reuse:
    from shu_wan_gou import draw as draw_shu_wan_gou
    draw_shu_wan_gou(t)                         # bottom stroke layout for 巴/已/七/也
    draw_shu_wan_gou(t, ox=-50, oy=0)           # shift left
    draw_shu_wan_gou(t, scale=0.8)              # smaller variant
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import brushed_bezier


def _w_A(s):
    if s < 0.12: return 16.0 - (s / 0.12) * 5.0
    return 11.0


def _w_B(s):
    return 11.0 + s * 2.0


def _w_C(s):
    if s < 0.15: return 13.0
    return 13.0 - ((s - 0.15) / 0.85) * 10.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    # Seg A: vertical drop
    A0 = (0.0 * scale + ox, 150.0 * scale + oy)
    A3 = (0.0 * scale + ox, -100.0 * scale + oy)
    A1 = (A0[0], A0[1] + (A3[1] - A0[1]) / 3.0)
    A2 = (A0[0], A0[1] + 2.0 * (A3[1] - A0[1]) / 3.0)
    brushed_bezier(t, A0, A1, A2, A3, _w_A, samples=220)

    # Seg B: quarter-arc, concave-up
    B0 = (0.0 * scale + ox, -100.0 * scale + oy)
    B3 = (150.0 * scale + ox, -150.0 * scale + oy)
    B1 = (0.0 * scale + ox, -150.0 * scale + oy)
    B2 = (100.0 * scale + ox, -150.0 * scale + oy)
    brushed_bezier(t, B0, B1, B2, B3, _w_B, samples=200)

    # Seg C: up-right hook
    C0 = (150.0 * scale + ox, -150.0 * scale + oy)
    C3 = (200.0 * scale + ox, -100.0 * scale + oy)
    C1 = (170.0 * scale + ox, -148.0 * scale + oy)
    C2 = (190.0 * scale + ox, -125.0 * scale + oy)
    brushed_bezier(t, C0, C1, C2, C3, _w_C, samples=180)
