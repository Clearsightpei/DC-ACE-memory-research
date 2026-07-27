"""Render 了 (liǎo) — 2 strokes: 横撇弯钩 + 竖钩 (curving left)."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

INK = "black"
W = 7  # stroke width


def stroke_polyline(points, width=W):
    draw.line(points, fill=INK, width=width, joint="curve")
    r = width // 2
    for x, y in points:
        draw.ellipse((x - r, y - r, x + r, y + r), fill=INK)


# Stroke 1: 横撇 — starts low-left, rises across to the right, curves down-right into a small hook
s1 = [
    (55, 85),
    (90, 78),
    (135, 72),
    (180, 70),
    (205, 74),
    (218, 88),
    (215, 105),
    (205, 112),
]
stroke_polyline(s1)

# Stroke 2: 弯钩 — vertical curve starting near top-right of stroke1,
# descending with slight leftward curve, then hooking left at the bottom.
s2 = [
    (180, 92),
    (175, 130),
    (165, 170),
    (152, 210),
    (135, 238),
    (115, 255),
    (92, 260),
    (72, 256),
]
stroke_polyline(s2)

out_path = os.path.join(os.path.dirname(__file__), "01_了.png")
img.save(out_path)
print(f"Wrote {out_path}")
