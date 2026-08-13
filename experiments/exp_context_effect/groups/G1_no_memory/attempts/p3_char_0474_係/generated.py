"""G1 render of 係 (Phase 3 character).
Layout: 亻 radical on the left, 系 on the right.
Revised for cleaner proportions closer to GT.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- 亻 (person radical) on left ----
# 撇 (left-falling stroke starting from top)
stroke([(95, 60), (55, 210)], width=6)
# 竖 (vertical) from the middle of the 撇 downward
stroke([(78, 130), (78, 245)], width=6)

# ---- 系 on right, roughly centered around x=195, spanning y=55..255 ----
# Top 丿 (short slash coming down-left to make top of 系)
stroke([(200, 55), (170, 90)], width=5)
# Top horizontal-ish stroke going right from top
stroke([(180, 78), (240, 68)], width=5)

# Upper 幺 loop — triangular
stroke([(180, 85), (170, 115)], width=5)   # left slant
stroke([(230, 82), (240, 115)], width=5)   # right slant
stroke([(172, 115), (238, 115)], width=5)  # bottom of upper loop

# Lower 幺 loop
stroke([(185, 120), (175, 150)], width=5)  # left slant
stroke([(225, 120), (235, 150)], width=5)  # right slant
stroke([(175, 150), (235, 150)], width=5)  # bottom of lower loop

# 小 base of 系
# center vertical hook
stroke([(205, 155), (205, 230)], width=6)
# small hook at the very bottom (curls left)
stroke([(205, 230), (188, 220)], width=5)
# left dot/slash 丿
stroke([(180, 175), (150, 245)], width=5)
# right dot/slash 乀
stroke([(230, 175), (260, 245)], width=5)

out_path = os.path.join(os.path.dirname(__file__), "01_係.png")
img.save(out_path)
print("saved", out_path)
