"""Render 兀 (3 strokes) as 300x300 black-on-white PNG using PIL.

Strokes:
  1) Top horizontal (一) — spans most of the width, upper third.
  2) Left short 撇 — drops down and slightly left from under the
     left end of the horizontal.
  3) Right 竖弯 — drops straight down from under the right end of the
     horizontal, then curves gently to the right at the bottom.
"""
import os
from PIL import Image, ImageDraw

SIZE = 300
OUT = os.path.join(os.path.dirname(__file__), "01_兀.png")

img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 5  # stroke width

# 1) Top horizontal 一 — slight sag, spans upper region.
top_y = 90
d.line([(78, top_y + 6), (120, top_y - 2), (190, top_y - 2), (225, top_y + 8)],
       fill="black", width=W, joint="curve")

# 2) Left 撇 — from just under the left end, drops down and leftward,
# with a longer, more graceful curve.
d.line([(100, 96), (92, 140), (80, 190), (62, 245)],
       fill="black", width=W, joint="curve")

# 3) Right 竖弯 — drops straight from right end, curves right at bottom.
d.line([(200, 96), (200, 160), (200, 220), (205, 245), (225, 255), (245, 255)],
       fill="black", width=W, joint="curve")

img.save(OUT)
print(f"Wrote {OUT}")
