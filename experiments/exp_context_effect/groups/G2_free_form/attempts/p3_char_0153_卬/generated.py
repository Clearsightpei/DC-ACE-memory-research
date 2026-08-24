"""
卬 — 4 strokes, left-right composition.
Left component (卬-left, 匚-like with hook): 撇 at top + long 竖折 turning
right at bottom (like a broad L with the vertical rising then flick).
Actually from GT: left = short 撇 (upper) + long descending stroke that
hooks up-right at bottom.
Right component 卩: 横折钩 (short horizontal turning into vertical hook)
+ long 竖 (dropping from top down through and past the box).

Signature: NOT a sibling-risk item. 4 strokes. Two-part L/R layout with
gap in middle. Right side extends lower than left. Hook (in 卩's 横折钩)
flicks UP-and-LEFT per TIER-0 rule B.
"""
from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def bez(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts

def stroke(pts, width=8):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=width)
    # round joints
    for p in pts:
        d.ellipse([p[0] - width / 2, p[1] - width / 2,
                   p[0] + width / 2, p[1] + width / 2], fill="black")

# --- LEFT component (卬-left form) ---
# Stroke 1: short 撇 at upper-left area, sloping down-left
s1 = bez((115, 55), (100, 75), (78, 100), n=30)
stroke(s1, width=7)

# Stroke 2: long 竖提 — long descent then flick right along bottom
s2_down = [(90, 85), (88, 130), (87, 180), (90, 230)]
s2_flick = bez((90, 230), (110, 255), (155, 250), n=30)
stroke(s2_down + s2_flick, width=8)

# --- RIGHT component 卩 ---
# Stroke 3: 横折钩 — short horizontal top then vertical with hook up-left
top_h = [(175, 75), (195, 72), (215, 70), (230, 70)]
right_v = [(232, 70), (233, 110), (234, 150), (233, 195)]
hook = bez((233, 195), (225, 200), (208, 188), n=25)
stroke(top_h + right_v + hook, width=8)

# Stroke 4: long 竖 — drops from top down past the box, extends low
s4 = [(188, 62), (189, 120), (191, 180), (192, 235), (193, 275)]
stroke(s4, width=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0153_卬/01_卬.png")
print("wrote 01_卬.png")
