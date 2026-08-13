from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
LW = 5

# 更 — structure: 一 (top hat), 日 (middle box), 一 (long horizontal), 丿+捺 (X-legs)
# Center around x=150, char occupies roughly y=40..270

# 1. top horizontal (a bit wider slight tilt like the GT)
d.line([(70, 55), (230, 50)], fill="black", width=LW)

# 2-5. 日-like middle box
# left vertical
d.line([(95, 55), (95, 165)], fill="black", width=LW)
# right vertical (with hook down-right)
d.line([(205, 55), (210, 170)], fill="black", width=LW)
# middle horizontal
d.line([(95, 115), (210, 118)], fill="black", width=LW)
# bottom of box
d.line([(95, 165), (210, 170)], fill="black", width=LW)

# 6. long horizontal underneath (一)
d.line([(40, 200), (265, 200)], fill="black", width=LW)

# 7. 丿 — starts near top of box, sweeps down-left through bottom horizontal
d.line([(150, 60), (55, 275)], fill="black", width=LW)

# 8. 捺 — starts near middle of box, sweeps down-right
d.line([(155, 130), (255, 280)], fill="black", width=LW)

out = os.path.join(os.path.dirname(__file__), "01_更.png")
img.save(out)
print("saved", out)
