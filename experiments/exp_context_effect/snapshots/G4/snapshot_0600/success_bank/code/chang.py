"""厂 (chǎng, "cliff", 2 strokes: 横 + 撇) — B1 retry-1 pass.

Bootstrap batch failed because MMH's N-class joint was interpreted as
literal separation, giving a disconnected top-bar + bottom-left 撇.
The retry fix (per errata): weld the 撇 head to the 横 head via a
SHARED anchor tuple (T-class), producing the canonical inverted-J.

Strokes:
  s1 — 横 (top horizontal, slight upward-right slope).
  s2 — 撇 (sweeps from the shared head down and slightly left).

Joint override: T at TC(0.15, 0.50) — welded (0 px). MMH nominal was
N; T reads correctly for a standalone radical.
"""
from heng import draw_heng
from pie import draw_pie


def draw_chang(draw,
               s1_head=('TC', 0.15, 0.50), s1_tail=('TR', 0.55, 0.40),
               s2_tail=('BL', 0.55, 0.95)):
    # s2_head is INTENTIONALLY the same as s1_head (T-weld).
    draw_heng(draw, s1_head, s1_tail, width=9)
    draw_pie(draw, s1_head, s2_tail,
             head_width=10, tail_width=1, curve=0.14, segments=56)
