"""可 (kě) — 5 strokes.

Stroke order (MMH standard):
  1. 横 — long top bar across the character
  2. 竖 — left vertical of the 口 (upper-left region)
  3. 横折 — top+right of 口 (short horizontal then turn down)
  4. 横 — bottom of 口 (closing it)
  5. 竖钩 — long vertical starting from the top bar (right side),
     descending well below 口, then hooking UP-and-LEFT
     (per TIER-0 B: hook flicks into the character body, ~-105°)

Layout (300x300 canvas):
  - Top 横: y≈75, x from ~55 to ~245
  - 口: upper-left, occupies x≈60..145, y≈75..165
  - 竖钩 stem: x≈195, y from 75 down to ~245, then hook flicks
    up-left to end near (170, 230)
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=7):
    draw.line(points, fill=BLACK, width=width, joint="curve")
    # end caps
    for (x, y) in [points[0], points[-1]]:
        r = width / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# 1. 横 — top horizontal, slight rise to the right (calligraphic tilt)
stroke([(45, 85), (150, 78), (255, 72)], width=9)

# 2. 竖 — left side of 口 (starts just below the top bar)
stroke([(75, 95), (74, 175)], width=8)

# 3. 横折 — top of 口 (short horizontal) then turn down (right side of 口)
stroke([(74, 98), (150, 96), (148, 178)], width=8)

# 4. 横 — bottom of 口, closing it
stroke([(75, 175), (150, 178)], width=8)

# 5. 竖钩 — long vertical from top bar, then hook UP-and-LEFT
# Starts on top bar (right of 口), descends far below, hooks back
stroke(
    [
        (200, 80),   # start on the top bar
        (198, 150),
        (196, 220),
        (194, 258),  # bottom of stem
        (180, 250),  # hook flicks up-and-LEFT (into body, ~-110°)
        (165, 240),
        (155, 232),
    ],
    width=9,
)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0160_可/01_可.png"
)
print("saved 01_可.png")
