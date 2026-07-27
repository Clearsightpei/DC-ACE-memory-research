"""Render 凸 to a 300x300 PNG (white bg, black ink) using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 6

# 凸 is a stepped shape: a narrow tall top, wider base.
# Stroke order (5 strokes):
# 1. Left vertical of top |  (short, upper center)
# 2. Top horizontal of top _
# 3. Right vertical drop then bottom-right of top step (long line going down then right)
# 4. Bottom-left vertical + bottom horizontal (going up-left)
# 5. Final closing horizontal on the bottom (the long base horizontal)

# Actually simpler: draw as connected polyline segments matching GT shape.

# Coordinates (approximate GT):
# Top-left corner of upper block ~ (115, 70)
# Top-right corner of upper block ~ (175, 70)
# Right side goes down to (175, 130), then jumps out to right (240, 130)
# Right side then down to (240, 235)
# Bottom edge from (240, 235) back to (60, 235)
# Left side up from (60, 235) to (60, 130)
# Left top goes right from (60, 130) to (115, 130)
# Left of upper block up from (115, 130) to (115, 70)

# Stroke 1: left vertical of top block (top part - short vertical + short horiz)
# Stroke order for 凸: 竖, 横, 竖, 横折, 横
# Simpler: draw as one continuous outline done in 5 pen-strokes.

# Stroke 1: left vertical (upper) - short vertical going down
d.line([(115, 75), (115, 132)], fill="black", width=LW)
# Stroke 2: top horizontal of upper block
d.line([(115, 75), (178, 75)], fill="black", width=LW)
# Stroke 3: right vertical of upper block down to step
d.line([(178, 75), (178, 132)], fill="black", width=LW)
# Stroke 4: left bottom - vertical from top-left step down, then bottom-left horizontal shape
# Actually, the character 凸: strokes are:
# 1) 丨 left short vertical of top
# 2) 一 top horizontal
# 3) 丨 right short vertical of top ending at step, then continues as horizontal outward - this is 横折
# Let me redraw more faithfully.

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# Redo with 5-stroke structure of 凸:
# S1: left short vertical (of top nub): from (115,75) down to (115,130)
d.line([(115, 78), (115, 130)], fill="black", width=LW)
# S2: top horizontal of nub: from (115,78) to (178,78)
d.line([(113, 78), (180, 78)], fill="black", width=LW)
# S3: 横折折 or similar - right side: from (180,78) down to (180,130), then right to (240,130)
d.line([(180, 78), (180, 132)], fill="black", width=LW)
d.line([(178, 132), (240, 132)], fill="black", width=LW)
# S4: right side of base going down: (240,132) down to (240,240)
d.line([(240, 130), (240, 240)], fill="black", width=LW)
# S5: left side: from top of left base (115,130) go left to (60,130), then down to (60,240)
d.line([(115, 130), (60, 130)], fill="black", width=LW)
d.line([(60, 128), (60, 240)], fill="black", width=LW)
# S6 (final): bottom horizontal (long base): (60,240) to (240,240)
d.line([(58, 240), (242, 240)], fill="black", width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0215_凸/01_凸.png")
print("saved")
