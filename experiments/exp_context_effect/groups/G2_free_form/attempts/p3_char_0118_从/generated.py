"""
从 (cong) — "follow". Two 人 side-by-side.

# SIGNATURE CHECK:
# 人 | apex SHARED at same y; both strokes throw outward; 捺 has thick foot | 入
# For 从: LEFT 人 compressed — 捺 is a SHORT flick (does not reach bottom);
# RIGHT 人 is fuller with proper 撇 (down-left) and 捺 (down-right, thick foot).
# Both 人 share similar apex height; right 人 slightly lower than left.
# GT shows thinner, gently curved lines — not thick or straight.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, w_start=6, w_end=6, steps=80):
    n = len(pts)
    if n == 2:
        (x1,y1),(x2,y2) = pts
        for i in range(steps+1):
            t = i/steps
            x = x1 + (x2-x1)*t
            y = y1 + (y2-y1)*t
            r = w_start + (w_end - w_start)*t
            d.ellipse([x-r/2, y-r/2, x+r/2, y+r/2], fill="black")
    elif n == 3:
        (x1,y1),(x2,y2),(x3,y3) = pts
        for i in range(steps+1):
            t = i/steps
            x = (1-t)**2*x1 + 2*(1-t)*t*x2 + t**2*x3
            y = (1-t)**2*y1 + 2*(1-t)*t*y2 + t**2*y3
            r = w_start + (w_end - w_start)*t
            d.ellipse([x-r/2, y-r/2, x+r/2, y+r/2], fill="black")
    elif n == 4:
        (x1,y1),(x2,y2),(x3,y3),(x4,y4) = pts
        for i in range(steps+1):
            t = i/steps
            x = (1-t)**3*x1 + 3*(1-t)**2*t*x2 + 3*(1-t)*t**2*x3 + t**3*x4
            y = (1-t)**3*y1 + 3*(1-t)**2*t*y2 + 3*(1-t)*t**2*y3 + t**3*y4
            r = w_start + (w_end - w_start)*t
            d.ellipse([x-r/2, y-r/2, x+r/2, y+r/2], fill="black")

# LEFT 人 (compressed): apex around (95, 95)
# 撇 — from apex curving down-left to bottom, gentle S-curve
stroke([(97,90), (85,150), (70,210), (55,270)], w_start=7, w_end=3)
# 捺 as a SHORT flick — from apex area down-right, stops mid-body
stroke([(100,110), (115,150), (128,190)], w_start=3, w_end=6)

# RIGHT 人 (fuller): apex around (195, 95)
# 撇 — from apex curving down-left, ends around (135, 270)
stroke([(197,90), (180,160), (160,220), (140,275)], w_start=7, w_end=3)
# 捺 — from apex sweeping down-right with thick foot ending around (260, 275)
stroke([(200,105), (220,170), (240,220), (265,275)], w_start=3, w_end=9)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0118_从/01_从.png")
