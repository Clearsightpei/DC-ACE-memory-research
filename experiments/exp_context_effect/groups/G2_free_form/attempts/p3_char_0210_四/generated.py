"""
四 — 5 strokes. Wide rectangular frame with two internal marks.
Stroke order (MMH):
  1. 竖 left side
  2. 横折 top + right side (single stroke)
  3. 撇 inside left (short slanted flick down-left)
  4. 竖弯 inside right (down then bends right at bottom)
  5. 横 bottom seal

Layout: character sits roughly in the central 米字格.
Width slightly greater than height (per GT silhouette).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
BW = 6  # brush width

# Frame corners (wider than tall, sitting in the mid-lower area like GT)
L, R = 70, 235
T, B = 90, 235

# Stroke 1: 竖 left side (top-left going down)
d.line([(L, T), (L - 4, B)], fill=INK, width=BW)

# Stroke 2: 横折 top + right side, single stroke
#   horizontal from top-left across to top-right, then folds down
d.line([(L, T), (R, T - 4)], fill=INK, width=BW)  # top horizontal
d.line([(R, T - 4), (R + 4, B - 4)], fill=INK, width=BW)  # right side going down

# Stroke 3: 撇 inside left — from just below top edge down-left toward bottom seal
ix1, iy1 = 118, T + 6
ix2, iy2 = 100, B - 6
d.line([(ix1, iy1), (ix2, iy2)], fill=INK, width=BW)

# Stroke 4: 竖弯 inside right — vertical from top, bends right, meets bottom seal
rx1, ry1 = 180, T + 6
rx2, ry2 = 180, B - 20
rx3, ry3 = 210, B - 6
d.line([(rx1, ry1), (rx2, ry2)], fill=INK, width=BW)
d.line([(rx2, ry2), (rx3, ry3)], fill=INK, width=BW)

# Stroke 5: 横 bottom seal
d.line([(L - 4, B), (R + 4, B - 4)], fill=INK, width=BW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0210_四/01_四.png")
