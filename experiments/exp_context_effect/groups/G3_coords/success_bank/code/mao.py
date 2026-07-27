# mao.py — 毛 (máo, fur), 4 strokes.
# Batch B2 (position 135) — human PASSed.
# Inline-fresh 撇 + 2 hengs (with 顿笔 blobs) + bank shu_wan_gou.

import os
import sys

_BANK = os.path.dirname(os.path.abspath(__file__))
if _BANK not in sys.path:
    sys.path.insert(0, _BANK)

from shu_wan_gou import draw_shu_wan_gou  # noqa: E402


def _tapered_line_px(draw, p0, p1, w0, w1, n=24):
    for i in range(n):
        u0 = i / n
        u1 = (i + 1) / n
        x0 = p0[0] + u0 * (p1[0] - p0[0])
        y0 = p0[1] + u0 * (p1[1] - p0[1])
        x1 = p0[0] + u1 * (p1[0] - p0[0])
        y1 = p0[1] + u1 * (p1[1] - p0[1])
        w = w0 + (w1 - w0) * ((u0 + u1) / 2)
        draw.line([(x0, y0), (x1, y1)], fill=(0, 0, 0),
                  width=max(1, int(round(w))))


def _bez_px(draw, p0, pc, p1, w0, w1, n=40):
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * pc[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * pc[1] + u ** 2 * p1[1]
        w = w0 + (w1 - w0) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
        prev = (bx, by)


def draw_mao(t, ox=0.0, oy=0.0, scale=1.0):
    """毛 radical, 4 strokes. PIL pixel coords for inline parts."""
    # Stroke 1: short 撇 at top
    _bez_px(t, (168.0, 78.0), (125.0, 109.0), (98.0, 128.0), 8.0, 1.5)
    # Stroke 2: 短横
    _tapered_line_px(t, (102.0, 130.0), (205.0, 125.0), 7.0, 6.5)
    t.ellipse([201, 121, 209, 129], fill=(0, 0, 0))
    # Stroke 3: 长横
    _tapered_line_px(t, (65.0, 180.0), (220.0, 172.0), 8.0, 7.0)
    t.ellipse([215.5, 167.5, 224.5, 176.5], fill=(0, 0, 0))
    # Stroke 4: 竖弯钩 via bank primitive
    draw_shu_wan_gou(t, ox=5.0, oy=-20.0, scale=1.15)
