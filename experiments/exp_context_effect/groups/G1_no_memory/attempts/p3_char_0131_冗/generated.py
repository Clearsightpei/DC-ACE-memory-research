"""Render 冗 (redundant) at 300x300, white bg, black ink.

Structure (4 strokes):
1. 丶 left dot on top of cover.
2. 冖 top: horizontal that turns sharply down into a short right vertical.
3. 丨 left short vertical (short, under cover).
4. 乚 right vertical curving right and up (hook at end) — the tall leg.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 5


def polyline(pts, w=LW):
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i + 1]], fill=INK, width=w)


# 1) left dot (tick going down-right)
polyline([(88, 78), (100, 100)], w=6)

# 2) top cover: horizontal turning into a short vertical at right
polyline([(70, 105), (240, 100), (245, 155)], w=LW)

# 3) left short vertical/pie (under the cover, slight lean)
polyline([(115, 115), (100, 200)], w=LW)

# 4) right leg: vertical descending then curving right-up (hook)
polyline([(205, 115), (200, 235), (220, 260), (250, 258), (258, 235)], w=LW)

out = os.path.join(os.path.dirname(__file__), "01_冗.png")
img.save(out)
print("wrote", out)
