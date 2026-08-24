"""
Render 佽 (亻 + 次) at 300x300.

Composition:
  - LEFT: 亻 (person radical) in x=45-115, per composition_rules.md.
    * 撇: (110,60)→(55,155), thick→thin.
    * 竖: (110,115)→(110,260), through-axis.
  - RIGHT: 次 = 冫 (top-left of right) + 欠 (right main body).
    * 冫 (two dots, small): upper 点 ~(150,95)→(140,115);
      lower 提 ~(145,135)→(165,148).
    * 欠 (4 strokes, based on p2_radical_112_欠 PASS):
      - 撇 (short, hat): (215,72)→(180,115).
      - 横钩: (185,95)→(255,105) → hook (245,135).
      - 撇 (long): (220,135)→(150,270).
      - 捺: (215,150)→(285,265).

Reused primitives: brush-dab + bezier from prior 欠/亻 PASS attempts.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r0, r1, steps=None):
    if steps is None:
        steps = max(40, int(2 * math.hypot(x1 - x0, y1 - y0)))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r0, r1, steps=220, easing=None):
    for i in range(steps + 1):
        t = i / steps
        te = easing(t) if easing else t
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        r = r0 + (r1 - r0) * te
        dab(x, y, r)


# ============ LEFT: 亻 ============
# 撇
bezier_dabs((110, 60), (95, 100), (55, 155), r0=5.0, r1=1.5, steps=200)
dab(110, 60, 5.0)
# 竖 (through-axis) — extend to bottom of canvas
line_dabs(108, 108, 108, 285, r0=5.5, r1=4.8)
dab(108, 108, 5.5)  # 顿


# ============ RIGHT: 次 = 冫 + 欠 ============

# ---- 冫 (top-left of right area, two short compact strokes; higher and tighter) ----
# 点 1 (upper) — small down-left tick
bezier_dabs((158, 85), (150, 95), (140, 110), r0=3.8, r1=1.3, steps=80)
# 点 2 (lower) — 提 tick up-right, well below the upper dot
bezier_dabs((145, 148), (158, 152), (175, 155), r0=3.6, r1=1.3, steps=80)

# ---- 欠 (right main body) ----
# Stroke 1: 撇 (short hat, upper-left of the right region)
bezier_dabs((215, 68), (200, 88), (178, 118), r0=4.5, r1=1.3, steps=180)
dab(215, 68, 4.8)

# Stroke 2: 横钩 (short 横 across top-right + hook down-left)
line_dabs(188, 92, 258, 100, r0=3.8, r1=4.0)
dab(258, 100, 5.5)  # corner shoulder
# Hook flick DOWN-and-LEFT (per Tier-0 rule B: -105° to -120°)
line_dabs(258, 100, 240, 132, r0=4.5, r1=1.2, steps=100)

# Stroke 3: 撇 (long, sweeping down-left from below the hat)
# End must stay right of 亻's 竖 (x>=135)
bezier_dabs((225, 130), (200, 200), (158, 275), r0=6.0, r1=1.4, steps=280)
dab(225, 130, 6.2)

# Stroke 4: 捺 (down-right, thin→thick, broad foot)
bezier_dabs((218, 150), (245, 205), (285, 265),
            r0=1.6, r1=6.0, steps=280, easing=lambda t: t ** 1.15)
# broad foot terminal
dab(281, 265, 7.0)
dab(287, 263, 6.2)


img.save(
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0406_佽/01_佽.png"
)
