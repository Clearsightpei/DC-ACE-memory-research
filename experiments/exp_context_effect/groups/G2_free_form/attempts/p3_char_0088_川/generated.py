"""
川 (chuān) — 3 strokes: 撇, 竖, 竖 (left curves, middle short vertical, right tall vertical).

Layout from GT:
  - Left 撇: starts ~upper-mid-left, curves down and slightly to the left; starts LOWER than the right verticals.
  - Middle 竖: short straight vertical, slightly below the top; centered a bit left of middle.
  - Right 竖: tallest, straight vertical on the right; starts highest.
  Aspect: roughly evenly-spaced three vertical elements filling middle band.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def brush_line(pts, width=8):
    # Draw a smooth line with round caps by dabbing circles along interpolated points.
    for i in range(len(pts) - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        steps = max(int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 1)
        for s in range(steps + 1):
            t = s / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            r = width / 2
            d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# Stroke 1: 撇 (left curved stroke).
# Starts high-left, curves down, ending lower-left with slight leftward flare.
pian_pts = [
    (95, 105),
    (92, 130),
    (88, 155),
    (82, 185),
    (74, 215),
    (65, 245),
    (55, 268),
]
brush_line(pian_pts, width=9)

# Stroke 2: middle 竖 (short vertical). Starts a bit below top, ends around 3/4 height.
mid_pts = [
    (150, 130),
    (150, 160),
    (150, 200),
    (150, 235),
]
brush_line(mid_pts, width=9)

# Stroke 3: right 竖 (tall vertical). Starts highest, ends near bottom.
right_pts = [
    (215, 100),
    (215, 140),
    (215, 190),
    (215, 240),
    (215, 270),
]
brush_line(right_pts, width=10)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0088_川/01_川.png")
print("wrote 01_川.png")
