"""G1 render of 五 (wu, five). 4 strokes.
Revised pass.
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
TH = 6

def line(p0, p1, w=TH):
    d.line([p0, p1], fill=BLACK, width=w)

# Stroke 1: top horizontal — shorter, centered-upper
line((110, 90), (205, 88), w=TH)

# Stroke 2: left slant — from mid of top bar down-left to lower-left area
line((145, 90), (100, 200), w=TH)

# Stroke 3: middle horizontal with right vertical joined (horizontal-hook fold)
# Middle horizontal — spans wider than top, ends where right vertical drops
line((100, 175), (210, 172), w=TH)
# Right vertical drops down to just above bottom bar
line((208, 172), (215, 240), w=TH)

# Stroke 4: bottom horizontal — longest, slight upward tail on right
line((70, 245), (245, 240), w=TH)

out_path = os.path.join(os.path.dirname(__file__), "01_五.png")
img.save(out_path)
print(f"wrote {out_path}")
