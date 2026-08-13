"""Render 佶 (jí) — 亻 + 吉 (士 over 口)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, width=6):
    d.line([p1, p2], fill="black", width=width)

# ---- Left: 亻 (person radical) ----
# Falling stroke (撇) from upper area diagonally down-left
line((95, 55), (55, 190), width=7)
# Vertical stroke (竖) from mid-upper down
line((90, 100), (90, 260), width=7)

# ---- Right: 吉 ----
# Top part 士 (scholar): top horizontal (longer), vertical, middle horizontal (shorter)
# Top horizontal 一 (longest)
line((130, 60), (260, 60), width=7)
# Middle vertical 丨
line((195, 60), (195, 145), width=7)
# Middle-short horizontal
line((160, 110), (230, 110), width=7)

# Bottom part 口 (mouth) - rectangle
# Left vertical
line((150, 170), (150, 255), width=7)
# Top horizontal
line((150, 170), (245, 170), width=7)
# Right vertical
line((245, 170), (245, 255), width=7)
# Bottom horizontal
line((150, 255), (245, 255), width=7)

out = os.path.join(os.path.dirname(__file__), "01_佶.png")
img.save(out)
print(f"Saved {out}")
