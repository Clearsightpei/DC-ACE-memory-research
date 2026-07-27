# shi_pang.py — 饣 (shi-pang, "food" side radical), 3 strokes.
# Batch B1 (position 98) — human PASSed.
#
# Bank pie (compressed) + inlined small 横钩 (bank primitive doesn't
# linearly scale to needed anchor) + bank shu_ti.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from pie import draw_pie        # noqa: E402
from shu_ti import draw_shu_ti  # noqa: E402

_CANVAS = 300


def _apply(x, y, ox, oy, scale):
    """Apply outer (ox, oy, scale) to raw PIL coords centered on 150,150."""
    cx, cy = _CANVAS / 2, _CANVAS / 2
    return (cx + ox + (x - cx) * scale, cy - oy + (y - cy) * scale)


def draw_shi_pang(t, ox=0.0, oy=0.0, scale=1.0):
    """饣 radical: 撇 + small 横钩 + 竖提."""
    # Stroke 1: 撇 (bank pie compressed).
    draw_pie(t, ox=ox + (-22) * scale, oy=oy + 22 * scale, scale=0.55 * scale)

    # Stroke 2: 横钩 inlined (raw PIL coords).
    x0, y0 = 108, 158
    x1, y1 = 178, 165
    w_start = 5
    w_end = 8
    steps = 20
    for i in range(steps):
        t0 = i / steps
        t1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * t0
        ya = y0 + (y1 - y0) * t0
        xb = x0 + (x1 - x0) * t1
        yb = y0 + (y1 - y0) * t1
        w = max(1, int(round((w_start + (w_end - w_start) * t0) * scale)))
        pa = _apply(xa, ya, ox, oy, scale)
        pb = _apply(xb, yb, ox, oy, scale)
        t.line([pa, pb], fill="black", width=w)
    # 顿笔 blob.
    bx, by = _apply(x1, y1, ox, oy, scale)
    br = 5 * scale
    t.ellipse([bx - br, by - br, bx + br, by + br], fill="black")
    # Hook flick.
    hx0, hy0 = x1 + 1, y1 + 1
    hx1, hy1 = x1 - 14, y1 + 25
    hsteps = 12
    for i in range(hsteps):
        t0 = i / hsteps
        t1 = (i + 1) / hsteps
        xa = hx0 + (hx1 - hx0) * t0
        ya = hy0 + (hy1 - hy0) * t0
        xb = hx0 + (hx1 - hx0) * t1
        yb = hy0 + (hy1 - hy0) * t1
        w = max(1, int(round((9 - 8 * t0) * scale)))
        pa = _apply(xa, ya, ox, oy, scale)
        pb = _apply(xb, yb, ox, oy, scale)
        t.line([pa, pb], fill="black", width=w)

    # Stroke 3: 竖提.
    draw_shu_ti(t, ox=ox + (-8) * scale, oy=oy + (-58) * scale, scale=0.38 * scale)
