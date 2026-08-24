"""G1 render of radical 刂 (knife radical, 2 strokes).

Stroke 1: short vertical (竖) on the left side, upper region.
Stroke 2: longer vertical with hook at bottom (竖钩) on the right side.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
WIDTH = 6

# Stroke 1: short left vertical (竖) — sits in mid-upper area
draw.line([(125, 105), (130, 185)], fill=BLACK, width=WIDTH)

# Stroke 2: right vertical with hook at bottom (竖钩)
# Long vertical from near top to bottom
draw.line([(185, 70), (185, 240)], fill=BLACK, width=WIDTH)
# Bottom hook: curl up-left, more visible
draw.line([(185, 240), (160, 225)], fill=BLACK, width=WIDTH + 1)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_016_刂/01_刂.png")
