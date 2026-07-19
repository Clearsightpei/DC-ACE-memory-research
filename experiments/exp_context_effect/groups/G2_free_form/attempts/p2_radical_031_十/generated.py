"""
p2_radical_031_十 — the 2-stroke radical shí (ten).

Composition (label): 横 + 竖. Standard order: 横 first (left→right), 竖
second (top→bottom crossing through the 横 at roughly the 竖's upper third).

From GT observation (300×300):
- 横 crosses at about y≈150 (canvas midline), spanning ~x=45→255. In MMH's
  rendering it has a very slight upward tilt. Slight taper visible at ends
  as small 顿 presses.
- 竖 is centred near x≈155 (very slightly right of centre in this GT),
  descending from ~y=70 to y≈265. It crosses the 横 at roughly 40% of the
  竖's length, so the top nub is about 80 px and the bottom is about 115 px.
- Both strokes are roughly uniform thickness.

Technique: PIL brush-dabs, uniform radius r≈5 with r+2 顿 dab at both
endpoints of each stroke (following the batch-1 proven 横/竖 recipe).
Standalone-scale caveat applied: use r=5 uniform, r+1.5 at ends (not r+2),
to avoid balloon-y endpoint balls at 300×300.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

def stroke_line(x0, y0, x1, y1, r_start, r_end, steps=400,
                start_press=True, end_press=True):
    """Draw a straight tapered stroke. For standalone-scale, keep end
    dabs subtle (r+0.5) to avoid balloon-y endpoint balls per memory rule
    'No visible 顿-dab "balls" at standalone endpoints'."""
    if start_press:
        dab(x0, y0, r_start + 0.5)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)
    if end_press:
        dab(x1, y1, r_end + 0.5)

# ------ Stroke 1: 横 (heng) ------
# Slight upward tilt (left endpoint lower than right by ~4 px)
H_X0, H_Y0 = 45, 152
H_X1, H_Y1 = 255, 148
stroke_line(H_X0, H_Y0, H_X1, H_Y1, r_start=5, r_end=5)

# ------ Stroke 2: 竖 (shu) ------
# Centred slightly right of image midline, matching GT.
S_X0, S_Y0 = 155, 70
S_X1, S_Y1 = 155, 265
stroke_line(S_X0, S_Y0, S_X1, S_Y1, r_start=5, r_end=5)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_十.png")
img.save(out_path)
print(f"Saved: {out_path}")
