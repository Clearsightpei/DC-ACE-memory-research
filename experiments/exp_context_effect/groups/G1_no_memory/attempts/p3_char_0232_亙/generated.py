"""Render 亙 (p3_char_0232) to 01_亙.png at 300x300."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4

# Top horizontal stroke (long)
d.line([(45, 75), (255, 72)], fill=BLACK, width=LW)

# Bottom horizontal stroke (long)
d.line([(40, 250), (260, 253)], fill=BLACK, width=LW)

# Middle shape: 亘-like inner (a box resembling 日/月 with strokes inside)
# Left vertical (with slight lean at top -- the 撇 for outer)
d.line([(95, 100), (85, 225)], fill=BLACK, width=LW)
# Top of inner box (short horizontal, slightly below top stroke)
d.line([(95, 100), (215, 102)], fill=BLACK, width=LW)
# Right vertical of inner box
d.line([(215, 102), (215, 225)], fill=BLACK, width=LW)
# Bottom of inner box
d.line([(85, 225), (215, 225)], fill=BLACK, width=LW)
# Middle horizontal inside (like the crossbar of 日)
d.line([(100, 165), (215, 165)], fill=BLACK, width=LW)
# Two small diagonal strokes inside lower half (dot-like)
d.line([(130, 180), (150, 215)], fill=BLACK, width=LW)
d.line([(165, 180), (185, 215)], fill=BLACK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_亙.png")
img.save(out)
print(f"Wrote {out}")
