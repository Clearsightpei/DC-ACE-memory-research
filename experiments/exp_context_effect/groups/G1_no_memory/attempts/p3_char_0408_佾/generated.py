"""Render 佾 (yì) to a 300x300 PNG. G1 no-memory control."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=INK, width=w)

# --- Left: 亻 (person radical) ---
# Slanting top stroke (piě)
line((85, 70), (55, 160), w=5)
# Vertical stroke
line((75, 130), (75, 275), w=5)

# --- Right side ---
# Top: 八 (two slanting strokes)
# Left piě of 八
line((160, 75), (135, 130), w=5)
# Right nà of 八
line((185, 75), (240, 130), w=5)

# Bottom: rectangular frame with two horizontal lines inside
# Frame:
# Left vertical
line((140, 145), (140, 275), w=5)
# Right vertical (slightly curved into hook)
line((235, 145), (235, 265), w=5)
line((235, 265), (225, 275), w=5)
# Top horizontal
line((140, 145), (235, 145), w=5)
# Inner horizontal 1
line((145, 190), (230, 190), w=4)
# Inner horizontal 2 (bottom)
line((145, 235), (230, 235), w=4)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_佾.png"))
print("wrote", os.path.join(out_dir, "01_佾.png"))
