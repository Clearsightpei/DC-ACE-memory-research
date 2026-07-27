"""Render 无 (wu2) — 4 strokes — to 300x300 PNG."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

W = 6  # stroke width

def line(pts, width=W):
    d.line(pts, fill="black", width=width, joint="curve")

# Stroke 1: short horizontal (upper)
line([(90, 78), (215, 82)])

# Stroke 2: long horizontal (middle) — main heng
line([(45, 145), (260, 140)])

# Stroke 3: 撇 — starts from top area, sweeps down-left with curve
line([(125, 80), (118, 150), (100, 210), (70, 270)])

# Stroke 4: 竖弯钩 — down then sweeps right and hooks upward
line([(178, 145), (182, 215), (195, 255), (230, 270), (255, 258), (252, 235)])

out_path = os.path.join(os.path.dirname(__file__), "01_无.png")
img.save(out_path)
print(f"wrote {out_path}")
