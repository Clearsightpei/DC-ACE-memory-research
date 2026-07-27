"""Render 也 to a 300x300 PNG using PIL.

也 has 3 strokes:
  Stroke 1 (横折钩): horizontal top, folds down on the right, small hook
    at bottom-left. This forms the top-lid and the right vertical wall
    of the container.
  Stroke 2 (竖): a short vertical inside the container (starts high up
    near/above the top lid, drops through it).
  Stroke 3 (竖弯钩): a big sweeping stroke — starts upper-left, sweeps
    DOWN-LEFT as a long shallow diagonal (crossing under everything),
    curls RIGHT along the bottom baseline, then HOOKS UP at the far
    right. This is the signature "belly" of 也.

Reference: sibling of 乜 (which lacks the middle 竖). 也 = 乜 + middle 竖.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def line(x1, y1, x2, y2, width=7):
    draw.line([(x1, y1), (x2, y2)], fill="black", width=width)


def dab(x, y, r=4):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier(p0, p1, p2, width=7, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    for a, b in zip(pts[:-1], pts[1:]):
        draw.line([a, b], fill="black", width=width)


# ---------------------------------------------------------------
# Stroke 1: 横折钩 — top-lid + right vertical wall + tiny bottom hook
# top: from (105, 110) to (225, 105)
# fold down on right to (230, 250)
# small hook at bottom pointing up-left (tiny flick)
# ---------------------------------------------------------------
# 顿 at start
dab(105, 110, r=5)
# top horizontal
line(105, 110, 225, 105, width=8)
# shoulder dab at fold
dab(225, 105, r=6)
# vertical drop on right
line(225, 105, 230, 250, width=8)
# small terminal hook at bottom (up-left flick)
line(230, 250, 215, 240, width=7)

# ---------------------------------------------------------------
# Stroke 2: middle 竖 — tall vertical inside the container
# starts ABOVE the top-lid (piercing through it) and drops down
# into upper-mid body. In 也 this middle 竖 is prominent.
# ---------------------------------------------------------------
dab(165, 60, r=5)
line(165, 60, 165, 180, width=8)

# ---------------------------------------------------------------
# Stroke 3: 竖弯钩 (the signature belly)
# Phase A: starts upper-left around (80, 130). Long sweep down-LEFT
#          as a shallow diagonal crossing under the top-lid, ending
#          near bottom-left (30, 225).
# Phase B: bottom curl going RIGHT along baseline, ending ~(255, 255).
# Phase C: terminal hook UP at far right ~(260, 215).
# ---------------------------------------------------------------

# Phase A: start dab, long down-left diagonal
dab(80, 130, r=5)
bezier((80, 130), (55, 180), (30, 225), width=8)

# Phase B: bottom curl right along baseline
bezier((30, 225), (110, 275), (255, 255), width=8)

# Phase C: terminal hook up at right end
line(255, 255, 262, 215, width=7)
dab(262, 215, r=4)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0047_也/01_也.png"
)
print("saved")
