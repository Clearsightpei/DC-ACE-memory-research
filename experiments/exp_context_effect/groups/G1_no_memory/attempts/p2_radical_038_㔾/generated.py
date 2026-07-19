"""G1 render of radical 㔾 (2 strokes)."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

W = 7  # brush width

# Stroke 1: 横折 — small starting tick, top horizontal, then right side down.
# Small starting tick (little diagonal nub above the top-left)
draw.line([(78, 105), (92, 118)], fill="black", width=W)
# Top horizontal
draw.line([(85, 115), (208, 118)], fill="black", width=W)
# Right side descending (slightly curving inward at bottom)
right_pts = [(208, 118), (210, 160), (211, 200), (208, 225)]
draw.line(right_pts, fill="black", width=W)

# Stroke 2: 竖弯 — left vertical curving into bottom sweep.
left_curve = [
    (86, 128),
    (84, 160),
    (82, 195),
    (84, 220),
    (92, 238),
    (110, 250),
    (140, 256),
    (170, 255),
    (195, 248),
    (208, 235),
    (212, 220),
]
draw.line(left_curve, fill="black", width=W)

# Small internal hook (㇄-like: short down then flick right)
hook_pts = [(115, 175), (128, 200), (150, 195)]
draw.line(hook_pts, fill="black", width=W)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_㔾.png"))
print("saved", os.path.join(out_dir, "01_㔾.png"))
