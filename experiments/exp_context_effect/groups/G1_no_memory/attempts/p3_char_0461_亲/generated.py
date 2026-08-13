"""Render 亲 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, w=4):
    d.line([p1, p2], fill="black", width=w)

# 亲 = 立 (top) + 木 (bottom)
# --- 立 part (top) ---
# dot (top): short diagonal stroke
line((150, 40), (170, 55), 5)
# short horizontal stroke (under dot)
line((110, 75), (185, 75), 4)
# left dot/short stroke
line((115, 100), (100, 118), 4)
# right dot/short stroke
line((175, 100), (195, 118), 4)
# long horizontal (middle of char)
line((60, 145), (245, 145), 5)

# --- 木 part (bottom) ---
# horizontal of 木
line((75, 185), (225, 185), 4)
# vertical of 木
line((150, 155), (150, 260), 5)
# left falling (撇)
line((145, 195), (85, 265), 4)
# right falling (捺)
line((155, 195), (220, 265), 4)

out_path = os.path.join(os.path.dirname(__file__), "01_亲.png")
img.save(out_path)
print("saved", out_path)
