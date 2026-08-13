"""Render 俯 (bow) - 亻 + 府"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=4):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)

# ===== LEFT: 亻 (person radical) =====
# Slanting stroke (撇) starting upper
stroke([(85, 65), (78, 100), (60, 155), (42, 215)], width=5)
# Vertical stroke
stroke([(82, 130), (82, 265)], width=5)

# ===== RIGHT: 府 =====
# 广 - top dot
stroke([(175, 45), (188, 62)], width=5)
# 广 - horizontal (a bit slanted, top)
stroke([(130, 82), (265, 75)], width=5)
# 广 - long left-falling stroke (撇) starting from left end of horizontal
stroke([(145, 82), (130, 135), (115, 195), (100, 260)], width=5)

# Inside 府 = 付 (亻 + 寸), positioned in the lower-right pocket
# small 亻 - slanting stroke
stroke([(165, 130), (155, 165), (148, 200)], width=4)
# small 亻 - vertical
stroke([(162, 155), (162, 235)], width=4)

# 寸 - horizontal (right side, inside)
stroke([(180, 155), (255, 150)], width=5)
# 寸 - vertical hook
stroke([(218, 150), (218, 225), (200, 232)], width=5)
# 寸 - dot on right
stroke([(232, 190), (248, 210)], width=5)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0556_俯/01_俯.png")
print("saved")
