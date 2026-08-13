"""伫 (zhu) — left 亻 + right 宁.
Revision 1: continuous roof, tighter right-side proportions.
(v8: bank primitives reference only; trust GT.)"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def line(pts, width=6):
    d.line(pts, fill=BLACK, width=width, joint="curve")


# --- LEFT: 亻 (person radical) ---
# 撇 (pie): from upper mid-left, curving down-left
pie_pts = [(110, 75), (95, 110), (78, 145), (58, 180)]
line(pie_pts, width=8)

# 竖 (vertical): starting where pie has descended a bit, straight down
line([(102, 125), (102, 260)], width=8)


# --- RIGHT: 宁 ---
# top 丶 (dot / short pie)
line([(190, 55), (178, 82)], width=9)

# 冖 (roof): left short down-tick then long horizontal, one continuous
roof = [(158, 88), (168, 100), (265, 100)]
line(roof, width=7)

# middle 一 (horizontal, part of 丁)
line([(150, 175), (270, 175)], width=8)

# 丨 with small 亅 hook (vertical hook)
line([(208, 105), (208, 255)], width=8)
# small hook to the left at bottom
line([(208, 255), (188, 248)], width=8)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_伫.png")
img.save(out_path)
print(f"Wrote {out_path}")
