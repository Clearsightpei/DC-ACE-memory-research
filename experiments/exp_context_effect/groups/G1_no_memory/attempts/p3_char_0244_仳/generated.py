"""Render 仳 (亻 + 比) to 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def line(pts, width=6):
    draw.line(pts, fill="black", width=width, joint="curve")

# --- 亻 (person radical) on the left ---
# Slanting stroke: from upper right down to lower left
line([(100, 65), (58, 210)], width=6)
# Vertical stroke: from about middle of slant down
line([(90, 130), (90, 265)], width=6)

# --- 比 (right side) ---
# LEFT half of 比 (looks like a short 匕 rotated):
# Stroke 1: short horizontal-ish at top (short slash)
line([(140, 95), (135, 155)], width=6)
# Stroke 2: horizontal bar in the middle
line([(135, 150), (175, 145)], width=6)
# Stroke 3: long vertical downstroke
line([(140, 100), (140, 260)], width=6)

# RIGHT half of 比 (匕):
# Stroke 1: short slash from upper-right area down-left
line([(215, 90), (185, 145)], width=6)
# Stroke 2: vertical going down from the end of slash
line([(185, 145), (190, 235)], width=6)
# Stroke 3: rising base stroke that hooks upward
line([(190, 235), (255, 218)], width=6)
line([(255, 218), (258, 175)], width=6)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_仳.png"))
print("saved")
