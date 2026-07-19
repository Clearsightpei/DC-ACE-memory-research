"""G1 attempt: 斤 (radical 101, 4 strokes) — PIL renderer, 300x300. Revision 1."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def stroke(points, width=6):
    d.line(points, fill="black", width=width, joint="curve")
    r = width / 2
    for (x, y) in [points[0], points[-1]]:
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# Stroke 1: 短撇 — short flick coming down-left, ending at top of vertical curve
s1 = [(128, 65), (120, 80), (110, 100)]
stroke(s1, width=6)

# Stroke 2: 横 — horizontal from meeting point of stroke 1, sweeping right with tiny down-hook at end
s2 = []
# quadratic Bezier P0=(120,82) P1=(170,72) P2=(215,92)
for t in [i / 30 for i in range(31)]:
    x = (1 - t) ** 2 * 120 + 2 * (1 - t) * t * 170 + t ** 2 * 215
    y = (1 - t) ** 2 * 82 + 2 * (1 - t) * t * 72 + t ** 2 * 92
    s2.append((x, y))
stroke(s2, width=6)

# Stroke 3: 竖撇 — mostly vertical in upper section, curves left near bottom.
s3 = []
# Use two-segment: straight-ish top, then curve
# Bezier P0=(115, 95) P1=(105, 200) P2=(65, 250)
for t in [i / 40 for i in range(41)]:
    x = (1 - t) ** 2 * 115 + 2 * (1 - t) * t * 108 + t ** 2 * 65
    y = (1 - t) ** 2 * 95 + 2 * (1 - t) * t * 190 + t ** 2 * 250
    s3.append((x, y))
stroke(s3, width=7)

# Stroke 4: 竖 — right vertical starting just below the right end of the horizontal, going straight down
s4 = [(198, 100), (198, 260)]
stroke(s4, width=6)

out_dir = os.path.dirname(os.path.abspath(__file__))
img.save(os.path.join(out_dir, "01_斤.png"))
print("saved:", os.path.join(out_dir, "01_斤.png"))
