"""
p3_char_0385_物 (wù) — 8 strokes total:
Left = 牜 (牛 as left radical, compressed, 4 strokes):
  1) 撇 short slanted flick at top
  2) 横 short horizontal
  3) 竖 long central vertical
  4) 提 small rising tick (bottom-left up to right) — the 牛's lower 横 becomes 提 in radical form
Right = 勿 (4 strokes):
  5) 撇 short top-left (shoulder)
  6) 横折钩 top 横 + long descending right curve + hook UP-LEFT
  7) 撇 short interior
  8) 撇 longer interior below

Layout on 300x300 canvas: left half x=25..130, right half x=130..275.
Hook rule (from memory index Tier-0 B): 横折钩 flick UP-LEFT (~-115°).
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)
BLACK = (0, 0, 0)


def taper(p0, p1, r0, r1, steps=80):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        d.ellipse((x - r, y - r, x + r, y + r), fill=BLACK)


def bezier(p0, p1, p2, n=50):
    pts = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        pts.append((x, y))
    return pts


def stroke_poly(points, width=6):
    d.line(points, fill=BLACK, width=width, joint="curve")
    for (x, y) in [points[0], points[-1]]:
        r = width / 2
        d.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# ============ LEFT: 牜 ============
# 1) 撇 - short slanted flick top-left of the radical
taper((85, 55), (55, 105), r0=4.0, r1=1.5, steps=60)

# 2) 横 - short top horizontal
taper((55, 108), (115, 100), r0=3.0, r1=3.2, steps=60)
d.ellipse((112, 96, 120, 104), fill=BLACK)

# 3) 竖 - long central vertical of left radical
taper((85, 78), (85, 265), r0=3.5, r1=2.8, steps=120)
d.ellipse((82, 75, 88, 82), fill=BLACK)

# 4) 提 - rising tick from lower-left up to right, crossing 竖
taper((35, 185), (120, 155), r0=4.0, r1=1.5, steps=70)

# ============ RIGHT: 勿 ============
# 5) 撇 short top-left (shoulder of 勹) - starts around top of right half
s5 = bezier((175, 60), (163, 90), (145, 120))
stroke_poly(s5, width=6)

# 6) 横折钩 - top 横, then long descending curve, then hook UP-LEFT
# top horizontal
taper((160, 108), (258, 100), r0=3.2, r1=3.5, steps=80)
# descending curve (shoulder + right side)
descend = bezier((258, 100), (255, 190), (200, 260))
stroke_poly(descend, width=7)
# hook flick UP-LEFT
taper((200, 260), (180, 240), r0=3.5, r1=1.5, steps=40)

# 7) 撇 short interior (upper)
s7 = bezier((200, 140), (185, 168), (160, 200))
stroke_poly(s7, width=5)

# 8) 撇 longer interior (lower right)
s8 = bezier((235, 165), (200, 218), (145, 275))
stroke_poly(s8, width=6)

out = ("<REPO_ROOT>/experiments/exp_context_effect/"
       "groups/G2_free_form/attempts/p3_char_0385_物/01_物.png")
img.save(out)
print("wrote", out)
