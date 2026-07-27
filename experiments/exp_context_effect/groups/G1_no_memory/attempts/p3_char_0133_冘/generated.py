"""Render 冘 (p3_char_0133) to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 6

# Stroke 1: short 撇 on top (small diagonal from upper right to lower left)
d.line([(158, 45), (140, 78)], fill=BLACK, width=LW)

# Stroke 2: 冖-like cap (left tick down, long horizontal, right end hook down)
# left small tick
d.line([(78, 92), (92, 108)], fill=BLACK, width=LW)
# horizontal top
d.line([(88, 105), (222, 105)], fill=BLACK, width=LW)
# right end curves down (the 冖 hook)
d.line([(222, 105), (228, 128)], fill=BLACK, width=LW)

# Stroke 3: long 撇 - starts from under the cap center-left, sweeps down-left
points = [(128, 115), (115, 155), (95, 205), (70, 265)]
d.line(points, fill=BLACK, width=LW, joint="curve")

# Stroke 4: 横折弯钩 - horizontal, turn down, curve, hook up
# The right leg: from under cap it goes right a bit, then down curving right, ends with hook up
# Since stroke 2 already drew the top-right hook down to (228,128), stroke 4 continues:
# Actually stroke 4 is a separate stroke starting from the cap area
# top small horizontal
d.line([(165, 128), (225, 128)], fill=BLACK, width=LW)
# turn down and curve (弯)
curve = [(225, 128), (228, 175), (235, 225), (245, 258)]
d.line(curve, fill=BLACK, width=LW, joint="curve")
# hook up-left at end
d.line([(245, 258), (225, 250)], fill=BLACK, width=LW)

out_path = os.path.join(os.path.dirname(__file__), "01_冘.png")
img.save(out_path)
print(f"Saved {out_path}")
