"""G1 render of 三 (three) — three horizontal strokes."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = "black"
THICK = 8

# Top stroke: short-medium, upper area
draw.line([(95, 85), (200, 78)], fill=INK, width=THICK)

# Middle stroke: shortest, centered
draw.line([(110, 155), (195, 150)], fill=INK, width=THICK)

# Bottom stroke: longest, lower area
draw.line([(55, 235), (245, 230)], fill=INK, width=THICK)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0055_三/01_三.png")
