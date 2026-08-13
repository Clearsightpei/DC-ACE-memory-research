"""Render 冱 (hu4 - freeze) — left: 冫 (ice), right: 互 (mutual)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=7):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- LEFT: 冫 (ice, two dots) ----
# upper dot (going down-left, thicker)
stroke([(65, 105), (48, 130)], width=8)
# lower dot / 提 (going up-right)
stroke([(50, 195), (78, 175)], width=8)

# ---- RIGHT: 互 ----
# Stroke 1: top horizontal
stroke([(115, 90), (255, 88)], width=7)

# Stroke 2: middle Z (one continuous stroke)
# starts top-right, goes down as small vertical, then left as horizontal, then down
# right-vertical from top-right area down to middle
stroke([(240, 92), (235, 155)], width=7)
# middle horizontal (from right going left)
stroke([(238, 158), (130, 160)], width=7)
# left-vertical down from middle to bottom
stroke([(133, 158), (128, 232)], width=7)

# Stroke 3: bottom horizontal (long)
stroke([(110, 240), (272, 235)], width=7)

out = os.path.join(os.path.dirname(__file__), "01_冱.png")
img.save(out)
print("wrote", out)
