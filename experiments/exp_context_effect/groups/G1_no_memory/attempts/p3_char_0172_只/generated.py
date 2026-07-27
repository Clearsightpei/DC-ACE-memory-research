"""Render 只 (zhǐ) — 5 strokes: 口 (3) + 丿 + 丶(捺).
Output: 300x300 white bg, black ink.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

def line(p1, p2, w=LW):
    d.line([p1, p2], fill=INK, width=w)

def poly(points, w=LW):
    d.line(points, fill=INK, width=w, joint="curve")

# 只 layout in a 300x300 grid:
# Top portion 口 (mouth) — roughly centered, y ~ 70..145
# Bottom portion 八 — spreads out below

# ---- 口 (mouth): 3 strokes ----
# 口 sits upper-center, slightly wider than tall
# Stroke 1: left vertical 竖 (slight lean inward)
poly([(95, 85), (100, 155)])
# Stroke 2: top horizontal + right vertical (横折)
poly([(95, 85), (200, 82), (195, 155)])
# Stroke 3: bottom horizontal 横 (slight tilt)
poly([(100, 155), (195, 152)])

# ---- 八 (bottom two strokes) ----
# Stroke 4: 丿 — starts just under-left of 口 bottom, sweeps to lower-left
poly([(120, 175), (65, 265)])
# Stroke 5: 捺 — starts just under-right of 口 bottom, sweeps to lower-right
poly([(175, 175), (240, 265)])

out_path = os.path.join(os.path.dirname(__file__), "01_只.png")
img.save(out_path)
print(f"Saved {out_path}")
