"""
Render 九 (jiǔ) — 2 strokes, matched to the clean GT.

GT observations:
  - The 撇 starts near top-center (~x=140, y=55), body crosses down-left,
    ending at lower-left (~x=50, y=270). Gentle rightward bow.
  - The 横折弯钩 has a short top 横 starting where the 撇 crosses (~x=130,
    y=95) going right to (~x=205, y=88), a fold, then a big bowl curving
    RIGHT and DOWN to reach ~y=250, and finally a hook (弯钩) that curves
    LEFT along the bottom before flicking UP-LEFT.
  - Body proportions: character occupies roughly the central 60% width,
    top~60, bottom~275.

Canvas: 300x300, white background, black ink.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def tapered_line(x0, y0, x1, y1, r_start, r_end, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def quad_bezier(p0, p1, p2, r_start, r_end, steps=400):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def cubic_bezier(p0, p1, p2, p3, r_start, r_end, steps=500):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = (u**3) * p0[0] + 3 * (u**2) * t * p1[0] + 3 * u * (t**2) * p2[0] + (t**3) * p3[0]
        y = (u**3) * p0[1] + 3 * (u**2) * t * p1[1] + 3 * u * (t**2) * p2[1] + (t**3) * p3[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---- Stroke 2: 横折弯钩 (draw body first for cleaner crossing) ----
# Top 横: short, mildly slanted up-right, from (130,98) to (205,88)
dab(130, 98, 5)  # left 顿
tapered_line(130, 98, 205, 88, r_start=4.5, r_end=5.5, steps=250)
# Fold shoulder press
dab(207, 88, 7)

# Belly curve: from shoulder, out RIGHT and DOWN, then curve back LEFT
# reaching bottom around (150, 258). Use cubic for smoother 弯 shape.
cubic_bezier((207, 88), (255, 155), (240, 240), (150, 258),
             r_start=5.5, r_end=5.0, steps=550)

# Hook (钩): from (150,258), flick UP-LEFT
quad_bezier((150, 258), (140, 245), (118, 220),
            r_start=5.0, r_end=1.0, steps=220)

# ---- Stroke 1: 撇 — body-crossing diagonal ----
# Starts above/near the top bar (~x=148, y=55). Sweeps down-left with a
# gentle rightward bow, ending at lower-left (~x=48, y=272).
dab(148, 58, 6)  # 顿 press at start
quad_bezier((148, 58), (105, 160), (48, 272),
            r_start=5.8, r_end=1.2, steps=550)

img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0023_九/01_九.png"
)
