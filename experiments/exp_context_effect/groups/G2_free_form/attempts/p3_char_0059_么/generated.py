"""
Render 么 to a 300x300 PNG.

么 has 3 strokes (matching GT reading):
  1. Top small 撇 — short diagonal from upper-right to lower-left,
     sitting near the top-center of the glyph.
  2. 撇折 — starts a bit lower and to the right of stroke 1, sweeps
     down-left as a 撇, then turns with a short flick to the right/down
     (the 折). This is the middle "belly".
  3. 捺 / long slanted point — starts near where stroke 2 turned
     (or just below/right of it), sweeps down and to the right,
     broadening toward the tail (like a 长点 / 捺).

Layout (300x300):
- Whole glyph occupies roughly x=[70..245], y=[55..245].
"""

from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke_polyline(points, widths):
    n = len(points)
    if n < 2:
        return
    for i in range(n - 1):
        x0, y0 = points[i]
        x1, y1 = points[i + 1]
        w0 = widths[i]
        w1 = widths[i + 1]
        seg_len = math.hypot(x1 - x0, y1 - y0)
        steps = max(2, int(seg_len * 3))
        for s in range(steps + 1):
            t = s / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            w = w0 + (w1 - w0) * t
            r = w / 2
            draw.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


# ---- Stroke 1: top small 撇 (short flick) ----
# Upper-right to lower-left, small.
s1_pts = [(160, 60), (150, 72), (135, 90), (122, 105)]
s1_w = [6, 7, 7, 4]
stroke_polyline(s1_pts, s1_w)

# ---- Stroke 2: 撇折 — body's belly ----
# Start upper-mid-right (a bit below/right of stroke 1),
# sweep down-left, then折 turn to the lower-right (short flick).
s2_pts = [
    (175, 110),
    (165, 130),
    (145, 155),
    (120, 178),
    (105, 195),
    (115, 205),   # 折 turn (small hook)
    (135, 208),
]
s2_w = [7, 8, 8, 7, 6, 6, 5]
stroke_polyline(s2_pts, s2_w)

# ---- Stroke 3: 捺 (long slanted point) ----
# Starts near the top of stroke-2's ending region (a bit above the折 turn),
# sweeps down and to the lower-right with a broadening tail.
s3_pts = [
    (150, 165),
    (170, 190),
    (195, 215),
    (220, 235),
    (240, 245),
    (248, 244),  # slight tail lift
]
s3_w = [5, 8, 11, 13, 12, 6]
stroke_polyline(s3_pts, s3_w)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0059_么/01_么.png"
img.save(out)
print("saved", out)
