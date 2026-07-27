"""Render 亡 (wang) - 3 strokes."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
LW = 7

# Stroke 1: short diagonal (点/丶) top-center, going down-right slightly
d.line([(140, 60), (165, 95)], fill=INK, width=LW)

# Stroke 2: long horizontal (一) across middle
d.line([(55, 140), (245, 140)], fill=INK, width=LW)

# Stroke 3: L-shape (乚 style) - vertical down from left of horizontal, then hook right
# Start just below the left end of horizontal, go down, then turn right
d.line([(85, 140), (85, 235)], fill=INK, width=LW)   # vertical
d.line([(82, 232), (225, 232)], fill=INK, width=LW)  # horizontal bottom

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0052_亡/01_亡.png")
