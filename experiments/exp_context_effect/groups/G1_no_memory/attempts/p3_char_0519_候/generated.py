"""Render 候 to 01_候.png (300x300, white bg, black ink)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=4):
    d.line(pts, fill="black", width=w, joint="curve")

# ---- Left radical 亻(person) ----
# slanted top stroke (piě)
line([(85, 70), (60, 130)], 4)
# vertical stroke
line([(82, 115), (85, 255)], 4)

# ---- Right side of 候 ----
# small top piě above the horizontal
line([(150, 55), (135, 85)], 3)

# top long horizontal (roof top)
line([(130, 85), (245, 85)], 4)
# right long vertical from roof going down (long descending)
line([(245, 85), (240, 200)], 4)

# inside: small horizontal near upper middle (top of inner ヨ)
line([(155, 115), (215, 115)], 3)
# short vertical piě coming down through inside (this is the extra vertical in 候)
line([(180, 115), (175, 165)], 3)
# second inner horizontal
line([(155, 145), (215, 145)], 3)

# bottom 矢-ish component
# horizontal beam under the box
line([(140, 195), (245, 195)], 4)
# short horizontal above the 大 crossing (the 一 inside)
line([(155, 175), (220, 175)], 3)
# piě down-left from beam
line([(180, 195), (140, 265)], 4)
# nà down-right from beam center-ish
line([(185, 205), (255, 265)], 5)

os.makedirs(os.path.dirname(__file__), exist_ok=True)
out = os.path.join(os.path.dirname(__file__), "01_候.png")
img.save(out)
print("wrote", out)
