"""G1 attempt for 佔 (p3_char_0334).
佔 = 亻(person radical, left) + 占 (right = 卜 above 口).
Renders 300x300 PNG with PIL.
"""
import os
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5  # line width

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=BLACK, width=w)

# ---- Left: 亻 (person radical) ----
# 撇 (slanted top stroke): starts around top-right of the radical, slants down-left
line((95, 50), (45, 180), w=LW)
# vertical stroke: shares top with 撇, drops straight down
line((88, 90), (88, 275), w=LW)

# ---- Right: 占 ----
# 卜 top:
# Vertical of 卜
line((190, 45), (190, 145), w=LW)
# horizontal of 卜 (crosses vertical near upper)
line((175, 80), (250, 80), w=LW)
# small dot/tick to lower-right of vertical, angling down-right
line((210, 100), (235, 130), w=LW)

# ---- 口 (mouth) below ----
# rectangle, positioned close under 卜
L, T, R, B = 155, 160, 265, 265
# top
line((L, T), (R, T), w=LW)
# left vertical
line((L, T), (L, B), w=LW)
# right vertical (in Chinese, right side often extends slightly below bottom)
line((R, T), (R, B), w=LW)
# bottom
line((L, B), (R, B), w=LW)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_佔.png")
img.save(out)
print("wrote", out)
