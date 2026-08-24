"""
Draw 亍 (chù) — 3 strokes:
  1. Short 横 near top (a bit right-of-center).
  2. Longer 横 in the middle spanning most of the width.
  3. 竖钩 starting from the middle-横 (right of center), going down,
     ending with a small hook to the LEFT.
Canvas: 300x300, white bg, black ink.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BRUSH = 10  # medium-thick brush

def stroke(pts, width=BRUSH):
    """Draw a polyline with rounded joins/caps by drawing lines + dabs."""
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        draw.line([(x1, y1), (x2, y2)], fill="black", width=width)
    r = width // 2
    for (x, y) in pts:
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")

# --- Stroke 1: short top 横 (slightly slanted up-right, calligraphic) ---
# Positioned near top, ~x from 95 to 195, y ~ 80
stroke([(95, 82), (200, 76)])

# --- Stroke 2: long middle 横, spans wider ---
# from x ~ 45 to x ~ 260, y ~ 145 (slight up-tilt)
stroke([(48, 152), (260, 142)])

# --- Stroke 3: 竖钩 through middle 横, then hook LEFT at bottom ---
# Vertical descent from ~(165, 138) down to ~(165, 245), then hook left/up
# The vertical is right-of-center.
stroke([(168, 138), (166, 245), (140, 258)])
# Small hook flick continues up-left
stroke([(140, 258), (128, 248)], width=BRUSH)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0050_亍/01_亍.png")
