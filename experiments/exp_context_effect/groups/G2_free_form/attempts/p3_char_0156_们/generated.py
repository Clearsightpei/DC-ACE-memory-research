"""
们 = 亻 (person radical, left, narrow) + 门 (right, wider).

# SIGNATURE CHECK (per sibling_signature_checklist.md):
#   target = 们
#   sub-signature = 门: top-left dot + 横折钩 with UP-LEFT hook
#   flick = 横折钩 terminal flicks UP-and-LEFT (~-105° to -120°)

Strokes:
  亻 (2 strokes): (1) 撇 from upper apex sloping down-left,
                  (2) tall 竖 from same apex going straight down.
  门 (3 strokes): (1) top-left 丶 (short dot), (2) tall left 竖,
                  (3) 横折钩: 横 across top -> right 竖 down -> UP-LEFT hook.

Layout: 亻 in left ~30% (x 40-100), 门 in right ~60% (x 120-260).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 8  # stroke width

def line(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

def dot(cx, cy, r=6):
    d.ellipse([cx-r, cy-r-1, cx+r+2, cy+r+2], fill=INK)

# ---- 亻 (person radical) — left column, narrow ----
# 撇: apex ~(75, 70), curves down-left to (35, 225)
apex_x, apex_y = 78, 72
pts_pie = [(apex_x, apex_y), (68, 115), (52, 170), (35, 228)]
line(pts_pie, width=9)

# 竖: from just below apex straight down to (78, 275) — the person's leg
line([(apex_x, apex_y+30), (apex_x-2, 275)], width=9)

# ---- 门 — right column, wider ----
# (1) top-left 丶 dot (short slanted stroke, becomes head of left 竖)
# In the GT the dot sits above/left of the left-竖's start
d.line([(128, 70), (135, 82)], fill=INK, width=10)

# (2) left 竖 of 门 — tall, from ~(135, 100) down to (135, 275)
line([(138, 105), (135, 278)], width=10)

# (3) 横折钩: 横 across top -> right 竖 down -> UP-LEFT hook
# horizontal top
top_h = [(150, 95), (200, 92), (258, 96)]
line(top_h, width=9)

# right vertical (slight taper inward)
right_v = [(258, 96), (256, 175), (252, 250)]
line(right_v, width=9)

# Hook: pronounced up-and-left flick from bottom of right 竖
hook = [(252, 250), (240, 240), (222, 225)]
line(hook, width=9)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0156_们/01_们.png")
print("saved 01_们.png")
