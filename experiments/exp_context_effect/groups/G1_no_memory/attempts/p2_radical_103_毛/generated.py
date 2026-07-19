"""G1 render of 毛 (radical 103, 4 strokes) — revision 2."""
from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

INK = "black"
TH = 6

def line(pts, width=TH):
    d.line(pts, fill=INK, width=width, joint="curve")

# Stroke 1: 短撇 at top — starts right-upper, swoops down-left
line([(170, 60), (115, 95)], width=TH)

# Stroke 2: first 横 (upper horizontal, short-medium), slight rising
line([(100, 100), (200, 92)], width=TH)

# Stroke 3: second 横 (middle horizontal, longer), slight rising
line([(65, 165), (220, 155)], width=TH)

# Stroke 4: 竖弯钩 — vertical from just under top horizontal,
# down and curving right, ending with small upward hook
# vertical segment
line([(150, 95), (150, 215)], width=TH)

# curve segment: bezier-like from (150,215) sweeping right to (235, 245)
curve_pts = []
for t in range(0, 25):
    u = t / 24.0
    # quadratic bezier: P0=(150,215), P1=(160,260), P2=(235,245)
    x = (1-u)*(1-u)*150 + 2*(1-u)*u*175 + u*u*235
    y = (1-u)*(1-u)*215 + 2*(1-u)*u*260 + u*u*245
    curve_pts.append((x, y))
line(curve_pts, width=TH)

# small hook: from (235, 245) up-left slightly
line([(235, 245), (238, 218)], width=TH)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_毛.png")
img.save(out)
print(f"wrote {out}")
