"""Render 第 to 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- 竹字头 (bamboo radical top) ----
# Left cluster
stroke([(75, 55), (65, 85)], width=5)                  # left slash (撇)
stroke([(78, 75), (130, 68)], width=5)                 # horizontal
stroke([(115, 65), (120, 90)], width=5)                # short vertical dot

# Right cluster
stroke([(165, 55), (155, 85)], width=5)                # right slash (撇)
stroke([(168, 75), (235, 68)], width=5)                # horizontal (slightly rising)
stroke([(215, 65), (220, 90)], width=5)                # short vertical dot

# ---- Body (弓-like structure of 第) ----
# Top horizontal
stroke([(70, 120), (230, 118)], width=6)

# Left short vertical/slant down from top-left of box
stroke([(80, 120), (72, 175)], width=6)

# Middle horizontal
stroke([(80, 160), (215, 160)], width=6)

# Right vertical dropping with hook at bottom-left (forms the box's right wall + hook)
stroke([(215, 118), (218, 220), (185, 230)], width=6)

# Bottom horizontal of box
stroke([(75, 205), (215, 205)], width=6)

# Central long vertical (亅) — goes from just above middle horizontal down past bottom
stroke([(148, 135), (148, 275)], width=6)

# Bottom hook — curl up-left at end of vertical
stroke([(148, 273), (125, 258)], width=6)

out_path = os.path.join(os.path.dirname(__file__), "01_第.png")
img.save(out_path)
print(f"Saved {out_path}")
