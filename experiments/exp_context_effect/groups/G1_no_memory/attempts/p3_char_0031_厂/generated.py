"""Render 厂 (p3_char_0031_厂) at 300x300, white bg, black ink.

Redrawn against the CLEAN GT (2026-07-19). Prior attempt was against
a corrupted GT.

厂 has 2 strokes:
  1) heng (horizontal) across the top — starts around left-center,
     runs rightward to right edge, slight upward tilt.
  2) pie (left-falling curve) — begins at/just below the left end of
     the heng with a tiny leftward tick, then sweeps down and curves
     to the lower-left corner.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 7

# ---- Stroke 1: heng ----
# GT: starts near (100, 100), ends near (258, 82) — subtle rise.
heng_pts = [
    (100, 100),
    (140, 92),
    (185, 86),
    (225, 82),
    (258, 82),
]
for i in range(len(heng_pts) - 1):
    draw.line([heng_pts[i], heng_pts[i + 1]], fill=INK, width=LW)

# ---- Stroke 2: pie with tiny hook entry, then long left-curving fall ----
# Small tick going slightly up-left at the top (visible in GT).
hook_pts = [(108, 105), (96, 95)]
draw.line([hook_pts[0], hook_pts[1]], fill=INK, width=6)

# Main pie: starts just below hook, curves down and to the lower-left.
pie_pts = [
    (106, 105),
    (102, 130),
    (95, 160),
    (86, 195),
    (72, 225),
    (58, 250),
    (46, 270),
    (40, 280),
]
for i in range(len(pie_pts) - 1):
    w = max(4, LW - (i // 3))
    draw.line([pie_pts[i], pie_pts[i + 1]], fill=INK, width=w)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_厂.png")
img.save(out_path)
print(f"Wrote {out_path}")
