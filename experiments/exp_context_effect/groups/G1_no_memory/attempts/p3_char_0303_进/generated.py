"""Render 进 (jin4) — 井 + 辶 walk radical — 300x300 PNG."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

def line(pts, width=LW):
    d.line(pts, fill=BLACK, width=width, joint="curve")

# --- 井 (right side) ---
# Two verticals of 井 (slightly slanted, right side taller)
line([(165, 70), (155, 220)], width=LW)   # left vertical of 井
line([(225, 70), (240, 235)], width=LW)   # right vertical of 井

# Two horizontals of 井
line([(140, 105), (255, 115)], width=LW)  # upper horizontal
line([(135, 165), (250, 170)], width=LW)  # lower horizontal

# --- 辶 (walk radical, left) ---
# Top dot (small slanted stroke)
line([(105, 55), (120, 72)], width=LW)

# Small horizontal-ish stroke below dot
line([(80, 95), (115, 108)], width=LW)

# The 撇折 body (smooth Z-curve, comes down-left then curves)
zig = [
    (110, 108),
    (85, 135),
    (100, 155),
    (75, 195),
    (95, 220),
]
line(zig, width=LW)

# Bottom 平捺 sweep — gentle downward-then-upward curve across bottom
sweep = [
    (55, 235),
    (100, 250),
    (160, 258),
    (220, 253),
    (265, 240),
    (280, 225),
]
line(sweep, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_进.png")
img.save(out_path)
print("wrote", out_path)
