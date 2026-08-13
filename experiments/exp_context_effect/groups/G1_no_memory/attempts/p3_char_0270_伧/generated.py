"""Render 伧 (cāng) = 亻 (left) + 仓 (right)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLK = (0, 0, 0)
LW = 5


def stroke(pts, w=LW):
    d.line(pts, fill=BLK, width=w, joint="curve")


# ---- 亻 person radical (left side) ----
# Left downward slant (piē)
stroke([(90, 95), (58, 165)], w=LW)
# Vertical (shù) - starts a bit right of slant's midpoint, extends down
stroke([(78, 135), (78, 270)], w=LW)

# ---- 仓 (right side) ----
# 人 top: left diagonal (piē) from apex
stroke([(200, 65), (135, 150)], w=LW)
# 人 top: right diagonal (nà)
stroke([(200, 65), (260, 155)], w=LW)

# Small horizontal 一 below the roof
stroke([(170, 155), (230, 155)], w=LW)

# Bottom enclosure (kind of like 巳/㔾):
# Left downward curve (piē) starting from mid, going down-left with hook up
stroke([(175, 175), (155, 230), (170, 275), (200, 265)], w=LW)
# Top horizontal + right vertical + bottom horizontal = a ⊐ shape opening left
stroke([(175, 178), (235, 178)], w=LW)          # top
stroke([(235, 178), (235, 240)], w=LW)          # right vertical
stroke([(235, 240), (180, 240)], w=LW)          # bottom horizontal closing back

out = os.path.join(os.path.dirname(__file__), "01_伧.png")
img.save(out)
print("saved", out)
