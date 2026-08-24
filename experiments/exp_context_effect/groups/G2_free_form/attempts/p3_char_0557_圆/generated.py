"""
p3_char_0557_圆  (yuan2, round/circle)

Structure: 囗 (outer enclosure, 3 strokes) wrapping 员 inside
  员 = 口 (top, small) + 贝 (bottom: box + 2 inner 横 + 撇+点 legs)

Total ~10 strokes. Components MUST touch inner content near outer walls
but not cross them (TIER-0 rule H: gap => FAIL for LR; here inner sits
inside enclosure with small margins).

Uses bez+stroke helpers per TIER-0 rule F (calligraphic weight moves):
- teardrop taper on 撇/捺 legs
- shoulder dab at 折 corners
- UP-LEFT hook flick where applicable (bottom-right of frames has slight
  inward taper, no protruding hook here since 囗/口 don't hook)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts


def stroke(pts, widths):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line(p0, p1, w=7):
    pts = bez(p0, (p0[0]*0.66 + p1[0]*0.34, p0[1]*0.66 + p1[1]*0.34),
              (p0[0]*0.34 + p1[0]*0.66, p0[1]*0.34 + p1[1]*0.66), p1, n=40)
    stroke(pts, (w, w))


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ---------------- OUTER 囗 (large enclosure) ----------------
# GT shows the enclosure is tall, with slight rightward opening
L, R = 40, 260
T, B = 30, 275

# 1. 竖 (left wall)
line((L, T + 2), (L, B), w=6)
# 2. 横折 (top + right wall)
line((L - 2, T), (R, T), w=6)          # top horizontal
dab(R, T, 4)                            # shoulder dab
line((R, T), (R, B - 2), w=6)          # right wall
# 3. 横 (bottom, closes the enclosure)
line((L - 2, B), (R + 2, B), w=6)


# ---------------- INNER 员 (口 + 贝) ----------------
# Inner content sits well inside the enclosure with margin
# 口 at top (~y=55..115), 贝 below (~y=125..245)

# --- top 口 (small) ---
kx0, kx1 = 110, 190
ky0, ky1 = 55, 115
# 竖 left
line((kx0, ky0 + 1), (kx0, ky1), w=6)
# 横折 top+right
line((kx0 - 1, ky0), (kx1, ky0), w=6)
dab(kx1, ky0, 4)
line((kx1, ky0), (kx1, ky1 - 1), w=6)
# 横 bottom
line((kx0 - 1, ky1), (kx1 + 1, ky1), w=6)

# --- bottom 贝 (larger) ---
bx0, bx1 = 88, 212
by0, by1 = 130, 235
# 竖 left
line((bx0, by0 + 1), (bx0, by1), w=7)
# 横折 top+right
line((bx0 - 1, by0), (bx1, by0), w=7)
dab(bx1, by0, 5)
line((bx1, by0), (bx1, by1 - 1), w=7)
# inner 横 #1 (upper interior bar)
in_y1 = by0 + 30
line((bx0 + 4, in_y1), (bx1 - 4, in_y1), w=5)
# inner 横 #2 (lower interior bar)
in_y2 = by0 + 62
line((bx0 + 4, in_y2), (bx1 - 4, in_y2), w=5)
# closing bottom horizontal of 贝
line((bx0 - 1, by1), (bx1 + 1, by1), w=6)

# 撇 (left leg) — teardrop taper down-left, exits below box
pie = bez((bx0 + 30, by1 - 2), (bx0 + 15, by1 + 10),
          (bx0 - 5, by1 + 18), (bx0 - 20, by1 + 28), n=50)
stroke(pie, (7, 3))

# 点 (right leg) — short down-right, thickens
dot = bez((bx1 - 30, by1 - 2), (bx1 - 15, by1 + 8),
          (bx1 - 2, by1 + 16), (bx1 + 15, by1 + 26), n=50)
stroke(dot, (3, 8))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0557_圆/01_圆.png")
print("wrote 01_圆.png")
