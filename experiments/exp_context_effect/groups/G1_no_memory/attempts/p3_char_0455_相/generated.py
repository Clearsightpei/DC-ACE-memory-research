"""G1 render of 相 (xiang) — 木 + 目."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

def line(x1, y1, x2, y2, w=LW):
    d.line([(x1, y1), (x2, y2)], fill=INK, width=w)

# ---------- 木 (left side) ----------
# Horizontal (heng) of mu — slightly tilted down-right
line(20, 105, 140, 100)

# Vertical (shu) — long, from top through middle
line(80, 55, 80, 275)

# Left-falling (pie) from crossing area
line(75, 115, 25, 220)

# Right-falling (na) from crossing area
line(85, 115, 145, 210)

# ---------- 目 (right side) ----------
# Outer box: left vertical, top horizontal, right vertical (with hook base)
# Top horizontal
line(165, 90, 275, 90)
# Left vertical
line(165, 90, 165, 275)
# Right vertical
line(275, 90, 275, 275)
# Bottom horizontal
line(165, 275, 275, 275)

# Inner horizontal 1
line(170, 150, 270, 150)
# Inner horizontal 2
line(170, 210, 270, 210)

out = os.path.join(os.path.dirname(__file__), "01_相.png")
img.save(out)
print(f"wrote {out}")
