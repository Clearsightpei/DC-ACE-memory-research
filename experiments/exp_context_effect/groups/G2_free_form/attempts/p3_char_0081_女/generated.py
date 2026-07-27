"""
Render 女 (nǚ, woman) — 3 strokes:
  1) 撇点 (piě-diǎn compound): a downward-left 撇 then a 反捺-style
     dot going down-right, sharing a joint at the 撇's tip.
  2) 撇 (long body-crossing diagonal): from upper-right down to
     lower-left, passing THROUGH the future 横 line.
  3) 横 (horizontal crossbar): a slightly rising horizontal across
     the middle, crossing both diagonals.

Canvas 300x300, white background, black ink, PIL.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def bezier(p0, p1, p2, widths, steps=80):
    """Quadratic bezier stroke with taper via dabs.
    widths = (w_start, w_end) radii."""
    w0, w1 = widths
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = w0 * (1 - t) + w1 * t
        dab(x, y, r)


def segment(p0, p1, widths, steps=60):
    """Straight tapered segment."""
    w0, w1 = widths
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] * (1 - t) + p1[0] * t
        y = p0[1] * (1 - t) + p1[1] * t
        r = w0 * (1 - t) + w1 * t
        dab(x, y, r)


# ---------------------------------------------------------------
# Stroke 1: 撇点 — upper-left component.
# 撇: starts a bit right-of-center up top (~155, 55), throws
#   down-left to about (110, 155).
# 点 (反捺): from that tip, sweeps down-right at a steeper angle
#   to about (185, 215), thin→thick terminal press.
# ---------------------------------------------------------------
pie_start = (158, 58)
pie_ctrl = (140, 105)   # gentle bow
pie_tip = (108, 158)

dab(*pie_start, 5)
bezier(pie_start, pie_ctrl, pie_tip, widths=(5.0, 2.2), steps=80)

# joint dab
dab(*pie_tip, 4.0)

# 点 (反捺): thin at joint, thick terminal press, steeper down-right
dian_end = (188, 218)
dian_ctrl = (140, 178)
bezier(pie_tip, dian_ctrl, dian_end, widths=(2.5, 6.0), steps=70)
# broad terminal press
dab(*dian_end, 6.0)

# ---------------------------------------------------------------
# Stroke 2: long 撇 — body-crossing diagonal.
# Starts higher and more toward top-center (~205, 75), sweeps
# down-left through the whole body to a low-left tip (~50, 275).
# Gentle rightward bow.
# ---------------------------------------------------------------
pie2_start = (210, 75)
pie2_ctrl = (155, 175)
pie2_tip = (48, 278)

dab(*pie2_start, 5.5)
bezier(pie2_start, pie2_ctrl, pie2_tip, widths=(5.8, 2.0), steps=110)

# ---------------------------------------------------------------
# Stroke 3: 横 crossbar — slight rise from left to right, crossing
# both diagonals near their intersection point.
# ---------------------------------------------------------------
heng_start = (30, 200)
heng_end = (280, 188)

dab(*heng_start, 4.5)
segment(heng_start, heng_end, widths=(4.2, 4.2), steps=130)
# terminal 顿 press
dab(*heng_end, 5.5)


out_path = (
    "/Users/peilinwu/Documents/AI memory research/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/"
    "p3_char_0081_女/01_女.png"
)
img.save(out_path)
print(f"wrote {out_path}")
