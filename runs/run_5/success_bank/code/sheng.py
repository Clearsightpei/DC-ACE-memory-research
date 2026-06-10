"""生 (shēng) — 撇 + 横 + 横 + 竖 + 横 (top-left pie then 3-heng stack with shu).

Tags: tag:character tag:5-strokes tag:pie+heng-stacked+shu tag:turtle-renderer
Mastered: run_5 c13. visual=0.860, OCR='生' margin=0.98. Panel 3/3 YES.

First mastered run_5 character containing a diagonal (撇). Reaches
visual > 0.8 because the 撇 is short (scale 0.32) — the brushwork's
total off-skeleton pixel surplus is smaller than for full-sized
diagonals like in 八/人/入.

Reuse:
    from sheng import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from shu  import draw as draw_shu
from pie  import draw as draw_pie


def draw(t, ox=0, oy=0, scale=1.0):
    draw_pie (t, ox=ox + -89 * scale, oy=oy + -17  * scale, scale=0.32 * scale)
    draw_heng(t, ox=ox + 54  * scale, oy=oy + 5    * scale, scale=0.23 * scale)
    draw_heng(t, ox=ox + 6   * scale, oy=oy + -88  * scale, scale=0.38 * scale)
    draw_shu (t, ox=ox + 8   * scale, oy=oy + -26  * scale, scale=0.70 * scale)
    draw_heng(t, ox=ox + 11  * scale, oy=oy + -182 * scale, scale=0.79 * scale)
