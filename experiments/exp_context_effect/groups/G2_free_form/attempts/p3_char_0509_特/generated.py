"""
p3_char_0509_特 (tè) — 10 strokes total:
Left = 牜 (牛 as left radical, 4 strokes):
  1) 撇 short slanted flick at top
  2) 横 short horizontal
  3) 竖 long central vertical
  4) 提 rising tick from lower-left up to right (crosses 竖)
Right = 寺 (6 strokes = 土 + 寸):
  5) 横 short top of 土
  6) 竖 short middle of 土
  7) 横 long middle horizontal (bottom of 土, also top of 寸 area)
  8) 横 medium horizontal (top of 寸)
  9) 竖钩 long vertical with UP-LEFT hook at bottom (through 寸)
  10) 点 small dab at upper right of 寸

# SIGNATURE CHECK: right-top is 土 (bottom 横 longer than top 横).
# TIER-0 B: 竖钩 flick UP-and-slightly-LEFT (~-100° to -110°).
# TIER-0 H: left 提 must reach toward right component (touch).
# TIER-0 F: use taper+bezier for curved strokes; shoulder dab at 折 joints.
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


def bezier(p0, p1, p2, n=60):
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


# ============ LEFT: 牜 (compressed to left third x=25..130) ============
# 1) 撇 - short slanted flick top-left of the radical
taper((90, 55), (58, 105), r0=4.0, r1=1.5, steps=60)

# 2) 横 - short top horizontal
taper((58, 108), (118, 100), r0=3.0, r1=3.2, steps=60)
d.ellipse((114, 96, 122, 104), fill=BLACK)

# 3) 竖 - long central vertical of left radical
taper((88, 78), (88, 260), r0=3.5, r1=2.8, steps=120)
d.ellipse((85, 75, 91, 82), fill=BLACK)

# 4) 提 - rising tick from lower-left up to right, reaching right side (H rule: touch)
taper((42, 195), (128, 160), r0=4.0, r1=1.5, steps=70)


# ============ RIGHT: 寺 (right two-thirds x=140..280) ============
# --- 土 top (3 strokes) ---
# 5) 横 - short top horizontal of 土 (top-shorter)
taper((178, 75), (238, 72), r0=3.0, r1=3.2, steps=60)

# 6) 竖 - short middle vertical of 土
taper((208, 55), (208, 130), r0=3.2, r1=3.0, steps=60)
d.ellipse((205, 52, 211, 60), fill=BLACK)

# 7) 横 - long middle horizontal (bottom of 土 = longer than top)
taper((150, 132), (275, 128), r0=3.5, r1=3.5, steps=90)

# --- 寸 bottom (3 strokes) ---
# 8) 横 - medium horizontal (top of 寸)
taper((155, 180), (270, 176), r0=3.3, r1=3.3, steps=90)

# 9) 竖钩 - long vertical with UP-LEFT hook at bottom
# vertical trunk
taper((215, 145), (215, 255), r0=3.5, r1=3.2, steps=100)
# hook flick UP-and-LEFT (~ -110°) - larger flick
taper((215, 255), (188, 235), r0=3.5, r1=1.3, steps=40)

# 10) 点 - small dab upper right of 寸, attached to vertical crossing
# small teardrop, thick-to-thin, going down-right
taper((228, 192), (248, 212), r0=3.8, r1=1.5, steps=40)


out = ("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
       "groups/G2_free_form/attempts/p3_char_0509_特/01_特.png")
img.save(out)
print("wrote", out)
