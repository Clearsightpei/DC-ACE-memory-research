"""
佃 = 亻 (person radical, left, narrow) + 田 (right, boxy square with cross).

Layout:
  亻 in left ~30% (apex ~x 70, curves down-left; 竖 straight down)
  田 in right ~55% (box x 130-260, y 75-235, with internal cross)

田 strokes (5):
  1. 竖 (left wall)
  2. 横折 (top + right wall)
  3. 竖 (middle vertical, inside)
  4. 横 (middle horizontal, inside)
  5. 横 (bottom of box)

亻 strokes (2):
  1. 撇 from upper apex sloping down-left
  2. 竖 from near apex straight down (tall)

GT observation: 田 sits slightly higher than 亻's foot; 亻's 竖 extends
down slightly below 田's baseline.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 8

def line(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

def dab(cx, cy, r=4):
    d.ellipse([(cx-r, cy-r), (cx+r, cy+r)], fill=INK)

# ---- 亻 (person radical) — left, narrow ----
apex_x, apex_y = 78, 68
# 撇: from apex, curve down-left to about (32, 230)
pts_pie = [(apex_x, apex_y), (68, 115), (52, 170), (32, 232)]
line(pts_pie, width=9)

# 竖: just below apex, straight down (extend a bit lower)
line([(apex_x, apex_y + 28), (apex_x - 2, 278)], width=9)

# ---- 田 — right, boxy ----
TOP, BOT, L, R = 78, 235, 130, 258
MID_X = (L + R) // 2   # ~194
MID_Y = (TOP + BOT) // 2  # ~156

# Stroke 1: 竖 (left wall)
dab(L, TOP, 4)
line([(L, TOP), (L - 2, BOT)], width=8)

# Stroke 2: 横折 (top + right wall)
# top horizontal
line([(L - 2, TOP - 2), (R + 2, TOP)], width=8)
# shoulder dab
dab(R + 1, TOP + 2, 5)
# right vertical
line([(R + 2, TOP), (R, BOT)], width=8)

# Stroke 3: middle vertical (inside)
line([(MID_X, TOP + 3), (MID_X, BOT - 3)], width=7)

# Stroke 4: middle horizontal (inside)
line([(L + 2, MID_Y), (R - 2, MID_Y)], width=7)

# Stroke 5: bottom horizontal
line([(L - 2, BOT), (R + 2, BOT - 2)], width=8)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0322_佃/01_佃.png"
img.save(out)
print("saved", out)
