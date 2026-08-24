"""Render 乛 (héng gōu / horizontal-turn radical) to 300x300 PNG.

Based on GT observation: a single continuous stroke that forms
- a small vertical tick at top-left (small entry hook downward)
- a horizontal top going right
- a sharp turn down (折)
- a long vertical going down
- a curve/hook back to the right at bottom (bottom-right corner)

Actually GT shows it as a large squared C-like shape opening rightward
with a short hook at the top-left corner going down.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
LW = 6

# Coordinates loosely calibrated to GT: character occupies roughly
# x in [70, 230], y in [70, 250].

# 1) Small top-left tick (entry) going down a bit
draw.line([(78, 78), (82, 110)], fill=INK, width=LW)

# 2) Horizontal top: from top-left corner going right
draw.line([(78, 78), (215, 82)], fill=INK, width=LW)

# 3) Turn down (折) — short diagonal inward down-left, mimicking hook return
draw.line([(215, 82), (185, 130)], fill=INK, width=LW)

# 4) Left vertical going down (long)
draw.line([(82, 110), (82, 235)], fill=INK, width=LW)

# 5) Bottom horizontal curving right
draw.line([(82, 235), (218, 232)], fill=INK, width=LW)

# 6) Small bottom-right upward hook
draw.line([(218, 232), (222, 205)], fill=INK, width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0007_乛/01_乛.png")
print("saved")
