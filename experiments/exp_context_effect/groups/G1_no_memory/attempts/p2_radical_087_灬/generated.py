"""Render 灬 (4-dot fire radical) as a 300x300 PNG.

Four short slanted dots along a baseline. Leftmost dot slants
leftward (like a small 撇); middle two slant slightly leftward;
rightmost dot slants rightward (like a small 捺/点).
"""
import os
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# Baseline area around y ~ 200-235 (lower-middle of canvas)
# Four dots roughly evenly spaced across x = 60..240
def draw_dot(draw, x_top, y_top, x_bot, y_bot, width=8):
    """Draw a slanted dot as a thick line with rounded ends."""
    # Draw main line
    draw.line([(x_top, y_top), (x_bot, y_bot)], fill="black", width=width)
    # Rounded ends
    r = width // 2
    draw.ellipse([x_top - r, y_top - r, x_top + r, y_top + r], fill="black")
    draw.ellipse([x_bot - r, y_bot - r, x_bot + r, y_bot + r], fill="black")

# All three left dots slant down-left (like small 撇); rightmost is a 点 slanting down-right.
# Dot 1 (leftmost): longest, most pronounced left slant
draw_dot(draw, 88, 200, 62, 240, width=8)

# Dot 2: shorter, slants down-left
draw_dot(draw, 128, 208, 112, 240, width=7)

# Dot 3: shorter, slants down-left
draw_dot(draw, 172, 208, 156, 240, width=7)

# Dot 4 (rightmost): slants down-right (top-left to bottom-right), like a 点
draw_dot(draw, 212, 200, 240, 240, width=8)

out_path = os.path.join(os.path.dirname(__file__), "01_灬.png")
img.save(out_path)
print(f"Saved {out_path}")
