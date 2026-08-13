"""Render 町 (field + 丁) at 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 6  # stroke width

def line(x1, y1, x2, y2, w=W):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

# ---- Left: 田 (roughly x: 40-140, y: 70-230) ----
L, R = 40, 140
T, B = 70, 230
MX = (L + R) // 2
MY = (T + B) // 2

# 田 stroke order: left vertical, top+right (single 横折), middle horizontal, middle vertical, bottom horizontal
# We'll draw the box + inner cross
# Left vertical
line(L, T, L, B)
# Top horizontal + right vertical (横折)
line(L, T, R, T)
line(R, T, R, B)
# Middle horizontal
line(L, MY, R, MY)
# Middle vertical
line(MX, T, MX, B)
# Bottom horizontal
line(L, B, R, B)

# ---- Right: 丁 (roughly x: 160-280, y: 70-260) ----
# Top horizontal + vertical hook
TL, TR = 160, 280
TT = 85
# Top horizontal (slight downward slant common in handwriting)
line(TL, TT, TR, TT)
# Vertical stroke with a small hook at the bottom-left (亅)
VX = 230
VT = TT
VB = 250
line(VX, VT, VX, VB)
# small hook to the left
line(VX, VB, VX - 20, VB - 15)

out = os.path.join(os.path.dirname(__file__), "01_町.png")
img.save(out)
print(f"Saved {out}")
