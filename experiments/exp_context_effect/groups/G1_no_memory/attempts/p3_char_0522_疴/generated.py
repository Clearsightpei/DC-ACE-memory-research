"""G1 render of 疴 (illness): 疒 radical enclosing 可."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=4):
    d.line(pts, fill="black", width=width)

# ---- 疒 radical: dot, horizontal, dot, long throw (semi-encloses 可) ----
# Top small dot (upper center-left, slanted)
line([(105, 55), (118, 72)], width=4)

# Top horizontal (moderate, goes right across upper area)
line([(75, 95), (215, 90)], width=4)

# Left small dot descending from horizontal
line([(90, 105), (78, 128)], width=4)

# Long throw (撇): from horizontal down-left, curving
line([(130, 95), (115, 140), (95, 190), (65, 250)], width=4)

# Two small inner marks (the little strokes inside 疒 on left)
line([(100, 155), (112, 168)], width=4)
line([(105, 190), (117, 203)], width=4)

# ---- 可 (inside enclosure of 疒) ----
# Top horizontal of 可
line([(135, 130), (220, 128)], width=4)

# 口 (small mouth) — under-left of the horizontal
# top
line([(140, 165), (185, 165)], width=4)
# left
line([(140, 165), (140, 205)], width=4)
# right
line([(185, 165), (185, 205)], width=4)
# bottom
line([(140, 205), (185, 205)], width=4)

# Vertical hook (竖钩) of 可 on the right side
line([(210, 130), (210, 235), (195, 245)], width=4)

out = os.path.join(os.path.dirname(__file__), "01_疴.png")
img.save(out)
print("saved", out)
