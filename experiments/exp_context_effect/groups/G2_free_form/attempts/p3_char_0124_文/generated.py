"""
文 (wen) — Phase-3 character, standalone.
Template (from form_catalog char x role): 亠 lid + 乂 body.
4 strokes:
  1. 点 (top dot, above the 横 lid) — small teardrop
  2. 横 (top-lid) — medium horizontal, slight up-tilt
  3. 撇 (body) — from upper-right area of body, down-left
  4. 捺 (body) — from upper-left, crossing the 撇 near vertical middle,
     down-right, thin -> thick with terminal foot.

Rendering: PIL brush-dabs (drawer_memory technique) on 300x300 white.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab_line(p0, p1, r0, r1, steps=None):
    """Brush-dab tapered stroke from p0 to p1 with radius ramp r0->r1."""
    x0, y0 = p0
    x1, y1 = p1
    if steps is None:
        dist = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        steps = max(60, int(dist * 2))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab_bezier(p0, p1, p2, r0, r1, steps=200):
    """Quadratic-Bezier tapered stroke."""
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * x0 + 2 * u * t * x1 + t * t * x2
        y = u * u * y0 + 2 * u * t * y1 + t * t * y2
        r = r0 + (r1 - r0) * t
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---- Stroke 1: 点 (top dot, above the 横) ----
# Simple short teardrop-like flick, angled slightly down-left.
# The GT shows a short curved comma-like dot above the lid.
dab_bezier(
    p0=(155, 55), p1=(148, 70), p2=(135, 82),
    r0=1.5, r1=3.2, steps=100,
)

# ---- Stroke 2: 横 (top-lid) ----
# Medium horizontal, ~150 px, slight up-tilt.
dab_line((70, 108), (232, 100), r0=3.2, r1=3.2)
# 顿 dabs at ends
draw.ellipse((66, 104, 76, 114), fill="black")
draw.ellipse((228, 96, 240, 108), fill="black")

# ---- Stroke 3: 撇 (body) ----
# Body 撇: starts just under the lid (right of center),
# throws down-left to lower-left. Thick -> thin with slight curve.
dab_bezier(
    p0=(175, 122), p1=(135, 185), p2=(75, 258),
    r0=4.5, r1=1.5, steps=250,
)
# 顿 press at start
draw.ellipse((170, 117, 182, 129), fill="black")

# ---- Stroke 4: 捺 (body) ----
# Body 捺: starts just under the lid (left of center),
# passes down-right, crossing the 撇 near vertical middle, thin -> thick,
# ending with terminal foot pressed outward (flat, broad) extending right.
dab_bezier(
    p0=(115, 124), p1=(175, 190), p2=(240, 255),
    r0=1.8, r1=5.0, steps=250,
)
# terminal foot: broaden and flick outward horizontally
draw.ellipse((232, 250, 248, 264), fill="black")
dab_line((244, 258), (262, 253), r0=4.5, r1=1.5)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0124_文/01_文.png"
)
print("wrote 01_文.png")
