"""Render 切 to a 300x300 PNG using PIL. Revision 2."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

def polyline(points, w=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=BLACK, width=w)

# 切 = 七 (left) + 刀 (right), 4 strokes total.
# Left component 七: 1) horizontal, 2) vertical-curve-with-hook (竖弯钩)
# Right component 刀: 3) 横折钩, 4) 撇
# GT positions: center around y~110-230, x-split around 140.

# ---- Left 七 ----
# Stroke 1: horizontal, slightly rising to the right
polyline([(55, 145), (135, 138)], w=LW)

# Stroke 2: starts above the horizontal on right side, goes down-left through the
# horizontal, curves down and then hooks up to the right (竖弯钩)
pts_s2 = [
    (108, 115),  # top-right start
    (95, 135),   # crossing near horizontal center
    (78, 165),
    (72, 195),
    (78, 220),   # bottom curve begins
    (95, 235),
    (125, 235),  # bottom-right
    (140, 225),  # small hook up
]
polyline(pts_s2, w=LW)

# ---- Right 刀 ----
# Stroke 3: 横折钩. Short horizontal at top-right, turn down, long descent curving
# slightly right, end with small hook toward upper-left at bottom.
pts_s3 = [
    (155, 115),  # start of horizontal
    (235, 108),  # end horizontal
    (232, 140),  # corner turn down
    (222, 180),
    (215, 220),
    (208, 240),  # bottom
    (192, 232),  # hook up-left
]
polyline(pts_s3, w=LW)

# Stroke 4: 撇, long diagonal sweep from inside-top of 刀 down to lower-left
pts_s4 = [
    (190, 138),  # start upper-inside
    (178, 175),
    (162, 215),
    (148, 250),
    (140, 268),  # tail
]
polyline(pts_s4, w=LW)

out = os.path.join(os.path.dirname(__file__), "01_切.png")
img.save(out)
print(f"Saved {out}")
