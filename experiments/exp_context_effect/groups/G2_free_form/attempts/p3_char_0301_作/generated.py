"""
作 = 亻 (person radical, left, narrow) + 乍 (right, wider).

Reference precedents (from pass_index):
  - p3_char_0156_们 (PASS): 亻 on left, right component in ~60% width.
  - p2_radical_029_亻 (PASS): 亻 shape reference.

亻 (2 strokes):
  1) 撇 from upper apex sloping down-left
  2) tall 竖 from just below apex going straight down

乍 (5 strokes) — right component:
  1) top 撇 (short, upper-left of 乍) sloping down-left
  2) top 横 (short horizontal)
  3) long 竖 going down from top area through the horizontals
  4) middle 横 (short, from 竖 going right)
  5) bottom 横 (slightly longer, from 竖 going right)

Layout: 亻 in left ~30% (x 40-100), 乍 in right ~60% (x 120-260).
No hooks in 作 — nothing to flick.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 8  # stroke width

def line(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

# ---- 亻 (person radical) — left column, narrow ----
apex_x, apex_y = 78, 72
# 撇: apex → down-left curve to (35, 228)
pts_pie = [(apex_x, apex_y), (68, 115), (52, 170), (35, 228)]
line(pts_pie, width=9)
# 竖: from just below apex straight down (person's leg)
line([(apex_x, apex_y+30), (apex_x-2, 278)], width=9)

# ---- 乍 (right component) ----
# (1) top 撇: from apex ~(175, 60) down-left to (128, 118)
# The 撇 meets the top-横 near its start
line([(175, 60), (158, 85), (140, 108), (128, 120)], width=9)

# (2) top 横: horizontal across the top, from where 撇 crosses through
# to the right edge (~145, 90) to (255, 88)
line([(145, 92), (200, 88), (255, 88)], width=9)

# (3) long 竖: descends from top area (~205, 78) all the way down to (~205, 280)
# Main vertical spine of 乍
line([(205, 78), (205, 175), (205, 280)], width=10)

# (4) middle 横: from spine going right, shorter
line([(205, 175), (240, 174), (265, 175)], width=8)

# (5) bottom 横: from spine going right, at the bottom
line([(205, 258), (240, 258), (268, 258)], width=9)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0301_作/01_作.png")
print("saved 01_作.png")
