"""Render 侯 (marquis) at 300x300, white bg, black ink.

Structure: 亻(person radical) on left + 矦-body on right.
Right body top-to-bottom:
  - short 丿 (top-left tick)
  - long 一 (top horizontal)
  - short 一 (second horizontal, inside)
  - 大-like bottom: 一 + 丿 (long) + 捺 (long)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(pts, width=4):
    d.line(pts, fill="black", width=width, joint="curve")


# ---- Left radical 亻 ----
# 撇 (curved top - falling left)
stroke([(85, 80), (75, 110), (60, 155)], width=5)
# 竖 (long vertical)
stroke([(85, 115), (85, 265)], width=5)

# ---- Right body 矦 ----
# Small 丿 at top
stroke([(165, 65), (155, 90)], width=4)
# Top horizontal 一 (roof)
stroke([(135, 95), (245, 95)], width=5)

# Second (inner) horizontal
stroke([(155, 130), (225, 130)], width=4)

# Third horizontal (a bit above the 大 group)
stroke([(140, 165), (240, 165)], width=5)

# ---- Bottom 大-like group ----
# Horizontal
stroke([(125, 200), (250, 200)], width=5)
# Long 丿 (from top-center going down-left)
stroke([(185, 175), (170, 215), (130, 280)], width=5)
# 捺 (from center going down-right, thickens)
stroke([(185, 200), (215, 235), (260, 285)], width=6)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0464_侯/01_侯.png"
)
print("saved")
