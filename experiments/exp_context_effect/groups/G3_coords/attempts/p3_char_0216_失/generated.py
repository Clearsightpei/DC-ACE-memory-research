"""p3_char_0216_失 — 失 (shi, "lose")

5 strokes:
  1. 丿  short pie top-left tick
  2. 一  short heng upper (starts near tick tail, goes right)
  3. 一  longer heng lower (middle band, wider)
  4. 丿  long pie sweeping from upper-right down through both hengs to lower-left
  5. 乀  na from the crossing point on the second heng down-right

Fresh inline render (v8: bank primitives reference only). Uniform thin
lines per P12 (MMH GT convention). No bank primitive fits 失 as a
simple identity or uniform scale, so inline is cleaner than force-fit.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
INK = 5  # thin uniform MMH-style width

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def line(p0, p1, w=INK):
    d.line([p0, p1], fill="black", width=w)


def polyline(pts, w=INK):
    for a, b in zip(pts[:-1], pts[1:]):
        line(a, b, w=w)


# --- Stroke 1: short 丿 tick at top-left ------------------------------
# small pie starting slightly right of center-top, tail curving down-left
polyline([(140, 55), (128, 72), (115, 92)])

# --- Stroke 2: short 一 heng at top -----------------------------------
# starts near where tick began, goes right, slight upward tilt
polyline([(138, 78), (175, 72)])

# --- Stroke 3: longer 一 heng in middle band --------------------------
# wider; slight upward slope typical of calligraphic heng
polyline([(70, 138), (220, 130)])

# --- Stroke 4: long 丿 sweeping upper-right -> lower-left ------------
# starts upper-right corner area, crosses through both hengs, sweeps
# to lower-left; slight curve.
pie_pts = [
    (198, 55),
    (185, 90),
    (168, 125),
    (150, 160),
    (125, 200),
    (95, 240),
    (60, 275),
]
polyline(pie_pts)

# --- Stroke 5: 乀 na from crossing down-right -------------------------
# springs from the point where 丿 crosses the second heng
# (approx (150, 160)), sweeps down-right with slight curve
na_pts = [
    (150, 160),
    (175, 195),
    (205, 230),
    (240, 260),
    (260, 275),
]
polyline(na_pts)


out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_失.png"))
print("wrote", os.path.join(out_dir, "01_失.png"))
