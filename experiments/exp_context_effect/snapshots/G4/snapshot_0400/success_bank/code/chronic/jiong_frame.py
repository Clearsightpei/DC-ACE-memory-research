"""冂 (jiōng) — enclosing frame, 2-stroke, canonical hand-written primitive.

Chronic-cluster item, promoted at position 300 after 3 failed retries.

Baked anchors (do NOT tune):
  s1 = 竖   : head @ ('TL', 0.20, 0.15)  (top of left wall)
             tail @ ('BL', 0.20, 0.85)  (bottom of left wall)
             (STRICT vertical — same x_frac in TL/BL column)

  s2 = 横折 : head   @ ('TL', 0.22, 0.15)  (top-left corner, ~5 px right of s1.head)
             corner @ ('TR', 0.80, 0.15)  (top-right corner, same row as head)
             tail   @ ('BR', 0.80, 0.85)  (bottom of right wall, same col as corner)

Joints:
  s1.head ⇆ s2.head  N at top-left (~6 px, near-weld — closes the corner)
  s1.tail             (open at bottom — 冂 has no bottom bar)
  s2.tail             (open at bottom)

Frame proportion: 230-px wide × 210-px tall (canonical 冂 is wider
than tall; retry_2 failed with near-square 280×285).

Root cause fix: chronic B2-B5 failures either compressed to
upper-half (TR9 not applied) OR made frame too square. This plan
hits both invariants — TR9 span + wider-than-tall proportion.
"""
import os, sys
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(_HERE, '..')))

from _anchor import anchor_to_xy, fat_line
from shu import draw_shu
from heng_zhe import draw_heng_zhe


def draw_jiong_frame(draw, color=(0, 0, 0)):
    # s1 — left wall (strict vertical)
    draw_shu(draw, ('TL', 0.20, 0.15), ('BL', 0.20, 0.85),
             width=10, color=color)

    # s2 — top bar + right wall (横折)
    draw_heng_zhe(draw,
                  ('TL', 0.22, 0.15),
                  ('TR', 0.80, 0.15),
                  ('BR', 0.80, 0.85),
                  h_width=10, v_width=10, shoulder=13,
                  color=color)
