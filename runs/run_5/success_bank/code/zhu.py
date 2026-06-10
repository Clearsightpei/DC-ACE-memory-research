"""主 (zhǔ) — 点 + 王 pattern.

Tags: tag:character tag:5-strokes tag:dian+heng-stacked+shu tag:turtle-renderer
Mastered: run_5 c13. visual=0.860, OCR='主' margin=1.00. Panel 3/3 YES.

Reuse:
    from zhu import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu
from dian import draw as draw_dian


def draw(t, ox=0, oy=0, scale=1.0):
    draw_dian(t, ox=ox + 4  * scale, oy=oy + 99   * scale, scale=1.0  * scale)
    draw_heng(t, ox=ox + 4  * scale, oy=oy + 18   * scale, scale=0.48 * scale)
    draw_heng(t, ox=ox + 0  * scale, oy=oy + -65  * scale, scale=0.38 * scale)
    draw_shu (t, ox=ox + 0  * scale, oy=oy + -80  * scale, scale=0.42 * scale)
    draw_heng(t, ox=ox + 12 * scale, oy=oy + -175 * scale, scale=0.85 * scale)
