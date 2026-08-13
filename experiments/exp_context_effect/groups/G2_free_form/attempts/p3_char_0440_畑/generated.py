"""
畑 (kokuji: 'field/dryland') — 9 strokes = 火 (left) + 田 (right).

Composition (left-right, left compressed ~40%, right ~50%):
  Left 火 (4 strokes): compressed narrow — L1 short left 点/撇,
    L2 short right 撇, L3 long central 撇 (bowed), L4 捺 (short, doesn't dominate).
  Right 田 (5 strokes): 竖 (left wall), 横折 (top+right wall),
    横 (mid horizontal cross), 竖 (mid vertical cross), 横 (bottom).

Calligraphic-weight 4-move applied:
  - Teardrop taper on 撇 / 捺 (火 side).
  - Shoulder dab at 横折 corner (田 side).
  - Bezier for bowed 撇 and 捺.
  - No hooks in this character.
"""
import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line(x1, y1, x2, y2, w=6):
    d.line([(x1, y1), (x2, y2)], fill="black", width=w)


def taper_bez(p0, p1, p2, r_start, r_end, steps=250, ease=1.0):
    x0, y0 = p0; x1, y1 = p1; x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        te = t ** ease
        omt = 1 - t
        x = omt * omt * x0 + 2 * omt * t * x1 + t * t * x2
        y = omt * omt * y0 + 2 * omt * t * y1 + t * t * y2
        r = r_start + (r_end - r_start) * te
        dab(x, y, r)


# =============================================================
# LEFT: 火 — compressed, occupies x ~ 25..130
# =============================================================
# L1: left short 撇 (upper-left, throws down-left)
dab(70, 105, 5.0)
taper_bez((70, 105), (60, 125), (42, 155), 4.5, 1.0, steps=200)

# L2: right short 撇 (mid-upper, throws down-left toward center)
dab(115, 108, 5.0)
taper_bez((115, 108), (103, 130), (85, 158), 4.5, 1.0, steps=200)

# L3: long central 撇 (top → lower-left, bowed)
dab(92, 70, 6.0)
taper_bez((92, 70), (75, 150), (28, 240), 5.5, 1.2, steps=400, ease=1.05)

# L4: 捺 (from mid-upper, short down-right — kept short to fit)
p0 = (85, 108); p1 = (105, 165); p2 = (135, 235)
steps = 350
for i in range(steps + 1):
    t = i / steps
    omt = 1 - t
    x = omt * omt * p0[0] + 2 * omt * t * p1[0] + t * t * p2[0]
    y = omt * omt * p0[1] + 2 * omt * t * p1[1] + t * t * p2[1]
    if t < 0.85:
        r = 1.3 + (7.0 - 1.3) * (t / 0.85) ** 1.15
    else:
        r = 7.0
    dab(x, y, r)
# broad foot
tx, ty = 135 - 105, 235 - 165
tl = math.hypot(tx, ty)
tx, ty = tx / tl, ty / tl
for i in range(60 + 1):
    t = i / 60
    x = 135 + tx * 20 * t
    y = 235 + ty * 20 * t
    r = 7.0 - 6.0 * t
    dab(x, y, r)


# =============================================================
# RIGHT: 田 — box with cross, occupies x ~ 155..270, y ~ 75..220
# =============================================================
TOP, BOT, L, R = 75, 220, 155, 270
MID_Y = (TOP + BOT) // 2
MID_X = (L + R) // 2

W_S = 6

# R1: 竖 (left wall)
dab(L, TOP, 4)
line(L, TOP, L, BOT, w=W_S)

# R2: 横折 (top horizontal + shoulder + right wall)
line(L - 1, TOP, R + 2, TOP, w=W_S)
dab(R + 1, TOP + 2, 5)  # shoulder dab at top-right corner
line(R, TOP, R, BOT, w=W_S)

# R3: 横 (middle horizontal cross-bar, wall to wall)
line(L, MID_Y, R, MID_Y, w=W_S)

# R4: 竖 (middle vertical cross-bar, top to bottom)
line(MID_X, TOP, MID_X, BOT, w=W_S)

# R5: 横 (bottom horizontal — slight up-tilt)
line(L - 1, BOT, R + 2, BOT - 1, w=W_S)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0440_畑/01_畑.png"
)
print("Saved 01_畑.png")
