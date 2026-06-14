"""人 (rén, "person") — composed character. 2 strokes.

Mastered: run_6 c54, panel 3/3 YES.

Architecture: **apex_share override** — raw MMH places pie's head at
y=+89.6 and na's head at y=-14.0 (a 100 px vertical gap; raw render
read as disconnected). Override lifts na's head y to match pie's so
both strokes meet at the apex. Heads end up 3.6 px horizontally apart
(visually merged). Distinct from 八 (no meeting) and 入 (撇 attaches
onto 捺 instead).

Reuse:
    from ren import draw_ren
    draw_ren(t)
"""
from pie import draw_pie
from na import draw_na


def draw_ren(t):
    # apex_share: na.head.y lifted from -14.0 to +89.6 to match pie.head.y
    draw_pie(t, ('TC', 0.384, 0.604), ('BL', -0.26, 1.168))
    draw_na(t,  ('TC', 0.348, 0.604), ('BR', 1.3, 1.188))
