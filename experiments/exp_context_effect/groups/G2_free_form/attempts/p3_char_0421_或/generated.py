"""
Item: p3_char_0421_或  (huò)
Group: G2

Structure (8 strokes):
  1. 一 top horizontal (top of 戈; short, upper-left)
  2. 丨 left vertical of 口
  3. 横折 top+right of 口
  4. 一 bottom of 口
  5. 一 horizontal under 口 (base of 戈, extends right)
  6. 斜钩 long diagonal from upper-center down to lower-right,
     with UP-and-LEFT hook flick (TIER-0 rule B; belly on lower-left,
     Bezier P0=(150,60), P2=(255,238), ctrl=(170,200); hook flick
     ~40 px at ~-115°). This is a FROZEN 戈-family recurring failure
     mode -- the hook MUST be present and MUST flick up-left.
  7. 丿 short flick from upper-mid going down-left
  8. 丶 dot at top-right (identity bit of 戈 family; missing dot
     collapses to 弋)

Sibling risk: 戈 family (代, 成, 伐, 我, 找 all failed on missing
hook + missing dot). Enforce: (i) 斜钩 hook flick, (ii) top-right 丶.
"""

from PIL import Image, ImageDraw
import math, os

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

def stroke_line(p0, p1, r0, r1, n=60):
    x0, y0 = p0; x1, y1 = p1
    for i in range(n + 1):
        t = i / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)

def bezier(p0, p1, p2, r0, r1, n=100, ease=1.0):
    for i in range(n + 1):
        t = i / n
        tt = t ** ease
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)

def dot_tear(p0, p1, r0, r1, n=40):
    # teardrop, thin -> thick with easing then terminal press
    for i in range(n + 1):
        t = i / n
        tt = t ** 1.4
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)
    dab(p1[0], p1[1], r1 + 1)

# ---- 1. 一 top of 戈 (short, upper-left/center) ----
stroke_line((55, 82), (185, 78), 5, 5)
dab(55, 82, 7); dab(185, 78, 7)

# ---- 2. 丨 left of 口 ----
stroke_line((60, 118), (60, 190), 4.5, 4.5)
dab(60, 118, 6); dab(60, 190, 6)

# ---- 3. 横折 top+right of 口 ----
# top 横
stroke_line((60, 118), (135, 115), 4.5, 4.5)
dab(60, 118, 6)
# shoulder dab
dab(135, 115, 6.5)
# right 竖
stroke_line((135, 115), (132, 190), 4.5, 4.5)
dab(132, 190, 6)

# ---- 4. 一 bottom of 口 ----
stroke_line((60, 190), (132, 190), 4.5, 4.5)
dab(60, 190, 6); dab(132, 190, 6)

# ---- 5. 一 horizontal under 口 (base, extends further right) ----
stroke_line((48, 225), (200, 222), 5, 5)
dab(48, 225, 7); dab(200, 222, 7)

# ---- 6. 斜钩 (long diagonal, belly lower-left, hook up-left) ----
# Primary Bezier: P0 upper-center, P2 lower-right, ctrl toward lower-left
P0 = (150, 60)
P1 = (170, 200)   # control -> belly on lower-left
P2 = (260, 240)
bezier(P0, P1, P2, 6, 4, n=140, ease=0.9)
dab(*P0, 7)
# Hook flick: 40 px @ ~-115° (up-and-slightly-left)
ang = math.radians(-115)
hx = P2[0] + 40 * math.cos(ang)
hy = P2[1] + 40 * math.sin(ang)
stroke_line(P2, (hx, hy), 5, 1.5, n=40)
dab(*P2, 6)

# ---- 7. 丿 short flick upper-mid ----
# from around top of 斜钩, going down-left
bezier((155, 70), (135, 90), (115, 108), 4.5, 2, n=50, ease=1.2)

# ---- 8. 丶 dot top-right (identity bit) ----
dot_tear((225, 60), (250, 88), 2, 9)

out_path = os.path.join(os.path.dirname(__file__), "01_或.png")
img.save(out_path)
print(f"wrote {out_path}")
