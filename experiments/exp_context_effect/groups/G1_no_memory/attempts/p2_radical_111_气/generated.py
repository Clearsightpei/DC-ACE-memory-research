"""Render 气 (4-stroke radical) at 300x300 using PIL.

Stroke order (standard):
  1. 撇 (pie): short diagonal at top-left.
  2. 横 (heng): top horizontal.
  3. 横 (heng): middle horizontal, shorter, inset.
  4. 横斜钩 (heng-xie-gou): starts at top (near stroke 1's start),
     goes down through the character, curves right along bottom,
     ends with an upward hook at the lower-right.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 7

def curve(points, width=LW):
    d.line(points, fill=INK, width=width, joint="curve")
    for (x, y) in [points[0], points[-1]]:
        d.ellipse([x - width/2, y - width/2, x + width/2, y + width/2], fill=INK)

# Stroke 1: 撇 short — top-left small diagonal
s1 = [(95, 70), (85, 88), (75, 108)]
curve(s1)

# Stroke 2: top 横 — from near stroke1's top area extending right
s2 = [(90, 105), (140, 108), (195, 110), (230, 112)]
curve(s2)

# Stroke 3: middle 横 — shorter, inset
s3 = [(88, 148), (140, 150), (185, 152)]
curve(s3)

# Stroke 4: 横斜钩 — starts at top near s1 top, goes mostly vertical down (slight left curve),
# then sweeps right along the bottom, ends with upward hook.
# Note: in 气 the 4th stroke actually starts from top (essentially at same origin area as s1 start),
# goes down-left slightly, then right along bottom, hook up.
s4 = [
    (92, 88),           # top start (just below s1 origin)
    (92, 125),
    (95, 165),
    (100, 200),
    (115, 230),
    (145, 250),
    (185, 258),
    (220, 255),
    (245, 245),
    (252, 228),         # hook base
    (245, 215),         # hook tip up-left
]
curve(s4)

out = os.path.join(os.path.dirname(__file__), "01_气.png")
img.save(out)
print(f"Saved {out}")
