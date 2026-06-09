"""竖 — atomic vertical stroke, 垂露 variant (rounded bottom).

Tags: tag:atomic-stroke tag:shu tag:垂露竖 tag:楷书 tag:PIL-renderer
Component-of: 十, 上, 下, 王, 中, 工, 卜, 干, ... (any char with a vertical)
Mastered: run_5 cycle 3 (verified in 十 with rubric 9/10 and 上 with rubric 7/10)
Vision identity: PASSED — small top entry-hook + heavy rounded 垂露 bottom.

Width profile: entry-press 16 (top) → shaft 11 → bottom-press 18 (rounded).
The 垂露 (rounded bottom) variant is preferred for general reuse inside
compound characters. If a 悬针 (needle-tip) is needed later (e.g. lone 竖
in 中), add a separate `shu_needle.py` entry.

Renderer: PIL `draw.ellipse` per sample, same Bezier+width-floor pattern
as `heng.py` (principle §1.0). 220 samples for the shaft, 80 for the
small top hook.

Reuse interface:
    from shu import draw_shu
    draw_shu(pil_draw, ox=<center_x>, oy_top=<top_y>, length=<px>, scale=1.0)

`oy_top` is the math-coords y of the TOP of the stroke (entry press).
The stroke extends downward by `length` to `(ox, oy_top - length)`.
"""

from heng import to_px, bezier_point, brushed_bezier  # reuse §1.0 primitives


def w_profile_shu(s):
    """entry press 16 → shaft 11 → bottom press 18 (垂露)."""
    if s <= 0.10:
        return 16.0
    elif s <= 0.20:
        t = (s - 0.10) / 0.10
        return 16.0 + (11.0 - 16.0) * t
    elif s <= 0.80:
        return 11.0
    elif s <= 0.95:
        t = (s - 0.80) / 0.15
        return 11.0 + (18.0 - 11.0) * t
    else:
        return 18.0


def draw_top_hook_shu(pil_draw, ox, oy_top, scale=1.0):
    """Small leftward top entry-hook visible in MMH 竖 GTs.
       Drawn at constant entry-press width 16."""
    flen = 12.0 * scale
    P0 = (ox - flen * 0.55, oy_top + flen * 0.40)
    P1 = (ox - flen * 0.35, oy_top + flen * 0.25)
    P2 = (ox - flen * 0.15, oy_top + flen * 0.10)
    P3 = (ox, oy_top)
    brushed_bezier(pil_draw, P0, P1, P2, P3, lambda s: 16.0, samples=80)


def draw_shu(pil_draw, ox, oy_top, length, scale=1.0):
    """Draw a 楷书 垂露 竖 from (ox, oy_top) down by `length` px.

    Top hook + shaft Bezier + rounded 垂露 disk at the bottom.
    """
    oy_bot = oy_top - length
    bow = 2.0 * scale
    P0 = (ox, oy_top)
    P1 = (ox + bow * 0.5, oy_top - length * 0.30)
    P2 = (ox + bow, oy_top - length * 0.70)
    P3 = (ox, oy_bot)

    draw_top_hook_shu(pil_draw, ox, oy_top, scale)
    brushed_bezier(pil_draw, P0, P1, P2, P3, w_profile_shu, samples=220)
    # Guarantee a fully round 垂露 bottom.
    bx, by = to_px(ox, oy_bot)
    r = 18.0 / 2.0
    pil_draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
