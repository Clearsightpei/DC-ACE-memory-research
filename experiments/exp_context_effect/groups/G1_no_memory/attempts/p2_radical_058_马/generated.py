"""G1 attempt: 马 (radical, 3 strokes) — revised.
Simplified 马: 3 strokes.
  S1: 横折 — top horizontal + right side down to middle
  S2: 竖折折钩 — down (left), across (middle bar), then long diagonal
      down-left, hook up-right at bottom
  S3: 一 — long bottom horizontal, slight tilt
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

def curve(pts, width=LW):
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=INK, width=width)

# ---- Stroke 1: 横折 (top of 马 head) ----
# Top bar (rises slightly to the right, ends with a small down-tick)
curve([(95, 95), (130, 90), (170, 85), (205, 88)])
# Fold: right side descends to the middle-bar level
curve([(205, 88), (208, 115), (203, 140), (195, 152)])

# ---- Stroke 2: 竖折折钩 (body zigzag with hook) ----
# A) left side vertical from top-left of head down
curve([(102, 108), (100, 130), (100, 152)])
# B) middle horizontal bar (across the head)
curve([(100, 152), (140, 150), (180, 150), (200, 152)])
# C) long diagonal sweeping down-left from right end
curve([(200, 152), (185, 180), (160, 205), (130, 225), (108, 240)])
# D) hook at bottom: small flick up-right
curve([(108, 240), (125, 235), (138, 230)])

# ---- Stroke 3: 一 (long bottom horizontal) ----
curve([(65, 260), (120, 255), (180, 252), (235, 250)])

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_058_马/01_马.png")
