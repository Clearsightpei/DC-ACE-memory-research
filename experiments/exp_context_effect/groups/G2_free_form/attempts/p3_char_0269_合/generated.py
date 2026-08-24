"""
合 - 6 strokes: 撇, 捺, 一 (under 人), 口 (竖, 横折, 横)
Layout: 人 roof at top spans wide, 一 tucked under, 口 centered below.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def bezier(p0, p1, p2, steps=40):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t*t * p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t*t * p2[1]
        pts.append((x, y))
    return pts

def stroke(pts, w=6):
    for i in range(len(pts)-1):
        d.line([pts[i], pts[i+1]], fill="black", width=w)
    for p in pts:
        d.ellipse([p[0]-w/2, p[1]-w/2, p[0]+w/2, p[1]+w/2], fill="black")

# 1. 撇 - from apex down-left, curving
pie = bezier((150, 45), (130, 100), (70, 175), steps=50)
stroke(pie, w=7)

# 2. 捺 - from apex down-right, straighter with slight curve, ending flat-thick
na = bezier((150, 45), (180, 105), (240, 170), steps=50)
stroke(na, w=7)
# small tail extension
d.line([(240, 170), (255, 173)], fill="black", width=8)

# 3. 一 - horizontal bar under the 人 roof
d.line([(95, 185), (215, 183)], fill="black", width=7)

# 4-6. 口 centered below
# 竖 (left)
d.line([(115, 210), (113, 275)], fill="black", width=7)
# 横折 (top + right)
d.line([(115, 210), (200, 208)], fill="black", width=7)
d.line([(200, 208), (198, 273)], fill="black", width=7)
# 横 (bottom)
d.line([(113, 273), (200, 273)], fill="black", width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0269_合/01_合.png")
print("saved")
