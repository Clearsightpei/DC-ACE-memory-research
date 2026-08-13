"""Render 问 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

# 门 gate frame (main enclosure) — occupies roughly right 3/4 of char
# Left vertical (丨 falling downward, slight left lean at top)
d.line([(70, 70), (55, 260)], fill=BLACK, width=LW)

# Small dot on top-left of the frame (丶)
d.line([(75, 50), (85, 65)], fill=BLACK, width=LW)

# Top horizontal of right side (short, starts high)
d.line([(115, 75), (235, 75)], fill=BLACK, width=LW)

# Right vertical + bottom-left horizontal-hook (right column of 门: 横折钩)
# Down stroke of right column
d.line([(235, 75), (245, 265)], fill=BLACK, width=LW)
# Hook flick at the bottom-left of right column (small hook curling left)
d.line([(245, 265), (225, 258)], fill=BLACK, width=LW)

# Inside: 口 (mouth) — small square in the center-bottom of the frame
# Top-left corner of 口
x0, y0, x1, y1 = 115, 140, 200, 210
# Left vertical
d.line([(x0, y0), (x0, y1)], fill=BLACK, width=LW)
# Top horizontal
d.line([(x0, y0), (x1, y0)], fill=BLACK, width=LW)
# Right vertical (with slight hook)
d.line([(x1, y0), (x1 + 3, y1)], fill=BLACK, width=LW)
# Bottom horizontal
d.line([(x0, y1), (x1 + 3, y1)], fill=BLACK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0257_问/01_问.png")
print("saved")
