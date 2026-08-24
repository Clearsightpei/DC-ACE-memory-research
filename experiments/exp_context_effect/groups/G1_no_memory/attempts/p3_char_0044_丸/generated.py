"""Render 丸 (wan) - 3 strokes: 撇, 横斜钩(with turn), 点"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 5

# Stroke 1: 撇 - long diagonal from upper area sweeping down-left
# Start at upper-middle-right, sweep to lower-left
draw.line([(175, 60), (60, 230)], fill=INK, width=LW)

# Stroke 2: 横斜钩 (the main body of 丸)
# It's a horizontal then a long curve that goes down-right then hooks up
# horizontal top segment (short)
draw.line([(130, 110), (210, 105)], fill=INK, width=LW)
# From right end of horizontal, a long curve going down and to the right,
# then curving back left at the bottom, ending with a small upward hook
# Approximate with a smooth polyline
pts = []
# curve from (210, 105) going down-right, bowing outward, then bottom sweep left, hook up
# Parametric: use quadratic-ish approximation
# Segment: down-right bulge to bottom-right then sweep left, ending hook up
curve_points = [
    (210, 105),
    (222, 140),
    (235, 180),
    (240, 220),
    (230, 245),
    (205, 258),
    (170, 258),
    (140, 245),
]
for i in range(len(curve_points)-1):
    draw.line([curve_points[i], curve_points[i+1]], fill=INK, width=LW)
# hook up at end
draw.line([(140, 245), (135, 225)], fill=INK, width=LW)

# Stroke 3: 点 - small dot inside body (lower-middle area)
draw.line([(150, 190), (170, 215)], fill=INK, width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0044_丸/01_丸.png")
print("saved")
