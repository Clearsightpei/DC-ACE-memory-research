"""三 (sān) — three stacked 横, bottom longest.

Tags: tag:character tag:3-strokes tag:heng-stacked
Component-of: 王 (3 hengs + 1 shu), ... (chars built from stacked 横)
Mastered: run_5 cycle 2, rubric 7/10 (dunbi=2 hudu=1 taper=1 proportion=2 overall=1)
Vision identity: PASSED. OCR returned 三 conf 1.00.

Composition: top 横 at oy=+90 length 200 (scale 0.85);
middle at oy=0 length 210 (scale 0.85);
bottom at oy=-90 length 310 (scale 1.0).

Reuse:
    from san import draw
    draw(pil_draw, ox=0, oy=0, scale=1.0)
"""

from heng import draw_heng


def draw(pil_draw, ox=0, oy=0, scale=1.0):
    """三: three horizontal strokes stacked, bottom longest."""
    draw_heng(pil_draw, ox=ox + 0, oy=oy + 90 * scale, length=200 * scale, scale=0.85 * scale)
    draw_heng(pil_draw, ox=ox + 0, oy=oy + 0, length=210 * scale, scale=0.85 * scale)
    draw_heng(pil_draw, ox=ox + 0, oy=oy + -90 * scale, length=310 * scale, scale=1.0 * scale)
