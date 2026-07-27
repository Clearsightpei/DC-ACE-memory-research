# 乑 (yín) — three-人-family character
# Look at GT: short heng-hook at top-center, long left-descending pie from top,
# central vertical, small pie+na (人 shape) at bottom-right.
# Draw fresh (v8: trust GT).
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=5):
    d.line(pts, fill="black", width=w, joint="curve")

def draw_char(d):
    # Top short heng with downward hook at right end (like 乛)
    line([(115, 62), (185, 58)], w=5)
    line([(185, 58), (182, 78)], w=5)

    # Long descending pie sweeping from top-right down through center to lower-left
    # curves like an S
    line([(178, 78), (155, 115), (120, 165), (85, 220), (65, 265)], w=5)

    # Central vertical shaft
    line([(148, 105), (148, 285)], w=5)

    # Small 人 on bottom-right: pie (upper-left slant) + na (upper-right slant)
    # apex around (215, 170)
    line([(215, 170), (188, 235)], w=5)     # pie
    line([(215, 170), (260, 255)], w=6)     # na

draw_char(d)

out = os.path.join(os.path.dirname(__file__), "01_乑.png")
img.save(out)
print("wrote", out)
