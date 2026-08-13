"""Render 侌 (yīn = 今 over 云) to a 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill=BLACK, width=w)

def poly(points, w=LW):
    d.line(points, fill=BLACK, width=w, joint="curve")

# ============ TOP: 今 (人 roof + horizontal + small hook) ============
# 人 roof — the two diagonals meeting at top-center
# apex around (150, 40); left leg to (95, 105), right leg to (205, 105)
poly([(150, 40), (95, 110)], w=LW)          # left diagonal (撇)
poly([(150, 40), (208, 108)], w=LW)         # right diagonal (捺)

# Horizontal stroke of 今 (a bit shorter than the roof width)
line(105, 118, 200, 118)

# The small hook/dot inside 今 (亠-like inner mark) — a short slanted stroke
poly([(140, 130), (160, 148)], w=LW)

# ============ BOTTOM: 云 (two horizontals + ㄙ) ============
# Top horizontal of 云
line(105, 175, 200, 175)

# Second horizontal (a bit shorter, shifted)
line(115, 200, 195, 200)

# ㄙ shape below: a short down-left stroke then a horizontal, then hook
# stroke going down-left from top
poly([(145, 210), (120, 240)], w=LW)
# horizontal bottom
poly([(120, 240), (185, 245)], w=LW)
# small right hook up
poly([(185, 245), (192, 235)], w=LW)

os.makedirs(os.path.dirname(os.path.abspath(__file__)), exist_ok=True)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_侌.png")
img.save(out)
print("wrote", out)
