"""Render 佇 (person radical + 宁) at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 6

def line(pts, width=LW):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- Left: 亻 (person radical) ----
# Slanted stroke (撇) from upper-mid-left down to lower-left
line([(85, 70), (50, 220)], width=7)
# Vertical stroke (竖) starting mid-way on the slant, going straight down
line([(78, 115), (78, 250)], width=7)

# ---- Right: 宁 ----
# Top dot (点) - short slanted stroke on top center
line([(195, 50), (205, 78)], width=7)

# Horizontal roof (横) with slight curve, wide across
line([(135, 105), (260, 100)], width=7)
# Left hook of roof (short slant down-left from left end)
line([(135, 105), (125, 130)], width=7)
# Right hook of roof (curving down from right end, longer)
line([(260, 100), (255, 140)], width=7)

# Middle horizontal (top of 丁)
line([(145, 170), (250, 165)], width=7)

# Vertical hook (亅) - straight down then curl left at bottom
line([(200, 170), (200, 245), (180, 240)], width=7)

out = os.path.join(os.path.dirname(__file__), "01_佇.png")
img.save(out)
print("Saved:", out)
