"""十 (shí) — 横 + 竖 cross.

Tags: tag:character tag:2-strokes tag:heng+shu tag:component-of(古, 干, 平, 早, 卄)
Component-of: 古, 干, 平, 早, 卄 ... (chars containing the 十 cross)
Mastered: run_5 cycle 3, rubric 9/10 (dunbi=2 hudu=1 taper=2 proportion=2 overall=2)
Vision identity: PASSED. OCR returned 十 conf high.

Composition: 横 at oy=0, length=320 (canvas-center horizontal);
竖 starts at oy_top=+90, extends down 280px (asymmetric: ~90 above heng, ~190 below).

Reuse:
    from shi import draw
    draw(pil_draw, ox=0, oy=0, scale=1.0)
"""

from heng import draw_heng
from shu import draw_shu


def draw(pil_draw, ox=0, oy=0, scale=1.0):
    """十: long 横 across middle, long 竖 crossing through it (more length below)."""
    heng_y = oy + 0
    draw_heng(pil_draw, ox=ox + 0, oy=heng_y, length=320 * scale, scale=1.0 * scale)
    draw_shu(pil_draw, ox=ox + 0, oy_top=heng_y + 90 * scale, length=280 * scale, scale=1.0 * scale)
