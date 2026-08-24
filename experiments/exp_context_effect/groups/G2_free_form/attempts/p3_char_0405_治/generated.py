"""
治 (zhi) — 氵 + 台
Left: 氵 three water dots (upper 点, middle 点, bottom 提 flicking up-right)
Right: 台 — 厶 on top (撇 + 折 with tucked 点), 口 on bottom
"""
from PIL import Image, ImageDraw

W = 300
img = Image.new("RGB", (W, W), "white")
d = ImageDraw.Draw(img)

def line(pts, width=7):
    d.line(pts, fill="black", width=width, joint="curve")

def dab(x, y, r=5):
    d.ellipse([x-r, y-r, x+r, y+r], fill="black")

# ============ Left: 氵 three drops water radical ============
# Drop 1 (upper 点): short slanted stroke, top-left to bottom-right
line([(58, 85), (85, 108)], width=8)
# Drop 2 (middle 点): similar slanted stroke, slightly further left
line([(48, 140), (78, 162)], width=8)
# Drop 3 (bottom 提): flick from lower-left going up-right
line([(58, 220), (95, 200)], width=7)

# ============ Right: 台 ============
# 厶 on top: 撇 + 折 (with 点)
# 撇: from top-right going down-left in a curve
# Approximate a curve
pts_pie = [(205, 75), (190, 95), (170, 120), (150, 140)]
line(pts_pie, width=7)
# 折: starts at top of 撇, goes horizontally right, then hooks down with a 点
# Start from where 撇 begins area, small horizontal to the right, then curl down-left as 点
pts_zhe = [(180, 100), (220, 115), (210, 140), (195, 148)]
line(pts_zhe, width=7)

# ============ 口 on bottom ============
# roughly a rectangle with slight tapering (top-left corner starts, right side has 折 corner)
# left vertical
line([(148, 195), (148, 260)], width=7)
# top and right (as one continuous 横折)
line([(148, 195), (230, 192), (230, 260)], width=7)
# bottom horizontal
line([(148, 260), (232, 260)], width=7)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0405_治/01_治.png")
