"""么 (me) — 3 strokes.
Stroke 1: 撇折 at top-left area — a small pie sweeping down-left, folding into
          a small horizontal tick to the right (looks like a tiny ㄥ).
Stroke 2: 撇 in the middle — starts upper-right, sweeps down-left across.
Stroke 3: 捺 sweeping down-right from apex near stroke 2's tail.
Drawn inline with PIL (no bank primitive fits cleanly for 么's compound top).
"""
from PIL import Image, ImageDraw
from math import comb
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def bezier(pts, n=80):
    k = len(pts) - 1
    out = []
    for i in range(n + 1):
        t = i / n
        x = sum(comb(k, j) * (1 - t) ** (k - j) * t ** j * pts[j][0] for j in range(k + 1))
        y = sum(comb(k, j) * (1 - t) ** (k - j) * t ** j * pts[j][1] for j in range(k + 1))
        out.append((x, y))
    return out

def stroke(pts, width=6):
    poly = bezier(pts, n=100)
    for i in range(len(poly) - 1):
        d.line([poly[i], poly[i + 1]], fill="black", width=width)
    for (x, y) in (poly[0], poly[-1]):
        r = width / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill="black")

# --- Stroke 1: small 撇折 near top-center ---
# The GT shows the top stroke as a small 撇 that folds with a hook to lower-right.
# Pie portion: starts upper-right, sweeps down-left.
p1_a = [(165, 60), (150, 80), (130, 105)]
# Fold portion: tick going right-down, ending slightly higher (creates the hook look).
p1_b = [(130, 105), (150, 110), (165, 95)]
stroke(p1_a, width=5)
stroke(p1_b, width=5)

# --- Stroke 2: middle 撇, longer, sweeping from upper-right to lower-left ---
# GT: starts around (185, 130), sweeps down-left ending near (110, 205)
p2 = [(190, 130), (165, 165), (115, 210)]
stroke(p2, width=6)

# --- Stroke 3: 捺 sweeping down-right ---
# Starts near the tail of stroke 2 (apex meeting), sweeps down-right with a belly.
# In GT it curves gently and ends around the lower-right, tapering.
p3 = [(130, 190), (170, 220), (225, 255)]
stroke(p3, width=6)

out = os.path.join(os.path.dirname(__file__), "01_么.png")
img.save(out)
print(f"wrote {out}")
