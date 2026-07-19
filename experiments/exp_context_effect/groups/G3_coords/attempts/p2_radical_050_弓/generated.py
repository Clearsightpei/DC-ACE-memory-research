# p2_radical_050_弓 — G3 coord-bank attempt
#
# 弓 is 3画:
#   1) 横折 — top: short horizontal then bend down
#   2) 横   — middle horizontal (slightly longer than top)
#   3) 竖折折钩 — bottom: short vertical → horizontal right → down (with slight
#       bow) → hook flicks UP-and-LEFT
#
# The composition is three horizontally-aligned stroke groups stacked
# vertically. Left edges of all three roughly align. The middle 横 is
# the widest; the bottom sweep extends slightly rightward and dives down
# to hook back.
#
# Coord convention: math coords, center origin, +y up. Converted via
# _to_pixel to PIL 300x300.

import os
from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _stroke_line(t, p0, p1, w0, w1, steps=40):
    """Stamped-circle taper from p0 to p1 with width w0 -> w1."""
    x0, y0 = _to_pixel(*p0)
    x1, y1 = _to_pixel(*p1)
    for i in range(steps + 1):
        u = i / steps
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        w = w0 + (w1 - w0) * u
        r = max(0.5, w / 2)
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _stroke_bezier(t, p0, p1, p2, w0, w1, steps=60):
    """Quadratic bezier tapered line from p0 through control p1 to p2."""
    x0, y0 = _to_pixel(*p0)
    xc, yc = _to_pixel(*p1)
    x2, y2 = _to_pixel(*p2)
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * xc + u * u * x2
        y = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * yc + u * u * y2
        w = w0 + (w1 - w0) * u
        r = max(0.5, w / 2)
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def draw_gong(t):
    """Draw 弓 on the given ImageDraw t at canvas center.

    Three strokes. Approximate math-coord anchors:
      Stroke 1 (横折 top):
        head (-45, +85) → corner (+35, +80) → tail (+30, +50)
      Stroke 2 (横 middle):
        left (-50, +18) → right (+40, +18)
      Stroke 3 (竖折折钩 bottom):
        head (-50, -20) → right corner (+40, -25) → down to (+35, -85)
        → sweep-and-hook up-left to (-55, -70) with a slight downward bow,
        then hook flicks up-and-left to (-40, -50).
    """
    # ---- Stroke 1: 横折 (top) ----------------------------------------
    # short horizontal top, then bend down
    _stroke_line(t, (-45, 85), (35, 82), w0=8, w1=9)
    # small 顿笔 blob at the corner
    cx1, cy1 = _to_pixel(35, 82)
    t.ellipse([cx1 - 5, cy1 - 5, cx1 + 5, cy1 + 5], fill=(0, 0, 0))
    # short vertical drop after the fold
    _stroke_line(t, (33, 80), (30, 48), w0=9, w1=7)

    # ---- Stroke 2: 横 (middle) --------------------------------------
    # horizontal, slightly wider than top; roughly at y=18
    _stroke_line(t, (-50, 20), (42, 18), w0=8, w1=9)

    # ---- Stroke 3: 竖折折钩 (bottom) --------------------------------
    # Head starts left, horizontal sweep right, dive down deeply, curve
    # back leftward along the bottom, end with a hook that flicks
    # UP-and-LEFT (clearly visible tapered flick).
    #
    # Segment A: horizontal top of bottom group
    _stroke_line(t, (-50, -20), (40, -22), w0=8, w1=9)
    # Segment B: 顿笔 blob at right corner (fold)
    cx2, cy2 = _to_pixel(40, -22)
    t.ellipse([cx2 - 5, cy2 - 5, cx2 + 5, cy2 + 5], fill=(0, 0, 0))
    # Segment C: descending arc — down first (short), then curves back
    # leftward along the base. Bezier for smooth sweep. Push the tail
    # further down and further left so the hook has real room.
    _stroke_bezier(
        t,
        p0=(38, -24),        # top of the drop
        p1=(35, -95),        # control: pulled well below to make the descent taller
        p2=(-30, -100),      # tail: sweeps back leftward, deeper down
        w0=9, w1=7,
    )
    # Segment D: the hook — a distinctly tapered flick UP-and-LEFT.
    # Anchor at the arc tail; tip lifts noticeably above tail (higher y).
    _stroke_line(t, (-30, -100), (-52, -70), w0=8, w1=1)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), "white")
    t = ImageDraw.Draw(img)
    draw_gong(t)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "01_弓.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
