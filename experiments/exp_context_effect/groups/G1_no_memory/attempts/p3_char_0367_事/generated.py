"""Render 事 as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

# 事 — 8 strokes:
# 1. Top short horizontal (一)
d.line([(115, 55), (175, 55)], fill="black", width=LW)

# 2. Long horizontal below top (the roof)
d.line([(45, 90), (255, 90)], fill="black", width=LW)

# 3. Left vertical of upper 口-like box
d.line([(90, 90), (90, 145)], fill="black", width=LW)

# 4. Right vertical of upper 口-like box
d.line([(215, 90), (215, 145)], fill="black", width=LW)

# 5. Middle horizontal inside the box
d.line([(90, 120), (215, 120)], fill="black", width=LW)

# 6. Bottom horizontal of the box
d.line([(90, 145), (215, 145)], fill="black", width=LW)

# 7. Wide horizontal (long stroke across middle-lower)
d.line([(30, 195), (270, 195)], fill="black", width=LW)

# 8. Central vertical with a hook at bottom (long spine through the whole char, ends with left hook)
d.line([(150, 45), (150, 260)], fill="black", width=LW)
# hook - curve to the left at the bottom
d.line([(150, 260), (110, 245)], fill="black", width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_事.png")
img.save(out_path)
print(f"Saved {out_path}")
