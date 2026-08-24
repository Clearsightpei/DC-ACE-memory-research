"""
又 (yòu) — 2 strokes: 横撇 (short 横 + shoulder + long 撇 tail) + 捺.

Reflecting clean GT (2026-07-19):
- Character is compact & centered, slightly upper-mid of canvas.
- Stroke 1 (横撇): short slanted 横 across top (left slightly lower
  than right — very slight upward slant), sharp shoulder 顿笔 at
  top-right, then a long 撇 curving down-left, ending near lower-
  left area past the 横's left edge.
- Stroke 2 (捺): starts near the shoulder / top-mid, sweeps down-
  and-right, gentle S-curve, ends in a broad flat foot at lower-
  right, tail extending horizontally past its lowest point.
- The two strokes cross around the vertical mid, forming the X body.

Rendered with PIL brush-dabs (per drawer_memory technique).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_quad_dabs(p0, p1, p2, r0, r1, steps=500):
    """Quadratic Bezier with tapered radius."""
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# -----------------------------------------------------------------------------
# Stroke 1: 横撇  (short slanted 横 + shoulder + long pie tail)
# -----------------------------------------------------------------------------
# 1a. short 横 across top: (75,110) -> (195,100), slight upward tilt
line_dabs(75, 110, 195, 100, 4.5, 4.5, steps=300)

# 1b. shoulder dab at top-right corner (顿笔)
dab(195, 100, 6.0)

# 1c. 撇 tail — long bowed sweep, ends past 横's left edge
# Start at shoulder (195,100), curve through (135,175), end at (60,245).
bezier_quad_dabs((195, 100), (135, 175), (60, 245), 5.0, 1.4, steps=500)

# -----------------------------------------------------------------------------
# Stroke 2: 捺  (press-down, thin -> thick with broad flat foot)
# -----------------------------------------------------------------------------
# Starts near the shoulder / just under the 横 on the left-center,
# sweeps down-right with gentle curve, ends broad at lower-right.
# Start ~(105,130), pass through control (170,190), end (255,245).
bezier_quad_dabs((105, 130), (170, 190), (255, 245), 2.0, 7.5, steps=500)

# Broad terminal foot (捺 flat press) — slight rightward extension
for k in range(14):
    dab(255 + k * 0.5, 245 + k * 0.05, 7.5 - k * 0.4)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0017_又/01_又.png"
)
