"""
Render 九 (jiǔ) — retry #1. 2 strokes: 撇 + 横折弯钩.

Prior attempt (p3_char_0023_九) failed: 横折弯钩 bowl too small and hook
came inward too tightly, reading as 力/刀-like. Also the 撇 crossed but
the whole silhouette was squashed.

Errata fix: "撇 shorter and higher; 横折弯钩 dominates and sweeps wider
(~200 px x-extent)". Cross-ref form_catalog "撇 as body-crossing diagonal".

GT observations (looking at gt/phase3/九.png):
  - 撇 starts high (~y=55), throws long and low to bottom-left corner
    (~x=45, y=270). Gentle rightward bow.
  - 横折弯钩: short top 横 from crossing point (~x=130,y=95) rightward
    to (~x=210, y=90). Then a fold, then a big rightward-and-downward
    bowl reaching (~x=235, y=245). Then it runs LEFT along the bottom
    (~y=270) to about x=170, and finally flicks UP-LEFT sharply.

Canvas: 300x300, white background, black ink.
"""

from PIL import Image, ImageDraw
import math

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


def cubic_bezier(p0, p1, p2, p3, r_start, r_end, steps=600):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = (u**3) * p0[0] + 3 * (u**2) * t * p1[0] + 3 * u * (t**2) * p2[0] + (t**3) * p3[0]
        y = (u**3) * p0[1] + 3 * (u**2) * t * p1[1] + 3 * u * (t**2) * p2[1] + (t**3) * p3[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---------------------------------------------------------------------
# Stroke 1: 撇 — body-crossing diagonal, drawn FIRST (canonical order)
# Start high near top-center, throw down-left with gentle rightward bow.
# ---------------------------------------------------------------------
dab(150, 55, 6)  # 顿 press at start
quad_bezier(
    (150, 55),      # start (top pixel WELL above the 横 line at y=95)
    (100, 165),     # control pulled left-down for gentle rightward bow
    (45, 273),      # end at lower-left corner
    r_start=6.0,
    r_end=1.2,
    steps=600,
)

# ---------------------------------------------------------------------
# Stroke 2: 横折弯钩 — dominant sweeping bowl
# Segments: short 横 → fold → long convex bowl (right & down) →
# leftward run along bottom → sharp up-left hook flick.
# ---------------------------------------------------------------------

# Top 横: from just RIGHT of the 撇 crossing point (~x=125, y=98) rightward
# to a shoulder at (~x=225, y=88). Slight upward tilt. WIDER than before.
dab(125, 98, 5)  # left 顿
tapered_line(125, 98, 225, 88, r_start=5.0, r_end=5.5, steps=280)

# Fold shoulder — small press
dab(227, 89, 7)

# Bowl: sweep right-then-down, reaching a max x around 262-265 mid-height,
# then arcing down to a wide flat bottom around y=278 at x~170.
# Widen significantly so the bowl DOMINATES the character.
cubic_bezier(
    (227, 89),      # start of bowl (right after shoulder)
    (280, 155),     # control 1: pull far right for bigger bulge (was 262)
    (260, 275),     # control 2: pull down and slightly left, near bottom
    (170, 278),     # end: at flat bottom, left of the bulge
    r_start=5.5,
    r_end=5.0,
    steps=700,
)

# Hook (钩) flick: from (170,278), sweep UP and LEFT — smaller/shorter
# than a full 竖钩 hook (this is a 弯钩 terminus). ~25 px, angle ~-120°.
quad_bezier(
    (170, 278),
    (162, 268),
    (150, 253),
    r_start=5.0,
    r_end=1.0,
    steps=220,
)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0023_九__retry_1/01_九.png"
)
