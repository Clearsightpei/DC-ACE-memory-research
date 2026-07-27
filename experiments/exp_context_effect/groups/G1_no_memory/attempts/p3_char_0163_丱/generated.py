"""Render 丱 (guan) at 300x300 using PIL.

GT observation: symmetric character. Each half looks like a small hooked
shape in the upper-middle (a short stroke that curls into a J-like hook)
with a long vertical stroke passing through it descending to the bottom.
Left half mirrors right half.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

def curve(points, w=LW):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=BLACK, width=w)

# ---- LEFT HALF ----
# Long vertical (slight lean left as descends): top~30 down to bottom~275
left_vert = [(110, 30), (105, 100), (100, 175), (95, 250), (92, 278)]
curve(left_vert)

# Left "knot" — a short stroke that comes in from upper-left and hooks around,
# shaped like a small レ (angle then curl right)
# Start upper-left, go down-right, then curl up-right forming a small loop opening right
left_knot = [
    (55, 105),   # start upper-left
    (65, 125),
    (75, 145),
    (90, 155),   # bottom of the curl
    (100, 150),  # curl up
    (108, 140),  # hook tip
]
curve(left_knot)

# ---- RIGHT HALF (mirror) ----
right_vert = [(190, 30), (195, 100), (200, 175), (205, 250), (208, 278)]
curve(right_vert)

right_knot = [
    (245, 105),
    (235, 125),
    (225, 145),
    (210, 155),
    (200, 150),
    (192, 140),
]
curve(right_knot)

out_path = os.path.join(os.path.dirname(__file__), "01_丱.png")
img.save(out_path)
print(f"Saved: {out_path}")
