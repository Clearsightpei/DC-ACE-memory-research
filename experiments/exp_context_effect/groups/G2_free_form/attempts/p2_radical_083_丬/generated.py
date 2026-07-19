"""
Render 丬 (radical 083, 3画) on 300x300 white canvas, black ink, PIL brush-dabs.

丬 = 点 (upper-left) + 提 (mid-left) + 竖 (tall right vertical).

Revision 1 notes:
- First attempt made stroke 1 look too much like another 提 (parallel to
  stroke 2). Fix: stroke 1 is a downward-throwing 撇/点 — top-right dab
  (thick) throwing DOWN-and-LEFT with a stronger curve, so its
  orientation clearly contrasts with the rising 提 below it.
- First attempt gave the top of the 竖 a hard rightward cap that read
  as a 横折 shoulder. GT shows a plain 竖 (no shoulder). Fix: remove
  the horizontal top-cap, keep the 竖 straight.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(cx, cy, r):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")


def line_taper(x0, y0, x1, y1, r0, r1, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=300, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
        y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)


# --- Stroke 1: 点/短撇 (downward-throwing curve, upper-left) ---
# Start upper-right (thick 顿), throw down-and-left with pronounced
# rightward-bowing Bezier so it clearly contrasts with the 提 below.
p0 = (150, 82)     # upper-right start
p1 = (135, 108)    # control pulled to the interior/right
p2 = (85, 138)     # lower-left tip
dab(p0[0], p0[1], 8)  # 顿 press at start
bezier_taper(p0, p1, p2, r0=7, r1=1.2, steps=280, ease=1.3)

# --- Stroke 2: 提 (rising stroke, lower-left) ---
# Lower-left (thick 顿) → upper-right (sharp thin tip).
q0 = (78, 190)
q1 = (150, 158)
dab(q0[0], q0[1], 7)  # 顿 press at start
line_taper(q0[0], q0[1], q1[0], q1[1], r0=6.5, r1=1.2, steps=260)

# --- Stroke 3: 竖 (tall clean vertical on the right, no top cap) ---
# Plain 竖: uniform width top to bottom, small 顿 press at both ends.
x_shu = 205
y_top = 68
y_bot = 268
dab(x_shu, y_top, 7)   # top 顿
line_taper(x_shu, y_top, x_shu, y_bot, r0=5.5, r1=5.5, steps=400)
dab(x_shu, y_bot, 6.5)  # small terminal press

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_083_丬/01_丬.png"
)
print("saved 01_丬.png (revision 1)")
