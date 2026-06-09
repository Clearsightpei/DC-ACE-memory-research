"""三 (sān) — three stacked 横, bottom longest.

Tags: tag:character tag:3-strokes tag:heng-stacked tag:turtle-renderer
Component-of: 王 ... (any char with stacked-横 pattern)
Mastered: run_5 cycle 6 under 4-gate hard gate.
Numbers: visual=0.878, OCR='三' conf 1.00 margin 1.00 is_correct=True.
Panel: 3/3 YES (fresh-context skeptics each saw only attempt+GT+target).

Composition: top heng (5, +60, 0.42); middle (4, -38, 0.38); bottom (14, -140, 0.84).

Reuse:
    from san import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""

from heng import draw as draw_heng


def draw(t, ox=0, oy=0, scale=1.0):
    """三: three stacked 横, bottom longest."""
    draw_heng(t, ox=ox + 5 * scale, oy=oy + 60 * scale, scale=0.42 * scale)
    draw_heng(t, ox=ox + 4 * scale, oy=oy + -38 * scale, scale=0.38 * scale)
    draw_heng(t, ox=ox + 14 * scale, oy=oy + -140 * scale, scale=0.84 * scale)
