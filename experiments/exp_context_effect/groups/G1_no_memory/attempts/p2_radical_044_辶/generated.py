"""Render the radical 辶 (chuo, walk) at 300x300, black on white."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def stroke(points, width=6):
    # Draw a smoothed polyline with rounded caps by using multiple line segments
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill="black", width=width)
    # Rounded caps/joints
    r = width // 2
    for (x, y) in points:
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

# 1) Top dot/short diagonal (点) — small comma-shaped stroke, slanting down-right
stroke_top = [(90, 65), (105, 78), (115, 92)]
stroke(stroke_top, width=6)

# 2) Middle stroke (横折折撇) — smoother S curve
stroke_mid = [
    (70, 140),  # left start
    (100, 133), # horizontal right
    (115, 145), # turn down
    (95, 170),  # curve down-left (撇 direction)
    (90, 190),
    (100, 205), # bottom hook back to right
    (115, 210),
]
stroke(stroke_mid, width=6)

# 3) Bottom 平捺 — starts thin at upper-left, dips down, rises to right with a flare
stroke_bot = [
    (55, 220),
    (75, 235),
    (110, 250),
    (150, 258),
    (195, 255),
    (230, 245),
    (265, 225),
]
stroke(stroke_bot, width=7)
# Add a small flare at the right end (捺 tail)
draw.polygon([(258, 222), (275, 218), (268, 232)], fill="black")

out_path = os.path.join(os.path.dirname(__file__), "01_辶.png")
img.save(out_path)
print(f"Saved {out_path}")
