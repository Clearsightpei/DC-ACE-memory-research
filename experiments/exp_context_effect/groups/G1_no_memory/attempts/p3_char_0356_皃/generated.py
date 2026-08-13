"""Render 皃 (variant of 貌) as 300x300 PNG.
Structure: 白 (top) + 儿-like base (bottom, left slant + right hook).
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, w=4):
    d.line([p0, p1], fill="black", width=w)

def curve(pts, w=4):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=w)

# --- Top: 白 ---
# tiny top tick (撇)
curve([(140, 40), (135, 55)], w=4)

# top horizontal of 白 box
line((105, 60), (185, 60))

# left vertical of box
line((105, 60), (105, 145))

# right vertical of box (slight hook at bottom-right)
line((185, 60), (185, 145))

# middle horizontal
line((105, 100), (185, 100))

# bottom of 白 (which also serves as the top of the base)
line((105, 145), (185, 145))

# --- Bottom: 儿-like (two legs) ---
# left leg: 撇 curving down-left from just below the box
curve([(130, 145), (128, 175), (120, 210), (100, 250), (80, 275)], w=4)

# right leg: 竖弯钩 — down then curves right and hooks up
curve([
    (170, 145),
    (172, 180),
    (175, 215),
    (185, 245),
    (205, 265),
    (230, 270),
    (245, 265),
    (250, 255),
], w=4)

out = os.path.join(os.path.dirname(__file__), "01_皃.png")
img.save(out)
print("saved", out)
