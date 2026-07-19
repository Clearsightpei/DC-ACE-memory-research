"""
G2 render of radical 士 (scholar), 3 strokes.
Canvas: 300x300, white bg, black ink.
Strokes:
  1. Top 横 (shorter) — around y≈110
  2. 竖 (middle vertical) — x≈150, y≈95→220
  3. Bottom 横 (longer) — around y≈225
Key structural rule vs 土: TOP heng is SHORTER than BOTTOM heng in 士.
Uses PIL brush-dab technique (from memory).
"""
from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def stroke_taper(x0, y0, x1, y1, r_start, r_mid, r_end, steps=None):
    """Straight stroke with gently tapered thick-middle, thin-ends profile.
    Radius interpolates: r_start -> r_mid at t=0.5 -> r_end at t=1."""
    length = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(80, int(length * 4))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        # Parabolic radius profile: thick in middle, thin at ends
        if t < 0.5:
            tt = t / 0.5
            r = r_start + (r_mid - r_start) * tt
        else:
            tt = (t - 0.5) / 0.5
            r = r_mid + (r_end - r_mid) * tt
        dab(x, y, r)


# --- Stroke 1: top 横 (shorter) ---
# Slight up-tilt. Length ~80 px. Thin at ends per GT — no bulbous end dabs.
top_x0, top_y0 = 118, 113
top_x1, top_y1 = 200, 107
stroke_taper(top_x0, top_y0, top_x1, top_y1, r_start=2.0, r_mid=3.8, r_end=1.8)

# --- Stroke 2: 竖 (middle vertical) ---
# Straight down. Starts slightly above top 横 crossing, extends just past bottom 横 (matches GT).
shu_x = 158
shu_y0, shu_y1 = 95, 222
stroke_taper(shu_x, shu_y0, shu_x, shu_y1, r_start=3.0, r_mid=4.0, r_end=2.5)

# --- Stroke 3: bottom 横 (longer) ---
# Slight up-tilt. Length ~155 px (nearly 2x the top heng). Thin tapered ends.
bot_x0, bot_y0 = 78, 232
bot_x1, bot_y1 = 235, 224
stroke_taper(bot_x0, bot_y0, bot_x1, bot_y1, r_start=2.2, r_mid=4.2, r_end=2.0)

# Save
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_士.png")
img.save(out_path)
print(f"Wrote {out_path}")
