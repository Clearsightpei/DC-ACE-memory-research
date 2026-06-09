"""干 (gān) — 短横 + 长横 + 竖 piercing through the long heng.

Tags: tag:character tag:3-strokes tag:heng+heng+shu tag:竖-pierces-heng
Component-of: 罕, 平, 年 ... (chars built from 干 silhouette)
Mastered: run_5 cycle 4, rubric 9/10. OCR returned 干.
Vision identity: PASSED.

Composition: top short heng at oy=+110, length=200, scale=0.85;
middle long heng at oy=+10, length=330;
竖 oy_top=+80 (above the long heng, between the two hengs), length=270 (pierces
through the long heng and extends well below).

Reuse:
    from gan import draw
    draw(pil_draw, ox=0, oy=0, scale=1.0)
"""

from heng import draw_heng
from shu import draw_shu


def draw(pil_draw, ox=0, oy=0, scale=1.0):
    """干: top short heng + middle long heng + 竖 piercing through middle."""
    draw_heng(pil_draw, ox=ox + 0, oy=oy + 110 * scale, length=200 * scale, scale=0.85 * scale)
    draw_heng(pil_draw, ox=ox + 0, oy=oy + 10 * scale, length=330 * scale, scale=1.0 * scale)
    draw_shu(pil_draw, ox=ox + 0, oy_top=oy + 80 * scale, length=270 * scale, scale=1.0 * scale)
