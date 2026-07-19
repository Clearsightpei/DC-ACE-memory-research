"""Render 幺 (radical, 3 strokes) at 300x300, black ink on white."""
from PIL import Image, ImageDraw
import os
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"

def stroke(points, width=7):
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=INK, width=width)
    for p in points:
        r = width // 2
        draw.ellipse([p[0]-r, p[1]-r, p[0]+r, p[1]+r], fill=INK)

# 幺 has 3 strokes:
#   1. Upper 撇折 (piezhe): diagonal down-left then short turn right/down — a small "z" shape near top
#   2. Lower 撇折: larger, similar shape, positioned below the first
#   3. 点 (dian): a diagonal dot at bottom-right
# In GT the two 撇折 form a stacked loop shape; the whole thing sits center-left,
# with the final 点 to the lower-right.

# --- Stroke 1: upper 撇折 (smaller, near top) ---
s1 = [
    (170, 80),    # start (upper-right)
    (155, 95),
    (140, 115),   # end of pie (down-left)
    (150, 128),   # turn (zhe)
    (170, 135),   # end (short right/down)
]
stroke(s1, width=6)

# --- Stroke 2: lower 撇折 (larger, dominant) ---
# Starts just below where s1 ended, sweeps down-left further, then curves right
s2_pie_start = (165, 140)
s2 = [
    s2_pie_start,
    (145, 165),
    (125, 195),
    (110, 220),   # bottom-left tip of pie
    (130, 235),   # turn
    (160, 240),   # move right along bottom
    (180, 232),   # ends slightly upward
]
stroke(s2, width=7)

# --- Stroke 3: 点 (dot) at bottom right, diagonal ---
# A tapered diagonal from upper-left to lower-right
def dian(x0, y0, x1, y1, wmax=10):
    steps = 20
    for i in range(steps):
        t = i / (steps - 1)
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = int(3 + (wmax - 3) * t)  # tapered, thicker at end
        draw.ellipse([x-w/2, y-w/2, x+w/2, y+w/2], fill=INK)

dian(195, 225, 220, 250, wmax=11)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_幺.png"))
print("Saved 01_幺.png")
