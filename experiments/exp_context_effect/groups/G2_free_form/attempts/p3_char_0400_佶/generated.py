"""
佶 = 亻 (left) + 吉 (right), where 吉 = 士 (top) + 口 (bottom).

# SIGNATURE CHECK (士 sibling row, applied to 士 sub-component of 吉):
# 士 = TOP 横 LONGER than bottom (~1.5x). Distinguishes from 土.

Layout on 300x300 canvas:
- 亻 occupies left ~30% (撇 from ~(95,80) down-left to ~(60,175); 竖 from ~(95,80) down to ~(90,255))
- 吉 occupies right ~65%, centered horizontally around x=200
  - 士 top: top-横 (long ~118-260), 竖 (center down), bottom-横 (short ~150-235)
  - 口 bottom: rectangle ~ (145,205)-(255,265)
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
ink = (0, 0, 0)


def stroke(pts, width=7):
    d.line(pts, fill=ink, width=width, joint="curve")


# ---- 亻 (person radical, left) ----
# 撇: from top ~(100, 70) sweeping down-left to (55, 190)
stroke([(100, 70), (92, 100), (80, 135), (65, 170), (55, 195)], width=8)
# 竖: attaches to 撇 midway (~y=115), goes straight down
stroke([(88, 118), (88, 265)], width=8)

# ---- 吉 (right side): 士 on top + 口 on bottom ----
# 士 top-横 (LONGER, ~1.5x)
stroke([(130, 70), (270, 70)], width=8)
# 士 竖 (center vertical, short)
stroke([(200, 70), (200, 155)], width=8)
# 士 bottom-横 (SHORTER)
stroke([(155, 155), (245, 155)], width=8)

# 口 rectangle (bottom of 吉)
# top横 of 口
stroke([(145, 185), (260, 185)], width=8)
# left 竖
stroke([(145, 185), (145, 265)], width=8)
# right 竖折 (right side plus bottom)
stroke([(260, 185), (260, 265), (145, 265)], width=8)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0400_佶/01_佶.png"
)
