"""G1 render of 佗 (tuō) — 亻 + 它."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# ---- Left: 亻 (person radical) ----
# 撇 — curving from upper right down to lower left
line([(105, 85), (95, 130), (75, 175), (55, 230)], width=6)
# 竖 — vertical, starting from mid of 撇
line([(95, 135), (95, 255)], width=6)

# ---- Right: 它 ----
# 宀 roof
# top dot (点)
line([(190, 60), (198, 78)], width=6)
# roof left tick (short slanted)
line([(150, 90), (145, 105)], width=6)
# roof horizontal
line([(148, 92), (240, 92)], width=6)
# roof right drop (short)
line([(240, 92), (238, 115)], width=6)

# 匕 body
# top-left short horizontal-slash (the top of 匕)
line([(160, 145), (215, 130)], width=6)
# vertical-ish left of 匕
line([(165, 145), (160, 215)], width=6)
# bottom curve — sweeping right and hooking up (乚 shape)
line([(160, 215), (215, 225), (240, 215), (245, 175), (240, 165)], width=6)
# horizontal cross of 匕 (small stroke crossing middle)
line([(170, 180), (225, 175)], width=6)

out = os.path.join(os.path.dirname(__file__), "01_佗.png")
img.save(out)
print("wrote", out)
