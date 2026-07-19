"""G1 render of 二 (radical, 2 strokes). Revision 1.

Two horizontal strokes: a shorter upper 横 and a longer lower 横.
Adds a gentle arc (rise then dip toward end) and clear 起笔/顿笔
so the shape reads more brush-like, matching GT proportions.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def heng(draw, x0, y0, x1, y1, thickness=12, arc=6):
    """A 横 stroke drawn as a chain of short segments along a shallow
    arc: subtle rise in the middle, tiny drop at the very right, with
    an 起笔 nub on the left and 顿笔 thickening on the right."""
    steps = 40
    pts = []
    for i in range(steps + 1):
        t = i / steps
        # Linear interpolation for the baseline
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        # Shallow parabolic rise: peak of -arc at t=0.5
        y -= arc * 4 * t * (1 - t)
        # Small dip at very right end (last 15%)
        if t > 0.85:
            y += (t - 0.85) / 0.15 * (arc * 0.6)
        pts.append((x, y))

    # Draw the body
    draw.line(pts, fill=BLACK, width=thickness, joint="curve")

    # 起笔 (left) — small round nub
    r_start = thickness // 2 + 1
    draw.ellipse(
        [pts[0][0] - r_start, pts[0][1] - r_start,
         pts[0][0] + r_start, pts[0][1] + r_start],
        fill=BLACK,
    )

    # 顿笔 (right) — larger thickening
    r_end = thickness // 2 + 3
    ex, ey = pts[-1]
    draw.ellipse(
        [ex - r_end, ey - r_end + 1, ex + r_end, ey + r_end + 1],
        fill=BLACK,
    )


# Upper 横 — shorter (~35% of width), around y=118, gentle arc
heng(draw, x0=100, y0=122, x1=205, y1=118, thickness=11, arc=5)

# Lower 横 — longer (~65% of width), around y=225, gentler arc
heng(draw, x0=50, y0=228, x1=250, y1=222, thickness=13, arc=6)

out = (
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G1_no_memory/attempts/"
    "p2_radical_018_二/01_二.png"
)
img.save(out)
print(out)
