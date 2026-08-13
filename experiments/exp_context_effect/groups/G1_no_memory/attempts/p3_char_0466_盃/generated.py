"""Render 盃 = 不 (top) + 皿 (bottom) at 300x300."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

# ---- 不 (top half, roughly y=30..135) ----
# 1: top horizontal
line((70, 55), (225, 50), w=6)
# 2: vertical descending through center (short, stops mid)
line((150, 55), (148, 135), w=6)
# 3: left falling stroke (piě) from just under horizontal
line((115, 70), (75, 135), w=5)
# 4: right dot / short stroke (diǎn)
line((175, 75), (215, 130), w=5)

# ---- 皿 (bottom half, roughly y=150..270) ----
# top horizontal of 皿 (short, above the box)
# Actually 皿 structure: left vertical, right vertical, two inner verticals, bottom long horizontal
# Top "opening" is implicit — let's draw:
# Outer box top (short curve): often written as slight bracket
line((80, 175), (220, 170), w=6)  # top of 皿
# left vertical
line((85, 175), (95, 250), w=5)
# right vertical
line((215, 172), (210, 250), w=5)
# inner vertical left
line((130, 185), (130, 245), w=5)
# inner vertical right
line((170, 185), (170, 245), w=5)
# bottom long horizontal (extends beyond)
line((55, 258), (245, 258), w=7)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_盃.png"))
print("saved")
