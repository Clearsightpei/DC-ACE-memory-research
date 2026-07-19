"""Render radical 见 (4画) as 300x300 PNG using PIL.
Structure (matching GT):
  Top: small enclosed box (目-like) with a horizontal bar at its base.
  Bottom: two legs - 撇 (left, curved down-left) and 竖弯钩 (right, curves right with hook up).

Nominal 4 strokes:
  1. 竖 - left vertical of the top box
  2. 横折 - top horizontal + right vertical of the top box (one stroke)
  3. 撇 - left leg, curves down-left from bottom-left of box
  4. 竖弯钩 - right leg from bottom of box, curves right, hooks up
The bottom horizontal of the box is drawn as part of stroke 4's start (a common
brush-order simplification) so overall shape matches GT.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
T = 5


def line(p1, p2, w=T):
    d.line([p1, p2], fill=INK, width=w)


def curve(points, w=T):
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=INK, width=w)
    for p in points:
        d.ellipse([p[0] - w // 2, p[1] - w // 2, p[0] + w // 2, p[1] + w // 2], fill=INK)


# --- Top box: upper-center of canvas ---
box_L = 110
box_R = 195
box_T = 70
box_B = 165

# Stroke 1: 竖 (left vertical of box)
line((box_L, box_T + 5), (box_L + 4, box_B), T)

# Stroke 2: 横折 (top horizontal + right vertical, one stroke)
# horizontal top
line((box_L, box_T), (box_R, box_T + 5), T)
# tiny fold
line((box_R, box_T + 5), (box_R, box_T + 8), T)
# right vertical (slight inward taper)
line((box_R, box_T + 8), (box_R - 5, box_B), T)

# Inner/base horizontal of the box (bottom bar of 目-like shape)
# Drawn as bottom close of box - part of the visual identity of 见.
line((box_L + 2, box_B), (box_R - 4, box_B), T)

# Stroke 3: 撇 (left leg) - starts at bottom-left of box, curves down-left
pie_pts = [
    (box_L + 5, box_B - 2),
    (box_L, box_B + 25),
    (box_L - 12, box_B + 55),
    (box_L - 30, box_B + 80),
    (box_L - 50, box_B + 100),
]
curve(pie_pts, T)

# Stroke 4: 竖弯钩 (right leg) - starts roughly middle of box base,
# goes down (竖), curves right along bottom (弯), then a short hook up (钩)
shu_wan_gou = [
    (155, box_B - 2),   # start at middle-bottom of box
    (152, box_B + 25),
    (152, box_B + 55),  # vertical segment
    (156, box_B + 80),
    (168, box_B + 95),  # begin curve right
    (188, box_B + 100),
    (210, box_B + 98),
    (225, box_B + 92),  # end of horizontal-ish sweep
    (232, box_B + 82),  # hook up
]
curve(shu_wan_gou, T)

out_path = os.path.join(os.path.dirname(__file__), "01_见.png")
img.save(out_path)
print(f"Saved {out_path}")
