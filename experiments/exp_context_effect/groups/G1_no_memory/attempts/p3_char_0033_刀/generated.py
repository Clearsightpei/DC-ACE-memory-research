"""G1 render of 刀 (dao, 'knife') — 2 strokes.

Stroke 1 (横折钩): horizontal top from left to right, sharp turn down
along the right side, curving inward at the bottom, ending with a small
hook back up-left.
Stroke 2 (撇): a long left-falling diagonal starting from under the
top-left of stroke 1, sweeping down through and out the lower-left.
"""

from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
W = 4

def poly(points, w=W):
    draw.line(points, fill=BLACK, width=w, joint="curve")
    r = w / 2
    for (x, y) in (points[0], points[-1]):
        draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)

# --- Stroke 1: 横折钩 ---
# Top horizontal from ~x=95 to ~x=210 at y~100, slight arch
# Then sharp corner down the right side, curving inward, ending
# with a small hook back up-left near y~250.
s1 = [
    (88, 108),        # small starting dip
    (105, 100),
    (135, 96),
    (170, 96),
    (200, 100),
    (215, 108),       # corner (折)
    (218, 135),
    (215, 165),
    (208, 195),
    (195, 225),
    (175, 250),
    (155, 262),
    (140, 260),       # bottom
    (128, 252),       # hook back up-left
    (122, 245),
]
poly(s1)

# --- Stroke 2: 撇 ---
# Starts on the underside of the top horizontal (upper-left area of
# stroke 1) and sweeps diagonally down and out to the lower-left.
s2 = [
    (145, 118),
    (128, 148),
    (108, 180),
    (88, 210),
    (68, 245),
    (52, 278),
]
poly(s2)

out = os.path.join(os.path.dirname(__file__), "01_刀.png")
img.save(out)
print("wrote", out)
