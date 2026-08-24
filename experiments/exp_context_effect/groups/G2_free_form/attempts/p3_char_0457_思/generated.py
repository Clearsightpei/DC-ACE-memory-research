"""
Render 思 (si1) at 300x300, black ink on white.

Structural read from GT:
  Top:    田 — square box with an interior cross.
          Strokes: (1) left 竖, (2) top 横折 [top横 + right 竖],
                   (3) middle 横 crossing, (4) middle 竖 crossing,
                   (5) bottom 横 sealing.
  Bottom: 心 — 4 strokes.
          (a) left 点 (short flick down-left)
          (b) 卧钩 — shallow bowl sweeping right, terminal flick
              UP-and-LEFT (~-145°) per TIER-0 rule B.
          (c) middle 点 (small, sitting on the bowl)
          (d) right 点 (short flick down-right)

Applies the 4-move calligraphic-weight recipe (TIER-0 F):
  - teardrop taper on every 点 and hook flick
  - shoulder dab at 折 corner of 横折
  - bezier for the 卧钩 arc
  - correct hook flick UP-and-LEFT
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
    """Draw a variable-width stroke via overlapping circles."""
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


# ========== 田 (top) ==========
# Bounding box roughly (95, 40) to (210, 150)
L, R = 95, 210
T, B = 40, 150
MID_V = (L + R) // 2   # 152
MID_H = (T + B) // 2   # 95

# (1) left 竖
left_v = bez((L, T), (L, T + 35), (L, T + 70), (L, B), n=50)
stroke(left_v, (8, 7))

# (2) top 横折 — top horizontal then right vertical
top_h = bez((L, T), (L + 30, T - 1), (R - 30, T - 1), (R, T), n=50)
stroke(top_h, (7, 8))
# shoulder dab at top-right corner
dab(R, T, 6)
right_v = bez((R, T), (R, T + 35), (R, T + 70), (R, B), n=50)
stroke(right_v, (8, 7))

# (3) middle 横
mid_h = bez((L + 4, MID_H), (L + 40, MID_H), (R - 40, MID_H), (R - 4, MID_H), n=50)
stroke(mid_h, (6, 6))

# (4) middle 竖
mid_v = bez((MID_V, T + 4), (MID_V, T + 35), (MID_V, T + 70), (MID_V, B - 4), n=50)
stroke(mid_v, (7, 7))

# (5) bottom 横
bot_h = bez((L, B), (L + 40, B), (R - 40, B), (R, B), n=50)
stroke(bot_h, (7, 8))

# ========== 心 (bottom) ==========
# spread across (45, 185) to (265, 280)

# (a) left 点 — short flick down-left
ldot = bez((72, 195), (68, 210), (63, 225), (55, 240), n=40)
stroke(ldot, (10, 3))

# (b) 卧钩 — shallow bowl left-to-right, then hook flick UP-LEFT
wo = bez((95, 215), (110, 275), (185, 285), (240, 250), n=80)
stroke(wo, (6, 11))
# hook flick UP-and-LEFT from the bowl's right end
flick = bez((240, 250), (233, 242), (225, 233), (215, 222), n=30)
stroke(flick, (11, 3))

# (c) middle 点 — small teardrop sitting above the bowl
mdot = bez((155, 220), (158, 232), (160, 244), (158, 254), n=30)
stroke(mdot, (4, 9))

# (d) right 点 — short flick down-right (or nearly vertical)
rdot = bez((205, 200), (210, 213), (215, 226), (222, 238), n=30)
stroke(rdot, (4, 10))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0457_思/01_思.png")
