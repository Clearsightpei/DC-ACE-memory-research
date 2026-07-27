"""Render 八 (bā) to a 300x300 PNG.

Two strokes:
  - Left: 撇 (piě) — slanting downstroke from upper-middle to lower-left,
    slight curve, tapering to a fine tail.
  - Right: 捺 (nà) — slanting downstroke from upper (near top of piě)
    to lower-right, thicker with a slight curve and a broader end.

Uses PIL to draw smooth curves with variable width by stamping circles
along parametric paths.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stamp(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke(points_fn, t_start=0.0, t_end=1.0, steps=200, width_fn=None):
    """Draw a stroke by stamping circles along a parametric curve."""
    prev = None
    for i in range(steps + 1):
        t = t_start + (t_end - t_start) * i / steps
        x, y = points_fn(t)
        r = width_fn(t) if width_fn else 4
        stamp(x, y, r)
        if prev is not None:
            # fill gaps by interpolation
            px, py = prev
            dist = math.hypot(x - px, y - py)
            if dist > 1:
                nseg = int(dist) + 1
                for k in range(1, nseg):
                    fx = px + (x - px) * k / nseg
                    fy = py + (y - py) * k / nseg
                    stamp(fx, fy, r)
        prev = (x, y)


# --- 撇 (left stroke): shorter, curving from ~(110, 130) to ~(70, 235) ---
# Sits to the left, does NOT reach the top of 捺; clear gap between strokes.
def pie(t):
    p0 = (110, 130)
    p1 = (95, 190)
    p2 = (72, 240)
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return x, y


def pie_width(t):
    # thick at top, tapered at tail (piě tapers to a point)
    return max(1.2, 5.0 - 4.0 * t)


# --- 捺 (right stroke): taller, from ~(160, 80) sweeping to ~(260, 250) ---
# Starts higher & further right than piě's top, giving a visible gap.
def na(t):
    p0 = (162, 80)
    p1 = (195, 155)
    p2 = (262, 250)
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return x, y


def na_width(t):
    # thin at start, thickens through the belly, then slight taper into a broad end
    return 2.5 + 3.8 * math.sin(math.pi * min(1.0, 0.15 + 0.85 * t))


stroke(pie, width_fn=pie_width)
stroke(na, width_fn=na_width)

out = os.path.join(os.path.dirname(__file__), "01_八.png")
img.save(out)
print(f"Wrote {out}")
