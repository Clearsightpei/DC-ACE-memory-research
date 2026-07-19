"""Render the radical 儿 (2 strokes) to a 300x300 PNG.

Strokes:
  1) 撇 (pie): starts upper-left area, curves down and to the left.
  2) 竖弯钩 (shu-wan-gou): vertical from upper-right area, curves
     rightward at bottom, then small hook up at the end.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
STROKE = 6


def smooth_curve(points, steps=40):
    """Sample a smooth Catmull-Rom-ish curve through control points."""
    # Duplicate endpoints for boundary handling.
    pts = [points[0]] + list(points) + [points[-1]]
    result = []
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
            result.append((x, y))
    result.append(points[-1])
    return result


def draw_smooth(control_pts, width=STROKE):
    curve = smooth_curve(control_pts)
    draw.line(curve, fill=INK, width=width, joint="curve")
    # Round caps
    r = width / 2
    for end in (curve[0], curve[-1]):
        draw.ellipse((end[0] - r, end[1] - r, end[0] + r, end[1] + r), fill=INK)


# Stroke 1: 撇 (pie) — starts upper mid-left, curves down-left with
# gentle arc; ends near bottom-left.
pie_pts = [
    (130, 80),
    (118, 130),
    (102, 180),
    (82, 225),
    (62, 255),
]
draw_smooth(pie_pts)

# Stroke 2: 竖弯钩 — vertical from upper-right, curves rightward at
# the bottom into a longer horizontal, ending with a short upward hook.
# Down + curve segment
shuwan_pts = [
    (170, 85),
    (172, 135),
    (176, 185),
    (188, 225),
    (215, 250),
    (245, 253),
    (258, 250),
]
draw_smooth(shuwan_pts)

# Hook up at end (short upward tick)
hook_pts = [
    (258, 250),
    (259, 235),
    (256, 220),
]
draw_smooth(hook_pts)

out_path = os.path.join(os.path.dirname(__file__), "01_儿.png")
img.save(out_path)
print(f"Wrote {out_path}")
