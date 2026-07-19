"""
G2 render for 忄 (radical 077 — 竖心旁, heart-on-the-left).

Revised (pass 2) after comparing to GT:
- Original had 竖 body too thin/short and missing the top curl.
- Left 点 was too straight; needs more of a leftward curve as a
  proper teardrop.
- Right 点 too small; needs to read as a clear short rightward 提.

Anatomy:
  Stroke 1: LEFT 点 (左点) — curved teardrop slanting down-and-left,
            starts thin at top-right, ends thick at bottom-left.
  Stroke 2: LONG 竖 (竖) — central vertical, tall.  Top has a small
            curl/lean (brush start creates a NE→SW curve as visible in
            GT).  Extends nearly full canvas height.  NO hook.
  Stroke 3: RIGHT 点 (右点 / 提) — short rising stroke attached to
            the right side of the 竖 at upper-third, thick→thin.

Renderer: PIL brush-dabs.
"""

from PIL import Image, ImageDraw
import math
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    if steps is None:
        dist = math.hypot(x1 - x0, y1 - y0)
        steps = max(30, int(dist * 4))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)

def bezier_dabs(p0, p1, p2, r_start, r_end, steps=400, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)

# ---------------------------------------------------------------
# Stroke 2: LONG 竖 with top curl.
# Anchor: CX = 180 (right of center to leave room for left 点).
# Top of curl at ~y=55, bottom terminal press at ~y=270.
# Top has a small NE→SW curl: start at (188, 60) and curl down-left
# onto the main vertical at (180, 90), then descend straight.
# ---------------------------------------------------------------
CX = 180
# top curl (mini 撇-style entry — thin start, thickens into the body)
bezier_dabs(
    (192, 58),      # top-right start (small tick)
    (188, 72),      # ctrl
    (180, 92),      # merges into main vertical
    r_start=2.5,
    r_end=7.0,
    steps=180,
    ease=1.4,
)
# main vertical body — uniform, slightly thicker
line_dabs(CX, 92, CX, 268, 7.0, 6.8)
# terminal press (blunt end, no hook — this is 忄, no hook)
dab(CX, 268, 8)

# ---------------------------------------------------------------
# Stroke 1: LEFT 点 (左点)
# Curved teardrop: starts thin around (145, 118), curves down-and-left,
# ends thick around (122, 185).  Should sit at upper-third of vertical.
# ---------------------------------------------------------------
bezier_dabs(
    (148, 118),     # top start
    (135, 145),     # ctrl (pulled left)
    (120, 188),     # bottom-left end
    r_start=2.2,
    r_end=7.0,
    steps=250,
    ease=1.4,
)
# terminal bulb press
dab(120, 188, 7.5)

# ---------------------------------------------------------------
# Stroke 3: RIGHT 点 / 提 — short rising stroke.
# Starts at 竖's right side around (188, 155), rises up-and-right to
# about (225, 138).  Thick→thin taper, sharp tip.
# ---------------------------------------------------------------
# starting joining dab (seats onto the 竖)
dab(188, 155, 7.5)
line_dabs(
    x0=188, y0=155,
    x1=228, y1=138,
    r_start=7.0, r_end=1.5,
    steps=150,
)

# ---------------------------------------------------------------
out = os.path.join(os.path.dirname(__file__), "01_忄.png")
img.save(out)
print(f"wrote {out}")
