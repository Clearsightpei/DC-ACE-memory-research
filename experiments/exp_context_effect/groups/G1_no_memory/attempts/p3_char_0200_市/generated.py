"""G1 draw of 市 (city). 5 strokes: dot(top), horizontal, left-down, box-like 冂, vertical through."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

# Stroke 1: top dot/short slanted stroke (点) — slant from upper-right down-left
d.line([(170, 50), (140, 75)], fill=BLACK, width=LW)

# Stroke 2: long horizontal (一) crossing middle-upper area
d.line([(55, 105), (245, 100)], fill=BLACK, width=LW)

# Stroke 3: short left-descending stroke starting on the horizontal (撇)
d.line([(80, 100), (60, 150)], fill=BLACK, width=LW)

# Stroke 4: box-like 冂 shape (small rectangle open at bottom)
# top of box
d.line([(85, 145), (215, 145)], fill=BLACK, width=LW)
# left side of box
d.line([(85, 145), (85, 220)], fill=BLACK, width=LW)
# right side of box (hook end)
d.line([(215, 145), (215, 220)], fill=BLACK, width=LW)
# small hook at bottom-right
d.line([(215, 220), (200, 210)], fill=BLACK, width=LW)

# Stroke 5: long vertical through the character (丨) extending below box
d.line([(150, 105), (150, 275)], fill=BLACK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0200_市/01_市.png")
print("Saved 市")
