"""Render 仫 = 亻 (left) + 厶 (right)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- 亻 (person radical) on the left ----
# 撇 piě
stroke([(95, 70), (75, 130), (55, 180)], width=6)
# 竖 vertical
stroke([(85, 135), (85, 275)], width=6)

# ---- 厶 on the right ----
# Stroke 1: 撇折 (piě-zhé) - starts upper, slants down-left, folds to right
stroke([(210, 110), (175, 165), (215, 170)], width=6)
# Stroke 2: 点 (dot / short slant down-right at bottom)
stroke([(210, 200), (240, 240)], width=6)
# Bottom héng closing (connecting under both parts)
stroke([(155, 245), (245, 235)], width=6)

img.save(os.path.join(os.path.dirname(__file__), "01_仫.png"))
print("saved")
