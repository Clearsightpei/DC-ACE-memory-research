"""Render 济 (jì) — 9 strokes: 氵 (3-drop water radical) + 齐.
300x300 white bg, black ink, PIL only."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- 氵 water radical (left side, 3 dots) ----
stroke([(60, 95), (78, 115)], width=6)   # top dot
stroke([(45, 140), (63, 158)], width=6)  # middle dot
stroke([(58, 210), (78, 195)], width=6)  # bottom rising tick

# ---- 齐 (right side) ----
# top dot (亠 dot)
stroke([(175, 60), (185, 78)], width=6)
# top long horizontal
stroke([(110, 105), (245, 108)], width=6)
# 撇 — left diagonal from just under center-top going down-left
stroke([(175, 108), (100, 260)], width=6)
# 捺 — right diagonal from mid-upper going down-right
stroke([(165, 145), (255, 220)], width=6)
# left short vertical/hook (丿) at bottom
stroke([(155, 195), (150, 270)], width=6)
# right vertical with hook (亅)
stroke([(195, 195), (195, 270), (183, 278)], width=6)

out = os.path.join(os.path.dirname(__file__), "01_济.png")
img.save(out)
print("saved", out)
