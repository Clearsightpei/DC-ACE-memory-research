"""G1 draw of 同 (tóng). 6 strokes: 丨(left vertical), 𠃌(top-right corner: horizontal then vertical),
inside 一 (short horizontal), inside 口 (small mouth: 丨 一 𠃌)."""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
INK = (20, 20, 20)
LW = 5

# Outer 冂 frame (open at bottom)
# Left vertical stroke (丨) — slightly slanted left at top
d.line([(70, 55), (65, 275)], fill=INK, width=LW)
# Top horizontal + right vertical (𠃌 shape)
d.line([(70, 55), (232, 60)], fill=INK, width=LW)
d.line([(232, 60), (240, 275)], fill=INK, width=LW)

# Inner short horizontal (一) — upper middle
d.line([(95, 135), (215, 132)], fill=INK, width=LW)

# Inner 口 (small mouth) — lower middle
# Left vertical
d.line([(110, 175), (108, 235)], fill=INK, width=LW)
# Top horizontal + right vertical (𠃌)
d.line([(110, 175), (205, 178)], fill=INK, width=LW)
d.line([(205, 178), (203, 235)], fill=INK, width=LW)
# Bottom horizontal of inner 口
d.line([(108, 235), (203, 235)], fill=INK, width=LW)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G1_no_memory/attempts/p3_char_0249_同/01_同.png")
