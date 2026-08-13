"""G1 draw 畧 = 田 (top) + 各 (bottom)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, w=4):
    d.line([p1, p2], fill="black", width=w)

def polyline(pts, w=4):
    d.line(pts, fill="black", width=w, joint="curve")

# ---- Top: 田 (field), roughly x 110..200, y 30..130 ----
L, R = 110, 200
T, B = 30, 130
MX = (L + R) // 2
MY = (T + B) // 2

line((L, T), (L, B))                # left vertical
polyline([(L, T), (R, T), (R, B)])  # top horiz + right vert (横折)
line((MX, T), (MX, B))              # middle vertical
line((L, MY), (R, MY))              # middle horizontal
line((L, B), (R, B))                # bottom horizontal

# ---- Bottom: 各 ----
# 夂 top: 3 strokes  (short 撇, 横撇 long, 捺)
# stroke 1: short 撇 at top, from upper-right to lower-left
line((165, 135), (140, 158))
# stroke 2: 横撇 - short horiz then long slash down-left
polyline([(148, 152), (200, 152), (135, 220)])
# stroke 3: 捺 - from midpoint of 横 going down-right
line((175, 165), (230, 220))

# 口 (mouth box) at bottom center
kL, kR = 130, 195
kT, kB = 225, 275
line((kL, kT), (kL, kB))                 # left vertical
polyline([(kL, kT), (kR, kT), (kR, kB)]) # top horiz + right vert
line((kL, kB), (kR, kB))                 # bottom horizontal

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_畧.png"))
print("saved 01_畧.png")
