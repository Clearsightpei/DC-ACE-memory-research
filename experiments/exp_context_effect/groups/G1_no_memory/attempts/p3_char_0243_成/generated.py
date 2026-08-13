"""Render 成 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(pts, width=LW):
    d.line(pts, fill="black", width=width, joint="curve")

# 成 - 6 strokes

# Stroke 1: short 撇 at upper-left (small left-falling)
line([(105, 75), (95, 100), (85, 130)])

# Stroke 2: 横折 - short horizontal top, then curve down (left part of body)
# horizontal
line([(100, 100), (160, 95)])
# curved vertical descending
line([(160, 95), (155, 135), (145, 175), (130, 215), (115, 245)])

# Stroke 3: 斜钩 (main slanting hook) - from top down to lower right, with hook
line([(140, 65), (160, 95), (185, 135), (215, 180), (245, 225), (265, 255)])
# hook at end (upward flick)
line([(265, 255), (280, 235)])

# Stroke 4: 撇 inside - short diagonal down-left across middle
line([(185, 140), (165, 170), (140, 200), (120, 220)])

# Stroke 5: short horizontal inside (crossing 撇 area)
line([(115, 155), (185, 148)])

# Stroke 6: 点 (dot) at upper right, small diagonal
line([(210, 75), (235, 95)], width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0243_成/01_成.png")
print("saved")
