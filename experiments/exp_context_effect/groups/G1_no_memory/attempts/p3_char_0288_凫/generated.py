from PIL import Image, ImageDraw
import os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

BLACK = (0, 0, 0)
LW = 4


def line(pts, width=LW):
    d.line(pts, fill=BLACK, width=width, joint="curve")


def bezier(p0, p1, p2, width=LW, steps=40):
    pts = []
    for t in range(steps + 1):
        u = t / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    line(pts, width)


# =====================================================
# TOP PART: 鸟 (simplified, sits center-top)
# =====================================================

# 1) Head tick (short diagonal, top of head)
line([(130, 55), (150, 45)], width=4)

# 2) Head - small horizontal top
line([(135, 62), (170, 60)], width=4)

# 3) Eye dot inside head
d.ellipse([150, 72, 158, 80], fill=BLACK)

# 4) Left vertical of head/body coming down from top-left of head horizontal
line([(135, 62), (128, 155)], width=4)

# 5) Right side: horizontal then curving down (横折弯)
line([(135, 88), (175, 88)], width=4)
bezier((175, 88), (185, 115), (170, 140), width=4)

# 6) Inner horizontal bars of 鸟
line([(128, 115), (172, 115)], width=4)
line([(128, 140), (172, 140)], width=4)

# =====================================================
# BOTTOM PART: 几 (wraps under the bird, wide)
# =====================================================

# 7) Short left stroke of 几 - piě (falling left)
bezier((115, 165), (95, 220), (65, 275), width=5)

# 8) Top horizontal of 几 (横 across whole width, connects to right)
line([(110, 170), (230, 170)], width=4)

# 9) Right stroke of 几: down then curve right with hook (横折弯钩)
bezier((230, 170), (235, 230), (255, 265), width=5)
# hook up-left at bottom
line([(255, 265), (270, 258)], width=4)
line([(270, 258), (263, 250)], width=4)

out = os.path.join(os.path.dirname(__file__), "01_凫.png")
img.save(out)
print("saved", out)
