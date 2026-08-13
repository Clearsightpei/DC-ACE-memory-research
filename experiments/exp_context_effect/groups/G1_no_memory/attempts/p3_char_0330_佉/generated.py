"""Render 佉 (kā) — 亻 (person radical) + 去 (leave).
G1 control: PIL, 300x300, cold render from GT observation.
Revision 1: fix 亻 slant and correct 厶 shape."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- Left component: 亻 (person radical) ----
# 撇 (slanted stroke) — from upper-right to lower-left
stroke([(105, 60), (95, 90), (80, 130), (60, 180)], width=6)
# 竖 (vertical stroke) — starts around mid of 撇, goes straight down
stroke([(88, 120), (88, 265)], width=6)

# ---- Right component: 去 ----
# 土 top: short horizontal
stroke([(170, 75), (225, 72)], width=6)
# 土 middle: long horizontal
stroke([(145, 130), (260, 127)], width=6)
# 土 vertical: through both horizontals
stroke([(198, 55), (198, 155)], width=6)

# ---- 厶 (bottom of 去) ----
# 撇折 (one stroke): starts upper-right, goes down-left (撇),
# then turns and goes right (折/横)
stroke([(215, 170), (185, 205), (170, 230), (235, 235)], width=6)
# 点 (small dot on upper right of 厶)
stroke([(225, 200), (245, 220)], width=7)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_佉.png"))
print("saved 01_佉.png")
