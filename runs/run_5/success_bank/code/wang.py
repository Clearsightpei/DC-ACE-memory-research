"""王 (wáng) — 4 strokes: 3 stacked heng + shu through all midpoints.

Tags: tag:character tag:4-strokes tag:heng-stacked tag:shu-piercing tag:turtle-renderer
Mastered: run_5 c15 (after c13 carry-over). visual=0.885, OCR='王' margin=0.97. Panel 3/3 YES.

Composition: shu (scale 0.62) + top heng (0.46) + mid heng (0.38) + bottom heng (0.82).
The c13 attempt used shu scale 0.48 — too short; c15 fix uses 0.62 to span GT's vertical extent.

Reuse:
    from wang import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu


def draw(t, ox=0, oy=0, scale=1.0):
    draw_shu (t, ox=ox + 3 * scale, oy=oy + -49  * scale, scale=0.62 * scale)
    draw_heng(t, ox=ox + 5 * scale, oy=oy + 64   * scale, scale=0.46 * scale)
    draw_heng(t, ox=ox + 5 * scale, oy=oy + -45  * scale, scale=0.38 * scale)
    draw_heng(t, ox=ox + 7 * scale, oy=oy + -158 * scale, scale=0.82 * scale)
