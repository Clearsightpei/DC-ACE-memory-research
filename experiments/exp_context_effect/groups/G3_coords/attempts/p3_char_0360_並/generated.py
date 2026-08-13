"""並 (bìng) — 8 strokes.

GT decomposition (from gt/phase3/並.png):
  1. LEFT small dot at top (丶 slanting down-right)
  2. RIGHT small pie at top (short 撇 slanting down-left)
  3. SHORT heng below the 丷 pair
  4. LEFT long vertical (竖) descending
  5. RIGHT long vertical (竖) descending, slight hook tail
  6. INNER LEFT small dot / stroke
  7. INNER RIGHT small pie
  8. LONG bottom heng (widest stroke, spans nearly full width)

Inline PIL, thin uniform ink per P12 (MMH style GT).
Similar in family to 兰 (lan_orchid.py) — 丷 + horizontals — but with
two verticals framing the middle and an inner 丷-like dot pair.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p0, p1, w=5):
    d.line([p0, p1], fill="black", width=w)

# ---- Top 丷 (mirror dots, asymmetric per ba_dot.py lesson) ----
# LEFT 丶: short slanting down-right
line((122, 55), (140, 92), w=5)
# RIGHT 撇: short slanting down-left
line((188, 55), (168, 92), w=5)

# ---- Short heng under the 丷 (top of the middle body) ----
line((100, 118), (205, 116), w=5)

# ---- Two long verticals framing middle (roughly parallel, slight outward splay) ----
# LEFT 竖 — descending straight down, slight outward tilt at bottom
line((110, 122), (95, 240), w=5)
# RIGHT 竖 — mirror, with small hook tail curving left
line((198, 122), (215, 235), w=5)
line((215, 235), (208, 245), w=5)

# ---- Inner small marks (like a lower 丷) ----
# Inner LEFT small stroke — slanting down-right
line((138, 175), (148, 210), w=4)
# Inner RIGHT small stroke — slanting down-left
line((175, 175), (165, 210), w=4)

# ---- Long bottom heng (widest, spans nearly full canvas) ----
line((25, 260), (280, 258), w=6)

import os
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_並.png")
img.save(out)
print("wrote", out)
