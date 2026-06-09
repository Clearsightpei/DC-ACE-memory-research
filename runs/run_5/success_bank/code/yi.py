"""一 (yī) — single 横 stroke.

Tags: tag:character tag:1-stroke tag:heng tag:turtle-renderer
Component-of: 二, 三, 王, 工, 干, 上, 下 ... (any char containing 一)
Mastered: run_5 cycle 6 under relaxed hard gate (OCR is_correct + visual>0.8 + vision)
Numbers: visual=0.85, OCR='一' (conf 0.79), is_correct=True. Vision: unambiguous.

Composition: one brushed 横 at (ox=6, oy=-47, scale=0.81) — read off the MMH GT's pixel band.

Reuse:
    from yi import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""

from heng import draw as draw_heng


def draw(t, ox=0, oy=0, scale=1.0):
    """一: single 横, positioned to match MMH GT."""
    draw_heng(t, ox=ox + 6 * scale, oy=oy + -47 * scale, scale=0.81 * scale)
