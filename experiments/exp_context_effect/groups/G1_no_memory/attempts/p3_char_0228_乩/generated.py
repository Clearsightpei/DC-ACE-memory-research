"""Render 乩 (p3_char_0228) as a 300x300 PNG.

乩 = 占 (left) + 乚 (right).
占 = 卜 (top: vertical stroke + short horizontal dot to its right)
   + 口 (bottom: small rectangle).
乚 = a tall vertical that hooks to the right at bottom.
"""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 6  # stroke width

# ---- Left: 占 ----
# 卜 vertical: from top down through mid-upper area
d.line([(90, 40), (90, 155)], fill="black", width=W)
# 卜 short horizontal dot (right of the vertical, upper area)
d.line([(95, 90), (135, 90)], fill="black", width=W)

# 口 rectangle (bottom left) — 4 sides
# top
d.line([(60, 175), (145, 175)], fill="black", width=W)
# left
d.line([(60, 175), (60, 255)], fill="black", width=W)
# right
d.line([(145, 175), (145, 255)], fill="black", width=W)
# bottom
d.line([(60, 255), (145, 255)], fill="black", width=W)
# inner horizontal (some 占 have a middle bar-like appearance in GT)
d.line([(75, 215), (130, 215)], fill="black", width=W)

# ---- Right: 乚 ----
# Vertical from top-right coming down, then hooking right at the bottom
# Vertical part
d.line([(215, 45), (215, 235)], fill="black", width=W)
# Bottom curve/hook to the right
d.line([(215, 235), (285, 255)], fill="black", width=W)
# small upward tip on the hook (optional — GT shows a clean curl)
# skip tip; end at (285, 255)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_乩.png"))
print("saved 01_乩.png")
