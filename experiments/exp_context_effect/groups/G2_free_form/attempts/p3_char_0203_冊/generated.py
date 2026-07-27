"""
冊 (cè) — 5 strokes, symmetric two-frame character.
Not in sibling-risk list. GT: two vertical frames sharing a long
horizontal bar through the middle; each frame has an inner vertical.

Stroke plan (per common calligraphic order):
1. 竖    — left outer vertical of left frame (slight curve, ends lower)
2. 横折  — top+right of left frame  (turns down at right shoulder)
3. 竖    — left outer vertical of right frame (upright)
4. 横折钩— top+right of right frame with small hook (or just 横折)
5. 横    — long central horizontal cutting through both frames

Rendering with PIL: black ink on 300x300 white, brush ~10px.
"""
from PIL import Image, ImageDraw
import os, math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BRUSH = 10

def stroke(points, width=BRUSH):
    d.line(points, fill="black", width=width, joint="curve")
    # round caps
    r = width // 2
    for (x, y) in [points[0], points[-1]]:
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# Layout: character occupies roughly x=45..255, y=55..255
# Two frames side by side, joined by a long horizontal bar around y=170.

# LEFT FRAME
# 1. Left outer vertical (slightly curved outward at bottom - 竖 with a mild 撇 tail)
stroke([(70, 70), (68, 130), (62, 200), (55, 260)], BRUSH)

# 2. Top + right side of left frame (横折)
stroke([(75, 62), (150, 60), (152, 130), (150, 210)], BRUSH)

# RIGHT FRAME
# 3. Left inner vertical of right frame (upright)
stroke([(158, 78), (158, 260)], BRUSH)

# 4. Top + right side of right frame (横折钩) with small hook
stroke([(160, 65), (245, 63), (247, 130), (245, 235)], BRUSH)
# small hook flick UP-LEFT
stroke([(245, 235), (235, 225)], BRUSH)

# 5. LONG central horizontal cutting through both frames
stroke([(38, 168), (270, 165)], BRUSH)

img.save(os.path.join(os.path.dirname(__file__), "01_冊.png"))
print("wrote 01_冊.png")
