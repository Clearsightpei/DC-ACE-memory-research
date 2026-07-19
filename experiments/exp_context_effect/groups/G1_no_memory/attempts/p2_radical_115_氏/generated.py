"""G1 render of radical 氏 (4 strokes) using PIL. Revision 2."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def stroke(points, width=6):
    draw.line(points, fill=BLACK, width=width, joint="curve")
    for (x, y) in [points[0], points[-1]]:
        r = width / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# 氏 has 4 strokes:
# 1. 撇 (piě): short slanted stroke top-left going down-left
# 2. 横折 (héng zhé): short horizontal on top-left then down (forms the top hat + left leg)
#    Actually canonical stroke order:
#    stroke 1 = 撇 (short piě on the top-left)
#    stroke 2 = 竖提 (shù tí) — down and up-right hook (the left vertical)
#    stroke 3 = 横 (short horizontal in the middle)
#    stroke 4 = 斜钩 (xié gōu) — big diagonal hook sweeping right

# Stroke 1: 撇 — from ~(140, 80) sweeping down-left to (100, 130)
stroke([(140, 78), (128, 100), (110, 128)], width=6)

# Stroke 2: 竖提 — vertical line dropping from top area down, then hooking up-right
# Starts at (108, 125), goes down to (115, 215), hook up-right to (150, 205)
stroke([(108, 125), (112, 170), (118, 215), (155, 205)], width=6)

# Stroke 3: 横 — short horizontal across middle
# from (110, 158) to (185, 155)
stroke([(112, 158), (150, 155), (188, 152)], width=6)

# Stroke 4: 斜钩 — starts at top (near where stroke 1 tip meets), curves down-right
# and out with a small upturn (hook) at the end
# Start at (155, 78), curve down through (175, 160), (200, 210), out to (250, 245), hook up (258, 232)
stroke([
    (155, 80),
    (168, 115),
    (180, 150),
    (195, 185),
    (215, 215),
    (240, 238),
    (258, 240),
    (262, 228),
], width=6)

out = os.path.join(os.path.dirname(__file__), "01_氏.png")
img.save(out)
print(f"Saved {out}")
