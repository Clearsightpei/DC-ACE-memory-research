"""伢 = 亻(person, left) + 牙(tooth, right). 6 strokes total.
G2 attempt. PIL, 300x300, white bg, black ink.

Layout: left 亻 compressed (~30% width, centered vertically);
right 牙 occupies ~60% width. 牙 stroke order:
  1) 横撇 (short flick down-left at top) - actually 竖 tick + 横折/横撇
  2) 横 (horizontal cross bar across middle)
  3) 竖钩 (vertical descending, hook flicks up-left at bottom)
  4) 撇 (long diagonal from mid-right slanting to bottom-left)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=5):
    d.line(pts, fill="black", width=w, joint="curve")

def stroke(pts, widths=None):
    # variable-width polyline via short segments
    if widths is None:
        widths = [5] * len(pts)
    for i in range(len(pts) - 1):
        w = int((widths[i] + widths[i+1]) / 2)
        d.line([pts[i], pts[i+1]], fill="black", width=w)
    # cap dots
    for (x, y), w in zip(pts, widths):
        r = max(1, w // 2)
        d.ellipse([x-r, y-r, x+r, y+r], fill="black")

# ---------- LEFT: 亻 ----------
# 撇: from upper-mid down-left
pts = [(95, 90), (85, 115), (72, 145), (58, 175)]
stroke(pts, [5, 6, 6, 5])

# 竖: from ~top of 撇's midpoint straight down
pts = [(88, 130), (88, 175), (88, 220), (88, 255)]
stroke(pts, [6, 6, 6, 5])

# ---------- RIGHT: 牙 ----------
# Stroke 1: short 竖/点 at top-left of 牙 (little tick)
pts = [(158, 75), (152, 92), (150, 108)]
stroke(pts, [5, 5, 5])

# Stroke 2: 横折 — horizontal top bar going right then hooking down-left slightly
# top horizontal from left tick to right edge
pts = [(148, 108), (185, 105), (220, 100), (245, 95)]
stroke(pts, [6, 6, 6, 6])
# turn: continue down and left as 横撇 tail
pts = [(245, 95), (238, 115), (225, 138), (210, 158)]
stroke(pts, [6, 6, 5, 5])

# Stroke 3: 横 — the middle horizontal cross bar
pts = [(150, 155), (185, 152), (220, 150), (245, 148)]
stroke(pts, [6, 6, 6, 6])

# Stroke 4: 竖钩 — vertical descending from top-right area down, hook at bottom flicks up-and-left
pts = [(230, 100), (230, 150), (230, 200), (232, 245)]
stroke(pts, [6, 6, 6, 6])
# hook flick UP-and-LEFT
pts = [(232, 245), (218, 235), (208, 228)]
stroke(pts, [6, 5, 4])

# Stroke 5: 撇 — long diagonal from mid area slanting down-left to bottom
pts = [(200, 158), (180, 190), (155, 225), (128, 260)]
stroke(pts, [6, 6, 5, 4])

import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_伢.png")
img.save(out)
print("saved", out)
