"""下 (xià) — long top 横 + 竖 (hanging) + 点 to the right.

Tags: tag:character tag:3-strokes tag:heng+shu+dian tag:turtle-renderer
Mastered: run_5 c12. visual=0.890, OCR='下' margin=1.00. Panel 3/3 YES.

Reuse:
    from xia import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu
from dian import draw as draw_dian


def draw(t, ox=0, oy=0, scale=1.0):
    draw_heng(t, ox=ox + 5  * scale, oy=oy + 75  * scale, scale=0.82 * scale)
    draw_shu (t, ox=ox + 3  * scale, oy=oy + -72 * scale, scale=0.69 * scale)
    draw_dian(t, ox=ox + 60 * scale, oy=oy + -27 * scale, scale=1.45 * scale)
