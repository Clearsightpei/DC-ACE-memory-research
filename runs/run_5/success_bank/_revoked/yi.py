"""一 (yī) — single 横 stroke character.

Tags: tag:character tag:1-stroke tag:heng tag:component-of(二, 三, 王, 工, 干, 上, 下)
Component-of: 二, 三, 王, 工, 干, 上, 下, 旦, 旨, ... (any char that contains 一)
Mastered: run_5 cycle 2, rubric 7/10 (dunbi=2 hudu=1 taper=1 proportion=2 overall=1)
Vision identity: PASSED. OCR returned none (RapidOCR has trouble with this
brushwork style on standalone 一) but Curator-vision confirmed unambiguous 一.

Reuse:
    from yi import draw
    draw(pil_draw, ox=0, oy=0, scale=1.0)
"""

from heng import draw_heng


def draw(pil_draw, ox=0, oy=0, scale=1.0):
    """一: single 横 stroke, centered slightly below the canvas middle."""
    draw_heng(pil_draw, ox=ox + 0, oy=oy + -30 * scale, length=280 * scale, scale=scale)
