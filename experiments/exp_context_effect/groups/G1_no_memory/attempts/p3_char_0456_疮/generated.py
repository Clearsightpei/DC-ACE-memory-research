"""Render 疮 (chuang - sore/wound) to a 300x300 PNG using PIL.
Character = 疒 (sickness radical) + 仓 (cang) inside.
Revision 2: improve proportions, fix 仓 to have curved bottom like 巴/㔾.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 4

def line(p0, p1, w=LW):
    d.line([p0, p1], fill="black", width=w)

def curve(points, w=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill="black", width=w)

# ============ 疒 (sickness radical) - spans left side ============
# Top dot (short slanted 点, upper-center)
line((135, 40), (150, 60))

# Horizontal top stroke of 疒 (广 top bar)
line((70, 80), (210, 80))

# Left long slant going down-left (the main slant of 疒/广)
curve([(115, 80), (95, 130), (70, 200), (45, 270)])

# Two short slant strokes on left side of 疒 (the 冫 marks)
line((105, 115), (80, 135))
line((95, 155), (70, 175))

# ============ 仓 (cang) - upper-right inside/beside 疒 ============
# 人 shape (roof) - apex around (170, 95)
line((170, 95), (135, 155))   # left slant (撇)
line((170, 95), (215, 145))   # right slant (捺)

# Middle short horizontal (the 一 under 人)
line((150, 165), (210, 165))

# Bottom part - like 㔾/巴: box with curved bottom-right
# top edge
line((155, 185), (215, 185))
# left vertical
line((155, 185), (155, 245))
# bottom edge with slight rise on right (curved 竖弯钩 style)
curve([(155, 245), (200, 245), (220, 235), (222, 215)])
# small inner horizontal
line((165, 215), (200, 215))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0456_疮/01_疮.png")
print("saved")
