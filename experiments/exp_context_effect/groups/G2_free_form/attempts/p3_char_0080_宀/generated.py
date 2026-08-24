"""Render 宀 (roof radical) to 300x300 PNG.

Structure (3 strokes):
  1. 点 — small dot at top-center, points down/slight-right.
  2. 点 — left descending short stroke (starts left-of-center under
     the lid, flicks down-left).
  3. 横钩 — long horizontal top-lid ending with a hook down on the right.

Uses PIL brush-dab teardrops. Radical fills canvas per GT (lid ~y=150,
hook descends to ~y=210).
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=BLACK)


def teardrop(x0, y0, x1, y1, r0, r1, steps=24):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, max(1.5, r))


# --- Stroke 1: top dot (点) — small teardrop, slight down-right ---
teardrop(148, 95, 158, 128, 3, 6, steps=20)

# --- Stroke 2: left short 点 (short down-left flick under lid's left) ---
teardrop(70, 145, 45, 200, 5, 3, steps=22)

# --- Stroke 3: 横钩 (top-lid horizontal + right hook) ---
hx0, hy0 = 62, 158
hx1, hy1 = 245, 148
n = 70
for i in range(n + 1):
    t = i / n
    x = hx0 + (hx1 - hx0) * t
    y = hy0 + (hy1 - hy0) * t + 2.5 * math.sin(math.pi * t)
    if t < 0.06:
        r = 7 - t * 30
    elif t > 0.94:
        r = 5 + (t - 0.94) * 40
    else:
        r = 4
    dab(x, y, max(3, r))

# 顿 dab at right end (corner before hook)
dab(245, 148, 8)

# Hook: down-left flick from (245, 148) to (228, 205)
teardrop(245, 150, 226, 208, 7, 3, steps=22)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0080_宀/01_宀.png")
print("Wrote 01_宀.png")
