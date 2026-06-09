"""上 (shàng) — 短竖 + 短横 + 长横.

Tags: tag:character tag:3-strokes tag:shu+heng tag:component-of(止, 让)
Component-of: 止, 让 ... (chars containing 上)
Mastered: run_5 cycle 3, rubric 7/10 (dunbi=2 hudu=1 taper=1 proportion=2 overall=1)
Vision identity: PASSED. OCR returned 上 conf high.

Composition: bottom long 横 at oy=-110 (the base);
竖 stands on the base at ox=-20, oy_top=+100, length=210;
short 横 to the right of the 竖, at ox=+70, oy=-30, length=130 (scale 0.7).

Reuse:
    from shang import draw
    draw(pil_draw, ox=0, oy=0, scale=1.0)
"""

from heng import draw_heng
from shu import draw_shu


def draw(pil_draw, ox=0, oy=0, scale=1.0):
    """上: 长底横 + 竖 standing on it + 短横 on the upper-right."""
    bot_y = oy + -110 * scale
    draw_heng(pil_draw, ox=ox + 0, oy=bot_y, length=320 * scale, scale=1.0 * scale)
    shu_ox = ox + -20 * scale
    draw_shu(pil_draw, ox=shu_ox, oy_top=bot_y + 210 * scale, length=210 * scale, scale=1.0 * scale)
    draw_heng(pil_draw, ox=shu_ox + 90 * scale, oy=oy + -30 * scale, length=130 * scale, scale=0.7 * scale)
