"""
Render 皃 (old form of 貌/兒 — 白 top + 儿 bottom).

Structure:
- Top: 白 (small squarish; 撇 + 竖 + 横 + inner 横 + bottom 横).
- Bottom: 儿 — a 撇 on the left; a 竖弯钩 on the right whose terminal
  hook flicks UP-and-LEFT (per TIER-0 rule B; this is a 见-family shape).

# SIGNATURE CHECK: 皃 = 白 (compact top-center) + 儿 (broad legs below).
# The right leg is a 竖弯钩; its terminal MUST flick UP-and-LEFT.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i+1]], fill="black", width=width)
    # rounded joints
    for (x, y) in pts:
        d.ellipse((x-width/2+1, y-width/2+1, x+width/2-1, y+width/2-1), fill="black")

# ---- Top: 白 (compact rectangle centered upper-half) ----
# rectangle roughly x=115..190, y=45..135
LX, RX = 115, 195
TY, BY = 55, 140

# small 撇 (top-left flick) leading into the 竖
stroke([(140, 45), (LX, 60)], width=5)

# left 竖 (top-left corner down)
stroke([(LX, 60), (LX, BY)], width=6)

# top 横折: horizontal top then折 down (right side of the box)
stroke([(LX, 60), (RX, 60), (RX, BY)], width=6)

# inner horizontal (middle bar of 白)
stroke([(LX+6, 98), (RX-6, 98)], width=5)

# bottom horizontal (closes the box)
stroke([(LX, BY), (RX, BY)], width=6)

# ---- Bottom: 儿 ----
# Left 撇 — starts near the middle-top area under 白 and sweeps down-left
stroke([(135, 155), (95, 260)], width=7)

# Right 竖弯钩 — starts under top-right of 白, goes down, curves right,
# then FLICKS UP-and-LEFT at the terminal.
# body straight down
right_body = [(175, 155), (175, 235)]
stroke(right_body, width=7)
# arc curving right along the bottom
arc = [(175, 235), (185, 250), (205, 260), (225, 262), (240, 258)]
stroke(arc, width=7)
# flick UP-and-LEFT (terminal hook) — angle roughly -105 to -115 deg
flick = [(240, 258), (232, 240)]
stroke(flick, width=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0356_皃/01_皃.png")
