"""Render 口 (radical, 3 strokes) at 300x300, black ink on white.

Strokes (canonical order for 口):
  1. 竖 (left vertical): top-left down to bottom-left
  2. 横折 (top+right): top-left across right, then turn down to bottom-right
  3. 横 (bottom): bottom-left across to bottom-right (sealing)
"""
from PIL import Image, ImageDraw

SIZE = 300
OUT = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_057_口/01_口.png"

img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)

# Bounding box for 口 — centered, moderately sized
# Roughly matches GT: box occupies middle region, slightly left-of-center
L = 80   # left x
R = 220  # right x
T = 100  # top y
B = 220  # bottom y

INK = (0, 0, 0)
W = 6  # stroke width

# Stroke 1: left vertical 竖 (slight overshoot at top like GT)
d.line([(L, T - 2), (L - 2, B + 4)], fill=INK, width=W)

# Stroke 2: 横折 — top horizontal from just left of L to R, then turn down to B
# Top horizontal (slight tilt down-right common in handwriting)
d.line([(L - 4, T), (R + 4, T + 4)], fill=INK, width=W)
# Right vertical (down from top-right corner)
d.line([(R + 2, T + 2), (R - 4, B - 2)], fill=INK, width=W)

# Stroke 3: bottom 横 (sealing bottom)
d.line([(L - 6, B + 2), (R + 2, B - 2)], fill=INK, width=W)

img.save(OUT)
print(f"wrote {OUT}")
