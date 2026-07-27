"""
化 = 亻 (left) + 匕 (right)  — 4 strokes

# SIGNATURE CHECK (from sibling_signature_checklist.md, 匕 row):
#   匕: top stroke is a 撇 (upper-right→lower-left);
#       terminal hook flicks UP-and-LEFT.
#   The 撇 CROSSES the 竖弯钩's vertical body (not floating outside it).

Layout (300×300):
 亻: left column, occupies x=50–130, y=70–260
 匕: right column, occupies x=155–260, y=80–255

Strokes:
 1) 亻-撇: short left-position 撇, ~x120,y80 → x60,y185
 2) 亻-竖: straight vertical from crossing to bottom, ~x100,y150 → x100,y260
 3) 匕-撇: upper-right→lower-left, CROSSES the vertical body of 匕
          ~x235,y95 → x160,y175 (passes through x≈185 which is the 竖弯钩 body)
 4) 匕-竖弯钩: starts at ~x185,y85, descends vertically to y≈205,
              arcs rightward along bottom to ~x255,y235,
              hook flicks UP-and-LEFT at ~-115°.
"""
from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def brush_line(p0, p1, width=6):
    d.line([p0, p1], fill="black", width=width)

def brush_taper(p0, p1, w0=8, w1=3, steps=60):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        t = i / (steps - 1)
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        w = w0 + (w1 - w0) * t
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def brush_curve(points, width=6):
    for i in range(len(points) - 1):
        d.line([points[i], points[i + 1]], fill="black", width=width)
    for (x, y) in points:
        r = width / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# ---------- 亻 (person radical, left side) ----------

# Stroke 1: 撇 — tapered, starts upper-mid-left, throws down-left
brush_taper((122, 80), (58, 190), w0=9, w1=3, steps=70)

# Stroke 2: 竖 — vertical, crosses the 撇 near its middle-right
brush_line((100, 148), (100, 260), width=7)

# ---------- 匕 (right side) ----------

# Stroke 4 body first is fine to draw first for layer feel; do 撇 last so
# it visually crosses on top.

# Stroke 4: 竖弯钩
curve_pts = []
# vertical descent along x=190
for y in range(88, 205, 3):
    curve_pts.append((190, y))
# rightward arc: quarter circle center (245, 205), r=55
cx, cy, r = 245, 205, 55
for deg in range(180, 358, 3):
    rad = math.radians(deg)
    x = cx + r * math.cos(rad)
    y = cy + r * math.sin(rad)
    curve_pts.append((x, y))

brush_curve(curve_pts, width=7)

# Hook: flick UP-and-LEFT from arc terminus (~ -115°)
tail = curve_pts[-1]
tx, ty = tail
hook_len = 24
angle = math.radians(-115)
hx = tx + hook_len * math.cos(angle)
hy = ty + hook_len * math.sin(angle)
brush_line((tx, ty), (hx, hy), width=7)

# Stroke 3: 匕-撇  (drawn LAST so it visibly crosses the 竖弯钩 body)
# Must pass through the vertical body (x ≈ 190).
brush_taper((238, 100), (158, 178), w0=9, w1=3, steps=70)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0134_化/01_化.png")
print("saved 01_化.png")
