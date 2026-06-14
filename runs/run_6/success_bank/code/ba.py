"""八 (bā, "eight") — composed character. 2 strokes.

Mastered: run_6 c53, panel 3/3 YES.

Architecture: **apex_share override** — raw MMH places pie's head at
y=-16.8 and na's head at y=+73.2 (~100 px vertical asymmetry that the
calligraphy-aware panel still rejects). Override lifts pie's head y to
match na's so both strokes start at the same apex_y. The two strokes
DO NOT touch (canonical 八 — distinct from 人).

Reuse:
    from ba import draw_ba
    draw_ba(t)
"""
from pie import draw_pie
from na import draw_na


def draw_ba(t):
    # apex_share: pie.head.y lifted from -16.8 to +73.2 to match na.head.y
    draw_pie(t, ('TL', 0.776, 0.768), ('BL', -0.192, 1.056))
    draw_na(t,  ('TC', 0.26, 0.768),  ('BR', 1.3, 0.96))
