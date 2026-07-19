"""
p2_radical_067_士 — retry_1

Fix from errata: prior attempt had TOP 横 shorter than BOTTOM (reading as 土).
Canonical 士: TOP 横 is LONGER than BOTTOM 横 (~150 vs ~110 px).

Structure (3 strokes):
  1. Top 横 — LONG (~150 px), roughly y=110
  2. Bottom 横 — SHORT (~110 px), roughly y=205
  3. Vertical passes through both, centered

PIL brush-dab renderer, 300x300 white canvas, black ink.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_seg(x0, y0, x1, y1, r0, r1, steps=None):
    dx, dy = x1 - x0, y1 - y0
    dist = math.hypot(dx, dy)
    if steps is None:
        steps = max(int(dist * 3), 40)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# Center x
CX = 150

# --- Stroke 1: TOP 横 (LONG, ~170 px) — dominant top bar ---
# slight up-tilt
top_y_left = 92
top_y_right = 85
top_x_left = CX - 85   # x=65
top_x_right = CX + 85  # x=235
# subtle start dab (standalone: r+1 max)
dab(top_x_left, top_y_left, 6)
line_seg(top_x_left, top_y_left, top_x_right, top_y_right, 5, 5)
dab(top_x_right, top_y_right, 6)

# --- Stroke 2: VERTICAL 竖 through both horizontals, spread longer ---
v_top = 92
v_bottom = 218
dab(CX, v_top, 6)
line_seg(CX, v_top, CX, v_bottom, 5, 5)
dab(CX, v_bottom, 5)

# --- Stroke 3: BOTTOM 横 (SHORT, ~100 px) ---
bot_y_left = 218
bot_y_right = 213
bot_x_left = CX - 50   # x=100
bot_x_right = CX + 50  # x=200
dab(bot_x_left, bot_y_left, 6)
line_seg(bot_x_left, bot_y_left, bot_x_right, bot_y_right, 5, 5)
dab(bot_x_right, bot_y_right, 6)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_067_士__retry_1/01_士.png"
)
