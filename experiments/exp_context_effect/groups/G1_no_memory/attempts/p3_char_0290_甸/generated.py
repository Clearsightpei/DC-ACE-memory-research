"""Render 甸 (dian) — 勹 wrap enclosing 田."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

# 勹 (wrap) — 2 strokes
# Stroke 1: 撇 at top (small diagonal going down-left)
d.line([(135, 45), (100, 80)], fill=INK, width=LW)

# Stroke 2: 横折钩 — horizontal top, then curved vertical, ending with hook
# top horizontal
d.line([(100, 75), (220, 72)], fill=INK, width=LW)
# curved right side descending, then hook to left
curve_pts = [
    (220, 72),
    (222, 130),
    (223, 180),
    (220, 220),
    (208, 240),
    (188, 240),
    (175, 232),
]
d.line(curve_pts, fill=INK, width=LW)

# 田 inside the wrap (larger, more centered)
left, top, right, bot = 110, 115, 200, 220
# outer rectangle
d.line([(left, top), (right, top)], fill=INK, width=LW)  # top
d.line([(left, top), (left, bot)], fill=INK, width=LW)   # left
d.line([(right, top), (right, bot)], fill=INK, width=LW) # right
d.line([(left, bot), (right, bot)], fill=INK, width=LW)  # bottom
# cross
mid_x = (left + right) // 2
mid_y = (top + bot) // 2
d.line([(mid_x, top), (mid_x, bot)], fill=INK, width=LW)
d.line([(left, mid_y), (right, mid_y)], fill=INK, width=LW)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_甸.png"))
print("wrote 01_甸.png")
