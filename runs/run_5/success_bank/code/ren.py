"""人 (rén) — 撇 + 捺, SHARED apex (撇 and 捺 emanate from the same point).

Tags: tag:character tag:2-strokes tag:撇捺-shared-apex tag:component-of(从, 众, 介)
Component-of: 从, 众, 介 ... (compounds containing 人)
Mastered: run_5 cycle 5, rubric 7/10. OCR returned 入 (canonical RapidOCR 人/入 confusion)
but Curator-vision PASSED — the shared apex unambiguously distinguishes 人 from 入
(where the 撇 attaches below the 捺's apex, not at it).

Composition: shared apex at (0, +130); 撇 to (-160, -150); 捺 to (+180, -130).
Symmetric-ish inverted V with 撇 slightly steeper than 捺.

Key structural rule: 人 has the 撇 and 捺 SHARING the apex. If they have a gap,
it's 八. If the 撇 starts BELOW the 捺's apex (as a secondary attachment), it's 入.

Reuse:
    from ren import draw
    draw(pil_draw, ox=0, oy=0, scale=1.0)
"""

from pie import draw_pie
from na import draw_na


def draw(pil_draw, ox=0, oy=0, scale=1.0):
    """人: 撇 + 捺 sharing an apex at the top."""
    apex_x, apex_y = ox + 0, oy + 130 * scale
    draw_pie(pil_draw,
             head_x=apex_x, head_y=apex_y,
             tail_x=ox + -160 * scale, tail_y=oy + -150 * scale,
             scale=scale)
    draw_na(pil_draw,
            head_x=apex_x, head_y=apex_y,
            tail_x=ox + 180 * scale, tail_y=oy + -130 * scale,
            scale=scale)
