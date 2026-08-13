"""Render 造 (zao) at 300x300, white background, black ink.

Structure: 辶 (walking radical, left+bottom) + 告 (upper right).
告 = 丿 + 土 (three horizontals + vertical) + 口.
辶 = 丶 (top dot) + 横折折撇 (middle turns) + 平捺 (long sweep).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 4

def line(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

# ============ Right side: 告 ============
# 丿 slash at top
line([(178, 45), (155, 78)], width=LW)

# short vertical (top of 土 part)
line([(200, 55), (200, 88)], width=LW)

# First horizontal (long — top of 土)
line([(140, 90), (260, 88)], width=LW)

# Continue vertical through
line([(200, 88), (200, 148)], width=LW)

# Second horizontal (middle of 土)
line([(160, 118), (245, 116)], width=LW)

# Third horizontal (bottom of 土 — longest)
line([(140, 148), (260, 146)], width=LW)

# 口 (mouth) box beneath
# left vertical (竖)
line([(160, 155), (160, 220)], width=LW)
# top + right (横折)
line([(160, 155), (245, 155)], width=LW)
line([(245, 155), (247, 220)], width=LW)
# bottom (横)
line([(160, 220), (247, 220)], width=LW)

# ============ Left/bottom: 辶 radical ============
# 丶 top dot
line([(78, 55), (95, 78)], width=LW+1)

# 横折折撇 — starts as short horizontal, folds down, folds again into slash
# First segment: small horizontal
line([(55, 108), (110, 108)], width=LW)
# Fold down-left
line([(110, 108), (85, 138)], width=LW)
# Second small horizontal
line([(85, 138), (125, 138)], width=LW)
# Fold into slash down-left
line([(125, 138), (95, 195)], width=LW)

# 平捺 — long sweeping bottom stroke
# Start upper-left, curve down, then long sweep right with slight uptick
line([(60, 210), (110, 260)], width=LW+1)
line([(110, 260), (270, 250)], width=LW+1)
line([(270, 250), (285, 235)], width=LW+1)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0527_造/01_造.png")
print("saved")
