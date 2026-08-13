"""
侈 = 亻 (left) + 多 (right, stacked 夕+夕 diagonally)
Left-right layout. Right side dominates width; two 夕 cascade down-right.
Revision 2: enlarge right-side, longer sweeping 撇s, hooks flick UP-LEFT.
"""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(points, width=6):
    if len(points) < 2:
        return
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill="black", width=width)
    for p in points:
        r = width / 2
        d.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill="black")

def bezier(p0, p1, p2, n=30):
    return [
        ((1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0],
         (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1])
        for t in [i/n for i in range(n+1)]
    ]

# ------ 亻 (left radical, x roughly 40..95, y 70..270) ------
# 撇: short flick down-left
stroke(bezier((80, 85), (68, 115), (48, 150)), width=6)
# 竖: long vertical
stroke([(72, 120), (72, 265)], width=6)

# ------ 多 (right side, x ~ 110..250, y ~ 60..285) ------
# --- top 夕 ---
# 撇 (starts upper, curves down-left long)
stroke(bezier((175, 65), (145, 105), (110, 155)), width=6)
# 横折钩: 横 then folds down then hook up-left
d.line([(150, 90), (210, 90)], fill="black", width=6)
stroke(bezier((210, 90), (208, 130), (150, 170)), width=6)
# hook flick UP-LEFT
d.line([(150, 170), (140, 158)], fill="black", width=6)
# 点: short inner stroke (inside top 夕)
stroke(bezier((165, 115), (178, 125), (188, 140)), width=6)

# --- bottom 夕 (offset right and below, overlaps upper 夕 hook area) ---
# 撇 (longer sweep, from upper-right down to bottom-left)
stroke(bezier((210, 155), (170, 210), (115, 285)), width=6)
# 横折钩
d.line([(185, 185), (250, 185)], fill="black", width=6)
stroke(bezier((250, 185), (245, 235), (175, 280)), width=6)
# hook flick UP-LEFT
d.line([(175, 280), (163, 265)], fill="black", width=6)
# 点: short inner stroke
stroke(bezier((200, 215), (213, 225), (222, 240)), width=6)

out = os.path.join(os.path.dirname(__file__), "01_侈.png")
img.save(out)
print("saved", out)
