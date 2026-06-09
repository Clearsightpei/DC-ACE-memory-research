"""入 (rù) — 撇 + 捺, 捺 DOMINANT (撇 attaches below the 捺's apex).

Tags: tag:character tag:2-strokes tag:捺-dominant tag:撇-attaches-below-apex tag:component-of(全, 内, 两)
Component-of: 全, 内, 两 ... (compounds containing 入)
Mastered: run_5 cycle 5, rubric 7/10. OCR returned 入.
Vision identity: PASSED — the 撇 attaches to the 捺's upper section (NOT sharing the apex),
which distinguishes 入 from 人.

Composition: 捺 head (-50, +150), tail (+200, -120) — dominant, long sweep with kick;
撇 head (+10, +100) — BELOW the 捺's head — tail (-110, -10) — short attached stroke.

Key structural rule (the run_4 false-positive class fix): 入's 撇 head MUST be below
the 捺's head. If they share the apex, the character reads as 人. This is the exact
distinction that text-prescription failed to enforce in run_4 c20; in run_5 the
Drawer sees the GT and reproduces the structural distinction.

Reuse:
    from ru import draw
    draw(pil_draw, ox=0, oy=0, scale=1.0)
"""

from pie import draw_pie
from na import draw_na


def draw(pil_draw, ox=0, oy=0, scale=1.0):
    """入: 捺 dominates from the top-left; 撇 attaches below the 捺's apex."""
    draw_na(pil_draw,
            head_x=ox + -50 * scale, head_y=oy + 150 * scale,
            tail_x=ox + 200 * scale, tail_y=oy + -120 * scale,
            scale=scale)
    draw_pie(pil_draw,
             head_x=ox + 10 * scale, head_y=oy + 100 * scale,
             tail_x=ox + -110 * scale, tail_y=oy + -10 * scale,
             scale=scale)
