"""Render 伉 - 亻 (person radical, left) + 亢 (right)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- 亻 (person radical, left side) ----
# Left slanted stroke (撇): from upper area down-left
stroke([(90, 80), (50, 200)], width=5)
# Vertical stroke (竖): starts at midpoint of pie, drops straight down
stroke([(72, 150), (78, 275)], width=5)

# ---- 亢 (right side) ----
# Top dot (点): small slanted dot up top center-right
stroke([(180, 55), (200, 75)], width=5)
# Long horizontal (横): across the top of 几
stroke([(120, 115), (260, 108)], width=5)
# Left leg (short 撇): curves down-left from horizontal
stroke([(160, 115), (130, 275)], width=5)
# Right leg (横折弯钩): drops down then curves right into hook
stroke([(240, 115), (238, 220), (260, 260), (275, 258)], width=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_伉.png"))
print("Wrote 01_伉.png")
