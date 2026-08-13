"""G1 render of 來 (p3_char_0412) at 300x300 — revised."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, w=5):
    d.line([p1, p2], fill="black", width=w)

def curve(pts, w=5):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=w)

# 來 has:
#  - a top short piě-nà cap (small 人) on top of the first horizontal
#  - first horizontal (upper bar)
#  - central long vertical from top through bottom
#  - middle horizontal bar (shorter)
#  - two small 人-like radicals flanking the vertical below the middle bar
#  - long piě going down-left and long nà going down-right (the 人 legs)

# Top cap 人
line((150, 55), (128, 82), w=5)  # small piě
line((150, 55), (172, 82), w=5)  # small nà

# Top horizontal
line((72, 90), (228, 90), w=5)

# Central long vertical (through the whole char)
line((150, 82), (150, 270), w=6)

# Middle horizontal (shorter)
line((88, 155), (212, 155), w=5)

# Small left 人 (below the middle bar, left of the vertical)
line((125, 165), (108, 200), w=4)  # small piě
line((118, 178), (135, 205), w=4)  # small nà

# Small right 人 (below the middle bar, right of the vertical)
line((175, 165), (192, 200), w=4)  # small nà
line((182, 178), (165, 205), w=4)  # small piě

# Long left leg (piě from around middle bar going down-left)
curve([(150, 155), (128, 190), (100, 225), (72, 258)], w=5)

# Long right leg (nà from around middle bar going down-right)
curve([(150, 155), (175, 190), (205, 225), (235, 258)], w=5)

out_path = os.path.join(os.path.dirname(__file__), "01_來.png")
img.save(out_path)
print(f"saved {out_path}")
