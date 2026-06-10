"""干 (gān) — two heng (top short, bottom long) + shu through both.

Tags: tag:character tag:3-strokes tag:heng-stacked tag:shu-piercing tag:turtle-renderer
Mastered: run_5 c11. visual=0.887, OCR='干' margin=0.98. Panel 3/3 YES.

Reuse:
    from gan import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu


def draw(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox + 8 * scale, oy=oy + 97  * scale, scale=0.43  * scale)
    draw_heng(t, ox=ox + 5 * scale, oy=oy + -20 * scale, scale=0.84  * scale)
    draw_shu (t, ox=ox + 2 * scale, oy=oy + -64 * scale, scale=0.805 * scale)
