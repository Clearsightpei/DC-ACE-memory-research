"""Render 社 as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# --- Left component: 礻 (shi radical) ---
# Top dot (short slanted stroke, upper) - 点
line([(75, 55), (90, 75)], width=5)

# Second stroke: short slanted diagonal upper - 短撇
line([(100, 90), (65, 125)], width=5)

# Horizontal short stroke - 横
line([(50, 145), (135, 140)], width=5)

# Vertical stroke of 礻 (long down stroke, slight curve into 竖钩)
line([(100, 105), (100, 250)], width=5)

# Small dot on the right side of 礻 (右点)
line([(125, 175), (140, 195)], width=5)

# --- Right component: 土 (earth) ---
# Top short horizontal
line([(175, 110), (240, 110)], width=5)

# Vertical stroke - extends slightly above top horizontal is not needed for 土
line([(205, 110), (205, 240)], width=5)

# Bottom long horizontal (longer than top)
line([(160, 240), (270, 240)], width=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_社.png"))
print("saved")
