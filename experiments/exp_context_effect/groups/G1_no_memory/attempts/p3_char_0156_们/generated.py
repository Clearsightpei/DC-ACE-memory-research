"""Render 们 to 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
TH = 6  # stroke thickness


def stroke(points, width=TH):
    d.line(points, fill=INK, width=width, joint="curve")
    # rounded caps
    for x, y in points:
        d.ellipse((x - width / 2, y - width / 2, x + width / 2, y + width / 2), fill=INK)


# ---------- Left: 亻 (person radical) ----------
# 1) 撇 (slant from upper-right to lower-left)
stroke([(95, 90), (88, 115), (78, 145), (65, 185), (55, 220)])

# 2) 丨 vertical descending from the middle-lower part of the slant
stroke([(92, 145), (92, 260)])

# ---------- Right: 门-like part of 们 ----------
# 3) 丶 short slant/dot at upper-left of right part
stroke([(150, 100), (158, 118)])

# 4) 横折钩-like: horizontal going right then bending down (top+right side of the box)
stroke([(165, 115), (200, 108), (235, 110)])  # top horizontal
stroke([(232, 108), (238, 140), (240, 200), (238, 255)])  # right vertical bending down

# 5) 竖 (left vertical of the right box, from just under the dot)
stroke([(162, 130), (160, 180), (158, 255)])

out = os.path.join(os.path.dirname(__file__), "01_们.png")
img.save(out)
print(f"wrote {out}")
