"""犬 (dog) radical — 4 strokes: 横 + 撇 + 捺 + 点.

犬 = 大 with an extra 点 in the upper-right corner.

Revision 1 notes:
- Made 横 slightly thinner (r=4) and shortened its dominant appearance
  by removing over-heavy end presses.
- Moved 撇 start closer to the 横 (small upstroke above at ~y=95), and
  shifted its crossing point slightly left so it crosses the 横 near
  the middle-left.
- Reduced 捺 terminal foot from r=12 balloon to a moderate press r=8,
  and started the 捺 higher (from just above the crossing).
- 点 tucked slightly closer to the 横's right endpoint.
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def uniform_line(p0, p1, r, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        dab(x, y, r)


def bezier(p0, p1, p2, r_start, r_end, steps=500, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# ------------------------------------------------------------------
# Stroke 1: 横 (horizontal top bar) — thinner, subtle end presses
# ------------------------------------------------------------------
h_start = (55, 118)
h_end = (225, 112)  # slight upward tilt
uniform_line(h_start, h_end, r=4)
dab(*h_start, 6)  # subtle 顿 press left
dab(*h_end, 6)    # subtle 顿 press right


# ------------------------------------------------------------------
# Stroke 2: 撇 (throw-away, upper-right → lower-left)
# Starts near the 横 (small entry above), crosses through, sweeps
# down-and-left to the lower-left. Gentle rightward bow.
# ------------------------------------------------------------------
pie_p0 = (140, 92)     # just above the 横
pie_p2 = (55, 260)     # tip at lower-left
pie_ctrl = (110, 165)  # bow: control pulled toward the interior (right)
bezier(pie_p0, pie_ctrl, pie_p2, r_start=8, r_end=1.3, steps=500, ease=1.3)
dab(*pie_p0, 9)  # small 顿 press at start


# ------------------------------------------------------------------
# Stroke 3: 捺 (press-down, upper-left → lower-right)
# Starts near the crossing on/just below the 横; thin→thick;
# broad flat foot (moderate — not a balloon).
# ------------------------------------------------------------------
na_p0 = (135, 115)    # near the crossing
na_p2 = (250, 250)    # lower-right
na_ctrl = (175, 165)  # subtle bow — belly on lower-left
bezier(na_p0, na_ctrl, na_p2, r_start=2.0, r_end=9, steps=500, ease=1.5)
# moderate terminal foot press (not a big ball)
dab(250, 250, 9)
# small horizontal extension to give a "flat foot" impression
uniform_line((246, 249), (263, 246), r=6, steps=150)


# ------------------------------------------------------------------
# Stroke 4: 点 (dot in upper-right)
# ------------------------------------------------------------------
def dot(p0, p1, r0=2, r1=7, steps=200):
    for i in range(steps + 1):
        t = i / steps
        tt = t ** 1.4
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r0 + (r1 - r0) * tt
        dab(x, y, r)
    dab(*p1, r1 + 1)


dot((225, 80), (252, 105), r0=2, r1=7)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_113_犬/01_犬.png"
)
