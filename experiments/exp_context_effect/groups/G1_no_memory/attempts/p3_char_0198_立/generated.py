from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
TH = 6

# 立 - stroke order:
# 1. top dot (short slanting stroke, upper-center)
# 2. short horizontal (below dot)
# 3. left dot (short slanting)
# 4. right dot (short slanting)
# 5. bottom horizontal (long)

# 1. top dot: short slant from upper-left to lower-right
d.line([(140, 70), (165, 90)], fill=BLACK, width=TH)

# 2. short horizontal (upper) — slightly above middle
d.line([(95, 130), (210, 128)], fill=BLACK, width=TH)

# 3. left dot: slant down-left
d.line([(115, 165), (100, 195)], fill=BLACK, width=TH)

# 4. right dot: slant down-right (short)
d.line([(190, 165), (200, 195)], fill=BLACK, width=TH)

# 5. bottom horizontal (long) — the base
d.line([(55, 235), (255, 232)], fill=BLACK, width=TH)

out = os.path.join(os.path.dirname(__file__), "01_立.png")
img.save(out)
print("wrote", out)
