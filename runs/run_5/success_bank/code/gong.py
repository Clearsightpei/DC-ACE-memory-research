"""工 (gōng) — two heng + short shu between them (NOT piercing through).

Tags: tag:character tag:3-strokes tag:heng-stacked tag:shu-between tag:turtle-renderer
Mastered: run_5 c11. visual=0.890, OCR='工' margin=0.82. Panel 3/3 YES.

Distinguishes from 干: shu is SHORT (scale 0.47), connects only the
two heng's midpoints, does not protrude above or below.

Reuse:
    from gong import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu


def draw(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox + 10 * scale, oy=oy + 52   * scale, scale=0.48  * scale)
    draw_heng(t, ox=ox + 8  * scale, oy=oy + -136 * scale, scale=0.853 * scale)
    draw_shu (t, ox=ox + 6  * scale, oy=oy + -42  * scale, scale=0.47  * scale)
