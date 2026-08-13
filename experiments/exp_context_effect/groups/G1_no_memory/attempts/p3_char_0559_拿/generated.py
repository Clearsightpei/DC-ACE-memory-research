"""Render 拿 (ná) — 合 on top, 手 on bottom."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
LW = 5

# --- 合 (top half) ---
# 人 roof — two diagonals from apex
d.line([(150, 25), (70, 100)], fill=BLACK, width=LW)   # left pie
d.line([(150, 25), (235, 105)], fill=BLACK, width=LW)  # right na

# 一 horizontal under roof
d.line([(80, 110), (225, 110)], fill=BLACK, width=LW)

# 口 (rectangle)
# left vertical
d.line([(105, 125), (105, 170)], fill=BLACK, width=LW)
# top horizontal
d.line([(105, 125), (200, 125)], fill=BLACK, width=LW)
# right vertical
d.line([(200, 125), (200, 170)], fill=BLACK, width=LW)
# bottom horizontal
d.line([(105, 170), (200, 170)], fill=BLACK, width=LW)

# --- 手 (bottom half) ---
# top short slant (撇) — ㇒
d.line([(115, 185), (95, 200)], fill=BLACK, width=LW)
# first horizontal (short)
d.line([(115, 195), (200, 195)], fill=BLACK, width=LW)
# second horizontal (medium)
d.line([(100, 220), (215, 220)], fill=BLACK, width=LW)
# long horizontal (bottom third stroke)
d.line([(60, 245), (245, 245)], fill=BLACK, width=LW)
# vertical hook — 亅
d.line([(155, 200), (155, 285)], fill=BLACK, width=LW)
# hook curl
d.line([(155, 285), (135, 275)], fill=BLACK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_拿.png")
img.save(out)
print("wrote", out)
