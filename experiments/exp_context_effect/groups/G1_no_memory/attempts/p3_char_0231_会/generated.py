"""G1 draws 会 (huì) — simplified: 人 (roof) + 云 (bottom = 二 + 厶)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")

# Top 人 (person radical): roof
# small tick at apex
line([(150, 45), (158, 38)], width=5)
# Left falling stroke (撇)
line([(150, 50), (70, 170)], width=6)
# Right falling stroke (捺) — longer, extends further right
line([(150, 50), (245, 170)], width=6)

# First horizontal (top of 二 inside 云)
line([(85, 180), (230, 178)], width=6)

# Second horizontal (short, above 厶)
line([(105, 215), (200, 213)], width=6)

# 厶 (bottom of 云): 撇折 + 点
# 撇 going down-left
line([(150, 225), (110, 275)], width=6)
# 折 turning right (bottom horizontal)
line([(110, 275), (185, 273)], width=6)
# small 点 (dot) top-right
line([(175, 250), (200, 275)], width=6)

out = os.path.join(os.path.dirname(__file__), "01_会.png")
img.save(out)
print("wrote", out)
