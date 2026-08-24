"""
伺 = 亻 (left, narrow) + 司 (right, wider).

# SIGNATURE CHECK (per sibling_signature_checklist.md / TIER-0):
#   target contains 亻 as component -> paste 亻 signature: 撇 + tall 竖.
#   target contains 横折钩 in 司 -> hook flicks UP-and-LEFT (~-105°..-120°).

Strokes (7 total):
  亻 (2 strokes):
    (1) 撇 from upper apex sloping down-left,
    (2) tall 竖 from just below apex going straight down.
  司 (5 strokes):
    (1) 横折钩: 横 across top -> right 竖 down -> UP-LEFT hook
        (this wraps top+right of the shape; opens to the LEFT).
    (2) 一 short horizontal inside, sitting under the top bar,
        starting near left opening extending right.
    (3) 口 竖 — left side of small mouth (inside, below the middle 一).
    (4) 口 横折 — top + right of small mouth.
    (5) 口 横 — bottom of small mouth.

Layout: 亻 in left ~25% (x 30-90), 司 in right ~65% (x 105-275).
Precedent: p3_char_0156_们 (亻+门) — same left-column pattern.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 8

def line(pts, width=LW):
    d.line(pts, fill=INK, width=width, joint="curve")

# ---- 亻 (person radical) — left column, narrow ----
apex_x, apex_y = 70, 68
# 撇: apex ~(70, 68), curves down-left to (30, 220)
pts_pie = [(apex_x, apex_y), (60, 115), (45, 170), (28, 228)]
line(pts_pie, width=9)

# 竖: from just below apex straight down to (70, 275)
line([(apex_x, apex_y + 30), (apex_x - 2, 278)], width=9)

# ---- 司 — right column, wider ----
# (1) 横折钩: top horizontal, right vertical, then UP-LEFT hook.
# top-across
top_h = [(115, 75), (180, 72), (255, 78)]
line(top_h, width=9)
# right-down (continuous with top; slight taper inward at bottom)
right_v = [(255, 78), (258, 160), (253, 250)]
line(right_v, width=9)
# hook: pronounced UP-and-LEFT flick from bottom of right 竖
hook = [(253, 250), (238, 240), (218, 226)]
line(hook, width=9)

# (2) middle 一: short horizontal inside, under the top bar.
# Starts at the left opening (~x=120) extending right (~x=225).
line([(122, 135), (170, 133), (228, 138)], width=8)

# (3)-(5) small 口 inside/below the middle 一.
# Bounding: left=140, right=235, top=165, bottom=225.
mouth_L, mouth_R = 140, 235
mouth_T, mouth_B = 168, 228

# (3) left 竖 of 口
line([(mouth_L, mouth_T), (mouth_L + 2, mouth_B)], width=7)
# (4) 横折 of 口: top + right
line([(mouth_L, mouth_T), (mouth_R - 5, mouth_T + 2)], width=7)
line([(mouth_R - 5, mouth_T + 2), (mouth_R, mouth_B - 2)], width=7)
# (5) bottom 横 of 口
line([(mouth_L, mouth_B), (mouth_R, mouth_B - 2)], width=7)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0316_伺/01_伺.png"
img.save(out)
print("saved", out)
