# p3_char_0220_丢  —  6 strokes: 丿 一 丨 一 撇折 点
# GT-driven inline render. G3 v8: bank is reference; hand-rendered here.
# Layout: top 丿+短一+短丨 (like 千 top), long 一 middle, 厶 bottom.
from PIL import Image, ImageDraw
import os

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def stroke(pts, width=6):
    d.line(pts, fill="black", width=width, joint="curve")


# 1. 丿 (top pie) — slants down-left, short
stroke([(175, 60), (150, 78), (120, 95)], width=6)

# 2. 一 (short heng) — under the pie
stroke([(90, 108), (200, 105)], width=6)

# 3. 丨 (short vertical) — centered, connects heng down to long heng
stroke([(148, 108), (148, 158)], width=6)

# 4. 一 (long heng) — wide horizontal across the middle
stroke([(40, 165), (262, 162)], width=7)

# 5. 撇折 (bottom-left of 厶) — pie down-left then折 right (small hook base)
stroke([(150, 190), (115, 235), (108, 258), (168, 258)], width=6)

# 6. 点 (bottom-right dot) — diagonal 捺-like short stroke
stroke([(170, 218), (205, 258), (215, 268)], width=6)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_丢.png")
img.save(out)
print("wrote", out)
