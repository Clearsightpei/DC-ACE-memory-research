"""Render 么 as a 300x300 PNG using PIL.

Structure (3 strokes) — 么 in standard form:
 1) 撇折 (top): a small 撇 going down-left then a short horizontal/rightward turn
 2) 撇 (main): a long diagonal from upper-middle area sweeping down-left
 3) 点 (bottom-right): a short thick diagonal press stroke
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def stroke(points, width=7):
    draw.line(points, fill="black", width=width, joint="curve")
    r = width // 2
    for (x, y) in [points[0], points[-1]]:
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


# Stroke 1: top 撇折 — start upper area, 撇 down-left, then折 turns rightward
# In GT this is a small "7"-like shape at top-center
s1 = [
    (170, 70),
    (150, 90),
    (135, 110),   # end of 撇
    (155, 115),   # 折: short turn to the right
    (170, 112),
]
stroke(s1, width=6)

# Stroke 2: main 撇 — long diagonal from upper-right area down to lower-left
# starts near where stroke 1 ended, sweeps far down-left with a slight curve
s2 = [
    (180, 115),
    (165, 140),
    (145, 170),
    (120, 205),
    (100, 235),
    (90, 255),
]
stroke(s2, width=7)

# Stroke 3: 点 — a short diagonal press stroke at bottom-right
# Goes from upper-left to lower-right, thickens as it goes
s3 = [
    (155, 215),
    (180, 235),
    (210, 255),
    (225, 260),
]
stroke(s3, width=7)

out = os.path.join(os.path.dirname(__file__), "01_么.png")
img.save(out)
print(f"Wrote {out}")
