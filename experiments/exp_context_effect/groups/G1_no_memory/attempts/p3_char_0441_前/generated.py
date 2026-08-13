"""G1 render of 前 (qián) — revision 1: fix bottom to 月 (left) + 刂 (right)."""
from PIL import Image, ImageDraw
import os

SIZE = 300
BG = 255
INK = 0
LW = 4

img = Image.new("L", (SIZE, SIZE), BG)
d = ImageDraw.Draw(img)

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill=INK, width=w)

def curve(points, w=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=INK, width=w)

# --- Top: 丷 (two small strokes) ---
curve([(120, 45), (110, 75)], w=4)   # left dot (down-left)
curve([(180, 45), (190, 75)], w=4)   # right dot (down-right)

# --- Big horizontal (一) ~y 115, spanning wide ---
line(35, 115, 265, 115, w=5)

# --- Bottom body split into 月 (left) and 刂 (right) ---
# Approx: left box x 70-160, right region x 180-250, y 115-265

# ---- LEFT: 月-like box ----
# Left downstroke — a 撇 curving down-left slightly
curve([(85, 115), (78, 180), (65, 265)], w=5)
# Top-right of box: goes from top down as vertical-hook forming right edge of 月
# horizontal top (small since 一 covers most)
# right vertical of left-月
line(160, 130, 160, 260, w=5)
# small hook at bottom-right of left-月
curve([(160, 260), (152, 268), (140, 265)], w=4)
# inner two horizontal bars (月's inside)
line(90, 165, 160, 165, w=4)
line(90, 210, 160, 210, w=4)
# bottom of left 月 (close the box)
line(70, 258, 160, 258, w=4)

# ---- RIGHT: 刂 (short vertical + long vertical-hook) ----
# short left vertical
line(200, 135, 200, 220, w=4)
# long right vertical with hook
line(245, 130, 245, 260, w=5)
curve([(245, 260), (238, 268), (225, 265)], w=4)

os.makedirs(os.path.dirname(__file__), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "01_前.png")
img.save(out)
print("Wrote", out)
