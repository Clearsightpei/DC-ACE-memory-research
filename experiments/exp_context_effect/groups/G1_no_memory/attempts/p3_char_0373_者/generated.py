"""Render 者 to a 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 4

def line(pts, w=LW):
    d.line(pts, fill="black", width=w)

# 者 — top half is 耂 (老字头), bottom is 日
# Order roughly: horizontal, vertical, horizontal, slash-丿, long horizontal, then 日

# 1. Top short horizontal
line([(115, 60), (185, 60)], w=LW)
# 2. Vertical stroke (short, from top down through second horizontal)
line([(150, 45), (155, 105)], w=LW)
# 3. Second horizontal (a bit lower, similar width, slight slant up-right)
line([(100, 100), (200, 95)], w=LW)
# 4. Small right tick from top-right corner (like the little 撇 above 日)
line([(195, 65), (205, 100)], w=LW)
# 5. Long left-slanting 丿 — from upper right area down to bottom-left
line([(215, 75), (55, 265)], w=LW)
# 6. Long horizontal bar crossing the slash (middle of character)
line([(50, 150), (260, 155)], w=LW)

# 日 (bottom, positioned centered slightly right)
L, R, T, B = 135, 210, 185, 270
line([(L, T), (R, T)], w=LW)      # top
line([(L, T), (L, B)], w=LW)      # left
line([(R, T), (R, B)], w=LW)      # right
line([(L, B), (R, B)], w=LW)      # bottom
line([(L + 3, 228), (R - 3, 228)], w=LW)  # middle bar

out = os.path.join(os.path.dirname(__file__), "01_者.png")
img.save(out)
print("wrote", out)
