"""Render 不 (p3_char_0094) — 4 strokes.

Structure (from GT):
  1. 横 — long top horizontal, spans most of width, slight upward slope.
  2. 撇 — from just below middle of 横, sweeps down-left to bottom-left.
  3. 竖 — from center of 横 down to bottom-middle (short-medium).
  4. 点 — small dot to right of the 竖, at mid-lower level.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(points, width=8):
    d.line(points, fill=BLACK, width=width, joint="curve")
    # cap
    r = width // 2
    for (x, y) in [points[0], points[-1]]:
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)

def taper(points, w_start, w_end, steps=None):
    if steps is None:
        steps = max(len(points) - 1, 20)
    # resample along polyline
    # compute cumulative length
    import math
    lens = [0.0]
    for i in range(1, len(points)):
        x0, y0 = points[i - 1]
        x1, y1 = points[i]
        lens.append(lens[-1] + math.hypot(x1 - x0, y1 - y0))
    total = lens[-1]
    if total == 0:
        return
    def at(t):
        target = t * total
        for i in range(1, len(lens)):
            if lens[i] >= target:
                seg = lens[i] - lens[i - 1]
                u = 0 if seg == 0 else (target - lens[i - 1]) / seg
                x0, y0 = points[i - 1]
                x1, y1 = points[i]
                return (x0 + u * (x1 - x0), y0 + u * (y1 - y0))
        return points[-1]
    prev = at(0)
    for i in range(1, steps + 1):
        t = i / steps
        cur = at(t)
        w = w_start + (w_end - w_start) * t
        d.line([prev, cur], fill=BLACK, width=int(round(w)))
        r = max(int(round(w / 2)), 1)
        d.ellipse([cur[0] - r, cur[1] - r, cur[0] + r, cur[1] + r], fill=BLACK)
        prev = cur


# Stroke 1: 横 — long top horizontal, very slight upward tilt to right,
# small terminal thickening (顿笔) at the right end.
heng = [(38, 92), (100, 84), (180, 78), (255, 82)]
taper(heng, 7, 10)

# Stroke 2: 撇 — starts just under 横 near center, sweeps down-left,
# tapers thin. Long curve.
pie = [(148, 100), (125, 145), (95, 195), (60, 245), (38, 278)]
taper(pie, 11, 3)

# Stroke 3: 竖 — from same joint area, straight down.
shu = [(158, 108), (158, 165), (158, 225), (158, 275)]
taper(shu, 9, 8)

# Stroke 4: 点 — short diagonal dot on right side, mid-lower, down-right.
dian = [(200, 185), (218, 210), (235, 232)]
taper(dian, 4, 11)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0094_不/01_不.png")
