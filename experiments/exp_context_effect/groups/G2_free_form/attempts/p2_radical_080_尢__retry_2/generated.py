"""
尢 retry #2.

SIGNATURE CHECK (per sibling_signature_checklist.md):
  target = 尢
  bit    = 一 top + 撇 + 竖弯钩 (3 strokes with LID)
  vs 九  = 九 has NO top 一 lid, only 撇 + 横折弯钩
  flick  = 竖弯钩 terminal UP-and-slightly-LEFT (~-100° to -110°)

Errata + retry_1 review:
  - Retry_1 read OK-ish but 撇 was too straight (no belly) AND extended
    too low-left (to y=268). GT's 撇 has a subtle rightward-bulging
    curve and lands ~y=250. Terminal hook was fine.
  - This retry: (a) restore modest belly on 撇 (belly to the RIGHT,
    opens LEFT), (b) shorten 撇 slightly (end at ~(58,255)),
    (c) keep 一 upper-mid, (d) 竖弯钩 with smoother arc and small
    UP-slightly-LEFT terminal flick.

Structure (image coords, y grows DOWN, canvas 300x300):
  Stroke 1 (一 top lid):
    (82,113) -> (188,108); thin, small end-dots.
  Stroke 2 (撇):
    (145,63) -> (58,255); Bezier control at (100,155) pulling belly
    modestly to RIGHT; thick->thin taper; 顿 press at start.
  Stroke 3 (竖弯钩):
    Beat A: near-vertical from (170,80) to (176,225), very slight
      rightward drift; 顿 top.
    Beat B: quarter-arc R=32 sweeping into rightward run.
      Arc ends at (208, 257). Extend to (232, 258).
    Beat C: hook flick 22px at -105° (UP-and-slightly-LEFT), r 5.0->1.2.
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def bezier_stroke(p0, p1, p2, r_start, r_end, steps=400, ease=1.0):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        tt = t ** ease
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


def line_stroke(p0, p1, r_start, r_end, steps=300):
    for i in range(steps + 1):
        t = i / steps
        x = p0[0] + (p1[0] - p0[0]) * t
        y = p0[1] + (p1[1] - p0[1]) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# --- Stroke 1: 一 (top lid, short, mild upward tilt)
h_p0 = (82, 114)
h_p1 = (188, 108)
dab(h_p0[0], h_p0[1], 5.5)
line_stroke(h_p0, h_p1, r_start=5.0, r_end=4.6, steps=250)
dab(h_p1[0], h_p1[1], 5.8)


# --- Stroke 2: 撇 (long, subtle belly-on-right curve, thick->thin)
p0 = (145, 63)
p2 = (58, 255)
# Straight midpoint would be (101, 159). Pull control RIGHT by ~10 px
# so belly bulges to the right, giving the calligraphic subtle curve.
ctrl = (111, 158)
dab(p0[0], p0[1], 8.0)  # 顿 press at start
bezier_stroke(p0, ctrl, p2, r_start=7.0, r_end=1.2, steps=520, ease=1.15)


# --- Stroke 3: 竖弯钩
# Beat A: near-vertical 竖 with tiny rightward drift
v_p0 = (170, 80)
v_p1 = (176, 225)
dab(v_p0[0], v_p0[1], 6.2)
bezier_stroke(v_p0, (173, 152), v_p1, r_start=5.3, r_end=5.0, steps=300)

# Beat B: tangent-continuous quarter-arc
x0, y0 = v_p1
R = 32
arc_steps = 160
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = x0 + R * (1 - math.cos(t * math.pi / 2))
    y = y0 + R * math.sin(t * math.pi / 2)
    dab(x, y, 4.9)
arc_end = (x0 + R, y0 + R)  # (208, 257)

# Short rightward extension
h2_end = (232, 258)
line_stroke(arc_end, h2_end, r_start=4.9, r_end=4.6, steps=140)

# Beat C: hook flick UP-and-slightly-LEFT at -105°
hook_len = 22
hook_angle_deg = -105
rad = math.radians(hook_angle_deg)
hx = h2_end[0] + hook_len * math.cos(rad)
hy = h2_end[1] + hook_len * math.sin(rad)
dab(h2_end[0], h2_end[1], 4.8)
line_stroke(h2_end, (hx, hy), r_start=4.8, r_end=1.2, steps=180)


out_path = (
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_080_尢__retry_2/01_尢.png"
)
img.save(out_path)
print(f"Saved {out_path}")
