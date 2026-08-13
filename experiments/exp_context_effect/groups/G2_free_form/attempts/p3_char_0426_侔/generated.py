"""
p3_char_0426_侔 — G2 attempt (revision 2)

Decomposition: 侔 = 亻 (left) + 牟 (right)
  牟 top = 厶: a 撇 flowing into an arc that closes to a small dot/hook
  牟 middle = 短撇 (small down-left flick)
  牟 bottom = 牛: horizontal 长横 + 竖 long descender + implied inner short 横

Composition rule: composition_rules.md "亻 + X"
  亻: x=40-110, body: x=120-260
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def stroke(points, width=6):
    if len(points) < 2:
        return
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        draw.line((x1, y1, x2, y2), fill="black", width=width)
    for x, y in points:
        r = width / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

def curve(p0, p1, p2, width=6, steps=40):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    stroke(pts, width=width)

def cubic(p0, p1, p2, p3, width=6, steps=50):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0]
        y = u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]
        pts.append((x, y))
    stroke(pts, width=width)

# ============ 亻 (LEFT radical) ============
# 撇 from ~ (95, 55) down-left to (50, 145)
curve((95, 55), (80, 95), (50, 148), width=6)
# 竖 from just below 撇 joint, straight down
stroke([(78, 128), (78, 250)], width=7)

# ============ 牟 (RIGHT body) ============
# 厶 top: a 撇 curving right then hooking down (single continuous stroke)
# starts at ~(180, 55), sweeps down-left to (155, 90), then arcs right to (210, 95)
cubic((180, 50), (150, 65), (155, 100), (210, 100), width=6)

# 短撇 middle: pointing down-left, sits under the 厶
curve((215, 105), (185, 130), (150, 155), width=6)

# 长横 (long horizontal cross): spans right two-thirds, slight upward slope
stroke([(130, 200), (275, 190)], width=7)

# 竖 (long central descender): from just above the 横 down to bottom
stroke([(200, 140), (200, 285)], width=7)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0426_侔/01_侔.png")
print("saved")
