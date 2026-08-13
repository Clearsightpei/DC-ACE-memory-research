"""
更 (gèng) — 7 strokes
Structure: 一 (top horizontal) + 曰 (rectangle with middle bar) +
           丿 (long left flick) + 乀 (long right press stroke)
The 丿 and 乀 cross through the 曰's bottom region and extend outward.

Layout (300x300):
- Top 一: y≈70, from x≈70 to x≈230
- 曰: box roughly x=95..205, y=80..165
- Middle bar of 曰: y≈122
- 丿 (撇): starts near top-center of 曰 (~x=140, y=90),
  sweeps down-left ending near (60, 250)
- 乀 (捺): starts near right-center of 曰 (~x=170, y=140),
  sweeps down-right ending near (255, 250) with a subtle press.
"""
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = (0, 0, 0)

def stroke(pts, width=8):
    d.line(pts, fill=INK, width=width, joint="curve")

def brush_stroke(pts, widths):
    """Variable-width polyline via overlapping ellipses along segments."""
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i+1]
        w1 = widths[i]
        w2 = widths[i+1]
        steps = max(6, int(((x2-x1)**2 + (y2-y1)**2) ** 0.5))
        for t_i in range(steps + 1):
            t = t_i / steps
            x = x1 + (x2 - x1) * t
            y = y1 + (y2 - y1) * t
            w = w1 + (w2 - w1) * t
            r = w / 2
            d.ellipse([x-r, y-r, x+r, y+r], fill=INK)

# 1) Top horizontal 一 (thinner)
brush_stroke([(60, 72), (150, 70), (238, 74)], [5, 6, 6])

# 2) 曰 left vertical 丨
brush_stroke([(105, 88), (105, 168)], [6, 7])

# 3) 曰 top-right corner 横折 (top horizontal then down)
brush_stroke([(105, 88), (155, 86), (198, 88), (200, 168)], [6, 6, 7, 7])

# 4) 曰 middle horizontal (short, only inside)
brush_stroke([(110, 128), (195, 128)], [5, 5])

# 5) 曰 bottom horizontal (close the box)
brush_stroke([(105, 165), (200, 165)], [6, 6])

# 6) 丿 long 撇 — starts inside/top of 曰, sweeps down-left
# Bezier-like curve via sampled points
import math
def bezier(p0, p1, p2, p3, n=40):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1-t)**3*p0[0] + 3*(1-t)**2*t*p1[0] + 3*(1-t)*t**2*p2[0] + t**3*p3[0]
        y = (1-t)**3*p0[1] + 3*(1-t)**2*t*p1[1] + 3*(1-t)*t**2*p2[1] + t**3*p3[1]
        pts.append((x, y))
    return pts

pie_pts = bezier((152, 85), (140, 150), (110, 210), (55, 258), n=50)
pie_widths = [max(3, 10 - 7 * (i / len(pie_pts))) for i in range(len(pie_pts))]
brush_stroke(pie_pts, pie_widths)

# 7) 乀 long 捺 — starts near middle-right of 曰, sweeps down-right with press
na_pts = bezier((170, 138), (190, 180), (215, 220), (258, 250), n=50)
# Press stroke: thin at start, thickens toward end, then a slight taper
na_widths = []
for i in range(len(na_pts)):
    t = i / (len(na_pts) - 1)
    if t < 0.75:
        w = 4 + 8 * (t / 0.75)  # 4 -> 12
    else:
        w = 12 - 6 * ((t - 0.75) / 0.25)  # 12 -> 6 (taper at press tail)
    na_widths.append(w)
brush_stroke(na_pts, na_widths)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0331_更/01_更.png")
print("saved")
