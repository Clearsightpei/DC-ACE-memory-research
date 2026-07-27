"""Render 本 (běn) — 木 with a horizontal line marking the root.

Strokes (MMH order):
 1. 一  top horizontal
 2. 丨  vertical descender (through the horizontal)
 3. 丿  left-falling diagonal from center
 4. 乀/㇏  right-falling diagonal from center
 5. 一  short horizontal near the bottom of the vertical (root mark)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

# 1) top horizontal (long)
d.line([(50, 95), (250, 95)], fill=BLACK, width=LW)

# 2) vertical descender through center
d.line([(150, 55), (150, 275)], fill=BLACK, width=LW)

# 3) left-falling 丿 from around the top intersection down-left
d.line([(150, 100), (55, 235)], fill=BLACK, width=LW)

# 4) right-falling 乀 from around the top intersection down-right
d.line([(150, 100), (255, 235)], fill=BLACK, width=LW)

# 5) short horizontal near bottom of vertical — the "root" mark
d.line([(105, 250), (195, 250)], fill=BLACK, width=LW)

out = __file__.rsplit("/", 1)[0] + "/01_本.png"
img.save(out)
print("wrote", out)
