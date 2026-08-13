"""仲 = 亻 (left, person radical) + 中 (right).
亻: 撇 (top-right down-left flick) + 竖 (long vertical, upper start ~mid of 撇).
中: 口 rectangle centered, then long 竖 piercing through top-to-bottom, extending below.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)

def stroke(pts, width=7):
    d.line(pts, fill=INK, width=width, joint="curve")

# ---- 亻 (person radical, left) ----
# 撇: top-right → sweep down-left
pie_pts = [(105, 70), (95, 100), (80, 135), (60, 175), (48, 205)]
stroke(pie_pts, width=7)

# 竖: from just below the top of the 撇, straight down
stroke([(97, 108), (97, 260)], width=8)

# ---- 中 (right) ----
# 口 rectangle (top, right, bottom, left as separate strokes for calligraphic feel)
left_x, right_x = 160, 245
top_y, bot_y = 95, 180

# top horizontal (of 口)
stroke([(left_x, top_y), (right_x, top_y)], width=7)
# left vertical
stroke([(left_x, top_y), (left_x, bot_y)], width=7)
# right vertical (with tiny hook feel — just straight down here)
stroke([(right_x, top_y), (right_x, bot_y)], width=7)
# bottom horizontal
stroke([(left_x, bot_y), (right_x, bot_y)], width=7)

# 竖: long vertical piercing through middle of 口, extending above and below
mid_x = (left_x + right_x) // 2
stroke([(mid_x, 55), (mid_x, 275)], width=9)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0242_仲/01_仲.png")
