"""二 (èr) — two stacked 横, top short, bottom long.

Tags: tag:character tag:2-strokes tag:heng-stacked tag:component-of(三, 王, 工, 二)
Component-of: 三, 王, 工, 元, 云, ... (any char with stacked 横 pattern)
Mastered: run_5 cycle 2, rubric 7/10 (dunbi=2 hudu=1 taper=1 proportion=2 overall=1)
Vision identity: PASSED. OCR returned 二 conf 0.96.

Composition: top 横 at oy=+60, length=190 (scale 0.85);
bottom 横 at oy=-70, length=280 (scale 1.0).

Reuse:
    from er import draw
    draw(pil_draw, ox=0, oy=0, scale=1.0)
"""

from heng import draw_heng


def draw(pil_draw, ox=0, oy=0, scale=1.0):
    """二: two horizontal strokes stacked, bottom clearly longer."""
    draw_heng(pil_draw, ox=ox + 0, oy=oy + 60 * scale, length=190 * scale, scale=0.85 * scale)
    draw_heng(pil_draw, ox=ox + 0, oy=oy + -70 * scale, length=280 * scale, scale=1.0 * scale)
