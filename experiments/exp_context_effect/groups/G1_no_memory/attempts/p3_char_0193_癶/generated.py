"""Render 癶 (bō) to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

def stroke(pts, width=LW):
    d.line(pts, fill=BLACK, width=width, joint="curve")
    # endpoint caps
    r = width // 2
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

# LEFT HALF (approx)
# Stroke L1: small horizontal-ish "hat" near top-left
stroke([(80, 95), (115, 90), (135, 100)])

# Stroke L2: long diagonal from upper area down to lower-left corner (piě)
stroke([(140, 85), (125, 130), (100, 170), (70, 210), (55, 235)])

# RIGHT HALF (approx)
# Stroke R1: small horizontal "hat" near top of right half
stroke([(155, 105), (185, 95), (215, 100)])

# Stroke R2: short piě going down-left from right hat
stroke([(190, 105), (170, 130), (155, 150)])

# Stroke R3: the long nà (going down-right) from the middle to lower right
stroke([(165, 130), (185, 165), (215, 195), (245, 215), (255, 220)])

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_癶.png"))
print("wrote", os.path.join(out_dir, "01_癶.png"))
