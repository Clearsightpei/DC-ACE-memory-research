"""下 (xià) — 横 (top) + 竖 (hanging) + 点 (right).

Tags: tag:character tag:3-strokes tag:heng+shu+dian tag:竖-hangs-from-heng
Component-of: 卞 ... (chars containing 下)
Mastered: run_5 cycle 4, rubric 9/10. Carry-over from c3 (where 竖 pierced above heng).
Vision identity: PASSED — 竖 hangs FROM the heng without poking above it.

Composition: top heng at oy=+80, length=330;
竖 oy_top=+70 (10 below heng centerline so it hangs, no pierce), length=240;
点 anchored at (+60, +20), length 42.

Key structural rule (verified c4): when 竖 sits BELOW a 横, `oy_top` must be
AT or just below the heng's centerline. If `oy_top` is above, the 竖 pierces
and the character reads as 十-with-dot.

Reuse:
    from xia import draw
    draw(pil_draw, ox=0, oy=0, scale=1.0)
"""

from heng import draw_heng
from shu import draw_shu
from dian import draw_dian


def draw(pil_draw, ox=0, oy=0, scale=1.0):
    """下: top heng (long), 竖 hanging from below, 点 to the right."""
    draw_heng(pil_draw, ox=ox + 0, oy=oy + 80 * scale, length=330 * scale, scale=1.0 * scale)
    draw_shu(pil_draw, ox=ox + 0, oy_top=oy + 70 * scale, length=240 * scale, scale=1.0 * scale)
    draw_dian(pil_draw, ox=ox + 60 * scale, oy=oy + 20 * scale, length=42.0, scale=1.0 * scale)
