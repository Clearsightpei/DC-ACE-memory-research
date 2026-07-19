"""G1 no-memory render of radical 丨 (vertical stroke)."""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

# 丨 = a vertical stroke. GT shows a slight top curl and a straight descent,
# roughly centered horizontally, occupying most of the vertical extent.
# Approximate the GT: top of stroke around y=55, bottom around y=255,
# x roughly centered at ~150 with a very slight top curve to the right.

# Main vertical body
draw.line([(150, 70), (150, 255)], fill="black", width=6)

# Small top curl (mimic GT's slight hook at the top)
draw.line([(150, 70), (155, 60)], fill="black", width=6)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p2_radical_001_丨/01_丨.png")
