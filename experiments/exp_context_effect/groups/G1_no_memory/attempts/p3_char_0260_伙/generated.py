"""Render 伙 (huǒ) — person radical 亻 + 火 (fire).
G1 control: no memory, PIL only, 300x300 white bg black ink.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
INK = 0
BG = 255

img = Image.new("L", (W, H), BG)
d = ImageDraw.Draw(img)


def stroke(pts, width=6):
    """Draw a smooth polyline stroke."""
    d.line(pts, fill=INK, width=width, joint="curve")
    # round caps
    r = width // 2
    for x, y in (pts[0], pts[-1]):
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# --- Left: 亻 (person radical) ---
# 撇 (left-falling), starts upper, curves down-left
pie_left = [(105, 70), (100, 105), (90, 145), (78, 190), (65, 235)]
stroke(pie_left, width=7)

# 竖 (vertical), from where 撇 begins area, going straight down
shu = [(105, 115), (105, 265)]
stroke(shu, width=7)

# --- Right: 火 (fire) ---
# Small left dot 点 (upper left of 火)
dot_l = [(165, 100), (155, 125)]
stroke(dot_l, width=7)

# Small right dot 点 (upper right of 火)
dot_r = [(210, 100), (218, 125)]
stroke(dot_r, width=7)

# 撇 (long left-falling stroke of 火)
pie_fire = [(200, 110), (185, 150), (170, 190), (155, 230), (140, 265)]
stroke(pie_fire, width=7)

# 捺 (long right-falling stroke of 火), starts near top-middle of 火, sweeps down-right
na_fire = [(195, 145), (210, 180), (225, 215), (245, 245), (270, 260)]
stroke(na_fire, width=7)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_伙.png"))
print("wrote 01_伙.png")
