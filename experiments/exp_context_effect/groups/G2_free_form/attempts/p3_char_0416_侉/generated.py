"""
侉 = 亻 (left) + 夸 (right)
夸 = 大 (top) + 亏 (bottom: 一 + 丂-like hook)

Layout on 300x300:
- 亻 occupies left ~30% (x 40-100), full height
- 夸 occupies right ~65% (x 100-270), full height, split top(大)/bottom(亏)

Rendered with PIL using thick black brush strokes on white background.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
BRUSH = 7  # base brush width


def stroke(pts, width=BRUSH):
    """Draw a stroke as connected line segments."""
    d.line(pts, fill=BLACK, width=width, joint="curve")
    # round ends
    for (x, y) in [pts[0], pts[-1]]:
        r = width // 2
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


def bezier(p0, p1, p2, steps=32):
    """Quadratic bezier control points -> list of (x,y)."""
    out = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        out.append((x, y))
    return out


# ---------------- 亻 (person radical, left) ----------------
# 撇 (top diagonal, from upper-right down to lower-left)
pie = bezier((85, 55), (75, 130), (35, 220))
stroke(pie, width=8)

# 竖 (vertical, from upper-mid down)
stroke([(78, 115), (78, 250)], width=8)


# ---------------- 夸 right side ----------------
# 大 on top
# 横 (horizontal top of 大)
stroke([(120, 90), (260, 88)], width=8)

# 撇 of 大 (diagonal from top-center down-left)
pie2 = bezier((190, 65), (170, 110), (135, 160))
stroke(pie2, width=8)

# 捺 of 大 (diagonal from top-center down-right)
na = bezier((190, 78), (215, 120), (255, 160))
stroke(na, width=8)

# 亏 on bottom
# 横 (long horizontal, top of 亏)
stroke([(115, 175), (265, 175)], width=8)

# 丂 style: short horizontal on top of the hook body
stroke([(140, 210), (240, 210)], width=8)

# 竖折折钩 -- the twisting bottom stroke of 亏 (looks like a hook)
# Start upper-right of the short horizontal, sweep down-left with a hook
hook_pts = bezier((235, 208), (215, 240), (145, 268))
stroke(hook_pts, width=8)
# small hook flick up-and-left at the terminal
stroke([(145, 268), (135, 258)], width=8)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0416_侉/01_侉.png")
