"""Render 平 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 6

# 平 has 5 strokes:
# 1) top-left short falling stroke (丿-like, short slanted)
# 2) top-right short slanted stroke (dot/na-like)
# 3) horizontal stroke across middle
# 4) short left dot below top area (left of vertical)  -- actually 平 is: 一 (top), 丶 left dot, 丶 right dot, 一 middle, 丨 vertical
# Standard stroke order for 平: 一 (top horizontal), 丶 (left dot), 丿 (right small), 一 (long horizontal), 丨 (vertical)

# 1) Top horizontal (short-ish), a bit slanted upward on the right
d.line([(95, 85), (215, 78)], fill=INK, width=LW)

# 2) Left small dot/slant (下点 pointing down-left)
d.line([(115, 115), (95, 140)], fill=INK, width=LW)

# 3) Right small slant (pointing down-right)
d.line([(190, 115), (215, 140)], fill=INK, width=LW)

# 4) Long horizontal across middle
d.line([(55, 175), (255, 170)], fill=INK, width=LW)

# 5) Vertical down the middle, from top area through the long horizontal to bottom
d.line([(155, 90), (155, 275)], fill=INK, width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0176_平/01_平.png")
print("saved")
