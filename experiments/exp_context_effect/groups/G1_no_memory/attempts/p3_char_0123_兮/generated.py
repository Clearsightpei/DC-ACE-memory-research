"""Render 兮 (xī) with PIL to a 300x300 PNG.

Strokes (4):
  1. left dot / 撇 (top-left, slanting down-left)
  2. right dot / 捺 (top-right, slanting down-right, longer)
  3. horizontal 一 in middle
  4. 乎-like hook curving down-left then hooking
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6

def line(p0, p1, width=LW):
    draw.line([p0, p1], fill=INK, width=width)

def curve(points, width=LW):
    # smooth polyline
    for i in range(len(points) - 1):
        draw.line([points[i], points[i+1]], fill=INK, width=width)
    # round joints
    for p in points:
        draw.ellipse([p[0]-width//2, p[1]-width//2, p[0]+width//2, p[1]+width//2], fill=INK)

# 1) left short 撇 (top-left slant): starts upper-mid-left, sweeps down-left
curve([(120, 90), (105, 110), (85, 135), (60, 160)])

# 2) right 捺 (long stroke from upper-mid going down-right to far right)
curve([(150, 80), (175, 105), (205, 130), (240, 150), (260, 155)])

# 3) horizontal 一 in middle
line((95, 155), (215, 152), width=LW)

# 4) bottom hook (亅-like): starts at horizontal center, curves down-right
# slightly, then hooks back up to the left at the bottom
curve([(155, 155), (162, 180), (165, 210), (158, 235), (140, 250), (118, 248), (110, 240)])

out = os.path.join(os.path.dirname(__file__), "01_兮.png")
img.save(out)
print("Wrote", out)
