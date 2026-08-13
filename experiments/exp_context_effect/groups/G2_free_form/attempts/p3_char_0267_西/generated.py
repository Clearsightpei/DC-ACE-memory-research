"""
西 — 6 strokes. Similar to 四 but with a short top horizontal tick above the frame.

Stroke order (MMH):
  1. 一 short top horizontal (small tick above the frame)
  2. 丨 left vertical of frame
  3. 横折 top + right side of frame (single stroke)
  4. 丿 inside-left short descender (slants down-left)
  5. 竖弯 inside-right vertical then bends right into bottom seal
  6. 一 bottom seal (closes the frame)

Layout: character body sits centrally, slightly wider than tall.
The top tick sits above and centered over the frame.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = "black"
BW = 6  # brush width

# --- Top tick (stroke 1) ---
# short horizontal, centered above the frame
d.line([(120, 55), (188, 52)], fill=INK, width=BW)

# --- Frame ---
# Frame corners (wider than tall)
L, R = 60, 240
T, B = 95, 240

# Stroke 2: 竖 left side (slightly slanted outward as often seen)
d.line([(L + 4, T), (L - 4, B)], fill=INK, width=BW)

# Stroke 3: 横折 top horizontal + right vertical (single stroke)
d.line([(L + 4, T - 2), (R, T - 2)], fill=INK, width=BW)   # top horizontal
d.line([(R, T - 2), (R + 6, B - 4)], fill=INK, width=BW)   # right vertical, slight flare

# Stroke 4: 丿 inside-left short descender (slants down-left)
d.line([(120, T + 12), (100, B - 10)], fill=INK, width=BW)

# Stroke 5: 竖弯 inside-right — vertical from top, curves right to meet bottom seal
rx1, ry1 = 180, T + 12
rx2, ry2 = 180, B - 22
rx3, ry3 = 210, B - 8
d.line([(rx1, ry1), (rx2, ry2)], fill=INK, width=BW)
d.line([(rx2, ry2), (rx3, ry3)], fill=INK, width=BW)

# Stroke 6: 一 bottom seal (closes the frame)
d.line([(L - 6, B - 2), (R + 8, B - 6)], fill=INK, width=BW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0267_西/01_西.png")
