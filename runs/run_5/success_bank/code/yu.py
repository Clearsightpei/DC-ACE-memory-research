"""玉 (yù) — 王 + 点 (dot below middle heng, right of central shu).

Tags: tag:character tag:5-strokes tag:王+点 tag:turtle-renderer tag:composes(王)
Mastered: run_5 c18. visual=0.831, OCR='玉' margin=0.97. Panel 3/3 YES.

Demonstrates Success Bank COMPOSITION: import a mastered character
and add a stroke. The wang.py call establishes the 4-stroke base;
draw_dian places the diagnostic dot.

Reuse:
    from yu import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from wang import draw as draw_wang
from dian import draw as draw_dian


def draw(t, ox=0, oy=0, scale=1.0):
    draw_wang(t, ox=ox, oy=oy, scale=scale)
    draw_dian(t, ox=ox + 70 * scale, oy=oy + -115 * scale, scale=0.95 * scale)
