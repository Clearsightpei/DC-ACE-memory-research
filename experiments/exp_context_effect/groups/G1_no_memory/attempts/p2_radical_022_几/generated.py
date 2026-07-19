"""G1 render of radical 几 (2 strokes).

Stroke 1: 撇 (piě) — starts near upper-left of the radical, curves down
and slightly left.
Stroke 2: 横折弯钩 (héng-zhé-wān-gōu) — horizontal top, turn down on the
right, curve leftward at the bottom, then a small hook up-right.
Rendered at 300x300, white background, black ink, using PIL.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6  # ink line width


def smooth_curve(points, steps=40):
    """Draw a smooth curve through the given control points using
    Catmull-Rom-style interpolation, as a series of short line segments."""
    if len(points) < 2:
        return
    # Duplicate endpoints so Catmull-Rom covers the whole path.
    pts = [points[0]] + list(points) + [points[-1]]
    out = []
    for i in range(len(pts) - 3):
        p0, p1, p2, p3 = pts[i], pts[i + 1], pts[i + 2], pts[i + 3]
        for s in range(steps):
            t = s / steps
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
    for a, b in zip(out[:-1], out[1:]):
        draw.line([a, b], fill=INK, width=LW)


def dot(p, r=LW / 2):
    draw.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=INK)


# Stroke 1: 撇 — starts near (108, 90) at top, curves down and left to (60, 245)
s1 = [
    (108, 88),
    (100, 120),
    (90, 155),
    (78, 195),
    (68, 225),
    (58, 248),
]
smooth_curve(s1, steps=30)
dot(s1[0])

# Stroke 2: 横折弯钩
# Starts just to the right of stroke 1's top (~118, 92), goes right along the
# top to (~225, 88), turns down along the right side, curves left near the
# bottom, and finishes with an upward-right hook.
s2_top = [
    (118, 92),
    (155, 88),
    (195, 86),
    (225, 88),
]
smooth_curve(s2_top, steps=25)
dot(s2_top[0])

# right side + bottom curve (弯)
s2_right = [
    (225, 88),
    (230, 125),
    (232, 160),
    (230, 190),
    (222, 220),
    (205, 240),
    (180, 250),
    (155, 248),
    (140, 240),
]
smooth_curve(s2_right, steps=40)

# hook: upward-right tick from end of curve
hook_start = (140, 240)
hook_end = (162, 218)
draw.line([hook_start, hook_end], fill=INK, width=LW + 1)
dot(hook_end)

out_path = os.path.join(os.path.dirname(__file__), "01_几.png")
img.save(out_path)
print(f"wrote {out_path}")
