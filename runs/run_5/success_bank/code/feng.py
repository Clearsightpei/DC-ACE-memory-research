"""丰 (fēng) — 4 strokes: 3 heng evenly stacked + shu protruding through.

Tags: tag:character tag:4-strokes tag:heng-stacked tag:shu-protrudes tag:turtle-renderer
Mastered: run_5 c24. visual=0.858, OCR='丰' margin=1.00. Panel 3/3 YES.

Distinguishes from 王: more uniformly-spaced hengs AND the shu protrudes
visibly above the top heng and below the bottom heng.

Reuse:
    from feng import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu


def draw(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox + -3 * scale, oy=oy + 50   * scale, scale=0.478 * scale)
    draw_heng(t, ox=ox + -3 * scale, oy=oy + -21  * scale, scale=0.480 * scale)
    draw_heng(t, ox=ox + 8  * scale, oy=oy + -102 * scale, scale=0.778 * scale)
    draw_shu (t, ox=ox + -7 * scale, oy=oy + -52  * scale, scale=0.915 * scale)
