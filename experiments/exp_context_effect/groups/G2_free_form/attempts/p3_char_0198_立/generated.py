"""
立 (stand) — 5 strokes:
  1. 点  top short diagonal dot (upper center)
  2. 横  short horizontal just below the dot (upper crossbar)
  3. 点  small left dot (lower-left, slanting down-left)
  4. 撇  small right flick (lower-right, slanting down-right — mirror-ish)
  5. 横  long bottom horizontal (wide base)

Silhouette: symmetric, top narrow, wide base. Aspect roughly square.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(pts, width):
    d.line(pts, fill=BLACK, width=width, joint="curve")
    # round end caps
    r = width / 2
    for (x, y) in [pts[0], pts[-1]]:
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)

# 1. 点 (top dot) — short diagonal from upper-left to lower-right, centered
stroke([(148, 55), (162, 78)], width=8)

# 2. 横 (upper short horizontal) — centered, moderate length
stroke([(95, 108), (208, 108)], width=9)

# 3. 点 (lower-left small dot) — slanting down-left
stroke([(112, 155), (95, 190)], width=8)

# 4. 撇 or 短横 (lower-right small stroke, mirror of #3, slanting down-right)
stroke([(188, 155), (205, 190)], width=8)

# 5. 横 (bottom long horizontal) — the wide base
stroke([(45, 235), (255, 235)], width=11)

img.save("01_立.png")
print("saved 01_立.png")
