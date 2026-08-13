"""Render 齐 (qi) — 6 strokes."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)
W = 6  # ink width

def line(pts, width=W):
    d.line(pts, fill="black", width=width, joint="curve")

# 齐 structure: apex "人"-like top, long horizontal, two inner
# slashes forming X, then left vertical and right hook.

# Stroke 1: left slash of the top "人" apex (丿) — from apex down-left
line([(150, 55), (105, 115)])

# Stroke 2: right slash of the top "人" apex (乀) — apex down-right
line([(150, 55), (200, 115)])

# Stroke 3: long horizontal (一) below the apex
line([(60, 135), (240, 135)])

# Stroke 4 & 5: inner X (short 丿 left, short 乀 right) between apex and horiz?
# Actually in 齐 below the horizontal we have a 丿 and 丨 forming the lower part.
# But GT shows a small cross in the middle — that's the 丿+乀 of the inner form.
# Place a small X centered just below the horizontal.
line([(125, 145), (95, 200)])   # inner left slash
line([(125, 145), (175, 200)])  # inner right slash

# Stroke 6: left vertical (short) hanging down from horizontal, outer left
line([(95, 155), (85, 245)])

# Stroke 7: right vertical hook (亅) hanging down from horizontal, outer right
line([(205, 155), (210, 240)])
line([(210, 240), (198, 245)])  # tiny hook

out = os.path.join(os.path.dirname(__file__), "01_齐.png")
img.save(out)
print("wrote", out)
