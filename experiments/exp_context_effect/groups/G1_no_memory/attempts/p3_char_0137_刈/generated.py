"""Render 刈 (yi) — 4 strokes: 乂 (X) on left + 刂 (vertical + hook) on right."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

W = 6  # stroke width

def curve(points, w=W):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill="black", width=w)

# ---- Left component 乂 ----
# Stroke 1: 撇 — starts upper-right of the X, sweeps down-left with a curve
p1 = [(140, 75), (128, 100), (110, 135), (90, 175), (68, 215), (48, 250)]
curve(p1)

# Stroke 2: 捺 — starts upper-left, sweeps down-right, crossing stroke 1
# In GT this looks like a curving 捺 that starts near top and ends bottom-right
p2 = [(70, 100), (95, 140), (125, 180), (150, 215), (170, 245)]
curve(p2)

# ---- Right component 刂 ----
# Stroke 3: short slanted stroke at top of 刂 (小撇/短竖)
p3 = [(210, 60), (206, 90), (202, 120)]
curve(p3)

# Stroke 4: 竖钩 — long vertical descending, then hook to the left at the bottom
p4 = [(245, 55), (244, 100), (243, 150), (242, 200), (240, 235),
      (236, 250), (226, 255), (215, 252)]
curve(p4)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_刈.png"))
print("saved 01_刈.png")
