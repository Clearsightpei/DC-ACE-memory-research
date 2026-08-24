"""
兀 — p3_char_0058
3 strokes: 一 (top lid), 撇 (left leg), 竖弯钩 (right leg splaying right).
Per form_catalog "撇 + 竖弯钩 as leg-pair under a lid".
Legs splay outward, bottom-heavy.
PIL brush-dab renderer, 300x300 white, black ink.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


def stroke_line(p0, p1, r0, r1, n=80):
    """Straight tapered stroke via brush dabs."""
    for i in range(n + 1):
        t = i / n
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def stroke_bezier(p0, p1, p2, p3, r0, r1, n=140):
    """Cubic Bezier with tapered width."""
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3 * p0[0] + 3 * u**2 * t * p1[0] + 3 * u * t**2 * p2[0] + t**3 * p3[0]
        y = u**3 * p0[1] + 3 * u**2 * t * p1[1] + 3 * u * t**2 * p2[1] + t**3 * p3[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Stroke 1: 一 (top lid) — wide horizontal, slight thickening at end
stroke_line((40, 95), (255, 92), r0=4.0, r1=5.0, n=140)
dab(257, 93, 6)

# ---- Stroke 2: 撇 (left leg) — from under the lid near center-left,
# throws sharply down-left, tapers to point at bottom-left corner.
stroke_bezier(
    (108, 100),  # start (under lid)
    (85, 160),   # control 1
    (55, 215),   # control 2
    (25, 265),   # end (tapered tip, far bottom-left)
    r0=5.5,
    r1=1.0,
    n=180,
)

# ---- Stroke 3: 竖弯钩 (right leg) — starts under right side of lid,
# descends nearly vertical, curves right at baseline, small hook up.
# Segment A: vertical descent (very slight rightward drift)
stroke_bezier(
    (195, 100),
    (196, 160),
    (198, 210),
    (200, 245),
    r0=5.0,
    r1=5.0,
    n=140,
)
# Segment B: arc curving to the right at the baseline
stroke_bezier(
    (200, 245),
    (204, 265),
    (225, 273),
    (255, 268),
    r0=5.0,
    r1=4.0,
    n=140,
)
# Segment C: small hook up-left (钩)
stroke_bezier(
    (255, 268),
    (257, 262),
    (254, 254),
    (248, 248),
    r0=4.0,
    r1=1.2,
    n=60,
)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0058_兀/01_兀.png"
)
print("wrote 01_兀.png")
