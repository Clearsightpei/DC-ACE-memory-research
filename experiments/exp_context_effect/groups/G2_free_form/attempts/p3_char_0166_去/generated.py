"""
p3_char_0166_去 — 5 strokes total.

Decomposition (top-to-bottom):
  Top: 土 (3 strokes)
    1. 横 short  — upper horizontal (shorter than the middle 横)
    2. 竖         — vertical through center, crosses both 横
    3. 横 long   — middle horizontal, the widest stroke in the char
                    (per form_catalog: 土 → BOTTOM 横 LONGER than top ~1.5×;
                     here the "bottom" of the top-土 is this middle 横)
  Bottom: 厶 (2 strokes)
    4. 撇折      — throws down-left, folds into a short right 横
    5. 点        — teardrop dot to the lower-right

Notes:
  * The middle 横 is the widest stroke in the whole glyph — it visually
    separates the 土 top from the 厶 bottom.
  * The 厶 sits below and slightly right of the 竖's baseline.
  * 竖 does NOT descend into the 厶; it terminates at the middle 横.
  * Standalone char scaling: fill most of a ~250px vertical band,
    top margin ~25 to bottom ~275.

Renderer: PIL brush-dabs (drawer_memory principle).
Canvas: 300x300, white bg, black ink. Image coords (y grows DOWN).
"""

from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(p0, p1, r_start, r_end, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=400):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def teardrop(p0, p1, r_start, r_end, steps=200, ease=1.4):
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ---------- TOP: 土 ----------
# Stroke 1: short 横 (top) — narrow, slight up-tilt.
top_heng_left = (115, 55)
top_heng_right = (185, 50)
line_taper(top_heng_left, top_heng_right, r_start=4.5, r_end=5.5, steps=200)
dab(top_heng_left[0], top_heng_left[1], 5.0)
dab(top_heng_right[0], top_heng_right[1], 6.0)

# Stroke 2: 竖 — vertical from just above top 横 to just above middle 横.
vert_top = (150, 42)
vert_bot = (150, 145)
line_taper(vert_top, vert_bot, r_start=5.0, r_end=5.5, steps=200)
dab(vert_top[0], vert_top[1], 5.5)
dab(vert_bot[0], vert_bot[1], 5.5)

# Stroke 3: long middle 横 — the widest stroke, separates 土 and 厶.
mid_heng_left = (45, 148)
mid_heng_right = (255, 143)
line_taper(mid_heng_left, mid_heng_right, r_start=5.0, r_end=6.0, steps=300)
dab(mid_heng_left[0], mid_heng_left[1], 5.5)
dab(mid_heng_right[0], mid_heng_right[1], 6.5)


# ---------- BOTTOM: 厶 ----------
# Stroke 4: 撇折 — 撇 down-left with gentle bow, folds into short right 横.
# Start upper-right of the 厶 region (below middle 横). Made wider and taller
# to match GT: 撇 throws from ~x=175 down to ~x=100, joint at ~y=255.
pie_p0 = (175, 172)
pie_ctrl = (160, 215)     # control pulled right → belly on the right
pie_p2 = (100, 260)       # lower-left tip (joint) — wider and lower than v1
bezier_stroke(pie_p0, pie_ctrl, pie_p2, r_start=5.5, r_end=1.8, steps=400)

JOINT = pie_p2
dab(JOINT[0], JOINT[1], 6.0)

# short 横 from joint going right with slight up-tilt (the 折 tail)
heng2_end = (185, 253)
line_taper(JOINT, heng2_end, r_start=5.5, r_end=4.5, steps=200)
dab(heng2_end[0], heng2_end[1], 5.0)

# Stroke 5: 点 — teardrop going down-and-right, at lower-right of 厶.
dot_p0 = (185, 250)
dot_p1 = (235, 285)
teardrop(dot_p0, dot_p1, r_start=2.0, r_end=7.0, steps=250, ease=1.3)
dab(dot_p1[0], dot_p1[1], 7.5)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p3_char_0166_去/01_去.png"
)
