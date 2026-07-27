"""冖 (mì, "cover" as Phase-3 CHAR, 2画) — B4 retry PASS promotion.

Thin wrapper: char-context reuse of mi_cover.py (Phase-2 radical) with
OVERRIDING anchors per TR1 that fix the retry-0 bugs:
  - Bug A: hook tip must sit BELOW shoulder (down-left flick), not above.
  - Bug B: cover sits in upper-third band (TR9-flavored lift).
  - Bug C: 短撇 tick nudged up so it reads as a small mark left of the
    horizontal head.

Strokes:
  s1 — 短撇 (short tick, upper-left).
  s2 — 横钩 (top horizontal + short down-left hook at the right end).

Joint: s1.tail-region ⇆ s2.head → N (small gap at top-left corner).
"""
from mi_cover import draw_mi_cover


def draw_mi_cover_char(draw,
                       s1_head=('TL', 0.60, 0.55),
                       s1_tail=('TL', 0.48, 0.90),
                       s2_head=('TL', 0.72, 0.75),
                       s2_shoulder=('TR', 0.75, 0.55),
                       s2_tip=('TR', 0.60, 0.95)):
    draw_mi_cover(draw,
                  s1_head=s1_head, s1_tail=s1_tail,
                  s2_head=s2_head, s2_shoulder=s2_shoulder, s2_tip=s2_tip)
