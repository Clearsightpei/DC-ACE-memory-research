"""Render 话 (huà) at 300x300 using PIL.
Structure: 讠 (left, speech radical) + 舌 (right = 千 over 口).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

def polyline(pts, w=LW):
    d.line(pts, fill=BLACK, width=w)

# ---------------- LEFT: 讠 (speech radical) ----------------
# 1) Top dot (点) — short slanted diagonal
polyline([(70, 70), (88, 92)], w=5)

# 2) The 折 stroke: horizontal top going into vertical going down with slight left curve then small hook right.
# We render as a connected polyline mimicking 乛 into 亅.
polyline([(60, 130), (95, 118), (85, 145), (78, 210), (100, 215)], w=LW)

# ---------------- RIGHT: 舌 ----------------
# 千 top:
#   a) 撇 (left-falling slant) from upper-right to center-left
polyline([(215, 65), (155, 110)], w=LW)
#   b) long horizontal (top bar of 舌) — extends across
polyline([(140, 115), (275, 115)], w=LW)
#   c) vertical (丨) going down through the character center
polyline([(205, 100), (205, 215)], w=LW)

# Second horizontal of 舌 (middle bar, shorter)
polyline([(165, 160), (255, 160)], w=LW)

# ---------------- 口 at bottom-right ----------------
x1, y1, x2, y2 = 160, 215, 255, 265
# Top: horizontal (part of horizontal stroke of top of 口, and starts with left vertical)
polyline([(x1, y1), (x2, y1)], w=LW)          # top horizontal
polyline([(x1, y1), (x1, y2)], w=LW)          # left vertical
polyline([(x2, y1), (x2, y2)], w=LW)          # right vertical (turn from top)
polyline([(x1, y2), (x2, y2)], w=LW)          # bottom horizontal (closing seal)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0389_话/01_话.png")
print("saved")
