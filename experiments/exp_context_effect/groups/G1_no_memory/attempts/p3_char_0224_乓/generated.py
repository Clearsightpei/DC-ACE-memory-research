from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 5

# 乓 — top like 斤 upper, plus long horizontal, plus right-down slash

# Stroke 1: short top slash (upper 丿)
d.line([(115, 65), (95, 90)], fill=BLACK, width=LW)

# Stroke 2: top horizontal with slight hook down at right end
d.line([(80, 100), (215, 90)], fill=BLACK, width=LW)
d.line([(215, 90), (215, 105)], fill=BLACK, width=LW)

# Stroke 3: descending left diagonal (丿) from top-mid down to lower-left
d.line([(130, 100), (85, 195)], fill=BLACK, width=LW)

# Stroke 4: inner short horizontal (mid)
d.line([(115, 150), (185, 145)], fill=BLACK, width=LW)

# Stroke 5: long bottom horizontal (extends widely, slight slant)
d.line([(40, 225), (260, 210)], fill=BLACK, width=LW)

# Stroke 6: final downward-right slash (丶/乀) at bottom-right of horizontal
d.line([(190, 230), (225, 285)], fill=BLACK, width=LW)

out = os.path.join(os.path.dirname(__file__), "01_乓.png")
img.save(out)
print(f"saved: {out}")
