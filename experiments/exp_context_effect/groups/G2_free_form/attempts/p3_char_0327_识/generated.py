"""识 (shí) — 7 strokes.
Composition: 讠 (left radical, 2 strokes) + 只 (right, 5 strokes).
Layout: left ~28%, right ~72%. 讠 sits mid-height left; 只 fills right.
Reusing patterns from prior 讠 (p2_radical_035) and 只 (p3_char_0172),
compressed and shifted.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(30, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def polyline(pts, width=6):
    draw.line(pts, fill=INK, width=width, joint="curve")


# ============ 讠 (left radical) ==============================
# Stroke 1: 点 (dot) at top-left
line_dabs(x0=45, y0=75, x1=68, y1=100, r0=1.2, r1=4.2)
dab(69, 101, 4.2)

# Stroke 2: 横折提
# 横 (short, upward tilt)
line_dabs(x0=25, y0=150, x1=85, y1=142, r0=3.3, r1=4.0)
# shoulder dab
dab(85, 142, 4.5)
# 竖 (slight left lean)
line_dabs(x0=85, y0=142, x1=72, y1=215, r0=4.0, r1=3.6)
# joining dab
dab(72, 215, 4.2)
# 提 (rising right, thick→thin)
line_dabs(x0=72, y0=215, x1=118, y1=195, r0=3.8, r1=1.0)


# ============ 只 (right) =====================================
# 口 (top box), x: 130..220, y: 55..130
LW = 6
L, R, T, B = 130, 220, 55, 130

# Stroke 3: 竖 (left vertical of 口)
polyline([(L+3, T+3), (L, B)], width=LW)

# Stroke 4: 横折 — top then right-vertical
polyline([(L-2, T), (R, T-2), (R+2, B-4)], width=LW)

# Stroke 5: 横 (bottom close of 口)
polyline([(L-3, B-2), (R+2, B-5)], width=LW)

# 八 (bottom two legs) — spread wide across right half
# Stroke 6: 撇 (left leg, sweeps down-left)
pie_start = (155, 150)
pie_mid = (135, 205)
pie_end = (110, 265)
polyline([pie_start, pie_mid, pie_end], width=LW)

# Stroke 7: 长点/捺 (right leg, down-right, thicker toward end)
na_start = (200, 150)
na_mid = (230, 205)
na_end = (275, 260)
polyline([na_start, na_mid, na_end], width=LW + 1)


out = (
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0327_识/01_识.png"
)
img.save(out)
print("wrote", out)
