"""Render 区 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

SIZE = 300
img = Image.new("RGB", (SIZE, SIZE), "white")
d = ImageDraw.Draw(img)
W = 6  # ink width

# 区 = 匚 (open right) enclosing 乂 (X)
# The GT shows: top horizontal starts a bit right of the left vertical (gap at top-left),
# and there's a tiny downward tick where they almost meet.

# Stroke 1: top horizontal with slight downward tick at the left end
d.line([(85, 60), (245, 55)], fill="black", width=W)
d.line([(85, 60), (88, 90)], fill="black", width=W)  # small tick down

# Stroke 4: 竖折 — vertical left side down, then horizontal bottom
d.line([(60, 75), (65, 255)], fill="black", width=W)
d.line([(63, 253), (258, 250)], fill="black", width=W)

# Inside: 乂
# Stroke 2: 撇 (upper-right diagonal down to lower-left)
d.line([(215, 110), (105, 235)], fill="black", width=W)
# Stroke 3: 捺 (upper-left diagonal down to lower-right)
d.line([(110, 120), (225, 230)], fill="black", width=W)

out = os.path.join(os.path.dirname(__file__), "01_区.png")
img.save(out)
print("saved", out)
