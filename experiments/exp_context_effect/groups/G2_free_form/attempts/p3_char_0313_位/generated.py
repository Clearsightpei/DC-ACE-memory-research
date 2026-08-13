"""
位 = 亻 (person radical, left, narrow) + 立 (right, wider).

# SIGNATURE CHECK:
#   target = 位
#   亻 sub-component: two strokes — 撇 from upper apex sloping down-left,
#                      then tall 竖 dropping from apex.
#   立 (5 strokes): 点 (top dot), 横 (short upper horizontal),
#                   点 (left slant middle), 撇 (right slant middle),
#                   横 (long bottom horizontal, widest).
# Layout: 亻 left ~30% (x 40-100), 立 right ~60% (x 120-270).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 8

def line(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

def dot(cx, cy, r=6):
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=INK)

# ---- 亻 (person radical) — left column, narrow ----
# 撇: apex ~(80, 65), curves down-left to (35, 235)
apex_x, apex_y = 82, 68
pts_pie = [(apex_x, apex_y), (70, 115), (55, 175), (38, 235)]
line(pts_pie, width=9)

# 竖: from just below apex straight down
line([(apex_x+2, apex_y+35), (apex_x-2, 280)], width=9)

# ---- 立 (right, wider) ----
# center around x=195
# (1) 点 — short top dot slanting down-right, top-center
d.line([(190, 60), (198, 78)], fill=INK, width=10)

# (2) 横 — short upper horizontal (narrower than bottom)
line([(158, 108), (230, 105)], width=8)

# (3) 点 — left slant middle (slants down-left)
d.line([(170, 148), (158, 178)], fill=INK, width=9)

# (4) 撇/点 — right slant middle (slants down-right)
d.line([(222, 148), (234, 178)], fill=INK, width=9)

# (5) 横 — long bottom horizontal (widest stroke)
line([(132, 235), (200, 232), (272, 236)], width=10)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0313_位/01_位.png")
print("saved 01_位.png")
