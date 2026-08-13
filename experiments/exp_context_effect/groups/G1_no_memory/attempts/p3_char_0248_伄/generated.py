"""Render 伄 = 亻 + 吊 at 300x300 PNG. Revision 1."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 5

def line(pts, width=T):
    d.line(pts, fill=INK, width=width, joint="curve")

# ---------- Left: 亻 (person radical) ----------
# 撇 (falling left) - long diagonal from upper area sloping down-left
line([(80, 55), (72, 130), (40, 235)], width=T)
# 竖 (vertical) - meets 撇 mid-height
line([(74, 125), (74, 265)], width=T)

# ---------- Right: 吊 ----------
# 口 box on top: horizontal ~y=70 to y=140, x from 130 to 250
# top horizontal (横)
line([(135, 65), (245, 65)], width=T)
# left vertical (竖)
line([(138, 65), (138, 145)], width=T)
# right vertical with slight hook look (横折)
line([(243, 65), (243, 145)], width=T)
# bottom horizontal (closes 口)
line([(138, 145), (243, 145)], width=T)

# 巾 below 口
# central vertical - long, from top of 口 all the way to bottom with hook
# passes through 口 (already drawn) and extends far down
line([(190, 65), (190, 275)], width=T)
# hook at bottom of central vertical (small hook to upper-left)
line([(190, 275), (170, 262)], width=T)

# left down-stroke of 巾 (short 竖 from bottom of 口 going down)
line([(155, 145), (155, 240)], width=T)
# right side of 巾: horizontal-fold-vertical (横折钩) hanging from 口 bottom
# short horizontal offset then vertical down with tiny hook
line([(155, 155), (228, 155)], width=T)  # inner top horizontal of 巾
line([(228, 155), (228, 230), (218, 240)], width=T)  # vertical + hook

os.makedirs(os.path.dirname(__file__), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "01_伄.png")
img.save(out)
print(f"wrote {out}")
