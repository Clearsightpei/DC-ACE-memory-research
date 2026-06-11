"""卞 (biàn) — small top dian + 下 (heng + shu + dian below). 4 strokes.

Tags: tag:character tag:4-strokes tag:turtle-renderer tag:composes(下)
Mastered: run_5 c21. visual=0.856, OCR='卞' margin=0.86. Panel 3/3 YES.

Composition: shifts the mastered 下 down by 20 and adds a small dian above.

Reuse:
    from bian import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from xia import draw as draw_xia
from dian import draw as draw_dian


def draw(t, ox=0, oy=0, scale=1.0):
    draw_xia (t, ox=ox + 0   * scale, oy=oy + -20 * scale, scale=1.0 * scale)
    draw_dian(t, ox=ox + -15 * scale, oy=oy + 130 * scale, scale=1.4 * scale)
