"""
Render 疡 (yang, sore) as 300x300 PNG.

Structure: 疒 (sickness radical, left) + simplified 昜/力-like (right).

Left 疒:
  - dot at top-center
  - long horizontal
  - long left-descending stroke from below horizontal to bottom-left
  - two small dashes on inside of the descent

Right:
  - one short curved slash near top (like 丿)
  - 力-shape (横折钩 + 撇) below, larger

Hook rule: any 钩 flicks UP-and-LEFT toward interior.
"""
from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

def line(pts, w=6):
    d.line(pts, fill="black", width=w, joint="curve")

# ---- LEFT: 疒 ----
# top-center dot
line([(118, 45), (135, 62)], w=8)

# long horizontal (top of the radical) - extends across full character
line([(55, 82), (230, 78)], w=7)

# long descending stroke: from just below horizontal, curves down-left
line([(120, 82), (108, 130), (85, 190), (55, 265)], w=7)

# two dashes on inside of the descent
line([(80, 120), (100, 130)], w=6)
line([(60, 180), (85, 195)], w=6)

# ---- RIGHT: slash + 力 ----
# short slash (丿) upper-right area (this is the 一 of 昜 simplified as slash-ish)
line([(200, 100), (180, 130)], w=6)

# 力: horizontal
line([(155, 145), (240, 143)], w=6)

# 横折钩: fold down and curve to bottom, with UP-LEFT hook
line([(240, 143), (245, 175), (225, 225), (200, 260)], w=7)
# hook flick UP-and-LEFT
line([(200, 260), (180, 245)], w=7)

# 撇 inside 力: from top-mid of the horizontal down-left
line([(200, 155), (155, 250)], w=7)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0384_疡/01_疡.png"
)
