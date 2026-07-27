"""G1 render of 业 (yè) — 5 strokes."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 6  # ink width

def line(x1, y1, x2, y2, w=W):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)

# Layout on a 300x300 canvas, character centered roughly in center block.
# Bottom horizontal (long) at y ~ 235, spans x 55..245
line(55, 238, 250, 232, W)

# Two central verticals (main pillars)
# Left vertical: from upper-mid down to horizontal
line(120, 90, 122, 235, W)
# Right vertical: slightly taller/starts higher
line(180, 70, 182, 235, W)

# Left slanting short stroke (丿-like): from upper-right down to lower-left
line(100, 130, 75, 165, W)

# Right slanting short stroke (丶-like): from upper-left down to lower-right
line(200, 125, 225, 165, W)

out = os.path.join(os.path.dirname(__file__), "01_业.png")
img.save(out)
print("wrote", out)
