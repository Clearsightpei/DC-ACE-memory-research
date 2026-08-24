"""礻 (spirit radical) — 4 strokes:
  1. 丶 top dot (small teardrop, upper area, slightly right of center)
  2. 横撇 — short 横 turning into medium 撇 sweeping lower-left
  3. 竖 — central vertical descending from the 折 point
  4. 点 — small dot to the right of the 竖 (ONE dot, not two like 衤)

Rendered via PIL brush-dab technique (see drawer_memory.md).
Canvas 300x300, white bg, black ink.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)


def dab(x, y, r):
    draw.ellipse([x - r, y - r, x + r, y + r], fill=INK)


def stroke(points, widths):
    """Interpolate a stroke through control points with per-point radius."""
    n = len(points)
    for i in range(n - 1):
        (x0, y0), (x1, y1) = points[i], points[i + 1]
        w0, w1 = widths[i], widths[i + 1]
        steps = max(int(((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5), 2)
        for s in range(steps + 1):
            t = s / steps
            x = x0 + (x1 - x0) * t
            y = y0 + (y1 - y0) * t
            r = w0 + (w1 - w0) * t
            dab(x, y, r)


# ---- Stroke 1: top dot 丶 ----
# small teardrop leaning down-right, upper area (well above 横撇)
stroke([(150, 40), (162, 62)], [2.0, 4.5])

# ---- Stroke 2: 横撇 (short 横 → shoulder → long 撇 down-left) ----
# Short 横 segment
stroke([(95, 118), (180, 112)], [3.0, 4.0])
# Shoulder + long 撇 sweeping down-left
stroke([(180, 112), (176, 128), (140, 180), (80, 235)], [4.0, 4.0, 3.5, 2.0])

# ---- Stroke 3: 竖 (central vertical) ----
# From under the 折 point straight down
stroke([(158, 135), (158, 275)], [3.5, 3.0])

# ---- Stroke 4: 点 (right dot) ----
# Below-right of the shoulder, angled down-right teardrop
stroke([(190, 175), (220, 210)], [2.0, 5.0])

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0139_礻/01_礻.png"
)
print("wrote 01_礻.png")
