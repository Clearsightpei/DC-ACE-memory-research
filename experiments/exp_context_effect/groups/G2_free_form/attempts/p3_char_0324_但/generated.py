"""
但 = 亻 (left) + 旦 (right).
旦 = 日 (top box, 4 strokes) + 一 (long bottom horizontal, 1 stroke).

Strokes (7 total):
  亻: (1) 撇 apex → down-left, (2) 竖 straight drop.
  日: (3) 竖 left wall, (4) 横折 (top + right wall),
      (5) 横 internal middle bar.
  旦: (6) 横 bottom of 日 (closes box, coincides with top of 一 zone? no,
         inside 日 the bottom bar closes it),
      (7) 一 long bottom horizontal (base of 旦, wider than 日).

Note: sibling risk here is with 但 vs 伯/佃 etc. — the distinguishing
feature of 旦 is a small 日 sitting on a LONG horizontal that extends
wider than the box. That long bottom line must clearly overhang both
sides of the 日 box.

Layout: 亻 in left ~28% (x 30-95), 旦 in right ~62% (x 120-275).
"""
from PIL import Image, ImageDraw
import random

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (15, 15, 15)
LW = 8

random.seed(3)

def wobble(p, amp=1.0):
    x, y = p
    return (x + random.uniform(-amp, amp), y + random.uniform(-amp, amp))

def brush(pts, width=LW, dabs=True):
    pts_w = [wobble(p) for p in pts]
    d.line(pts_w, fill=INK, width=width, joint="curve")
    if dabs:
        for p in (pts_w[0], pts_w[-1]):
            r = width * 0.55
            d.ellipse((p[0]-r, p[1]-r, p[0]+r, p[1]+r), fill=INK)

# ---- 亻 (person radical) — left column, narrow ----
# 撇: apex ~(80, 60), down-left curving to (30, 210)
apex_x, apex_y = 82, 62
pie = [(apex_x, apex_y), (72, 105), (55, 155), (32, 215)]
brush(pie, width=9)

# 竖: from a bit below apex straight down to (80, 268)
brush([(apex_x, apex_y + 28), (apex_x - 2, 270)], width=9)

# ---- 旦 (right column) ----
# 日 box: tall-narrow but not extreme; sits in upper 2/3.
LEFT   = 135
RIGHT  = 250
TOP    = 55
BOX_BOT = 220
MID_Y  = (TOP + BOX_BOT) // 2 + 4

# (3) 竖 left wall
brush([(LEFT, TOP + 2), (LEFT, BOX_BOT)], width=LW)

# (4) 横折 top + right wall
top_left  = (LEFT - 2, TOP)
top_right = (RIGHT, TOP)
shoulder  = (RIGHT + 2, TOP + 6)
bot_right = (RIGHT + 2, BOX_BOT)
brush([top_left, top_right, shoulder, bot_right], width=LW)

# (5) internal 横 middle bar
brush([(LEFT + 3, MID_Y), (RIGHT - 3, MID_Y)], width=LW - 1)

# (6) 横 closing bottom of 日 box
brush([(LEFT - 2, BOX_BOT), (RIGHT + 2, BOX_BOT)], width=LW)

# (7) 一 long bottom horizontal — extends WIDER than the 日 box
# Overhangs both sides visibly. This is the identity bit of 旦.
BASE_Y = 255
brush([(108, BASE_Y - 2), (180, BASE_Y), (282, BASE_Y + 3)], width=LW + 1)

out = ("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
       "groups/G2_free_form/attempts/p3_char_0324_但/01_但.png")
img.save(out)
print("wrote", out)
