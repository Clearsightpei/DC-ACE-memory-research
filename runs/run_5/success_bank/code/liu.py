"""六 (liù) — 4 strokes: top dian + heng + small 撇 + small right dian.

Tags: tag:character tag:4-strokes tag:turtle-renderer
Mastered: run_5 c22 (after c19 carry-over). visual=0.816, OCR='六' margin=0.97. Panel 3/3 YES.

c19 used pie scale 0.28 + right dian scale 2.0 → visual 0.74.
c22 fix: pie scale 0.22 + right dian scale 1.5 (shrink brushwork surplus
that was over-painting the thin MMH GT skeleton).

Reuse:
    from liu import draw
    draw(t, ox=0, oy=0, scale=1.0)
"""
from heng import draw as draw_heng
from pie  import draw as draw_pie
from dian import draw as draw_dian


def draw(t, ox=0, oy=0, scale=1.0):
    draw_dian(t, ox=ox + -10  * scale, oy=oy + 85  * scale, scale=1.3  * scale)
    draw_heng(t, ox=ox + -10  * scale, oy=oy + 20  * scale, scale=0.70 * scale)
    draw_pie (t, ox=ox + -83  * scale, oy=oy + -94 * scale, scale=0.22 * scale)
    draw_dian(t, ox=ox + 57.5 * scale, oy=oy + -80 * scale, scale=1.5  * scale)
