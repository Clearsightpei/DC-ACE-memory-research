"""二 (èr) — two stacked 横, top short, bottom long.

Tags: tag:character tag:2-strokes tag:heng-stacked tag:turtle-renderer
Component-of: 三, 王, 工 ...
Mastered: run_5 cycle 6. visual=0.88, OCR='二' (conf 0.99), is_correct=True. Vision: unambiguous.

Composition: top 横 at (3, +35, 0.45); bottom 横 at (6, -115, 0.80).

Reuse:
    from er import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""

from heng import draw as draw_heng


def draw(t, ox=0, oy=0, scale=1.0):
    """二: top short heng + bottom long heng."""
    draw_heng(t, ox=ox + 3 * scale, oy=oy + 35 * scale, scale=0.45 * scale)
    draw_heng(t, ox=ox + 6 * scale, oy=oy + -115 * scale, scale=0.80 * scale)
