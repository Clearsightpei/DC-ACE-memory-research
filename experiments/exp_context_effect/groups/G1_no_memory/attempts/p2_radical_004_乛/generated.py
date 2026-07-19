"""Render radical 乛 (héng-gōu / horizontal-turn) to 300x300 PNG."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# 乛 = horizontal stroke that turns and descends as a short pie.
# GT shows: starts left-low, rises slightly through a mostly-flat horizontal,
# then bends downward-left at the right end into a short falling stroke.
# The whole radical sits in the middle band of the canvas.

ink = "black"
thick = 7

# Horizontal segment: slight upward tilt from left to right.
# Left start ~ (70, 165) with a small nub tick at the beginning (typical 起笔).
# Then flat to about (215, 145) — the turn point.
x0, y0 = 70, 168
x1, y1 = 215, 148  # turn point

# Small starting nub (curved tick going down-left, typical 起笔 for 乛)
draw.ellipse((x0-8, y0-2, x0+2, y0+8), fill=ink)

# Horizontal stroke as a shallow arc (curving slightly downward-then-up).
# Approximate with a quadratic Bezier by sampling points.
def qbez(p0, p1, p2, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts

# Horizontal arc: dips slightly then rises to turn point
ctrl = (140, 175)
arc_pts = qbez((x0, y0), ctrl, (x1, y1))
for i in range(len(arc_pts) - 1):
    draw.line([arc_pts[i], arc_pts[i + 1]], fill=ink, width=thick)

# Falling segment (pie-like): from turn point down-slightly-left
x2, y2 = 205, 208
draw.line([(x1, y1), (x2, y2)], fill=ink, width=thick)

# Slight taper at the pie tip
draw.ellipse((x2-3, y2-3, x2+3, y2+3), fill=ink)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_004_乛/01_乛.png")
