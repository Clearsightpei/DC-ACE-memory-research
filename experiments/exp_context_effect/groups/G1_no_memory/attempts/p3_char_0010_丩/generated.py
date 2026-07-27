"""Render 丩 (jiū) to a 300x300 PNG using PIL.

Revised based on GT comparison:
  - Left stroke (竖折折钩-like): small top going down-left with slight curve,
    then angular corner at bottom, then hooks sharply up-right.
  - Right stroke (竖): top has small horizontal segment going right then curves
    down into a long vertical, ending straight (no bottom hook).
"""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
W = 6

def line(pts, width=W):
    draw.line(pts, fill=INK, width=width, joint="curve")

# --- Stroke 1: left component ---
# Top-left descends steeply/curves to bottom, sharp corner, then hook up-right.
# GT shows: starts ~ (110, 145), curves down-left slightly to (100, 190),
# corner/turn at (115, 220), rises up-right to (155, 200).
s1 = [
    (112, 140),
    (105, 165),
    (100, 190),
    (105, 210),
    (120, 222),
    (140, 218),
    (155, 205),
    (158, 195),
]
line(s1, width=W)

# --- Stroke 2: right vertical with tiny top ---
# GT: small top goes right-ish then vertical straight down, no bottom hook.
# Top hooklet: from (180, 120) small curve to (195, 115), then down straight.
s2 = [
    (178, 122),
    (188, 115),
    (196, 118),
    (198, 135),
    (198, 250),
]
line(s2, width=W)

out_path = os.path.join(os.path.dirname(__file__), "01_丩.png")
img.save(out_path)
print(f"wrote {out_path}")
