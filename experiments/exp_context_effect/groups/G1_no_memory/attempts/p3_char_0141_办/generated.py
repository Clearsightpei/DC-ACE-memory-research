"""Render 办 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)

def stroke(points, width=5):
    """Draw a polyline with rounded joints/caps."""
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=BLACK, width=width)
    r = width // 2
    for (x, y) in points:
        draw.ellipse((x-r, y-r, x+r, y+r), fill=BLACK)

# 办 — 4 strokes total. Structure: central 力 (2 strokes: 横折钩 + 撇)
# plus 丿 on left and 丶 on right.
# Center the character across the whole 300x300 canvas.

# Stroke 1: 横折钩 — top horizontal, turn down, small hook back to upper-left.
#   This forms the top and right side of the central 力.
p1 = [(120, 75), (200, 78), (195, 150), (180, 140)]
stroke(p1, width=6)

# Stroke 2: main 撇 — long sweeping curve from upper-middle down to lower-left.
#   Starts at the top-left of the 力, sweeps down and to the left.
p2 = [(130, 75), (128, 130), (115, 180), (90, 230), (65, 265)]
stroke(p2, width=7)

# Stroke 3: left 丿 (short slash) — sits to the LEFT of the 力, mid-height,
#   sloping down-left.
p3 = [(75, 150), (50, 205)]
stroke(p3, width=6)

# Stroke 4: right 丶 / short 捺 — sits to the RIGHT of the 力, mid-height,
#   sloping down-right.
p4 = [(220, 145), (250, 200), (265, 235)]
stroke(p4, width=6)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_办.png"))
print("Saved:", os.path.join(out_dir, "01_办.png"))
