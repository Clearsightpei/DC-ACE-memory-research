"""丨 (gǔn) — Phase-2 radical, 1画. Wrapper for draw_shu.

Anchor plan (米字格, PIL-native):
  stroke 1 (竖): head @ ('TC', 0.301, 0.665), tail @ ('BC', 0.412, 1.000)
                 width 10.
Joints: NONE (single stroke).

Bank composition rule (principle_bank Phase-1 wrappers): 丨 is a
1-画 radical whose canonical shape IS the 竖 stroke primitive. Use
draw_shu with these MMH-derived defaults; caller may override.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

from shu import draw_shu


def draw_gun(draw,
             head=('TC', 0.301, 0.665),
             tail=('BC', 0.412, 1.000),
             width=10):
    """Render 丨. Defaults match MMH anchors for standalone radical."""
    draw_shu(draw, head, tail, width=width)
