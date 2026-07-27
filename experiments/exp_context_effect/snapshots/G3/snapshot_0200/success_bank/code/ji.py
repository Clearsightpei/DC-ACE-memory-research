# ji.py — 几 (ji) radical, 2 strokes (撇 + 横折弯钩).
# Batch B1 (position 54) — human PASSed.
#
# Both strokes are inlined bezier curves — bank primitives don't match
# 几's nearly-vertical 撇 or its compound 横折弯钩 with rightward-sweep hook.
# All coords below are raw PIL pixels for the standalone 300x300 canvas;
# an outer (ox, oy, scale) is applied on top.

import os
import sys
from PIL import ImageDraw  # noqa: F401

_CANVAS = 300


def _apply(x, y, ox, oy, scale):
    """Apply outer (ox, oy, scale) around the raw-PIL recipe.
    Recipe was authored assuming canvas center = (150, 150). We scale
    around that center then translate."""
    cx, cy = _CANVAS / 2, _CANVAS / 2
    return (cx + ox + (x - cx) * scale, cy - oy + (y - cy) * scale)


def _tapered_bezier(draw, p0, p1, p2, w0, w1, ox, oy, scale, steps=60):
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        px, py = _apply(bx, by, ox, oy, scale)
        w = (w0 + (w1 - w0) * u) * scale
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _tapered_line(draw, p0, p1, w0, w1, ox, oy, scale, steps=40):
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = p0[0] + u0 * (p1[0] - p0[0])
        ya = p0[1] + u0 * (p1[1] - p0[1])
        xb = p0[0] + u1 * (p1[0] - p0[0])
        yb = p0[1] + u1 * (p1[1] - p0[1])
        pa = _apply(xa, ya, ox, oy, scale)
        pb = _apply(xb, yb, ox, oy, scale)
        w = max(1, int(round((w0 + (w1 - w0) * ((u0 + u1) / 2)) * scale)))
        draw.line([pa, pb], fill=(0, 0, 0), width=w)


def draw_ji(t, ox=0.0, oy=0.0, scale=1.0):
    """几 radical: nearly-vertical 撇 + 横折弯钩 as one continuous stroke."""
    # 撇: head (135,95), tail (75,250), ctrl (108,180).
    _tapered_bezier(t, (135.0, 95.0), (108.0, 180.0), (75.0, 250.0),
                    11, 2, ox, oy, scale, steps=60)

    # 横折弯钩:
    # A. Horizontal top from (135,95) to (215,95).
    _tapered_line(t, (135.0, 95.0), (215.0, 95.0),
                  10, 12, ox, oy, scale, steps=24)
    # 顿笔 blob at top-right.
    cx, cy = _apply(215.0, 95.0, ox, oy, scale)
    r = 6 * scale
    t.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))
    # B. Vertical descent with slight leftward bow.
    _tapered_bezier(t, (215.0, 95.0), (208.0, 170.0), (205.0, 245.0),
                    12, 11, ox, oy, scale, steps=40)
    # C. 弯 curve at bottom sweeping right.
    _tapered_bezier(t, (205.0, 245.0), (225.0, 262.0), (245.0, 260.0),
                    11, 10, ox, oy, scale, steps=30)
    # Blob at hook base.
    hx, hy = _apply(245.0, 260.0, ox, oy, scale)
    r = 5 * scale
    t.ellipse([hx - r, hy - r, hx + r, hy + r], fill=(0, 0, 0))
    # D. Upward hook.
    _tapered_line(t, (245.0, 260.0), (240.0, 232.0),
                  10, 2, ox, oy, scale, steps=16)
