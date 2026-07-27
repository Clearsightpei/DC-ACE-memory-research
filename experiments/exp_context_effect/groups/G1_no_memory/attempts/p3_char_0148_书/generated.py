"""Render 书 (shū) to a 300x300 PNG using PIL.

Structure of simplified 书 (4 strokes):
 1. 横折 (top): short horizontal at upper region, bends down forming
    a short vertical that reaches near / through the middle horizontal.
 2. 竖 with small 提/hook at bottom: long central vertical, extending
    below the horizontal, with tiny left-curl at the bottom.
 3. 横 (long horizontal) crossing through middle-lower area, whose
    right end continues as a curved 折折钩 that loops down and hooks
    back up-left (the characteristic right-side belly of 书).
 4. 点 (dot) at upper-right, diagonal.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 5


def line(p1, p2, w=LW):
    draw.line([p1, p2], fill=INK, width=w)


def polyline(points, w=LW):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i + 1]], fill=INK, width=w)


# --- Stroke 1: top 横折 (upper-left) ---
# Short horizontal high up, left of the vertical
polyline([(120, 90), (170, 90), (172, 165)])

# --- Stroke 3: long horizontal + right loop (drawn before vertical so
#     vertical overlays cleanly on top). Middle horizontal ---
polyline([(60, 165), (240, 165)])
# Right-side belly: from ~(240,165) curve down and back left-hooking
polyline([
    (240, 165),
    (248, 190),
    (240, 215),
    (215, 228),
    (195, 220),
])

# --- Stroke 2: main vertical with small hook at bottom ---
polyline([(150, 55), (150, 260)])
# Small hook curling left at the bottom
polyline([(150, 260), (140, 265), (128, 260)])

# --- Stroke 4: dot at upper right ---
polyline([(205, 88), (220, 108)], w=6)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G1_no_memory/attempts/p3_char_0148_书/01_书.png"
)
print("saved 01_书.png")
