"""二 (èr) — 2 stacked heng (top short, bottom long).

Tags: tag:character tag:2-strokes tag:heng-stacked
Mastered: run_6 c14. Structural ✓ (count=2, anchors ≤11 px).

Reuse:
    from er import draw_er
    draw_er(t)  # composes 2 calls to draw_heng
"""
from heng import draw_heng


def draw_er(t):
    draw_heng(t, ("ML", 0.81, 0.59), ("MR", 0.07, 0.49))
    draw_heng(t, ("ML", 0.03, 0.97), ("MR", 0.94, 0.94))
