"""
Render 斤 (radical, 4 strokes) at 300x300, black ink on white.

Stroke decomposition (canonical):
  1. Short 撇 (top-left): short throw-away, upper region, angles down-left.
  2. Long 撇 (main body): starts near top-center, sweeps down-and-left in
     a long bowed arc — this is the character's dominant silhouette line.
  3. Short 横 (top-right): horizontal beat near the top, meeting the long
     撇's start on the right side.
  4. 竖 (right vertical): descends straight down from the right end of
     the 横 (or just below it), forming the right "pillar" of the radical.

Uses PIL brush-dab technique per drawer_memory principles.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    dx, dy = x1 - x0, y1 - y0
    dist = math.hypot(dx, dy)
    if steps is None:
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + dx * t
        y = y0 + dy * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=400):
    """Quadratic Bezier with tapered brush dabs."""
    for i in range(steps + 1):
        t = i / steps
        one = 1 - t
        x = one * one * p0[0] + 2 * one * t * p1[0] + t * t * p2[0]
        y = one * one * p0[1] + 2 * one * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ----- REVISION notes vs GT -----
# GT is thinner overall, character fills more of the canvas, and the
# right 竖 extends far lower (nearly to the bottom, past the long 撇's
# tail). Also the short 横 in GT sits with a very slight upward tilt
# and joins the long 撇's shoulder near its start. Applied per
# principle 4 (standalone: thinner + longer flicks + fill the frame)
# and "move the knob further than intuition suggests."

# ----- Stroke 1: short 撇 (top-left) -----
# starts upper-right, throws down-left. Thin primary; a bit longer +
# more decisively down-left so it isn't a nub.
s1_p0 = (128, 58)
s1_p1 = (108, 82)
s1_p2 = (78, 118)
dab(s1_p0[0], s1_p0[1], 5.5)
bezier_dabs(s1_p0, s1_p1, s1_p2, r0=4.5, r1=1.2, steps=260)

# ----- Stroke 2: short 横 (top-right) -----
# Gentle up-tilt, wider extent to fill canvas.
s2_x0, s2_y0 = 138, 78
s2_x1, s2_y1 = 232, 62
dab(s2_x0, s2_y0, 4.8)
line_dabs(s2_x0, s2_y0, s2_x1, s2_y1, r0=3.8, r1=3.8, steps=220)
dab(s2_x1, s2_y1, 5.2)

# ----- Stroke 3: long 撇 (main body) -----
# Sweeps from top-center down-and-far-left. Longer, thinner, bows a bit
# harder for standalone scale.
s3_p0 = (152, 82)
s3_p1 = (120, 180)
s3_p2 = (42, 275)
dab(s3_p0[0], s3_p0[1], 6.5)  # 顿笔 at start
bezier_dabs(s3_p0, s3_p1, s3_p2, r0=5.5, r1=1.2, steps=520)

# ----- Stroke 4: 竖 (right vertical) -----
# Long vertical — extends nearly to the bottom of the canvas so the
# right pillar dominates like in GT. Slightly thinner. Blunt ends.
s4_x = 215
s4_y0 = 92
s4_y1 = 278
dab(s4_x, s4_y0, 5.2)  # 顿笔 top
line_dabs(s4_x, s4_y0, s4_x, s4_y1, r0=4.2, r1=4.2, steps=260)
dab(s4_x, s4_y1, 5.2)  # blunt terminal

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_101_斤/01_斤.png"
img.save(out)
print(f"wrote {out}")
