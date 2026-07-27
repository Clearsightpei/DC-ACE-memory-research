"""丶 (zhǔ) — Phase-2 radical, 1画. Wrapper for draw_dian.

Anchor plan (米字格, PIL-native):
  stroke 1 (点): head @ ('TC', 0.146, 0.946)  — thin 起笔, upper-left
                 tail @ ('C',  0.717, 0.652)  — rounded press, lower-right
Joints: NONE (single stroke).

Widths reduced from dian defaults (peak_width 7 vs 11) because GT
shows a thinner-curve dot without heavy 顿笔 bulb; caller may override.

Human PASS (bootstrap batch, 2026-07-17).
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from dian import draw_dian


def draw_zhu(draw,
             head=('TC', 0.146, 0.946),
             tail=('C', 0.717, 0.652),
             head_width=2, peak_width=7, curve=0.08, segments=24):
    """Render 丶. Defaults match MMH anchors for standalone radical."""
    draw_dian(draw, head, tail,
              head_width=head_width, peak_width=peak_width,
              curve=curve, segments=segments)
