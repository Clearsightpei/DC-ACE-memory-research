"""上 (shàng) — 竖 + short 横 + long bottom 横.

Tags: tag:character tag:3-strokes tag:heng+shu tag:turtle-renderer
Mastered: run_5 c12. visual=0.904, OCR='上' margin=1.00. Panel 3/3 YES.

Reuse:
    from shang import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu


def draw(t, ox=0, oy=0, scale=1.0):
    draw_shu (t, ox=ox + -6 * scale, oy=oy + -25  * scale, scale=0.66 * scale)
    draw_heng(t, ox=ox + 56 * scale, oy=oy + -17  * scale, scale=0.25 * scale)
    draw_heng(t, ox=ox + 11 * scale, oy=oy + -167 * scale, scale=0.81 * scale)
