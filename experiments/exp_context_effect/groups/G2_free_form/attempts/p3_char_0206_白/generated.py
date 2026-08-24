"""
白 (bái) — 5 strokes
Structure: short 撇 on top + 日-like rectangular body with two internal 横.

Strokes:
 1. 撇: short flick from upper-center going down-left
 2. 竖: left vertical of the box
 3. 横折: top horizontal then turn down (right vertical)
 4. 横: middle horizontal inside the box (does not touch right wall fully? actually it does)
 5. 横: bottom horizontal closing the box

Layout on 300x300 canvas:
 - Box (日 body) occupies roughly x=80..220, y=90..260
 - 撇 sits on top, from around (150, 55) down to (110, 100)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 9  # stroke width

# 1. 撇 — short flick, from top-center down-left
d.line([(150, 50), (108, 105)], fill=INK, width=LW)

# Box coordinates
L, R = 100, 220
T, B = 100, 260

# 2. 竖 — left vertical
d.line([(L, T + 2), (L, B)], fill=INK, width=LW)

# 3. 横折 — top horizontal then down (right vertical)
d.line([(L - 2, T), (R, T)], fill=INK, width=LW)  # top
d.line([(R, T), (R, B)], fill=INK, width=LW)      # right down

# 4. 横 — middle horizontal
MID_Y = T + (B - T) // 2 + 5
d.line([(L + 5, MID_Y), (R - 3, MID_Y)], fill=INK, width=LW)

# 5. 横 — bottom horizontal
d.line([(L - 2, B), (R + 2, B)], fill=INK, width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0206_白/01_白.png")
print("saved")
