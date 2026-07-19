"""G1 render for p2_radical_072_土 (radical 土, 3 strokes) — revision 1.

Strokes:
  1) short upper horizontal (heng)
  2) vertical (shu) intersecting both hengs (extends to touch bottom heng)
  3) long lower horizontal (heng), slightly wavy per GT

Rendered with PIL at 300x300, black on white.
"""

from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
INK = 6

# Upper (short) horizontal — around y=118, x from ~115 to ~195
draw.line([(115, 120), (195, 116)], fill=BLACK, width=INK)

# Vertical stroke — from y=~88 (tiny top tick) down to y=~248 (touching bottom heng)
draw.line([(148, 95), (154, 88)], fill=BLACK, width=INK)   # small top tick / 顿笔 opening
draw.line([(154, 88), (150, 248)], fill=BLACK, width=INK)  # main vertical, extends to touch bottom heng

# Lower (long) horizontal — around y=252, x from ~50 to ~258, gentle wave
pts = [(50, 252), (100, 248), (150, 254), (200, 250), (258, 253)]
draw.line(pts, fill=BLACK, width=INK, joint="curve")

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_土.png")
img.save(out_path)
print(f"Saved {out_path}")
