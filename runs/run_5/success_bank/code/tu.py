"""土 (tǔ) — 3 strokes: top heng (short) + shu + bottom heng (long).

Tags: tag:character tag:3-strokes tag:heng+shu tag:turtle-renderer
Mastered: run_5 c15. visual=0.876, OCR='土' margin=0.94. Panel 3/3 YES.

Reuse:
    from tu import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu


def draw(t, ox=0, oy=0, scale=1.0):
    draw_shu (t, ox=ox + 0 * scale, oy=oy + -25  * scale, scale=0.62  * scale)
    draw_heng(t, ox=ox + 2 * scale, oy=oy + -25  * scale, scale=0.47  * scale)
    draw_heng(t, ox=ox + 8 * scale, oy=oy + -157 * scale, scale=0.805 * scale)
