"""Render 予 (yǔ) — 4 strokes.
Structure (per GT):
  1. Upper 横折 — small angular hook top
  2. Middle 横折钩 — larger angular hook with tiny hook, nested below stroke 1
  3. Long horizontal across middle (widest element)
  4. Vertical stroke with small left hook, descending from where 横折s meet
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
TH = 5

def poly(points, w=TH):
    d.line(points, fill=INK, width=w, joint="curve")

def line(p1, p2, w=TH):
    d.line([p1, p2], fill=INK, width=w)

# Stroke 1: upper small 横折 — short horizontal, then diagonal down-left
# top ~ y=80, endpoint of diagonal near y=115
poly([(120, 82), (180, 78), (140, 118)], w=TH)

# Stroke 2: middle 横折钩 — starts a bit lower, wider, ends with small hook
# horizontal (slight up-slant) from (105, 118) to (200, 112),
# then diagonal down-left to (150, 165), tiny hook back up-left
poly([(108, 120), (202, 113), (150, 168), (142, 162)], w=TH)

# Stroke 3: long horizontal across middle
line((60, 168), (240, 165), w=TH)

# Stroke 4: 竖钩 vertical with small left hook at bottom
# starts near where stroke 2 diagonal ended, descends, hooks left
poly([(158, 140), (152, 255), (135, 245)], w=TH)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0099_予/01_予.png")
print("saved")
