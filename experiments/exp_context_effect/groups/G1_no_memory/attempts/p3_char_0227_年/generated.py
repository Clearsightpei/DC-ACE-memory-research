"""G1 render of 年 (year) at 300x300."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 6

# 年: strokes (6)
# 1. short left-falling 撇 top-left (short diagonal, meeting horizontal)
d.line([(140, 55), (110, 90)], fill="black", width=LW)
# 2. short horizontal near top
d.line([(110, 90), (190, 85)], fill="black", width=LW)
# 3. longer left-falling 撇 going down (stops near main crossbar)
d.line([(160, 60), (95, 200)], fill="black", width=LW)
# 4. horizontal middle (short)
d.line([(115, 145), (205, 142)], fill="black", width=LW)
# 5. long horizontal (main crossbar)
d.line([(55, 205), (255, 200)], fill="black", width=LW)
# 6. vertical stem down through center
d.line([(170, 90), (170, 285)], fill="black", width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0227_年/01_年.png")
