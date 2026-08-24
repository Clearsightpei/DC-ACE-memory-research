"""
自 (self) — 6 strokes:
1. 撇 (short slanted top flick)
2. 竖 (left vertical of box)
3. 横折 (top horizontal + right vertical, one stroke)
4. 横 (upper middle horizontal, doesn't touch right side in GT)
5. 横 (lower middle horizontal, doesn't touch right side)
6. 横 (bottom horizontal, closes box)

Layout: tall box occupying roughly middle of 300x300 canvas.
No sibling-risk row applies (自 isn't in the checklist).
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 7

# Box coordinates
left, right = 95, 205
top, bottom = 75, 265
mid1 = 130   # upper interior horizontal Y
mid2 = 180   # middle interior horizontal Y
mid3 = 225   # lower interior horizontal Y (still inside)
# Actually 自 has 3 interior horizontals (upper, middle) + bottom.
# Restructure: top=box top (from 横折), then two inner horizontals, then bottom horizontal.

# Re-layout for clarity
left, right = 95, 200
top, bottom = 80, 265
inner1_y = 135
inner2_y = 180
inner3_y = 225   # this is bottom actually
# Standard 自: top box line, two inner lines, bottom line = 4 horizontals total

# Use these:
h_top = 80
h_bot = 265
h_in1 = 145
h_in2 = 205

# 1) 撇 — short top flick, from upper right of box area, going up-left
pie_start = (155, 80)
pie_end   = (120, 55)
d.line([pie_start, pie_end], fill=INK, width=LW)

# 2) 竖 — left vertical of box
d.line([(left, h_top), (left-3, h_bot)], fill=INK, width=LW)

# 3) 横折 — top horizontal then right vertical (one stroke)
# Top horizontal: from left of box (slightly right of 竖 top) to right
d.line([(left, h_top), (right, h_top)], fill=INK, width=LW)
# Right vertical
d.line([(right, h_top), (right+2, h_bot)], fill=INK, width=LW)

# 4) 横 — inner upper horizontal (doesn't touch right side)
d.line([(left+5, h_in1), (right-5, h_in1)], fill=INK, width=LW-1)

# 5) 横 — inner middle horizontal
d.line([(left+5, h_in2), (right-5, h_in2)], fill=INK, width=LW-1)

# 6) 横 — bottom horizontal
d.line([(left-3, h_bot), (right+2, h_bot)], fill=INK, width=LW)

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0229_自/01_自.png")
print("saved")
