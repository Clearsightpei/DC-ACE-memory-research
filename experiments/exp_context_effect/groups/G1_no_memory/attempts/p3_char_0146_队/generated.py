"""Render 队 using PIL. 300x300, white background, black ink.
队 = 阝 (left) + 人 (right).
阝: an angular ear-shape (2 strokes: horizontal-fold + vertical descending).
人: two strokes meeting at the top (撇 left-fall + 捺 right-fall).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def curve(points, width=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=BLACK, width=width)
    for p in points:
        d.ellipse([p[0]-width/2, p[1]-width/2, p[0]+width/2, p[1]+width/2], fill=BLACK)

# ---------- LEFT: 阝 (positioned upper-left, shorter than the 人) ----------
# Stroke 1: 横折折折钩/耳刀 — starts upper-left going right, drops down, right, down,
# forming an angular loop that closes back to the vertical.
ear = [
    (60, 95),   # start upper-left
    (95, 92),   # go right along top
    (108, 105), # turn down (small corner)
    (110, 128), # descend
    (95, 145),  # curve back left along bottom of the "loop"
    (75, 148),  # meet the vertical
]
curve(ear)

# Stroke 2: 长竖 — long vertical descending, starts at top-left of ear and goes down
vert = [(72, 95), (70, 150), (68, 210), (66, 260)]
curve(vert)

# ---------- RIGHT: 人 ----------
# Both strokes meet at a peak near top-center-right
peak = (210, 100)

# Stroke 1: 撇 — from peak going down-left, slight curve
pie = [peak, (200, 130), (185, 165), (165, 205), (140, 250)]
curve(pie)

# Stroke 2: 捺 — from peak going down-right, curving to a flatter tail
na = [peak, (222, 135), (240, 175), (260, 215), (282, 250)]
curve(na)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0146_队/01_队.png")
print("saved")
