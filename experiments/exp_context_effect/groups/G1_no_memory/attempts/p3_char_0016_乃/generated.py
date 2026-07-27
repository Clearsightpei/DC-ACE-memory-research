"""G1 render of 乃 (nǎi) — 2 strokes: 横折折折钩 + 撇. Revision 2."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 6

# Stroke 1: 横折折折钩
# Smoother curve: horizontal top → sharp turn → long diagonal down-left →
# curve at bottom → sweep right → upward hook.
s1 = [
    (65, 100),
    (110, 95),
    (160, 92),
    (210, 92),
    (225, 100),
    (228, 118),
    (210, 145),
    (180, 180),
    (155, 215),
    (150, 240),
    (165, 255),
    (190, 255),
    (210, 245),
    (218, 225),
    (215, 205),  # hook tip curling up-left
]
draw.line(s1, fill=INK, width=LW, joint="curve")

# Stroke 2: 撇 — starts high inside the top-left area of stroke 1,
# sweeps down-left with a long tail.
s2 = [
    (120, 115),
    (115, 145),
    (108, 180),
    (95, 220),
    (75, 255),
    (55, 275),
]
draw.line(s2, fill=INK, width=LW, joint="curve")

out = os.path.join(os.path.dirname(__file__), "01_乃.png")
img.save(out)
print(out)
