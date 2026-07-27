"""
用 — 5 strokes: 撇, 横折钩, 横 (upper inner), 横 (lower inner), 竖 (middle, extends below).
Left wall slightly slanted (撇-like curve at bottom); right wall vertical with 竖钩 hook flicking UP-LEFT.
Middle 竖 pierces through both inner bars and extends slightly below the bottom horizontal.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 7  # line width

# Box (approx from GT): roughly x in [70, 220], y in [35, 275]
LEFT_X_TOP = 78
LEFT_X_BOT = 58   # slight 撇 curve outward at bottom
RIGHT_X = 220
TOP_Y = 42
BOT_Y = 265
MID_X = (LEFT_X_TOP + RIGHT_X) // 2  # inner middle vertical


def thick_line(p1, p2, width=LW):
    draw.line([p1, p2], fill=INK, width=width)
    # smooth ends
    r = width // 2
    for p in (p1, p2):
        draw.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill=INK)


# Stroke 1: 撇 — left wall, smoothly curving down-left as a quadratic Bezier
# Sample the curve as many short segments so the joint isn't visible.
def quad_bezier(p0, p1, p2, n=40, width=LW):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    for a, b in zip(pts, pts[1:]):
        thick_line(a, b, width)

quad_bezier((LEFT_X_TOP, TOP_Y + 5), (LEFT_X_TOP - 4, 175), (LEFT_X_BOT, BOT_Y + 8))

# Stroke 2: 横折钩 — top horizontal + right vertical + hook flicking UP-LEFT
# top horizontal
thick_line((LEFT_X_TOP - 2, TOP_Y), (RIGHT_X, TOP_Y + 6))
# right vertical (slight shoulder inward at the fold, then straight down)
thick_line((RIGHT_X, TOP_Y + 6), (RIGHT_X - 4, BOT_Y - 8))
# hook flicking UP and LEFT
thick_line((RIGHT_X - 4, BOT_Y - 8), (RIGHT_X - 22, BOT_Y - 22))

# Stroke 3: upper inner 横 — spans wall to wall at ~y=125
UPPER_H_Y = 128
thick_line((LEFT_X_TOP - 1, UPPER_H_Y), (RIGHT_X - 2, UPPER_H_Y))

# Stroke 4: lower inner 横 — spans wall to wall at ~y=200
LOWER_H_Y = 202
thick_line((LEFT_X_TOP - 2, LOWER_H_Y), (RIGHT_X - 3, LOWER_H_Y))

# Stroke 5: middle 竖 — from top horizontal down past the bottom horizontal
# extends slightly below BOT_Y
thick_line((MID_X, TOP_Y + 4), (MID_X, BOT_Y + 8))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0168_用/01_用.png")
print("saved 01_用.png")
