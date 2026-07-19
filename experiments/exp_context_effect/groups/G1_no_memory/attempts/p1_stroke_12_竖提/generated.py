"""
G1 no-memory attempt: p1_stroke_12_竖提 (vertical-then-rising ti).

The stroke goes:
  1. Straight down (竖) - a vertical stroke, slight thickening near
     the top and thinning at the bottom-hook pivot.
  2. Sharp hook to the upper right (提) - a short rising flick.

Rendered with PIL at exactly 300x300, white background, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# ---- Part 1: the vertical (竖) ----
# Slight rightward lean is common; we keep it near-vertical.
# Top thicker, bottom thinner (calligraphic taper).
top = (150, 60)
bot = (150, 210)

# Simulate a tapered brushstroke by stacking short line segments
# with decreasing width from top (~14 px) to bottom (~8 px).
N = 40
for i in range(N):
    t0 = i / N
    t1 = (i + 1) / N
    x0 = top[0] + (bot[0] - top[0]) * t0
    y0 = top[1] + (bot[1] - top[1]) * t0
    x1 = top[0] + (bot[0] - top[0]) * t1
    y1 = top[1] + (bot[1] - top[1]) * t1
    w = 14 - (14 - 8) * t0  # taper from 14 -> 8
    draw.line([(x0, y0), (x1, y1)], fill="black", width=int(round(w)))

# ---- Part 2: the rising ti (提) ----
# From the bottom of the vertical, flick up-right.
# Starts thick, tapers to a point.
start = (150, 210)
end = (230, 165)

M = 30
for i in range(M):
    t0 = i / M
    t1 = (i + 1) / M
    x0 = start[0] + (end[0] - start[0]) * t0
    y0 = start[1] + (end[1] - start[1]) * t0
    x1 = start[0] + (end[0] - start[0]) * t1
    y1 = start[1] + (end[1] - start[1]) * t1
    w = 10 - (10 - 2) * t0  # taper from 10 -> 2 (pointed tip)
    draw.line([(x0, y0), (x1, y1)], fill="black", width=max(1, int(round(w))))

# Round the joint where 竖 meets 提 so it looks like one brush motion.
draw.ellipse([(150 - 6, 210 - 6), (150 + 6, 210 + 6)], fill="black")

out = __file__.rsplit("/", 1)[0] + "/01_竖提.png"
img.save(out)
print(f"Saved {out}")
