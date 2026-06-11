"""丘 (qiū) — 6 strokes: short pie + top heng + left shu + middle heng + small right shu + bottom long heng.

Tags: tag:character tag:6-strokes tag:turtle-renderer
Mastered: run_5 c24. visual=0.850, OCR='丘' margin=0.91. Panel 3/3 YES.

Reuse:
    from qiu import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu
from pie  import draw as draw_pie


def draw(t, ox=0, oy=0, scale=1.0):
    draw_pie (t, ox=ox + -5  * scale, oy=oy + 46   * scale, scale=0.22 * scale)
    draw_heng(t, ox=ox + 0   * scale, oy=oy + 45   * scale, scale=0.27 * scale)
    draw_shu (t, ox=ox + -70 * scale, oy=oy + -66  * scale, scale=0.40 * scale)
    draw_heng(t, ox=ox + 36  * scale, oy=oy + -34  * scale, scale=0.45 * scale)
    draw_shu (t, ox=ox + 41  * scale, oy=oy + -91  * scale, scale=0.25 * scale)
    draw_heng(t, ox=ox + 6   * scale, oy=oy + -156 * scale, scale=0.85 * scale)
