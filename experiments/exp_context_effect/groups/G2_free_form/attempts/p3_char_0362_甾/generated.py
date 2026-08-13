"""
甾 — top: 巛 (three wavy vertical strokes), bottom: 田
Layout on 300x300:
  巛 spans y ~ 40..140, three strokes at x ~ 90, 150, 210
  田 spans ~ (x 90..210, y 150..260)
"""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)
LW = 6

def line(p1, p2, width=LW):
    d.line([p1, p2], fill=INK, width=width)

def curve(points, width=LW):
    # Draw a smooth polyline
    for i in range(len(points) - 1):
        d.line([points[i], points[i+1]], fill=INK, width=width)

# --- Top: 巛 (three wavy vertical strokes) ---
# Each stroke: small top-left flick, then long curve down-right then down-left (S-shape)
# Positions: left ~ x=85, middle ~ x=145, right ~ x=205
def zigzag(x_top, y_top=45, y_bot=140, curl=12):
    # Smooth S-curve using cubic Bezier sampling.
    # Small dot/flick at top, then wavy body flowing down.
    import math
    # tiny dot/flick at top
    d.line([(x_top + 6, y_top - 2), (x_top - 2, y_top + 6)], fill=INK, width=LW)
    # bezier for S body
    p0 = (x_top - 2, y_top + 8)
    p1 = (x_top + curl + 4, y_top + 30)
    p2 = (x_top - curl, y_top + 70)
    p3 = (x_top + curl + 2, y_bot)
    prev = p0
    N = 24
    for i in range(1, N + 1):
        t = i / N
        u = 1 - t
        x = (u**3)*p0[0] + 3*(u**2)*t*p1[0] + 3*u*(t**2)*p2[0] + (t**3)*p3[0]
        y = (u**3)*p0[1] + 3*(u**2)*t*p1[1] + 3*u*(t**2)*p2[1] + (t**3)*p3[1]
        d.line([prev, (x, y)], fill=INK, width=LW)
        prev = (x, y)

zigzag(80)
zigzag(145)
zigzag(210)

# --- Bottom: 田 ---
# Rectangle with cross
x0, y0 = 90, 158
x1, y1 = 210, 268
# outer rectangle - draw as 4 lines
line((x0, y0), (x1, y0))   # top
line((x1, y0), (x1, y1))   # right
line((x0, y1), (x1, y1))   # bottom
line((x0, y0), (x0, y1))   # left
# inner cross
mx = (x0 + x1) // 2
my = (y0 + y1) // 2
line((mx, y0), (mx, y1))   # vertical
line((x0, my), (x1, my))   # horizontal

out = os.path.join(os.path.dirname(__file__), "01_甾.png")
img.save(out)
print("wrote", out)
