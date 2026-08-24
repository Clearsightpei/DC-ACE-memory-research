"""G1 render for p2_radical_027_凵 (U-shape radical, 2 strokes).

Stroke 1: 竖折 (vertical-then-horizontal) — down the left side, turn
right along the bottom.
Stroke 2: 竖 (vertical) — right side, descending.

MMH shows stroke 1 as a single connected stroke (vertical + hook to
horizontal), stroke 2 as the right vertical.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
THICK = 8

# Layout: character occupies lower middle. Bounding box roughly:
# left x=80, right x=225, top y=130, bottom y=245
LEFT_X = 80
RIGHT_X = 225
TOP_Y = 130
BOT_Y = 245

# Stroke 1: 竖折 — left vertical going down, then horizontal across bottom
# Start at top-left, go down, curve right along bottom
p1 = [(LEFT_X + 4, TOP_Y),
      (LEFT_X, TOP_Y + 40),
      (LEFT_X + 2, BOT_Y - 10),
      (LEFT_X + 20, BOT_Y),
      (RIGHT_X - 25, BOT_Y),
      (RIGHT_X - 5, BOT_Y - 2)]
draw.line(p1, fill=INK, width=THICK, joint="curve")

# Stroke 2: 竖 — right vertical descending
p2 = [(RIGHT_X, TOP_Y + 5),
      (RIGHT_X + 2, TOP_Y + 60),
      (RIGHT_X, BOT_Y - 5)]
draw.line(p2, fill=INK, width=THICK, joint="curve")

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_027_凵/01_凵.png")
