from PIL import Image, ImageDraw
import os
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def line(p1, p2, w=6):
    d.line([p1, p2], fill="black", width=w)

def polyline(pts, w=6):
    for i in range(len(pts) - 1):
        line(pts[i], pts[i+1], w=w)

# 士 (top): long horizontal on top, short horizontal below, vertical through both
# Long top horizontal
line((60, 90), (240, 88), w=6)
# Vertical
line((150, 62), (150, 150), w=6)
# Short horizontal (lower)
line((100, 148), (200, 148), w=6)

# 心 (bottom): left dot, big U-shaped bowl (卧钩 wo-gou), middle dot, right dot
# Left short slash (dot)
line((72, 195), (88, 220), w=6)

# Bowl (卧钩): starts upper-left, curves down and right, ends with slight hook up-right
bowl_pts = []
# Approximate as arc: center around (150, 220), wide flat U
cx, cy = 150, 225
rx, ry = 70, 40
# arc from angle 200 deg (upper left) sweeping down/right to angle 340 deg (upper right)
for deg in range(200, 341, 10):
    a = math.radians(deg)
    x = cx + rx * math.cos(a)
    y = cy - ry * math.sin(a)  # y grows down; -sin so upper part
    bowl_pts.append((x, y))
polyline(bowl_pts, w=6)

# small hook up-right at end of bowl
end = bowl_pts[-1]
line(end, (end[0] + 8, end[1] - 12), w=6)

# Middle dot (inside bowl, slightly right of center)
line((155, 225), (168, 245), w=6)

# Right dot (top-right of 心, above/right of bowl end)
line((215, 195), (232, 218), w=6)

out = os.path.join(os.path.dirname(__file__), "01_志.png")
img.save(out)
print("wrote", out)
