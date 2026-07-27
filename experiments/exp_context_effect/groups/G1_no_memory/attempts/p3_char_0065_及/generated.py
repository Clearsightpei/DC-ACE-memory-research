"""G1 render of 及 (jí) — 3 strokes."""
from PIL import Image, ImageDraw
import os, math

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

def stroke(points, width=5):
    d.line(points, fill="black", width=width, joint="curve")

# Reference GT: character occupies roughly x=[55,255], y=[70,265]

# Stroke 1: top - starts lower-left, arcs up to right, then small hook down
# Looks like a slightly-dipped horizontal that then descends to form left side of the 乃-like shape
s1 = []
# leftmost dot/entry
s1.append((60, 92))
# gentle up-arc across
for t in [i/30 for i in range(31)]:
    x = 75 + t * 130
    y = 82 - 8 * math.sin(math.pi * t)
    s1.append((x, y))
# then descend at the right end (this forms the top-right corner)
s1.append((210, 78))
s1.append((215, 95))
stroke(s1, width=5)

# Stroke 2: the long 撇 - starts at the top-right (near stroke1 end),
# sweeps down and LEFT in a big curve, all the way to lower-left corner
s2 = []
x0, y0 = 210, 90
x1, y1 = 165, 145
x2, y2 = 130, 195
x3, y3 = 55, 260
for t in [i/60 for i in range(61)]:
    x = (1-t)**3*x0 + 3*(1-t)**2*t*x1 + 3*(1-t)*t**2*x2 + t**3*x3
    y = (1-t)**3*y0 + 3*(1-t)**2*t*y1 + 3*(1-t)*t**2*y2 + t**3*y3
    s2.append((x, y))
stroke(s2, width=5)

# Stroke 3: the 捺 - starts inside on the 撇 (around middle-left area),
# goes down-right to a low point, then flares HORIZONTALLY out to the right (long tail)
s3 = []
# starts on the 撇 around (110, 180)
sx0, sy0 = 108, 182
# descend to the low crossing point
sx1, sy1 = 155, 240
sx2, sy2 = 200, 258
sx3, sy3 = 265, 258
for t in [i/60 for i in range(61)]:
    x = (1-t)**3*sx0 + 3*(1-t)**2*t*sx1 + 3*(1-t)*t**2*sx2 + t**3*sx3
    y = (1-t)**3*sy0 + 3*(1-t)**2*t*sy1 + 3*(1-t)*t**2*sy2 + t**3*sy3
    s3.append((x, y))
stroke(s3, width=5)

out_path = os.path.join(os.path.dirname(__file__), "01_及.png")
img.save(out_path)
print(f"Wrote {out_path}")
