"""
丸 (wán) — 3 strokes: 撇, 横折弯钩, 点.
Revision 2: fixes for GT-match
  - 撇 starts higher and more to the right so it clearly PIERCES the top
    横 of the 横折弯钩 and continues down-left across the body.
  - 横 top segment starts LEFT of the 撇 pierce point, so the crossing
    is visible (like a hyphen with a diagonal spearing through it).
  - Bottom horizontal tail extends further LEFT, past the 撇's exit point,
    giving the character its characteristic wide "cradle" bottom.
  - 点 placed to the right of 撇 mid-body, below the top 横.
"""

import math
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def taper_line(x0, y0, x1, y1, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier2(P0, P1, P2, r0, r1, steps=400):
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0]
        y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---------- Stroke 1: 撇 (long body-crossing diagonal) ----------
# Starts near top-center-right with a small 顿, curves gently down-left,
# tapers to a sharp tip near lower-left. This is the DOMINANT diagonal.
pie_P0 = (175, 55)   # top press point (upper-middle-right)
pie_P1 = (135, 160)  # control point
pie_P2 = (45, 260)   # bottom-left tip (goes very far left/low)
dab(pie_P0[0], pie_P0[1], 7)  # 顿笔
bezier2(pie_P0, pie_P1, pie_P2, r0=6.0, r1=1.3, steps=500)


# ---------- Stroke 2: 横折弯钩 ----------
# 2a) Top 横: starts LEFT of the 撇's pierce point so the 撇 clearly
#     spears through it. Ends past the right side.
h_x0, h_y0 = 140, 78
h_x1, h_y1 = 240, 82
dab(h_x0, h_y0, 5.5)  # small entry press
taper_line(h_x0, h_y0, h_x1, h_y1, r0=5.5, r1=5.5, steps=250)

# Shoulder 顿 at corner
sh_x, sh_y = h_x1 + 2, h_y1 + 2
dab(sh_x, sh_y, 8)

# 2b) Short 竖 dropping from shoulder — the right wall.
v_x0, v_y0 = sh_x - 2, sh_y
v_x1, v_y1 = 240, 170
taper_line(v_x0, v_y0, v_x1, v_y1, r0=6, r1=6, steps=200)

# 2c) Tangent-continuous quarter-arc: downward → leftward.
#   x(t) = v_x1 - R*(1 - cos(t*pi/2))
#   y(t) = v_y1 + R*sin(t*pi/2)
R = 50
steps_arc = 220
for i in range(steps_arc + 1):
    t = i / steps_arc
    x = v_x1 - R * (1 - math.cos(t * math.pi / 2))
    y = v_y1 + R * math.sin(t * math.pi / 2)
    dab(x, y, 5.8)

arc_end_x = v_x1 - R
arc_end_y = v_y1 + R
# → (190, 220)

# 2d) Long leftward 横 tail continuing from arc endpoint — extends past
# where the 撇 exits (which is around x=45 at y=260), giving that
# characteristic wide "cradle" bottom.
tail_x0, tail_y0 = arc_end_x, arc_end_y
tail_x1, tail_y1 = 80, 235  # long leftward extension
taper_line(tail_x0, tail_y0, tail_x1, tail_y1, r0=5.8, r1=5.2, steps=300)

# 2e) Hook flick — up-and-slightly-left (~-115°), sharp tip.
hook_len = 30
hook_angle = math.radians(-115)
hx1 = tail_x1 + hook_len * math.cos(hook_angle)
hy1 = tail_y1 + hook_len * math.sin(hook_angle)
dab(tail_x1, tail_y1, 6.5)  # small joint press
taper_line(tail_x1, tail_y1, hx1, hy1, r0=5.5, r1=1.0, steps=200)


# ---------- Stroke 3: 点 (dot inside the belly, right of the 撇) ----------
# Small down-right 点; upper-left → lower-right, thin→thick.
dot_x0, dot_y0 = 165, 145
dot_x1, dot_y1 = 190, 172
taper_line(dot_x0, dot_y0, dot_x1, dot_y1, r0=2.5, r1=6.2, steps=100)
dab(dot_x1, dot_y1, 6.2)


out_path = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0044_丸/01_丸.png"
img.save(out_path)
print(f"saved: {out_path}")
