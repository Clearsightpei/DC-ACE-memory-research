# p3_char_0165_乍 — 乍 (zhà), 5 strokes.
# Structure (per GT inspection):
#   1. 撇 (pie): from upper-center, sweeping down-left, moderate length.
#   2. 短横 (short heng): top-right, short, from just right of pie's start
#      going right.
#   3. 长竖 (long shu): from the right end of stroke 2, straight down.
#   4. 短横 (mid heng): crossing the 竖 at middle height, short.
#   5. 长横 (bottom heng): at bottom, longer than mid heng, crosses 竖.
# MMH GT uses thin uniform lines (~3-4 px). We match with thin PIL lines.

import os
from PIL import Image, ImageDraw

CANVAS = 300
OUT = os.path.join(os.path.dirname(__file__), "01_乍.png")

img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
d = ImageDraw.Draw(img)

W = 4  # MMH-style thin uniform line width

# --- Stroke 1: 撇 (pie) — long sweeping curve from upper-center down-left ---
p0 = (155, 45)    # top start (near pie head)
p1 = (95, 130)    # control (pulled left for bow)
p2 = (55, 235)    # bottom-left tip

def bezier(d, p0, p1, p2, w, n=60):
    prev = None
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        if prev is not None:
            d.line([prev, (x, y)], fill=(0, 0, 0), width=w)
        prev = (x, y)

bezier(d, p0, p1, p2, W)

# --- Stroke 2: 短横 at top (from pie's head going right) ---
d.line([(153, 60), (220, 65)], fill=(0, 0, 0), width=W)

# --- Stroke 3: 长竖 from right end of top heng, going straight down (with tail below bottom heng) ---
d.line([(217, 65), (215, 275)], fill=(0, 0, 0), width=W)

# --- Stroke 4: 短横 (middle) — crosses the 竖 at mid-height ---
d.line([(135, 150), (230, 152)], fill=(0, 0, 0), width=W)

# --- Stroke 5: 长横 (bottom) — longer, crosses 竖 above its tail ---
d.line([(110, 230), (245, 232)], fill=(0, 0, 0), width=W)

img.save(OUT)
print(f"wrote {OUT}")
