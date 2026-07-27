"""Render 仕 (shì) — person radical 亻 + 士.
Output: 01_仕.png (300x300, white bg, black ink).
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
T = 5  # stroke thickness

def line(p1, p2, w=T):
    d.line([p1, p2], fill=INK, width=w)

def curve(points, w=T):
    d.line(points, fill=INK, width=w, joint="curve")

# ---- Left component: 亻 (person radical) ----
# 撇 (pie): starts upper-mid-left, sweeps down-left with slight curve
curve([(105, 70), (95, 115), (80, 165), (60, 220)], w=T)
# 竖 (shu): vertical from pie meeting point, extends to bottom
line((105, 130), (105, 275), w=T)

# ---- Right component: 士 (scholar) ----
# 横 (top heng): longer horizontal, top of 士
line((135, 100), (255, 100), w=T)
# 竖 (shu): vertical center of 士
line((195, 100), (195, 245), w=T)
# 横 (bottom heng): slightly shorter than top, per 士 convention
line((150, 245), (240, 245), w=T)

out_path = os.path.join(os.path.dirname(__file__), "01_仕.png")
img.save(out_path)
print(f"wrote {out_path}")
