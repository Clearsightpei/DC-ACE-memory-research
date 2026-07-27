"""Render 卅 (sà, thirty) as 300x300 PNG.

Structure: three vertical strokes crossed by one horizontal stroke.
- Leftmost vertical: slight curve to the left at bottom (piě-like)
- Middle vertical: straight
- Right vertical: straight, taller
- Horizontal: crosses all three near the upper-middle
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6

# Reference points from GT observation:
# Horizontal crossbar around y ≈ 130, spanning x ≈ 55 → 250
# Three verticals at approx x = 90 (curved left), 155 (straight), 215 (straight)
# Vertical tops around y ≈ 75, bottoms around y ≈ 240 (right one longest)

# Stroke 1: left vertical, slight curve down-left at the bottom (piě)
# Approximate with polyline
left_v = [(105, 80), (100, 130), (92, 180), (78, 230), (62, 260)]
draw.line(left_v, fill=INK, width=LW, joint="curve")

# Stroke 2: middle vertical (straight)
draw.line([(155, 90), (152, 250)], fill=INK, width=LW)

# Stroke 3: right vertical (straight, tallest)
draw.line([(215, 70), (218, 255)], fill=INK, width=LW)

# Stroke 4: long horizontal crossbar
draw.line([(55, 135), (255, 138)], fill=INK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0147_卅/01_卅.png")
print("saved")
