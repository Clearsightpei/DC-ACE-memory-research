"""G1 render of 疵 (cī) — 疒 radical + 此 inside. Revision 2."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=3):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- 疒 radical ----
# top short slanted dot (点)
stroke([(135, 45), (150, 65)], width=4)

# horizontal (top bar of 疒), fairly wide
stroke([(100, 85), (230, 85)], width=3)

# long left-falling 撇 from horizontal down to bottom-left
stroke([(150, 75), (120, 140), (85, 210), (55, 265)], width=3)

# two 点 on the left (inside the frame, along the left slope)
stroke([(95, 130), (75, 155)], width=4)   # upper (points down-left)
stroke([(105, 175), (85, 200)], width=4)  # lower

# ---- 此 inside (right/middle area, below horizontal) ----
# 止 (left half of 此) - compact
# short vertical
stroke([(150, 130), (150, 200)], width=3)
# left tick (short 竖)
stroke([(135, 155), (135, 195)], width=3)
# small horizontal cross
stroke([(135, 165), (165, 165)], width=3)
# base horizontal
stroke([(130, 205), (175, 205)], width=3)

# 匕 (right half of 此)
# horizontal-ish top stroke (short 横)
stroke([(185, 135), (215, 130)], width=3)
# vertical then curved base going right (the 竖弯钩)
stroke([(200, 120), (195, 175), (200, 220), (255, 220), (255, 205)], width=3)
# diagonal cross of 匕 (going up-right)
stroke([(185, 175), (240, 150)], width=3)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0580_疵/01_疵.png")
print("saved")
