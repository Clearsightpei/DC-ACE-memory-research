"""Render 了 (le) at 300x300, black on white.

了 is 2 strokes:
  1. 横撇 top: short horizontal from upper-left, small shoulder turn,
     then a downward-left flick (the 撇 tail).
  2. 弯钩: from just left of the top's shoulder, a long curved vertical
     that bows slightly right then straightens and hooks up-left at
     the bottom.
Silhouette (from GT): the character fills most of the canvas
vertically. Top bar around y=70..95, body descends to y~260, bottom
hook flicks up to about y=225 at x~110.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def stroke(points, r_start, r_end, step=1.0):
    """Brush-dab along polyline points, tapering radius start->end."""
    seglens = []
    total = 0.0
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        L = math.hypot(x1 - x0, y1 - y0)
        seglens.append(L)
        total += L
    if total < 1e-6:
        dab(points[0][0], points[0][1], r_start)
        return
    n = max(2, int(total / step) + 1)
    for k in range(n + 1):
        t = k / n
        target = t * total
        acc = 0.0
        seg = 0
        while seg < len(seglens) and acc + seglens[seg] < target:
            acc += seglens[seg]
            seg += 1
        if seg >= len(seglens):
            x, y = points[-1]
        else:
            local = (target - acc) / seglens[seg]
            x0, y0 = points[seg]
            x1, y1 = points[seg + 1]
            x = x0 + local * (x1 - x0)
            y = y0 + local * (y1 - y0)
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier(p0, p1, p2, p3, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0]
        y = u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


# ---- Stroke 1: 横撇 top ----
# Horizontal from ~(70, 90) with slight up-tilt to shoulder at ~(200, 78).
# The GT top bar tilts up slightly to the right, then a sharp shoulder
# turn, then a short downward-left flick.
top_h = [
    (70, 95),
    (110, 90),
    (150, 85),
    (185, 80),
    (205, 78),
]
stroke(top_h, r_start=6.0, r_end=5.0, step=1.0)
# 顿 at start of horizontal
dab(70, 95, 7)
# shoulder dab (small thick corner)
dab(205, 78, 6.5)

# 撇 flick from shoulder going down-left
pie = bezier(
    (205, 80),
    (204, 92),
    (198, 105),
    (188, 118),
    n=25,
)
stroke(pie, r_start=6.0, r_end=1.5, step=1.0)

# ---- Stroke 2: 弯钩 (long curved body + hook) ----
# From just left of shoulder (~x=175, y=82) descending in a gentle
# right-then-left curve down to ~y=258 near x=145. Then hook flicks
# up-left to ~(105, 228).
shu_start = (178, 82)
shu_end = (148, 258)

body = bezier(
    shu_start,
    (188, 130),  # bow slightly right in upper portion
    (168, 200),  # come back leftward
    shu_end,
    n=70,
)
stroke(body, r_start=6.0, r_end=5.5, step=1.0)
# 顿 at start
dab(shu_start[0], shu_start[1], 7)

# Hook: curve from end of body up and to the left
hook = bezier(
    shu_end,
    (135, 253),
    (118, 242),
    (100, 228),
    n=25,
)
stroke(hook, r_start=5.5, r_end=1.2, step=1.0)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0009_了/01_了.png"
)
