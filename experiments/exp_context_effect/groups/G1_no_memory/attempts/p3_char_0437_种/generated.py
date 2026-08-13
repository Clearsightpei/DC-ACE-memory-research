"""Render 种 (seed) — left: 禾 radical, right: 中. G1 no-memory attempt."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- LEFT half: 禾 (grain radical) centered around x ~ 85 ----
# 1. Top short slant (撇) — small diagonal at very top
stroke([(100, 55), (70, 85)], width=6)
# 2. Horizontal (一) — across upper middle of left half
stroke([(40, 110), (135, 100)], width=6)
# 3. Vertical (丨) — down the middle of left
stroke([(88, 85), (88, 260)], width=6)
# 4. Left slant (撇) — from center-top going down-left
stroke([(88, 135), (40, 205)], width=6)
# 5. Right slant (捺) — from center-top going down-right
stroke([(88, 135), (140, 210)], width=6)

# ---- RIGHT half: 中 centered around x ~ 215 ----
# Rectangle 口 shape (upper, more compact)
# Top horizontal
stroke([(180, 100), (250, 100)], width=6)
# Left vertical of box
stroke([(180, 100), (180, 175)], width=6)
# Right vertical of box
stroke([(250, 100), (250, 175)], width=6)
# Bottom horizontal
stroke([(180, 175), (250, 175)], width=6)
# Long vertical through the box (extends above and well below)
stroke([(215, 75), (215, 260)], width=6)

out_path = os.path.join(os.path.dirname(__file__), "01_种.png")
img.save(out_path)
print(f"Saved {out_path}")
