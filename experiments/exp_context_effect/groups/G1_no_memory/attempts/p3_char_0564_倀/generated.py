"""Render 倀 (person + long) at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=5):
    d.line(pts, fill="black", width=w, joint="curve")

# ============ Left: 亻 (person radical) ============
# Slanted top piě
line([(78, 55), (45, 135)], w=6)
# Vertical shù (ends around 2/3 down, not bottom)
line([(72, 105), (72, 240)], w=6)

# ============ Right: 長 (long) ============
# Body x range roughly 105..270

# Top horizontal
line([(135, 70), (245, 68)], w=5)
# Second horizontal
line([(150, 108), (250, 106)], w=5)
# Third horizontal
line([(145, 145), (255, 143)], w=5)
# Left vertical from top down through the horizontals
line([(160, 55), (155, 175)], w=5)
# Long wide horizontal (middle-bottom)
line([(110, 182), (260, 180)], w=5)

# Bottom section (like 衣-like legs of 長)
# Left short piě descending
line([(165, 182), (135, 245)], w=5)
# Small internal tick/dot
line([(180, 200), (200, 220)], w=5)
# Long right nà sweeping to lower-right
line([(205, 182), (285, 270)], w=6)

out = os.path.join(os.path.dirname(__file__), "01_倀.png")
img.save(out)
print("wrote", out)
