"""
亟 (jí) — 8 strokes. Structure (top to bottom):
  1. Top horizontal (一)
  2-4. Left middle: 口-like (small box, 3 strokes)
  5-7. Right middle: 又-like element (3 strokes with hook-flick)
  8. Bottom horizontal (一, longer)
Rendered with PIL on 300x300 white canvas, black ink.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6  # line width

def line(pts, width=LW):
    d.line(pts, fill=BLACK, width=width, joint="curve")

# --- Stroke 1: top horizontal (short) ---
line([(90, 60), (215, 55)], width=LW)

# --- Middle-left small box shape (口-ish) ---
# Stroke 2: left vertical of box
line([(75, 95), (78, 155)], width=LW)
# Stroke 3: top+right of box (横折)
line([(78, 92), (135, 90), (140, 155)], width=LW)
# Stroke 4: bottom of box
line([(80, 150), (140, 155)], width=LW)

# --- Middle-right element (又-shape, curved) ---
# Stroke 5: horizontal top of right piece
line([(150, 100), (225, 95)], width=LW)
# Stroke 6: sweeping curve from upper-right down-left (like a 撇 with hook)
line([(220, 100), (200, 130), (170, 165), (150, 195)], width=LW)
# Stroke 7: 捺 diagonal going down-right
line([(175, 130), (215, 175), (240, 200)], width=LW)

# --- Stroke 8: bottom horizontal (longer) ---
line([(45, 245), (260, 250)], width=LW+1)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0388_亟/01_亟.png")
