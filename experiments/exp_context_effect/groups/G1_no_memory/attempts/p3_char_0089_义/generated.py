"""Render 义 (yi) to a 300x300 PNG with PIL.

义 = 3 strokes:
  1) 点 (dot) — small stroke top-left area
  2) 丿 (long left-falling curve) — starts top-right, curves down-left through center to bottom-left
  3) 乀 (right-falling) — starts near center crossing point, extends to bottom-right

The GT shows a short dot at top-left, a curved stroke top-right descending
through the center, and a long shallow stroke crossing bottom-left to bottom-right.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"

def stroke(points, width=6):
    d.line(points, fill=INK, width=width, joint="curve")
    # round caps
    r = width // 2
    for (x, y) in [points[0], points[-1]]:
        d.ellipse((x - r, y - r, x + r, y + r), fill=INK)

# 1) Dot (点) — top-left, short slanted stroke going down-right, a bit more pronounced
dot = [(95, 100), (130, 118)]
stroke(dot, width=7)

# 2) 丿 long left-falling — starts near top-right, curves down through center to bottom-left
pie = [
    (195, 90),
    (192, 115),
    (185, 140),
    (172, 165),
    (155, 195),   # crossing point
    (130, 220),
    (95, 245),
    (55, 265),
]
stroke(pie, width=7)

# 3) 乀 right-falling — enters from upper-left of the crossing area, exits to bottom-right
na = [
    (75, 180),
    (105, 188),
    (135, 193),
    (155, 195),   # crossing
    (190, 220),
    (225, 240),
    (260, 258),
]
stroke(na, width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0089_义/01_义.png")
print("saved")
