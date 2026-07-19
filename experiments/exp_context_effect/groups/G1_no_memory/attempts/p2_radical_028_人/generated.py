"""Render 人 (radical) at 300x300 using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# 人 has two strokes:
# 1) 撇 (piě): from upper-center, sweeping down-left, curving.
# 2) 捺 (nà): from near the top of the piě, going down-right, thickening.

# Stroke 1: 撇 — curved sweep from top center down to lower-left.
# Use a quadratic-ish curve by plotting many points and drawing thick line segments.
def draw_curve(points, widths):
    """Draw a curve with variable width by drawing lines between consecutive points."""
    for i in range(len(points) - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w = (widths[i] + widths[i + 1]) / 2
        draw.line([(x0, y0), (x1, y1)], fill="black", width=int(round(w)))
        # cap with circles for smoothness
        r = w / 2
        draw.ellipse([x0 - r, y0 - r, x0 + r, y0 + r], fill="black")
    # final cap
    x1, y1 = points[-1]
    r = widths[-1] / 2
    draw.ellipse([x1 - r, y1 - r, x1 + r, y1 + r], fill="black")


# 撇 (piě): starts with a small tick/hook at top around (155, 75),
# sweeps down-left, curving. Ends around (55, 255).
import math

# Small opening hook: a tiny stroke at the very top (like the GT's little cap).
hook_points = [(148, 68), (152, 72), (158, 78), (160, 85)]
hook_widths = [3, 5, 6, 6]
draw_curve(hook_points, hook_widths)

pie_points = []
pie_widths = []
N = 50
for i in range(N + 1):
    t = i / N
    x0, y0 = 158, 82
    # bend leftward more strongly at the tail
    x = x0 - (x0 - 55) * (t ** 1.35)
    y = y0 + (255 - y0) * (t ** 0.9)
    pie_points.append((x, y))
    # Width: modestly thick at top, taper to thin whisker at tail
    w = 7.5 - 6 * (t ** 1.3)
    pie_widths.append(max(1.5, w))

draw_curve(pie_points, pie_widths)

# 捺 (nà): starts at the top-right of the piě around (162, 95),
# goes down-right in a slightly curving path, swelling in width.
# GT shows it ending around (245, 245) with a firm, thick body then a
# slight taper. Its start is thin, mid is thick.
na_points = []
na_widths = []
for i in range(N + 1):
    t = i / N
    x0, y0 = 162, 95
    # gently curving down-right; slight bow (concave-up)
    x = x0 + (245 - x0) * t
    # y follows a curve that bows down slightly then flattens
    y = y0 + (250 - y0) * (t ** 0.92)
    na_points.append((x, y))
    # Width: thin start, swell through middle to ~11, gentle taper at end
    if t < 0.12:
        w = 2 + t * 30  # 2 -> 5.6
    elif t < 0.80:
        w = 5.6 + (t - 0.12) * 8  # 5.6 -> ~11
    else:
        w = 11 - (t - 0.80) * 25  # taper 11 -> ~6
    na_widths.append(max(2, w))

draw_curve(na_points, na_widths)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_人.png")
img.save(out_path)
print(f"Saved: {out_path}")
