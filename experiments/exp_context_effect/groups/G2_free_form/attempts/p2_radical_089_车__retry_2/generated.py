"""G2 retry #2 for 车 (4-stroke simplified radical).

Prior attempts failed:
  - retry_0: symmetric 王-like collapse
  - retry_1: still too 王-like — three parallel horizontals + centered 竖,
             with a small ⊤-lid tacked on the right that reads as noise
             rather than the signature 撇折 middle stroke.

Vision of GT (viewed for retry_2):
  Stroke 1: SHORT top 横 (upper-left region), slight rightward-up tilt.
  Stroke 2: 撇折 — starts as a short 撇 (diagonal from top-right area
            going down-left), then FOLDS/turns to become the middle
            HORIZONTAL cross-bar that crosses the 竖. This is the
            canonical simplified-车 signature stroke, NOT a plain 横.
            It creates the "十"-cross look in the middle.
  Stroke 3: LONG bottom 横 — widest stroke, near y=210, slight up-tilt.
  Stroke 4: Central 竖 through-going axis — extends from above the top
            横 down through the middle cross and past the bottom 横,
            with a small hook / 提 kick at the very bottom-right.

Signature bits for 车:
  - The middle bar is a 撇折 (has an angled left/upper origin), NOT
    a symmetric 横.
  - The bottom 横 is clearly the longest.
  - The central 竖 pierces top+middle+bottom (through-going axis).
  - No top ⊤-lid box (that was retry_1's mistake).

Uses PIL brush-dabs (drawer_memory principle for calligraphic feel).
Canvas 300x300, white bg, black ink.
"""

from PIL import Image, ImageDraw
import math

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dabs(x0, y0, x1, y1, r_start, r_end, steps=None):
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(int(dist * 3), 40)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dabs(p0, p1, p2, r_start, r_end, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---------------------------------------------------------------
# S1: TOP 横 — short horizontal, upper region. Slight up-tilt.
# ---------------------------------------------------------------
top_x0, top_y0 = 105, 90
top_x1, top_y1 = 200, 82
line_dabs(top_x0, top_y0, top_x1, top_y1, r_start=6, r_end=6)
dab(top_x0, top_y0, 7)
dab(top_x1, top_y1, 8)  # small 顿 at right end

# ---------------------------------------------------------------
# S2: 撇折 — starts as short 撇 (from upper-right area going down-left),
#      then folds/turns to become the middle horizontal bar crossing
#      the 竖. Drawn as: bezier 撇 down-left, then straight 横 right.
# ---------------------------------------------------------------
# 撇 portion: from just under the top 横's right shoulder, sweeping
# down-left to the fold point (fold is on the left side, near y=145).
pie_p0 = (190, 100)          # starting near top-right shoulder
pie_p1 = (155, 125)          # control pulls it into a gentle curve
pie_p2 = (100, 148)          # fold point on the left
bezier_dabs(pie_p0, pie_p1, pie_p2, r_start=6, r_end=6)
dab(pie_p0, pie_p0, 6) if False else dab(pie_p0[0], pie_p0[1], 7)
dab(pie_p2[0], pie_p2[1], 7)  # 顿 at the fold

# 横 portion of the 撇折: horizontal bar rightward from the fold,
# crossing the central 竖 and extending past it.
fold_x, fold_y = pie_p2
mid_h_x1, mid_h_y1 = 218, 143   # slight up-tilt
line_dabs(fold_x, fold_y, mid_h_x1, mid_h_y1, r_start=6, r_end=6)
dab(mid_h_x1, mid_h_y1, 7)

# ---------------------------------------------------------------
# S3: BOTTOM 横 — LONGEST stroke. Spans nearly full width.
# ---------------------------------------------------------------
bot_x0, bot_y0 = 40, 215
bot_x1, bot_y1 = 265, 205
line_dabs(bot_x0, bot_y0, bot_x1, bot_y1, r_start=7, r_end=7)
dab(bot_x0, bot_y0, 8)
dab(bot_x1, bot_y1, 9)  # 顿 at right end

# ---------------------------------------------------------------
# S4: Central 竖 with small 提 kick at bottom — through-going axis.
#      Extends from above the top 横 (y=60) down through the middle
#      cross and past the bottom 横, ending with a tiny up-right 提.
# ---------------------------------------------------------------
v_x0, v_y0 = 152, 60
v_x1, v_y1 = 152, 245
line_dabs(v_x0, v_y0, v_x1, v_y1, r_start=6, r_end=6)
dab(v_x0, v_y0, 8)  # 顿 at top

# small 提 kick at the bottom — angles up-right briefly
ti_p0 = (152, 245)
ti_p1 = (168, 240)
ti_p2 = (180, 232)
bezier_dabs(ti_p0, ti_p1, ti_p2, r_start=6, r_end=3)

out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_089_车__retry_2/01_车.png"
img.save(out)
print("wrote", out)
