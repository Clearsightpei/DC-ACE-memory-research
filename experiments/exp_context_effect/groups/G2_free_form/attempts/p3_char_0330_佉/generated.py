"""
p3_char_0330_佉 — 佉 = 亻 (left) + 去 (right).
去 = 土 (top) + 厶 (bottom).

# SIGNATURE CHECK (D. compound-sibling rule, applies to 土 sub-glyph):
# 土: BOTTOM 横 LONGER than top (~1.5×). Contrast sibling 士 where
# top 横 is longer. Enforce inside the 去 sub-glyph.

Layout on 300x300 canvas, white bg, black ink.
- 亻 occupies left ~1/3 (x ~50..90).
- 去 occupies right ~2/3 (x ~110..250).
  - 土 upper portion: two 横 + one 竖. Bottom 横 clearly longer.
  - 厶 lower portion: left 撇折 + right 点.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6  # base line width

def line(a, b, w=LW):
    d.line([a, b], fill=BLACK, width=w)

def poly(points, w=LW):
    d.line(points, fill=BLACK, width=w, joint="curve")

# ---------------- 亻 (person radical, left) ----------------
# 撇: from upper-mid down-left to lower-left
poly([(88, 55), (78, 90), (62, 140), (48, 220)], w=LW)
# 竖: from mid-right of 撇, straight down
poly([(78, 120), (78, 260)], w=LW)

# ---------------- 去 (right side) ----------------
# 土 upper: top 横 (shorter), 竖, bottom 横 (longer ~1.5x)
top_hor_L, top_hor_R = 145, 215   # length 70
bot_hor_L, bot_hor_R = 125, 235   # length 110 (~1.57x top)

# top 横 (slight upward slant like the GT)
poly([(top_hor_L, 90), (top_hor_R, 82)], w=LW)
# 竖 through the middle
poly([(180, 70), (180, 155)], w=LW)
# bottom 横 (longer, slight rise to the right)
poly([(bot_hor_L, 152), (bot_hor_R, 145)], w=LW)

# ---------------- 厶 (lower portion of 去) ----------------
# 撇折: single continuous stroke from upper-right, down-left, then flat-right
poly([(200, 175), (170, 205), (150, 245), (215, 250)], w=LW)
# 点: short down-right dot from top area of 厶
poly([(198, 195), (218, 225)], w=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0330_佉/01_佉.png")
