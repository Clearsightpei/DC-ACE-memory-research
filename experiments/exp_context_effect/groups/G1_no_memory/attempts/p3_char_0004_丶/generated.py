"""G1 render of 丶 (dian / dot stroke).

The GT shows a single 点 (dot) stroke placed slightly right of center,
running from upper-left to lower-right with a slight rightward curve,
tapered thin at the top and thick at the bottom.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# The dot stroke: start upper-left, curve down-right, taper.
# Emulate a brush by drawing many overlapping circles along a quadratic
# bezier, with increasing radius (thin -> thick).
p0 = (120, 110)   # start (thin end, upper-left)
p1 = (135, 140)   # control (pulls curve rightward)
p2 = (175, 195)   # end (thick bottom-right)

def bezier(t, a, b, c):
    x = (1 - t) ** 2 * a[0] + 2 * (1 - t) * t * b[0] + t ** 2 * c[0]
    y = (1 - t) ** 2 * a[1] + 2 * (1 - t) * t * b[1] + t ** 2 * c[1]
    return x, y

N = 160
r_start = 1.5
r_end = 6.5
for i in range(N + 1):
    t = i / N
    x, y = bezier(t, p0, p1, p2)
    r = r_start + (r_end - r_start) * t
    draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

out = os.path.join(os.path.dirname(__file__), "01_丶.png")
img.save(out)
print(f"wrote {out} size={img.size}")
