"""八 (bā) — 撇 + 捺, SEPARATED heads (visible gap between the two stroke heads).

Tags: tag:character tag:2-strokes tag:撇捺-separated tag:component-of(只, 兵, 公)
Component-of: 只, 兵, 公 (chars with the 八-on-top pattern)
Mastered: run_5 cycle 5, rubric 7/10. OCR returned 八.
Vision identity: PASSED — clear horizontal gap between 撇 head and 捺 head distinguishes from 人.

Composition: 撇 head (-30, +50), tail (-160, -130) — short, lower;
捺 head (+60, +130), tail (+220, -90) — longer, higher.
Heads are separated by ~90px horizontally.

Reuse:
    from ba import draw
    draw(pil_draw, ox=0, oy=0, scale=1.0)
"""

from pie import draw_pie
from na import draw_na


def draw(pil_draw, ox=0, oy=0, scale=1.0):
    """八: 撇 + 捺 with a visible gap between the two stroke heads."""
    draw_pie(pil_draw,
             head_x=ox + -30 * scale, head_y=oy + 50 * scale,
             tail_x=ox + -160 * scale, tail_y=oy + -130 * scale,
             scale=scale)
    draw_na(pil_draw,
            head_x=ox + 60 * scale, head_y=oy + 130 * scale,
            tail_x=ox + 220 * scale, tail_y=oy + -90 * scale,
            scale=scale)
