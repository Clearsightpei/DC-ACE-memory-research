"""
心 (xin) — radical, 4 strokes.

Structure from GT:
  1. Left dot (点)  — small teardrop, tilted down-left, sits low on far left.
  2. 卧钩 (lying hook) — shallow smile arc dipping from upper-left area
     down through the bottom-middle and rising to upper-right, then flicking
     up-and-left at the tip.
  3. Middle dot (点) — small teardrop inside the bowl, upper-middle.
  4. Right dot (点) — short flicking dot upper-right.

Aspect ratio family: wide-ish, bottom-heavy (the 卧钩 forms the base bowl,
three dots hover above/around it). Canvas 300x300.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    """Filled circular dab — the basic ink primitive."""
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def tapered_dot(x0, y0, x1, y1, r_start, r_end, steps=30):
    """Teardrop / 点 — from (x0,y0) fat end to (x1,y1) tip; radius tapers."""
    for i in range(steps + 1):
        t = i / steps
        cx = x0 + (x1 - x0) * t
        cy = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(cx, cy, r)


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=100):
    """Quadratic Bezier ink stroke with tapered width."""
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        cx = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        cy = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(cx, cy, r)


# -----------------------------------------------------------
# Stroke 1: LEFT DOT (点) — small teardrop, tilted down-left.
# GT: fat at TOP-RIGHT, thin tip at BOTTOM-LEFT. Sits at mid-left.
# Roughly from (85, 175) fat → (55, 215) thin.
# -----------------------------------------------------------
tapered_dot(x0=85, y0=175, x1=55, y1=215, r_start=6.0, r_end=1.5, steps=30)

# -----------------------------------------------------------
# Stroke 2: 卧钩 (lying hook) — the signature stroke.
# GT has a deeper bowl with visible hook flicking up-and-left.
# Start upper-left ~ (105, 175), dip to bottom ~ (155, 235),
# rise to right ~ (215, 180), then hook flicks up-left ~ (195, 155).
# -----------------------------------------------------------
bezier_stroke(
    p0=(105, 175),
    p1=(150, 260),   # control point pulled DOWN → deep smile belly
    p2=(215, 180),
    r_start=3.0,
    r_end=5.5,
    steps=140,
)
# 顿 dab at the hook base (thicken the turn)
dab(215, 180, 6)
# Hook flick — from (215, 180) up-and-left to (192, 152), tapering to tip
tapered_dot(x0=214, y0=178, x1=192, y1=152, r_start=6.0, r_end=1.2, steps=30)

# -----------------------------------------------------------
# Stroke 3: MIDDLE DOT (点) — inside the bowl, upper area.
# GT: thin at top-left, fat at bottom-right (down-right flick).
# Roughly from (140, 128) thin → (162, 158) fat.
# -----------------------------------------------------------
tapered_dot(x0=140, y0=128, x1=162, y1=158, r_start=1.8, r_end=5.5, steps=30)

# -----------------------------------------------------------
# Stroke 4: RIGHT DOT (点) — upper right, short flick.
# GT: thin at top-left, fat at bottom-right.
# Roughly from (205, 115) thin → (230, 145) fat.
# -----------------------------------------------------------
tapered_dot(x0=205, y0=115, x1=230, y1=145, r_start=1.8, r_end=5.5, steps=30)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_126_心/01_心.png"
)
