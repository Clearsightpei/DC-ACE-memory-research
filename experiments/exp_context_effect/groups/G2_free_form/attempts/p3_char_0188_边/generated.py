"""
边 = 辶 (walking radical, bottom-left wrap) + 力 (upper-right).
力 = 横折钩 + 撇
辶 = 点 + 横折折撇 + 平捺 (simplified: dot then swoosh + long捺)

Hook flick rule: 横折钩 in 力 flicks UP-and-LEFT at terminal.
"""
from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=8):
    if len(pts) < 2:
        return
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    for p in pts:
        d.ellipse([p[0]-width/2, p[1]-width/2, p[0]+width/2, p[1]+width/2], fill="black")

def bezier(p0, p1, p2, n=30):
    return [(
        (1-t)**2*p0[0] + 2*(1-t)*t*p1[0] + t*t*p2[0],
        (1-t)**2*p0[1] + 2*(1-t)*t*p1[1] + t*t*p2[1]
    ) for t in [i/n for i in range(n+1)]]

# --- 力 in upper-right (roughly x: 140-250, y: 40-170) ---
# 横折钩: horizontal top, fold down, hook flick up-left at terminal
top_h = [(150, 55), (245, 60)]
fold_v = bezier((245, 60), (240, 130), (215, 175), n=25)
hook_flick = [(215, 175), (200, 160)]  # up-and-left flick
stroke(top_h + fold_v + hook_flick, width=8)

# 撇 in 力: from upper-middle diagonally down to bottom-left of 力
pie_pts = bezier((180, 90), (170, 140), (145, 195), n=25)
stroke(pie_pts, width=8)

# --- 辶 wrapping bottom-left ---
# 点 (dot at upper-left of radical zone, ~ (55, 100))
dot = bezier((50, 95), (60, 105), (70, 118), n=15)
stroke(dot, width=9)

# 横折折撇: starts around (75, 145), goes right-down, folds, then 撇 down-left
zigzag = ([(75, 145), (105, 140), (110, 170), (85, 195), (75, 220), (60, 240)])
stroke(zigzag, width=8)

# 平捺: long sweeping stroke from lower-left up-and-right across bottom
pn = bezier((45, 245), (140, 275), (270, 250), n=40)
stroke(pn, width=9)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0188_边/01_边.png")
print("saved")
