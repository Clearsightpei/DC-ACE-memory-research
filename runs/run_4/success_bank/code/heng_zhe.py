"""
横折 (heng_zhe) — compound L-turn stroke.

Tags: tag:compound-stroke tag:横折 tag:multi-segment tag:corner-顿笔
Component-of: (to fill — 口, 日, 目, 田, 国, 月, 见, 国, ...)
Mastered: run_4 cycle 7, rubric 10/10

A horizontal arm followed by a 90° downward turn into a vertical arm.
ONE continuous brushed path implemented as TWO Bézier segments
stitched at the upper-right corner with a 顿笔 (thickening) — the
visual signature of 横折. Without the corner thickening it reads as
two separate strokes glued together.

Reuse:
    from heng_zhe import draw as draw_heng_zhe
    draw_heng_zhe(t)                          # corner at (+100,+120), 200 px arms
    draw_heng_zhe(t, ox=0, oy=0, scale=0.6)   # smaller frame for inset use
    draw_heng_zhe(t, ox=-50, oy=0)            # shift left

Width profile:
  Heng arm: 16 (entry) → 11 (shaft) → 15 (corner build)
  Shu arm:  15 (corner inherit) → 11 (shaft) → 13 (slight 收笔)
Width is continuous across the junction (A ends 15, B starts 15).

What this entry establishes:
- The corner-顿笔 thickening pattern for L-turn compounds.
- Confirms the §1.5 two-segment pattern handles corners (not just
  tail kicks). Same template will apply to 横折钩, 竖钩, 竖弯钩, ...
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from heng import brushed_bezier


def _w_hengzhe_A(s: float) -> float:
    if s < 0.10: return 16.0 - (s / 0.10) * 5.0
    if s < 0.80: return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 4.0


def _w_hengzhe_B(s: float) -> float:
    if s < 0.15: return 15.0 - (s / 0.15) * 4.0
    if s < 0.85: return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 2.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    """Draw 横折. Heng arm from (-100,+120) to corner (+100,+120); shu arm down to (+100,-80)."""
    # Segment A: horizontal arm
    A0 = (-100.0 * scale + ox, 120.0 * scale + oy)
    A3 = (100.0 * scale + ox, 120.0 * scale + oy)
    A1 = (A0[0] + (A3[0] - A0[0]) / 3.0, A0[1])
    A2 = (A0[0] + 2.0 * (A3[0] - A0[0]) / 3.0, A0[1])
    brushed_bezier(t, A0, A1, A2, A3, _w_hengzhe_A, samples=200)

    # Segment B: vertical arm
    B0 = (100.0 * scale + ox, 120.0 * scale + oy)
    B3 = (100.0 * scale + ox, -80.0 * scale + oy)
    B1 = (B0[0], B0[1] + (B3[1] - B0[1]) / 3.0)
    B2 = (B0[0], B0[1] + 2.0 * (B3[1] - B0[1]) / 3.0)
    brushed_bezier(t, B0, B1, B2, B3, _w_hengzhe_B, samples=200)
