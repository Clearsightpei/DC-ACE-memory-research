"""Render radical 曰 (yue) — 4 strokes: 竖, 横折, 横, 横.
Output: 300x300 white PNG, black ink."""
from PIL import Image, ImageDraw

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
draw = ImageDraw.Draw(img)

W = 6  # ink width

# Bounding box — taller than wide, matching GT proportions
L, R = 80, 215
T, B = 75, 250
MID = (T + B) // 2 + 8  # middle horizontal a bit below center

# Stroke 1: left vertical (竖) — angles slightly outward at bottom
draw.line([(L + 3, T + 3), (L - 6, B)], fill="black", width=W)

# Stroke 2: 横折 (top horizontal + right vertical, one stroke)
#   top horizontal slightly rising, then hook down along right side
draw.line([(L - 2, T + 5), (R + 2, T)], fill="black", width=W)
draw.line([(R + 2, T - 2), (R - 4, B - 2)], fill="black", width=W)

# Stroke 3: middle horizontal — SHORT, clearly detached from right side
draw.line([(L + 8, MID), (R - 30, MID + 2)], fill="black", width=W)

# Stroke 4: bottom horizontal (closes the box)
draw.line([(L - 5, B + 2), (R - 2, B - 2)], fill="black", width=W)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_129_曰/01_曰.png")
print("saved 01_曰.png")
