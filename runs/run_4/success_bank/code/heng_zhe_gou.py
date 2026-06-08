"""
横折钩 (heng_zhe_gou) — compound L-corner with hook.

Tags: tag:compound-stroke tag:横折钩 tag:hook tag:multi-segment tag:corner-顿笔
Component-of: (to fill — 月, 力, 刀, 勺, 司, 习, 见, 风, 句, ...)
Mastered: run_4 cycle 9, rubric 10/10

Three-segment compound: 横折 (heng arm + shu arm) + hook tail. Each
junction uses §1.5 tangency control. Width profiles:
  Heng:  16 → 11 → 15 (entry dunbi, shaft, corner build)
  Shu:   15 → 11 → 14 (corner inherit, shaft, pre-hook thicken)
  Hook:  14 → 12 → 3 (brief hold, then long taper to fine point)

Reuse:
    from heng_zhe_gou import draw as draw_heng_zhe_gou
    draw_heng_zhe_gou(t)                        # corner at (+100,+120)
    draw_heng_zhe_gou(t, ox=0, oy=0, scale=0.7) # smaller for inset use
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import brushed_bezier


def _w_A(s):
    if s < 0.10: return 16.0 - (s / 0.10) * 5.0
    if s < 0.80: return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 4.0

def _w_B(s):
    if s < 0.15: return 15.0 - (s / 0.15) * 4.0
    if s < 0.80: return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 3.0

def _w_C(s):
    if s < 0.15: return 14.0 - (s / 0.15) * 2.0
    return 12.0 - ((s - 0.15) / 0.85) * 9.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    # Seg A: heng arm
    A0 = (-100.0 * scale + ox, 120.0 * scale + oy)
    A3 = (100.0 * scale + ox, 120.0 * scale + oy)
    A1 = (A0[0] + (A3[0] - A0[0]) / 3.0, A0[1])
    A2 = (A0[0] + 2.0 * (A3[0] - A0[0]) / 3.0, A0[1] - 3.0 * scale)
    brushed_bezier(t, A0, A1, A2, A3, _w_A, samples=200)

    # Seg B: shu arm
    B0 = (100.0 * scale + ox, 120.0 * scale + oy)
    B3 = (100.0 * scale + ox, -100.0 * scale + oy)
    B1 = (B0[0], B0[1] + (B3[1] - B0[1]) / 3.0)
    B2 = (B0[0] - 3.0 * scale, B0[1] + 2.0 * (B3[1] - B0[1]) / 3.0)
    brushed_bezier(t, B0, B1, B2, B3, _w_B, samples=200)

    # Seg C: hook (concave-up-right)
    C0 = (100.0 * scale + ox, -100.0 * scale + oy)
    C3 = (50.0 * scale + ox, -60.0 * scale + oy)
    C1 = (92.0 * scale + ox, -108.0 * scale + oy)
    C2 = (60.0 * scale + ox, -78.0 * scale + oy)
    brushed_bezier(t, C0, C1, C2, C3, _w_C, samples=180)
