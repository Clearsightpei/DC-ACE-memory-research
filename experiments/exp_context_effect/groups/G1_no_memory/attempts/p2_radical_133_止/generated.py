"""Render 止 (radical, 4 strokes) at 300x300 using PIL."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

W = 4  # stroke width

# Stroke order of 止:
# 1) short vertical (top-middle) — 竖
# 2) short horizontal (middle-left, from vertical going right)  — 横
# 3) longer vertical on the left going down — 竖
# 4) long bottom horizontal — 横 (bottom)

# Coordinates roughly matching GT (PIL: y grows DOWN)
# Middle vertical (stroke 1): from ~ (150, 80) down to (150, 220)
draw.line([(150, 80), (150, 220)], fill="black", width=W)

# Left short vertical (stroke 3-ish placement): the character has a short
# left vertical at middle-left going down to the base
draw.line([(105, 140), (105, 220)], fill="black", width=W)

# Short horizontal in the middle connecting left vertical to main vertical, extending right
draw.line([(105, 165), (200, 165)], fill="black", width=W)

# Bottom horizontal (long) — the base
draw.line([(60, 220), (240, 220)], fill="black", width=W)

out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "01_止.png")
img.save(out_path)
print(f"Saved {out_path}")
