"""G1 render of 佬 (lao) — 亻 (left) + 老 (right, 耂 over 匕)."""
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, width=5):
    d.line(pts, fill="black", width=width, joint="curve")

# --- 亻 radical (left) ---
# 撇 (top-right to lower-left slant)
line([(95, 85), (55, 195)], width=6)
# 竖 (vertical) starting from mid-slant
line([(80, 140), (80, 260)], width=6)

# --- 老 (right) ---
# 耂 top:
# 横 (long horizontal, slightly rising)
line([(125, 105), (250, 100)], width=6)
# 竖 through the horizontal (vertical stem)
line([(190, 80), (190, 155)], width=6)
# 横 (short second horizontal below, slightly right of first)
line([(155, 140), (235, 138)], width=6)
# 撇 (long slant from upper-right going down-left through the character)
line([(210, 90), (130, 245)], width=6)

# 匕 bottom:
# 短撇 into the 匕 (small slant top)
line([(170, 200), (200, 195)], width=6)
# 竖弯钩 — vertical then bend right then hook up
line([(200, 175), (200, 255)], width=6)
line([(200, 255), (265, 255)], width=6)
line([(265, 255), (265, 235)], width=6)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_佬.png"))
print("saved", os.path.join(out_dir, "01_佬.png"))
