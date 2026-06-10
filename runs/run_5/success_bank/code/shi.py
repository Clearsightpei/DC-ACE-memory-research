"""十 (shí) — heng + shu cross at center.

Tags: tag:character tag:2-strokes tag:heng+shu tag:turtle-renderer
Mastered: run_5 c11. visual=0.890, OCR='十' margin=0.83. Panel 3/3 YES.

Reuse:
    from shi import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu


def draw(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox + 6 * scale,  oy=oy + -22 * scale, scale=0.835 * scale)
    draw_shu (t, ox=ox + 3 * scale,  oy=oy + -57 * scale, scale=0.833 * scale)
