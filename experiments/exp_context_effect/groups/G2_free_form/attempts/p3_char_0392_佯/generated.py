"""
佯 = 亻 (left, ~30% width) + 羊 (right, ~55% width)

Cited memory:
#   file  = composition_rules.md
#   family = 亻+X
#   rule  = 亻 sits LEFT x=40-110; body sits RIGHT x=120-260 y=60-260;
#           亻 = short 撇 (95,60)->(50,130) + 竖 (75,120)->(75,240).
#           Body scales full-height on right ~55%.

羊 breakdown (top-to-bottom):
  1) short 丶/撇 dots at top (like 丷) — left one is 撇, right one is 点
  2) three horizontals (top short, middle short, bottom LONGEST)
  3) central 竖 through all horizontals to bottom
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=8):
    d.line(pts, fill="black", width=width, joint="curve")

# --- 亻 (left radical) ---
# 撇: starts upper-right, ends lower-left (short, ~85 px)
stroke([(100, 65), (85, 95), (65, 125), (48, 145)], width=8)
# 竖: straight vertical
stroke([(78, 118), (78, 245)], width=9)

# --- 羊 (right body) ---
# right body region: x=125..270, y=55..265
# Two top dots (丷): left = 撇 sloping down-left, right = 点 sloping down-right
stroke([(175, 60), (162, 82)], width=8)   # left 撇 dot
stroke([(220, 60), (232, 82)], width=8)   # right 点 dot

# Three horizontals (top -> middle -> bottom, bottom longest)
stroke([(160, 108), (235, 108)], width=7)   # top 横 (short)
stroke([(155, 158), (240, 158)], width=7)   # middle 横 (slightly longer)
stroke([(135, 215), (265, 215)], width=8)   # bottom 横 (longest)

# Central 竖 through the horizontals (from just above top-横 to bottom of char)
stroke([(198, 90), (198, 268)], width=9)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0392_佯/01_佯.png")
