"""G1 render of 攵 (radical, 4 strokes)."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(pts, width=6):
    # Draw a smooth polyline using round joins by drawing consecutive
    # ellipses at each endpoint and lines between them.
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill="black", width=width)
    for p in pts:
        r = width / 2
        d.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill="black")

# Stroke 1: short curved 撇 at top -- arcs from upper area down-left then hooks
# GT shows a short arc, roughly like a comma
s1 = [(148, 68), (142, 78), (135, 92), (128, 105), (125, 115)]
stroke(s1, width=6)

# Stroke 2: horizontal 横 -- from left extending right, longer than my first try
s2 = [(105, 135), (140, 132), (175, 133), (200, 138)]
stroke(s2, width=6)

# Stroke 3: long 撇 -- diagonal from upper-mid down to lower left
s3 = [(148, 138), (132, 165), (112, 200), (88, 240)]
stroke(s3, width=6)

# Stroke 4: 捺 -- from mid upper down-right, crossing stroke 3 below the 横
s4 = [(135, 175), (158, 205), (185, 235), (215, 260)]
stroke(s4, width=6)

out = os.path.join(os.path.dirname(__file__), "01_攵.png")
img.save(out)
print(f"Saved {out}")
