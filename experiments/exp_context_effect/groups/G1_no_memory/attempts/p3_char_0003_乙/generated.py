"""G1 render of 乙 (yǐ) — single stroke: 横折弯钩.

Composed as one continuous ink path:
  1) short slight rise from upper-left to upper-right (the 横 top segment)
  2) sharp turn downward-left (the 折), diagonal descending curve
  3) sweep along the bottom (弯), curving right along the baseline
  4) small upward hook at the right end (钩)

Rendered with PIL at 300x300, black ink on white.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6  # stroke width


def catmull_rom(points, samples_per_seg=40):
    """Return interpolated points along a Catmull-Rom spline through `points`."""
    pts = [points[0]] + list(points) + [points[-1]]
    out = []
    for i in range(len(pts) - 3):
        p0, p1, p2, p3 = pts[i], pts[i + 1], pts[i + 2], pts[i + 3]
        for s in range(samples_per_seg):
            t = s / samples_per_seg
            t2 = t * t
            t3 = t2 * t
            x = 0.5 * (
                (2 * p1[0])
                + (-p0[0] + p2[0]) * t
                + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2
                + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3
            )
            y = 0.5 * (
                (2 * p1[1])
                + (-p0[1] + p2[1]) * t
                + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2
                + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3
            )
            out.append((x, y))
    out.append(points[-1])
    return out


def stroke(points, width=LW):
    """Draw a smooth stroke through control points as a series of line segments and dots."""
    smooth = catmull_rom(points)
    for i in range(len(smooth) - 1):
        draw.line([smooth[i], smooth[i + 1]], fill=INK, width=width)
    # cap ends
    r = width / 2
    for p in (smooth[0], smooth[-1]):
        draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=INK)


# 乙 as one continuous stroke.
# Coordinates in image space (y grows DOWN).
# Segment A: 横 top -- small horizontal from left to right
# Segment B: 折 -- sharp turn, diagonal down-left descending curve
# Segment C: 弯 -- big bottom curve arcing right along the baseline
# Segment D: 钩 -- small vertical hook at right end
# Draw the main body of 乙 (横折弯) as one smooth stroke,
# then the terminal 钩 as a short vertical stub going upward.
body = [
    (85, 110),   # start of 横 (top-left), small dip
    (110, 100),  # rising
    (150, 100),  # top plateau
    (175, 108),  # end of 横 (small turn)
    (155, 145),  # 折 diagonal descent
    (115, 185),  # midway down-left
    (85, 225),   # bottom-left of belly
    (115, 250),  # sweep across bottom
    (170, 253),  # bottom center-right
    (215, 240),  # rising into base of 钩
]
stroke(body, width=LW)

# 钩 — short vertical stub going UP at the right end.
hook = [
    (215, 240),
    (218, 220),
    (220, 200),
]
stroke(hook, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_乙.png")
img.save(out_path)
print(f"Wrote {out_path}")
