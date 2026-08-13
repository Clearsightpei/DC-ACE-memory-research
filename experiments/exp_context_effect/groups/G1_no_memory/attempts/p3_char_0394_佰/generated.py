"""Render 佰 (bǎi) — 亻 + 百."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(pts, w=LW):
    d.line(pts, fill="black", width=w)

# --- 亻 (person radical, left) ---
# Slanting stroke: from upper to lower-left
line([(85, 75), (50, 235)], w=LW)
# Vertical: starts where slant meets midpoint
line([(85, 145), (85, 265)], w=LW)

# --- 百 (right side) ---
# Top short horizontal (丿 stub above box — simplified as horizontal)
line([(180, 75), (230, 78)], w=LW)
# The 一 crossbar (top of 日 box)
line([(130, 115), (260, 112)], w=LW)
# Left vertical of the 日 box
line([(150, 115), (150, 250)], w=LW)
# Right vertical of the 日 box
line([(248, 112), (248, 250)], w=LW)
# Bottom horizontal
line([(150, 250), (248, 250)], w=LW)
# Middle horizontal (inside 日)
line([(152, 195), (246, 195)], w=LW)

out = os.path.join(os.path.dirname(__file__), "01_佰.png")
img.save(out)
print("wrote", out)
