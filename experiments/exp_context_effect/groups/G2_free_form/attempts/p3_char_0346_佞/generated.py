"""佞 = 亻 (left) + 二 (upper right) + 女 (lower right).
Revision: shorten 二's lower horizontal so it doesn't collide with 女;
redraw 女 with clearer 撇点 + 撇 + 横 topology.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=7):
    d.line(pts, fill="black", width=width, joint="curve")
    for (x, y) in [pts[0], pts[-1]]:
        r = width // 2
        d.ellipse([x-r, y-r, x+r, y+r], fill="black")

# ---- 亻 (left radical) ----
# 撇
stroke([(95, 55), (85, 100), (68, 150), (48, 205)], width=8)
# 竖
stroke([(88, 115), (88, 265)], width=8)

# ---- 二 (upper right) ----
# short 横 (top)
stroke([(165, 65), (215, 62)], width=7)
# 横 (below) - shorter than before
stroke([(150, 108), (230, 102)], width=8)

# ---- 女 (lower right) ----
# stroke 1: 撇点  (down-left curve, then down-right)
stroke([(215, 135), (190, 180), (165, 225), (150, 265)], width=8)
# 点 part of 撇点 - starts near the bend
stroke([(180, 195), (215, 235), (240, 265)], width=8)

# stroke 2: 撇 (main long 撇) - from upper-right through the character
stroke([(245, 145), (215, 200), (170, 275)], width=8)

# stroke 3: 长横 - the horizontal crossing
stroke([(140, 215), (270, 213)], width=8)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0346_佞/01_佞.png")
print("saved")
