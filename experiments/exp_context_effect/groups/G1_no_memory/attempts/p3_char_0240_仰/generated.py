"""Render 仰 (yang) to a 300x300 PNG.

仰 = 亻 (person, left) + 卬 (right)
卬 = small ヒ-like left component + 卩 (seal, right)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 4


def line(pts, width=T):
    d.line(pts, fill=INK, width=width, joint="curve")


# ---- 亻 person radical (left) ----
# Slanted 丿 (piě)
line([(90, 70), (75, 130), (55, 205)], width=T)
# Vertical 丨
line([(92, 130), (92, 265)], width=T)

# ---- Middle component of 卬 (small 丿 + short horizontal + vertical) ----
# small piě at top
line([(150, 85), (140, 125)], width=T)
# short horizontal (crossbar)
line([(138, 118), (172, 118)], width=T)
# vertical descending
line([(155, 118), (155, 255)], width=T)

# ---- 卩 (right half of 卬) ----
# Top-right box: horizontal top + right vertical + bottom-right small hook (横折)
line([(195, 90), (240, 90), (240, 165), (222, 180)], width=T)
# Left long vertical of 卩 (the tall descender)
line([(195, 90), (195, 265)], width=T)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0240_仰/01_仰.png")
print("saved")
