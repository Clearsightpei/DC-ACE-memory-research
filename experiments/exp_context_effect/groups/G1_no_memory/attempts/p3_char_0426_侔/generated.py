from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(pts, w=4):
    d.line(pts, fill="black", width=w)

# 侔 = 亻 (left) + 牟 (right, 厶 over 牛)

# --- 亻 (person radical, left side) ---
# short diagonal piě
line([(75, 95), (55, 140)], 5)
# long vertical shù
line([(75, 95), (75, 245)], 5)

# --- 牟 top (厶) ---
# left piě going down-left
line([(180, 55), (145, 110)], 4)
# right stroke: going down-right, then hook back left (forms 厶)
line([(180, 55), (215, 100)], 4)
line([(215, 100), (170, 115)], 4)

# --- 牛 bottom part ---
# small piě on top-left of 牛
line([(155, 130), (140, 155)], 4)
# first horizontal (short, upper)
line([(150, 155), (215, 148)], 4)
# second horizontal (longer, middle)
line([(125, 195), (230, 195)], 5)
# long horizontal (bottom, longest)
line([(115, 240), (250, 235)], 5)
# vertical through center, extending down
line([(185, 130), (185, 280)], 5)

out = os.path.join(os.path.dirname(__file__), "01_侔.png")
img.save(out)
print("wrote", out)
