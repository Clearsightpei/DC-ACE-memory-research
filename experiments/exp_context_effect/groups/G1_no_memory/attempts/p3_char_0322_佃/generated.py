"""G1 render: 佃 (person radical + 田).

Layout:
  Left: 亻 (person radical) — a slanted top stroke and a long vertical.
  Right: 田 — outer rectangle with an internal cross.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
STROKE = 6

def line(p0, p1, w=STROKE):
    d.line([p0, p1], fill=INK, width=w)

# ---- 亻 (left radical) ----
# Top slanted stroke (short 撇 leaning left-down)
line((95, 70), (60, 130), w=6)
# Long vertical (竖)
line((95, 70), (95, 250), w=6)

# ---- 田 (right) ----
# Outer rectangle
left, right = 140, 260
top, bottom = 80, 240
# Top
line((left, top), (right, top), w=6)
# Right — with a small hook that opens down (typical 横折)
line((right, top), (right, bottom), w=6)
# Bottom
line((left, bottom), (right, bottom), w=6)
# Left vertical
line((left, top), (left, bottom), w=6)

# Inner cross
midx = (left + right) // 2
midy = (top + bottom) // 2
# Horizontal middle
line((left, midy), (right, midy), w=5)
# Vertical middle
line((midx, top), (midx, bottom), w=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(out_dir, "01_佃.png")
img.save(out)
print("Saved", out)
