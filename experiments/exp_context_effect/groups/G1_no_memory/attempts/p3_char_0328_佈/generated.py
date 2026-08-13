"""G1 render for 佈 (character p3_char_0328).
Left: 亻 (single-person radical). Right: 布 (cloth).
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- Left radical: 亻 ----
# Slanting 撇 from upper area down-left
stroke([(85, 70), (75, 130), (55, 200)], width=5)
# Vertical 竖 for 亻
stroke([(95, 130), (95, 260)], width=5)

# ---- Right: 布 ----
# Top short 撇 (small diagonal from upper right)
stroke([(200, 55), (165, 110)], width=5)
# Long horizontal (crosses over top of 巾)
stroke([(135, 125), (280, 118)], width=5)
# 巾 left vertical (slight lean)
stroke([(170, 125), (162, 235)], width=5)
# 巾 top-right corner: short horizontal then hook down and left
stroke([(170, 155), (255, 150), (250, 235), (225, 250)], width=5)
# 巾 center vertical (extends past bottom, forms tall descender)
stroke([(212, 155), (212, 285)], width=5)

out = os.path.join(os.path.dirname(__file__), "01_佈.png")
img.save(out)
print("wrote", out)
