from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 6

# 冉 — five strokes
# Frame roughly cx=150, top ~70, bottom ~240, left ~90, right ~210

# Stroke 1: short left-down diagonal at top (撇 short)
d.line([(148, 60), (128, 90)], fill="black", width=LW)

# Stroke 2: left vertical (long, from top down)
d.line([(100, 78), (100, 245)], fill="black", width=LW)

# Stroke 3: top horizontal + right vertical (横折钩 style — 冂 shape frame)
d.line([(100, 78), (210, 78)], fill="black", width=LW)  # top horizontal
d.line([(210, 78), (210, 245)], fill="black", width=LW)  # right vertical

# Stroke 4: middle horizontal extending well beyond left/right
d.line([(60, 175), (250, 175)], fill="black", width=LW)

# Stroke 5: middle vertical, extends below the frame with slight hook
d.line([(155, 90), (155, 265)], fill="black", width=LW)
# small hook at bottom-left of central vertical
d.line([(155, 265), (140, 258)], fill="black", width=LW)

out = os.path.join(os.path.dirname(__file__), "01_冉.png")
img.save(out)
print("saved", out)
