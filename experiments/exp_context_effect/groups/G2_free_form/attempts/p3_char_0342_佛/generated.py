"""
佛 = 亻 (left) + 弗 (right), revised pass 2.

Improvements over pass 1:
- 亻: shorter 撇, longer 竖 that extends fuller down (per GT).
- 弗: add a proper top-left curl (横折) that connects, extend both
  verticals well below the lower horizontal, right 竖钩 flicks UP-LEFT.
- Widen gap between the two horizontals; keep them tight-parallel.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def line(pts, width=6):
    draw.line(pts, fill="black", width=width, joint="curve")

# --- 亻 (left person radical), occupies x 40-105 ---
# 短撇: from top down to lower-left (steeper angle)
line([(100, 75), (60, 155)], width=8)
# 长竖: from the crossing point straight down
line([(88, 128), (88, 265)], width=8)

# --- 弗 (right side), occupies x 125-270 ---
# Top-left curl (a 横折-like small hook forming the top-left of 弗)
# Small horizontal going right, then folds down
line([(155, 78), (200, 82)], width=6)
line([(200, 82), (198, 105)], width=6)

# Upper horizontal (crosses both verticals)
line([(150, 118), (260, 115)], width=6)

# Lower horizontal (longer, crosses both verticals lower)
line([(140, 180), (270, 178)], width=6)

# Left vertical 竖 (starts near top, curves slightly, ends below with a slight left tail like a 撇)
# Draw as a series of near-vertical points to give a subtle S-shape
line([(178, 70), (180, 130), (183, 200), (178, 245)], width=8)
# Small tail extension (ends with a leftward flick)
line([(178, 245), (160, 275)], width=6)

# Right vertical 竖钩 (starts top, straight down, ends with UP-LEFT hook)
line([(232, 78), (238, 265)], width=8)
# Hook: UP-and-LEFT flick (per Tier-0 rule)
line([(238, 265), (215, 245)], width=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0342_佛/01_佛.png")
print("saved")
