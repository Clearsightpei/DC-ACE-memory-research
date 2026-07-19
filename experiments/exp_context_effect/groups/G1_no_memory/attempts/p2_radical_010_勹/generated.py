"""Render radical 勹 (bao) to a 300x300 PNG using PIL.

Two strokes:
  1) 撇 (pie): short diagonal from upper area, sits above/left of the
     horizontal start of stroke 2 (does NOT cross through it).
  2) 横折钩 (heng-zhe-gou): horizontal top, curves down the right with
     a rounded belly, sweeps left along the bottom, ending with a
     small upward-left hook.
"""
from PIL import Image, ImageDraw
from pathlib import Path

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
WIDTH = 5

# ---- Stroke 1: 撇 (short diagonal, upper-left, ABOVE the horizontal) ----
# Ends just above where stroke 2 begins.
s1 = [
    (140, 70),
    (130, 82),
    (118, 96),
    (108, 112),
]
for i in range(len(s1) - 1):
    draw.line([s1[i], s1[i + 1]], fill=INK, width=WIDTH)

# ---- Stroke 2: 横折钩 (rounded belly) ----
# Horizontal starts just to the right of and below stroke 1's tail,
# extends right, turns down with rounded curve, sweeps left, ends
# with a small hook up-left.
s2 = [
    (118, 118),   # start of horizontal (below stroke 1 tail)
    (150, 116),
    (185, 116),
    (210, 120),   # top-right, slight round-off
    (220, 138),   # begin descent (rounded)
    (222, 165),
    (220, 195),
    (212, 222),
    (198, 244),   # bottom-right curve into sweep
    (172, 254),
    (145, 254),
    (125, 248),   # bottom-left end before hook
    (115, 236),   # hook tip upward-left
]
for i in range(len(s2) - 1):
    draw.line([s2[i], s2[i + 1]], fill=INK, width=WIDTH)

out = Path(__file__).parent / "01_勹.png"
img.save(out)
print(f"wrote {out}")
