"""Render 美 to a 300x300 PNG using PIL."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"

def line(p1, p2, w=4):
    d.line([p1, p2], fill=INK, width=w)

def curve(points, w=4):
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=INK, width=w)

# 美 = 丷 (two dots) + three horizontals with vertical + 大 bottom

# Two top dots (丷) - slanting inward
curve([(115, 45), (108, 72)], w=5)     # left dot slants down-left
curve([(200, 42), (210, 68)], w=5)     # right dot slants down-right

# Top horizontal (short) with small hook at right - 羊 top
line((115, 85), (200, 82), w=5)

# Second horizontal (medium)
line((100, 125), (215, 122), w=5)

# Third horizontal (short, middle)
line((115, 158), (200, 155), w=5)

# Vertical bar through the middle of top stack
line((158, 82), (158, 205), w=5)

# Fourth horizontal - longest, base of upper section (中间长横)
line((70, 195), (245, 192), w=6)

# Bottom = 大 (left-falling 撇 + right-falling 捺 from below the long horizontal)
# Left-falling
curve([(155, 205), (135, 230), (108, 255), (75, 280)], w=5)
# Right-falling (捺)
curve([(160, 205), (185, 235), (215, 260), (250, 282)], w=5)

out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_美.png")
img.save(out_path)
print(f"Saved {out_path}")
