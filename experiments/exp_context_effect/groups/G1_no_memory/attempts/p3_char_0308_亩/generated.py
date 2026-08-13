"""G1 render for 亩 (p3_char_0308)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 5

# Top dot (点) - short diagonal stroke, slightly right of center
d.line([(155, 55), (172, 78)], fill=INK, width=LW)

# Top horizontal (long, slight arc) - the 亠 crossbar
# draw as slight curve using multiple segments
pts = [(50, 115), (100, 108), (150, 105), (200, 108), (255, 115)]
d.line(pts, fill=INK, width=LW)

# Bottom part 田 - a rectangle with cross inside
# rectangle
left, right = 90, 220
top, bottom = 135, 260
# left vertical (slightly slanted outward at bottom for handwritten feel)
d.line([(left, top), (left - 3, bottom)], fill=INK, width=LW)
# top horizontal of rectangle
d.line([(left, top), (right, top)], fill=INK, width=LW)
# right vertical
d.line([(right, top), (right + 2, bottom)], fill=INK, width=LW)
# bottom horizontal
d.line([(left - 3, bottom), (right + 2, bottom)], fill=INK, width=LW)
# middle horizontal
midY = (top + bottom) // 2
d.line([(left - 1, midY), (right + 1, midY)], fill=INK, width=LW)
# middle vertical
midX = (left + right) // 2
d.line([(midX, top), (midX, bottom)], fill=INK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0308_亩/01_亩.png")
