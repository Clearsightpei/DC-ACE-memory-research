"""G1 drawer for p3_char_0370_乶.

Char 乶 = top 甫-like component + bottom 乙 stroke.
Rendered with PIL at 300x300, black on white.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

LW = 5

def line(p0, p1, w=LW):
    d.line([p0, p1], fill="black", width=w)

def poly(points, w=LW):
    d.line(points, fill="black", width=w, joint="curve")

# Top component (looks like 甫 / 車-ish): horizontal top, vertical, box with cross bars
# Bounding box for top: x 70..210, y 40..170
# Top horizontal
poly([(70, 60), (210, 55)], w=LW)
# Small dot / short right stroke above right
poly([(215, 45), (225, 65)], w=LW)

# Vertical downstroke going through middle
poly([(140, 55), (135, 175)], w=LW)

# Box (田-like) around middle
# left vertical
poly([(95, 80), (95, 165)], w=LW)
# right vertical
poly([(180, 80), (185, 175)], w=LW)
# middle horizontal (top of box)
poly([(95, 80), (185, 80)], w=LW)
# middle horizontal (mid)
poly([(95, 120), (185, 122)], w=LW)
# bottom horizontal of box
poly([(95, 165), (185, 168)], w=LW)

# Bottom component: 乙 (curve starting upper-left going down, then hook up right)
# Path: horizontal short at top, then diagonal down-left curve, then long horizontal hook up
curve_pts = [
    (105, 200),
    (155, 200),
    (135, 220),
    (100, 245),
    (85, 260),
    (110, 265),
    (170, 262),
    (220, 255),
    (240, 245),
]
poly(curve_pts, w=LW+1)
# small upturn hook at end
poly([(240, 245), (245, 235)], w=LW+1)

out_path = os.path.join(os.path.dirname(__file__), "01_乶.png")
img.save(out_path)
print(f"wrote {out_path}")
