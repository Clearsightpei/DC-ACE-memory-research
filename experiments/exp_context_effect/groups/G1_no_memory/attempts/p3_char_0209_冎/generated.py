"""G1 render of 冎 (p3_char_0209)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)
LW = 5

# Top small box (like 口 with an inner cross-bar)
# top horizontal
d.line([(110, 70), (215, 70)], fill=BLACK, width=LW)
# left vertical (slightly slanted)
d.line([(110, 70), (108, 140)], fill=BLACK, width=LW)
# right vertical
d.line([(215, 70), (218, 140)], fill=BLACK, width=LW)
# bottom of top box (this is also part of the middle long horizontal that extends outward)
# inner horizontal bar
d.line([(120, 108), (205, 108)], fill=BLACK, width=LW)

# Long middle horizontal extending well past both sides
d.line([(70, 155), (260, 155)], fill=BLACK, width=LW)

# Left downward 丿 stroke, curving left
d.line([(108, 148), (78, 240)], fill=BLACK, width=LW)

# Right hook stroke — diagonal down-right then a small hook
d.line([(228, 155), (262, 215)], fill=BLACK, width=LW)
d.line([(262, 215), (248, 222)], fill=BLACK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0209_冎/01_冎.png")
