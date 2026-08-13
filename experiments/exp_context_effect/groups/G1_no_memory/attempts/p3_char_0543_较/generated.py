"""G1 render of 较 (compare/relatively) — 车 + 交.

车 as left-radical (4 strokes simplified): 一 (top), 乛 (small hook / dot area),
丨 (long vertical spine), 一 (rising bottom stroke).
交 (6 strokes): 丶, 一, 丶丶 (two dots), 撇, 捺.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(p1, p2, w=LW):
    d.line([p1, p2], fill="black", width=w)

def poly(pts, w=LW):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i + 1], w)

# ---------------- LEFT: 车 (radical form) ----------------
# Column roughly x=30..120, y=90..270
# 1) top short horizontal 一
line((45, 115), (115, 110))
# 2) middle box: horizontal top + short verticals + inner horizontal
line((50, 155), (115, 150))          # top of middle box
line((55, 155), (55, 195))           # left side of box
line((110, 150), (110, 200))         # right side of box
line((50, 180), (115, 178))          # inner horizontal (日 middle)
# 3) long vertical spine through the whole char
line((80, 100), (80, 265))
# 4) bottom rising horizontal (radical form ends with tick up-right)
poly([(35, 240), (120, 225)])

# ---------------- RIGHT: 交 ----------------
# Column roughly x=140..285, y=45..280
# 1) top dot 丶
poly([(198, 55), (212, 45)])
# 2) long horizontal 一
line((150, 110), (275, 105))
# 3) left dot 丶 (upper part of 父)
poly([(178, 135), (168, 155)])
# 4) right dot 丶
poly([(248, 135), (258, 155)])
# 5) 撇 — long diagonal from upper-right down to lower-left
poly([(235, 165), (150, 280)])
# 6) 捺 — long diagonal from upper-left down to lower-right
poly([(185, 165), (285, 270)])

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_较.png"))
print("saved 01_较.png")
