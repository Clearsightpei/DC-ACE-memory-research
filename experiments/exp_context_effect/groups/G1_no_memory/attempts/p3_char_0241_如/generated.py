"""Render 如 (rú) at 300x300, black ink on white.
Left: 女 radical (3 strokes). Right: 口 (3 strokes).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 5

# ---- Left: 女 (woman) ----
# Stroke 1: 撇点 — down-left slant then up-right hook (forms a v)
draw.line([(105, 70), (45, 175)], fill=INK, width=LW)
draw.line([(45, 175), (110, 200)], fill=INK, width=LW)

# Stroke 2: 撇 — long sweeping diagonal from upper-right to lower-left
draw.line([(130, 105), (25, 265)], fill=INK, width=LW)

# Stroke 3: 横 — long horizontal crossing near middle
draw.line([(30, 190), (145, 180)], fill=INK, width=LW)

# ---- Right: 口 (mouth) ----
# Stroke 1: 竖 — left vertical
draw.line([(180, 130), (180, 245)], fill=INK, width=LW)
# Stroke 2: 横折 — top horizontal, then down (right vertical)
draw.line([(180, 130), (270, 130)], fill=INK, width=LW)
draw.line([(270, 130), (270, 245)], fill=INK, width=LW)
# Stroke 3: 横 — bottom horizontal closing
draw.line([(180, 245), (270, 245)], fill=INK, width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0241_如/01_如.png")
print("saved")
