# bing.py — 冫 (bing) radical, 2 strokes (top dian + bottom slanted 提-like stroke).
# Bootstrap batch (position 44) — human PASSed.
#
# Top uses dian primitive at reduced scale. Bottom is INLINED (per TR5)
# because dian's built-in orientation slants down-right, but 冫's bottom
# slants down-LEFT with a small up-right hook flick.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from dian import draw_dian  # noqa: E402


def _px(cx_ox, cx_oy):
    return 150 + cx_ox, 150 - cx_oy


def _draw_bottom(t, ox, oy, scale):
    """冫's bottom stroke: down-left slanting curve with up-right flick.

    Bezier from (+5,-20) to (-35,-75), ctrl (mid+(2,3)). Width 3→15,
    then a small 10→2 hook up-right to (-25,-68).
    """
    x0, y0 = 5.0 * scale, -20.0 * scale
    x1, y1 = -35.0 * scale, -75.0 * scale
    mx = (x0 + x1) / 2.0 + 2.0 * scale
    my = (y0 + y1) / 2.0 + 3.0 * scale

    n_segments = 40
    th_head, th_tail = 3.0, 15.0
    prev_pt = None
    tail_pt = None
    for i in range(n_segments + 1):
        u = i / n_segments
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _px(ox + bx, oy + by)
        w = th_head * (1 - u) + th_tail * u
        w_int = max(1, int(round(w * scale)))
        if prev_pt is not None:
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w * scale / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)
        tail_pt = (px, py)

    hook_end = _px(ox + (-25.0) * scale, oy + (-68.0) * scale)
    n_hook = 10
    for i in range(1, n_hook + 1):
        u = i / n_hook
        hx = tail_pt[0] + (hook_end[0] - tail_pt[0]) * u
        hy = tail_pt[1] + (hook_end[1] - tail_pt[1]) * u
        w = 10.0 * (1 - u) + 2.0 * u
        w_int = max(1, int(round(w * scale)))
        prev = (
            tail_pt if i == 1
            else (
                tail_pt[0] + (hook_end[0] - tail_pt[0]) * ((i - 1) / n_hook),
                tail_pt[1] + (hook_end[1] - tail_pt[1]) * ((i - 1) / n_hook),
            )
        )
        t.line([prev, (hx, hy)], fill=(0, 0, 0), width=w_int)
        r = w * scale / 2.0
        t.ellipse([hx - r, hy - r, hx + r, hy + r], fill=(0, 0, 0))


def draw_bing(t, ox=0.0, oy=0.0, scale=1.0):
    """冫 radical: dian on top + down-left curved slash with up-right hook."""
    draw_dian(t, ox=ox + 0 * scale, oy=oy + 45 * scale, scale=0.55 * scale)
    _draw_bottom(t, ox=ox, oy=oy, scale=scale)
