"""
厄 (4-stroke radical) — PIL brush-dab render, 300x300 white canvas, black ink.

Decomposition:
  Stroke 1: 横 (top of 厂), left→right across upper area
  Stroke 2: 撇 (left leg of 厂), from left end of top 横, down-and-slightly-left
            with a gentle bow (Bezier). Shares corner with stroke 1.
  Stroke 3+4: 㔾 inside — 横折 + 竖弯钩 rendered as a single compound stroke:
            短 横 rightward → 折 shoulder → 竖 downward → 弯 smooth arc into
            rightward 横 → small up-left hook (竖弯钩 flavor)

References (from drawer_memory.md):
  - Bootstrap principle 2: shared corners for 厂-family — no inset
  - Principle 5: draw the hook as explicit final beat
  - KEY PRIMITIVE: tangent-continuous vertical→horizontal arc
  - 横折 shoulder dab; 弯 uses smooth arc (no shoulder dab)
"""

import math
from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_taper(p0, p1, r_start, r_end, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, r_start, r_end, steps=400):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * x1 + t * t * x2
        y = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * y1 + t * t * y2
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


# ---------- Stroke 1: 横 (top of 厂) ----------
# Slight up-tilt left→right; starts with a 顿-dab and ends at the shared corner
H1_LEFT = (78, 90)
H1_RIGHT = (218, 82)  # this is the shared corner for the 撇
dab(H1_LEFT[0], H1_LEFT[1], 7)  # 顿笔 start press
line_taper(H1_LEFT, H1_RIGHT, 5.0, 5.0, steps=350)
dab(H1_RIGHT[0], H1_RIGHT[1], 6)  # small terminal press

# ---------- Stroke 2: 撇 (left leg of 厂) ----------
# Starts AT the left end of the 横 (shared corner — bootstrap principle 2)
# Long bowed 撇 going down-and-slightly-left; thick→thin taper.
PIE_START = H1_LEFT  # share the corner pixel exactly
PIE_CTRL = (68, 190)  # bow slightly leftward
PIE_END = (55, 268)
dab(PIE_START[0], PIE_START[1], 8)  # 顿-dab at the shared corner
bezier_taper(PIE_START, PIE_CTRL, PIE_END, 9.0, 1.6, steps=500)

# ---------- Stroke 3+4: 㔾 (inside) ----------
# Structure: 横折 + 竖弯钩 combined; must fill vertical interior of 厂.
# beat A: 横 rightward from (118, 108) to (218, 100) — inner top slightly below outer 横
# shoulder dab at corner
# beat B: 竖 downward — LONG, descends to near the bottom of the character body
# beat C: smooth quarter-arc sweeping into rightward horizontal, wider R
# beat D: hook flick up-and-slightly-left from arc terminus (~-115°)

A0 = (118, 108)
A1 = (218, 100)  # shoulder corner (inner)
B1 = (218, 220)  # end of 竖, start of arc — extended much further down

# beat A — 横
dab(A0[0], A0[1], 6)  # start press
line_taper(A0, A1, 4.8, 5.0, steps=250)
# shoulder dab (顿 press at the corner)
dab(A1[0], A1[1], 7.5)

# beat B — 竖 downward
line_taper(A1, B1, 5.0, 5.0, steps=300)

# beat C — smooth tangent-continuous arc (竖 → 横)
# At t=0 tangent is (0,+) matching downward motion; at t=1 tangent is (+,0)
# matching rightward motion.
x0, y0 = B1
R = 30
arc_end_x = x0 + R
arc_end_y = y0 + R
steps_arc = 140
for i in range(steps_arc + 1):
    t = i / steps_arc
    xa = x0 + R * (1 - math.cos(t * math.pi / 2))
    ya = y0 + R * math.sin(t * math.pi / 2)
    dab(xa, ya, 5.0)

# Continue rightward-horizontal a tiny bit past arc endpoint before hook,
# to give the 弯 a proper "sitting" foot.
foot_end = (arc_end_x + 8, arc_end_y)
line_taper((arc_end_x, arc_end_y), foot_end, 5.0, 5.2, steps=60)

# beat D — hook flick up-and-slightly-left (~-115° in image coords)
HOOK_LEN = 24
angle_deg = -115.0
angle_rad = math.radians(angle_deg)
hook_end = (
    foot_end[0] + HOOK_LEN * math.cos(angle_rad),
    foot_end[1] + HOOK_LEN * math.sin(angle_rad),
)
# joining dab at hook base: use segment radius (NOT r+2) per principle-5 corollary
dab(foot_end[0], foot_end[1], 5.0)
line_taper(foot_end, hook_end, 5.0, 1.2, steps=120)

# ---------- save ----------
out_path = (
    "<REPO_ROOT>/experiments/"
    "exp_context_effect/groups/G2_free_form/attempts/p2_radical_092_厄/"
    "01_厄.png"
)
img.save(out_path)
print(f"wrote {out_path}")
