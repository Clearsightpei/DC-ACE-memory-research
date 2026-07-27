# generated.py — 毋 (wú), 4-stroke radical (revised).
# G3 coord-bank format: callable draw_wu(t, ox, oy, scale).
# Revision from pass-1: lighter strokes, tighter envelope corner, longer
# upper 撇 that visibly cuts through the top-right of the envelope
# (this is what distinguishes 毋 from 母/毌), thinner crossing bar.

import os
from PIL import Image, ImageDraw

INK = (0, 0, 0)


def _tapered_line(draw, p0, p1, w0, w1, steps=40):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        u = i / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def _tapered_bezier(draw, p0, p1, p2, w0, w1, steps=60):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * x1 + u ** 2 * x2
        y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * y1 + u ** 2 * y2
        w = w0 + (w1 - w0) * u
        r = w / 2.0
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def _dot_blob(draw, cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=INK)


def draw_wu(t, ox=0.0, oy=0.0, scale=1.0):
    """毋 radical (4 strokes). PIL pixel coords, canvas 300x300."""
    def P(x, y):
        return (x + ox, y + oy)

    # Stroke 1: 撇 — long slanting stroke from upper-right area sweeping
    # down and to the left; passes through/across the top of the envelope.
    # This is the visual marker of 毋 vs 母.
    _tapered_bezier(t, P(195, 72), P(160, 100), P(105, 135),
                    w0=7.0, w1=1.5)

    # Stroke 2: 横折钩 — top horizontal + right descending wall + tiny hook.
    # Top segment (slight downward slope)
    _tapered_line(t, P(80, 100), P(222, 108), 6.5, 7.5)
    # Corner 顿笔
    _dot_blob(t, 222 + ox, 108 + oy, 5)
    # Right wall descending (slight lean left as it goes down)
    _tapered_line(t, P(222, 108), P(212, 232), 8.0, 7.0)
    # Small hook at bottom of right wall pointing up-left
    _tapered_line(t, P(212, 232), P(200, 224), 7.0, 3.0)

    # Stroke 3: 竖折 — left wall + bottom base (drawn as one stroke).
    # Left wall descending (slight rightward lean toward the bottom)
    _tapered_line(t, P(82, 108), P(75, 238), 7.5, 8.0)
    # Bottom base sweeping right, gently curving
    _tapered_bezier(t, P(75, 238), P(140, 245), P(212, 233),
                    w0=8.0, w1=7.0)

    # Stroke 4: 横 — long crossing bar extending beyond both sides.
    _tapered_line(t, P(52, 172), P(248, 176), 6.0, 7.0)
    # Small 顿笔 at right end
    _dot_blob(t, 248 + ox, 176 + oy, 4)


if __name__ == "__main__":
    img = Image.new("RGB", (300, 300), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_wu(draw)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "01_毋.png")
    img.save(out)
    print("wrote", out)
