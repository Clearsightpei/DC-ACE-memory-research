"""Render 疖 (jiē) with PIL — 300x300, white bg, black ink."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(points, w=6):
    d.line(points, fill=BLACK, width=w, joint="curve")

# ---- 疒 (sickness radical) ----
# 1) 丶 top dot (slanting down-right, upper area)
stroke([(150, 55), (170, 78)], w=7)

# 2) 一 horizontal top (spans across, forms top of enclosure)
stroke([(80, 105), (235, 105)], w=6)

# 3) 丿 long left-falling — starts near left end of horizontal, curves down-left
stroke([(105, 105), (85, 165), (55, 245)], w=6)

# 4) 冫 two short dashes on left inside
stroke([(95, 165), (115, 175)], w=6)   # upper
stroke([(83, 205), (103, 215)], w=6)   # lower

# ---- 卩 (right side, inside radical enclosure) ----
# top box of 卩: small rectangle in upper right
# top horizontal (short, sits right of center)
stroke([(165, 130), (215, 130)], w=6)
# right side vertical going down (top box)
stroke([(215, 130), (215, 175)], w=6)
# bottom of top box
stroke([(165, 175), (215, 175)], w=6)

# left vertical of 卩 — long descending stroke, slight rightward curve at bottom
stroke([(165, 130), (165, 200), (170, 260)], w=6)

os.makedirs(os.path.dirname(__file__), exist_ok=True)
out_path = os.path.join(os.path.dirname(__file__), "01_疖.png")
img.save(out_path)
print(f"saved {out_path}")
