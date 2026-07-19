"""
Render 气 (radical 111, 4 strokes) at 300x300 PNG, black ink on white.

Structure (from GT observation):
  Stroke 1: 撇 — short, from upper-center throwing down-and-left.
  Stroke 2: 横 — upper horizontal, spanning from left area to right (long).
  Stroke 3: 横 — middle horizontal, shorter and slightly offset.
  Stroke 4: 横折弯钩 — starts as leftmost horizontal at lower-left area,
            corners at 折 shoulder, descends as short 竖, arcs tangent-
            continuously into rightward 横, ends with hook flicking
            up-and-left. (KEY PRIMITIVE — proven on 乙, 乚, 横折弯钩.)

Renderer: PIL brush-dabs.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(x0, y0, x1, y1, r0, r1, steps=None):
    """Straight tapered stroke via brush-dabs."""
    if steps is None:
        steps = max(int(math.hypot(x1 - x0, y1 - y0) * 2.5), 40)
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r0, r1, steps=200):
    """Quadratic Bezier tapered stroke."""
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# -------- Stroke 1: 撇 (short throw, upper-center → lower-left) --------
# Start upper-center around (115, 60), tip around (75, 130).
# Thick→thin taper with small 顿 press at start (r=6, standalone scale).
dab(115, 60, 7)  # 顿 press start
bezier_taper((115, 60), (108, 90), (75, 130), r0=6, r1=1.4)

# -------- Stroke 2: 横 (upper horizontal) --------
# From the 撇's midsection area going right. GT shows it starts just
# right of the 撇's start (~x=125) and extends far right (~x=225).
# Slight upward tilt (3-5°).
line_taper(115, 88, 225, 82, r0=5.5, r1=5.5)
dab(115, 88, 7)   # start 顿
dab(225, 82, 7)   # end 顿

# -------- Stroke 3: 横 (middle horizontal, shorter, offset right) --------
# GT shows this 横 is shorter and sits below the upper one, roughly
# centered right (from ~x=105 to ~x=215), with slight upward tilt.
line_taper(105, 135, 215, 128, r0=5.5, r1=5.5)
dab(105, 135, 7)
dab(215, 128, 7)

# -------- Stroke 4: 横折弯钩 --------
# Complex: starts as bottom-left horizontal, 折 shoulder, short 竖 down,
# tangent-continuous arc into rightward horizontal, hook up-left.
# Anchor positions:
#   H_start = (55, 175), H_end = (140, 168)   [bottom-left 横]
#   after shoulder, 竖 descends to (140, 225)
#   arc R=32, ends at (140+32, 225+32) = (172, 257)
#   rightward 横 to (220, 257)
#   hook flick 34 px @ -115°, up-and-slightly-left

# 4a: bottom-left 横 (opening beat)
line_taper(55, 175, 140, 168, r0=5.5, r1=5.5)
dab(55, 175, 7)   # start 顿

# 4b: shoulder dab at (140, 168)
dab(140, 168, 8)  # r+2 shoulder

# 4c: short 竖 from (140, 168) down to (140, 225)
line_taper(140, 168, 140, 225, r0=6, r1=6)

# 4d: tangent-continuous arc — descending-vertical → rightward-horizontal
# center at (140+32, 225) = (172, 225), R=32
# parametrization: x = x0 + R*(1-cos(t*pi/2)), y = y0 + R*sin(t*pi/2)
x0_arc, y0_arc = 140, 225
R = 32
arc_steps = 80
for i in range(arc_steps + 1):
    t = i / arc_steps
    x = x0_arc + R * (1 - math.cos(t * math.pi / 2))
    y = y0_arc + R * math.sin(t * math.pi / 2)
    dab(x, y, 5.5)
# arc ends at (172, 257)

# 4e: short rightward 横 from (172, 257) to (220, 257)
line_taper(172, 257, 220, 257, r0=5.5, r1=5.5)

# 4f: hook flick — 34 px @ -115° (up-and-slightly-left) from (220, 257)
# joining dab at hook base: EQUAL to segment radius (per hook-flick discipline)
dab(220, 257, 5.5)
hook_len = 34
hook_angle_deg = -115  # image coords: negative = up
ang = math.radians(hook_angle_deg)
hx_end = 220 + hook_len * math.cos(ang)
hy_end = 257 + hook_len * math.sin(ang)
# tapered flick
hs = 40
for i in range(hs + 1):
    t = i / hs
    x = 220 + (hx_end - 220) * t
    y = 257 + (hy_end - 257) * t
    r = 5.5 + (1.0 - 5.5) * t
    dab(x, y, r)

# Save
out_path = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_111_气/01_气.png"
img.save(out_path)
print(f"saved: {out_path}")
