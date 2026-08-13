"""Render 后 (hòu) — 6 strokes.
Stroke order:
 1. 短撇 top-left (going down-left from upper-right)
 2. 横 upper horizontal (attached to bottom of 撇)
 3. 长撇 long left descending curve
 4. 竖 left side of 口
 5. 横折 top-and-right of 口
 6. 横 bottom of 口
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(points, width=6):
    d.line(points, fill=BLACK, width=width, joint="curve")

# 1. Short 撇 at top (upper-right to lower-left slant)
stroke([(155, 45), (140, 62), (122, 82)], width=6)

# 2. Upper horizontal 一 (attaches at 撇 base, extends right, slight rise)
stroke([(122, 82), (180, 78), (240, 82)], width=6)

# 3. Long 丿 — starts inside top area, sweeps down and left with curve
stroke([(118, 70), (108, 130), (90, 195), (68, 262)], width=6)

# 4. 竖 — left side of 口 (compact, inside body)
stroke([(138, 160), (135, 250)], width=6)

# 5. 横折 — top of 口 then down the right (turn shoulder)
stroke([(138, 155), (222, 158), (225, 248)], width=6)

# 6. 横 — bottom of 口
stroke([(135, 250), (225, 250)], width=6)

out = os.path.join(os.path.dirname(__file__), "01_后.png")
img.save(out)
print("wrote", out)
