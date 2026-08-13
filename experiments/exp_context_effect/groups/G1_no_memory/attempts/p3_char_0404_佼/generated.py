"""Render 佼 (person radical 亻 + 交) at 300x300."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=5):
    d.line(pts, fill="black", width=w, joint="curve")

# ---- Left: 亻 (person radical) ----
# Piě: from top, sweeping down-left
line([(78, 75), (52, 155)], w=6)
# Vertical: descends from mid of piě straight down
line([(70, 130), (72, 265)], w=6)

# ---- Right: 交 ----
# Top dot (short piě) above the horizontal
line([(158, 55), (148, 78)], w=6)
# Horizontal stroke (heng) — the wide top bar
line([(112, 100), (245, 100)], w=6)
# Left dot of 父 (piě-dot below heng, left side)
line([(148, 115), (132, 140)], w=6)
# Right dot of 父 (na-dot below heng, right side)
line([(210, 115), (226, 140)], w=6)
# Big piě: from center-top sweeping down-left to bottom
line([(180, 150), (110, 270)], w=6)
# Big nà: from center-top sweeping down-right to bottom
line([(175, 155), (252, 270)], w=6)

img.save(os.path.join(os.path.dirname(__file__), "01_佼.png"))
print("saved")
