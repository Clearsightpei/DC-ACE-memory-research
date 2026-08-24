"""Render 屮 (chè) - 3 strokes.

Strokes (per GT):
1. Left vertical descending then rightward hook at bottom (like a small 'L').
2. Long horizontal stroke crossing near middle.
3. Central long vertical descending; the right side has a short vertical
   from the horizontal going down (small tick).

Actually 屮 canonical stroke order:
1. Short left vertical (top-left area, going down)
2. Long central vertical (top going down, longer)
3. Horizontal cutting across, with rightward small up-tick at right end
   -> combined as horizontal + short right vertical up.

We draw:
- left short vertical (upper-left)
- long central vertical (middle, longer)
- horizontal across the middle
- right short vertical up (right of horizontal)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
T = 5  # line thickness

# Long central vertical - dominant stroke, extends top to bottom
cx = 150
d.line([(cx, 60), (cx, 275)], fill=INK, width=T)

# Horizontal stroke across the middle
hy = 175
d.line([(70, hy), (230, hy)], fill=INK, width=T)

# Left branch: short vertical from horizontal extending UP-LEFT
# In GT this goes from horizontal upward with a slight lean
d.line([(90, 100), (90, hy)], fill=INK, width=T)

# Right branch: short vertical from horizontal extending UP-RIGHT
d.line([(210, 110), (210, hy)], fill=INK, width=T)

out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0084_屮/01_屮.png"
img.save(out)
print("saved", out)
