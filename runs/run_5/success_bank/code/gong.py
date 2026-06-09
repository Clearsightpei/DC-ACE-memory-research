"""工 (gōng) — 横 (top) + 竖 (spanning) + 横 (bottom).

Tags: tag:character tag:3-strokes tag:heng+shu+heng tag:竖-spans-between-hengs
Component-of: 红, 江, 巧 ... (any char with 工 component)
Mastered: run_5 cycle 4, rubric 9/10.
Vision identity: PASSED.

Composition: top short heng at oy=+90, length=200, scale=0.85;
bottom long heng at oy=-110, length=310;
竖 spans the gap, oy_top=+90, length=200 (= top_y - bot_y).

Key structural rule (verified c4): when 竖 sits BETWEEN two hengs (spanning),
`oy_top` is at the top heng's y and `length` is the vertical gap between hengs.
The 竖 should not pierce above the top heng or below the bottom heng.

Reuse:
    from gong import draw
    draw(pil_draw, ox=0, oy=0, scale=1.0)
"""

from heng import draw_heng
from shu import draw_shu


def draw(pil_draw, ox=0, oy=0, scale=1.0):
    """工: top heng + 竖 spanning between + bottom heng."""
    top_y = oy + 90 * scale
    bot_y = oy + -110 * scale
    draw_heng(pil_draw, ox=ox + 0, oy=top_y, length=200 * scale, scale=0.85 * scale)
    draw_heng(pil_draw, ox=ox + 0, oy=bot_y, length=310 * scale, scale=1.0 * scale)
    draw_shu(pil_draw, ox=ox + 0, oy_top=top_y, length=top_y - bot_y, scale=1.0 * scale)
