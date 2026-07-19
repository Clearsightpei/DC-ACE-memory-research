# zou_zhi.py — 辶 (chuo/zou-zhi) radical, 3 strokes.
# Batch B1 (position 76) — human PASSed.
#
# Bank 点 + inlined 横折折撇 zig-zag + inlined 平捺 (long flat sweep).

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)
from dian import draw_dian  # noqa: E402

_CANVAS = 300


def _to_pixel_scaled(bx, by, ox, oy, scale):
    px = _CANVAS / 2 + ox + bx * scale
    py = _CANVAS / 2 - (oy + by * scale)
    return px, py


def _tapered_bezier(t, x0, y0, mx, my, x1, y1, w_head, w_tail,
                    ox, oy, scale, n=40, belly=None, w_belly=None):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel_scaled(bx, by, ox, oy, scale)
        if belly is not None and w_belly is not None:
            if u <= belly:
                w = w_head + (w_belly - w_head) * (u / belly)
            else:
                w = w_belly + (w_tail - w_belly) * ((u - belly) / (1 - belly))
        else:
            w = w_head + (w_tail - w_head) * u
        w = w * scale
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def _tapered_segment(t, x0, y0, x1, y1, w0, w1, ox, oy, scale, n=20):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = x0 + (x1 - x0) * u
        by = y0 + (y1 - y0) * u
        px, py = _to_pixel_scaled(bx, by, ox, oy, scale)
        w = (w0 + (w1 - w0) * u) * scale
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_zou_zhi(t, ox=0.0, oy=0.0, scale=1.0):
    """辶 radical: 点 top-left + zig-zag under it + long flat 平捺."""
    # Stroke 1: 点.
    draw_dian(t, ox=ox + (-50) * scale, oy=oy + 90 * scale, scale=0.7 * scale)

    # Stroke 2: 横折折撇 zig-zag.
    A = (-80.0, 20.0)
    B = (-40.0, 15.0)
    C = (-75.0, -20.0)
    D = (-40.0, -55.0)
    _tapered_segment(t, A[0], A[1], B[0], B[1], 5, 6, ox, oy, scale, n=18)
    _tapered_bezier(t,
                    B[0], B[1],
                    B[0] + 5, (B[1] + C[1]) / 2 + 4,
                    C[0], C[1],
                    6, 7, ox, oy, scale, n=30)
    _tapered_bezier(t,
                    C[0], C[1],
                    (C[0] + D[0]) / 2 - 6, (C[1] + D[1]) / 2 - 2,
                    D[0], D[1],
                    7, 3, ox, oy, scale, n=30)

    # Stroke 3: 平捺.
    x0, y0 = -95.0, -55.0
    x1, y1 = 105.0, -100.0
    mx = (x0 + x1) / 2.0 + 5
    my = (y0 + y1) / 2.0 - 12
    _tapered_bezier(t, x0, y0, mx, my, x1, y1,
                    w_head=3, w_tail=2,
                    ox=ox, oy=oy, scale=scale,
                    n=70, belly=0.6, w_belly=10)
