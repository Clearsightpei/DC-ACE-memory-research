from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
TH = 6  # stroke thickness

# 兰 = two top dots (丶 丿) + three horizontals (short, shorter, long)

# Top-left mark 丶 (short, going down-right slightly)
d.line([(115, 80), (128, 115)], fill=BLACK, width=TH)

# Top-right mark 丿 (longer, going down-left)
d.line([(195, 78), (170, 118)], fill=BLACK, width=TH)

# Upper horizontal 一 (short)
d.line([(95, 140), (205, 138)], fill=BLACK, width=TH)

# Middle horizontal 一 (shortest)
d.line([(105, 190), (200, 188)], fill=BLACK, width=TH)

# Bottom horizontal 一 (longest)
d.line([(55, 250), (250, 248)], fill=BLACK, width=TH + 1)

out = os.path.join(os.path.dirname(__file__), "01_兰.png")
img.save(out)
print("wrote", out)
