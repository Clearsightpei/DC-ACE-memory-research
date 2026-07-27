from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

ink = "black"
thick = 7

# 艹 (grass radical): one long horizontal, two short verticals crossing it.
# Horizontal spans most of the width, slightly above center.
# Two verticals: left and right, angling slightly outward at the bottom.

# Horizontal stroke (heng)
d.line([(55, 150), (245, 145)], fill=ink, width=thick)

# Left vertical (short, slight left-slant at bottom)
d.line([(105, 120), (95, 205)], fill=ink, width=thick)

# Right vertical (short, slight right-slant at bottom)
d.line([(190, 120), (200, 205)], fill=ink, width=thick)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0078_艹/01_艹.png")
