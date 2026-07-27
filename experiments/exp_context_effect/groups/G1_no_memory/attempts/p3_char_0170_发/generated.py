"""Render 发 as a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def curve(points, width=LW):
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill=BLACK, width=width)
    for p in points:
        d.ellipse([p[0] - width/2, p[1] - width/2,
                   p[0] + width/2, p[1] + width/2], fill=BLACK)

# Stroke 1: short 撇 top-left (the small hook-like piece at top of 发)
curve([(115, 70), (105, 88), (98, 105)])

# Stroke 2: short 横折 / hook piece at top — small angle top-center-left
curve([(105, 105), (125, 100), (145, 105), (155, 115)])

# Stroke 3: long sweeping 撇 — top-center down to lower-left, main left diagonal
curve([(155, 75), (140, 110), (115, 150), (85, 195), (55, 240), (40, 265)])

# Stroke 4: dot (点) upper right
curve([(220, 90), (232, 105), (240, 122)], width=LW + 1)

# Stroke 5: the 乂 first stroke — 撇 from mid to lower-left
curve([(165, 155), (145, 185), (125, 215), (110, 245)])

# Stroke 6: the 乂 second stroke — long 捺 from mid down to lower-right
curve([(150, 155), (180, 190), (215, 220), (250, 245), (275, 258)])

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_发.png")
img.save(out)
print(f"Saved: {out}")
