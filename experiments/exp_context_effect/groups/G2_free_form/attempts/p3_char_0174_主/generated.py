"""Render 主 (zhǔ) — 5 strokes.

Stroke order:
  1. 丶  dot on top (short diagonal)
  2. 一  top horizontal (short)
  3. 一  middle horizontal (shortest)
  4. 丨  vertical from top-horizontal-center down to bottom-horizontal
  5. 一  bottom horizontal (longest, widest of the three)

Silhouette: tall-ish rectangle, top-heavy 王 with a dot floating above.
Bottom horizontal is markedly the widest.  Top horizontal a bit
narrower.  Middle horizontal narrower still.

Rendered at 300x300, white background, black ink, using PIL brush-dabs
for tapered strokes (line() joins can look pixelated at small scale).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def stroke(pts, width_start=9, width_end=9):
    """Draw a stroke as a series of overlapping circles (brush dabs)
    with linearly varying radius from start to end.
    pts is a list of (x, y) waypoints; we lerp between consecutive."""
    # Build a dense polyline
    dense = []
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        steps = max(int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 1)
        for s in range(steps + 1):
            t = s / max(steps, 1)
            dense.append((x0 + (x1 - x0) * t, y0 + (y1 - y0) * t))
    n = len(dense)
    for i, (x, y) in enumerate(dense):
        t = i / max(n - 1, 1)
        r = width_start + (width_end - width_start) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

# ---- Stroke 1: 丶 dot on top ----
# Small diagonal dab from upper-left to lower-right, thin -> thick.
stroke([(150, 50), (166, 78)], width_start=2, width_end=6)

# ---- Stroke 2: top horizontal (short) ----
# Centered around x=150, spanning ~90..215, y ~= 105
stroke([(92, 108), (215, 104)], width_start=4, width_end=5)

# ---- Stroke 3: middle horizontal (shortest) ----
# Centered around x=150, spanning ~100..200, y ~= 170
stroke([(100, 170), (200, 168)], width_start=4, width_end=5)

# ---- Stroke 4: vertical 丨 ----
# Runs from just above top-horizontal center down to bottom-horizontal.
stroke([(152, 100), (150, 240)], width_start=5, width_end=5)

# ---- Stroke 5: bottom horizontal (longest) ----
# Wide sweep across ~55..255, y ~= 243, slight rise at both ends.
stroke([(55, 248), (150, 242), (258, 248)], width_start=5, width_end=6)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0174_主/01_主.png")
print("wrote 01_主.png")
