"""Render 巳 (radical 071) as a 300x300 PNG using PIL.

巳 is a 3-stroke radical:
  1. 横折 (heng-zhe): horizontal top going right, then turning down (right side of the upper box).
  2. 横 (heng): horizontal middle stroke that closes the upper box.
  3. 竖弯钩 (shu-wan-gou): vertical from top-left going down, curving right along the bottom,
     ending with an upward hook.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
T = 5  # stroke thickness


def line(p1, p2, width=T):
    draw.line([p1, p2], fill=INK, width=width)


def curve(points, width=T):
    # draw a series of connected segments (polyline)
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=INK, width=width)


# Frame reference (glyph roughly centered in 米字格):
# top of glyph ~ y=80, bottom ~ y=230
# left ~ x=90, right ~ x=210

# --- Stroke 1: 横折 (top horizontal + turn down on right) ---
# Horizontal top from left-top to right, then a vertical going down to about mid.
curve([
    (95, 85),      # top-left corner (start of top horizontal)
    (200, 82),     # top-right corner
    (203, 100),    # small turn
    (200, 150),    # comes down to middle right
])

# --- Stroke 2: 横 (middle horizontal closing the upper box) ---
# from the left vertical inward to the right vertical, forming closed upper pocket.
line((94, 145), (200, 148))

# --- Stroke 3: 竖弯钩 (vertical-bend-hook) ---
# starts near top-left, goes down, curves right along bottom, ends with an upward hook.
curve([
    (95, 85),      # top start (same as stroke 1 origin)
    (92, 135),
    (92, 185),
    (98, 220),
    (120, 238),    # curve begins at bottom
    (170, 240),
    (210, 235),
    (222, 220),    # bottom-right corner
    (225, 200),    # hook rising upward
    (215, 195),    # hook tip
])

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_巳.png")
img.save(out_path)
print(f"Wrote {out_path}")
