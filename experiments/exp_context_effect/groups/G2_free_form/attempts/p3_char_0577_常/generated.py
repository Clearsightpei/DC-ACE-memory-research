"""
Render 常 (cháng) at 300x300, black ink on white.

Structural read from GT:
  ⺌ (top three flicks): center small 竖 + left 点/撇 + right 点
  冖 lid: small left tick + top horizontal with a right-side 折 shoulder
          descending on the right
  Middle body: 口-like small rectangle tucked under the lid
  巾 (bottom): 冂 wrap with center 竖 that extends well below the wrap,
              right side hooking UP-LEFT at the bottom of the 冂

Techniques (per memory_index TIER-0 F):
  - Bezier for every curved sweep
  - stroke(pts, widths=(a,b)) for taper on 撇/点/捺
  - Shoulder dab at every 折 joint
  - Hook flicks UP-and-LEFT
  - Components must TOUCH (rule H)
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

def bez(p0, p1, p2, p3, n=60):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        pts.append((x, y))
    return pts

def stroke(pts, widths):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(n - 1, 1)
        if isinstance(widths, tuple):
            w = widths[0] + (widths[1] - widths[0]) * t
        else:
            w = widths
        r = w / 2
        d.ellipse((x - r, y - r, x + r, y + r), fill="black")

def dab(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# ---------- ⺌ TOP (three flicks) ----------
# left 点 (slants down-left)
left_dot = bez((95, 30), (88, 45), (82, 60), (75, 72), n=30)
stroke(left_dot, (4, 8))

# center small 竖 (short vertical/point)
center = bez((148, 25), (149, 45), (150, 60), (150, 72), n=30)
stroke(center, (7, 5))

# right 点 (slants down-right)
right_dot = bez((205, 30), (212, 45), (218, 58), (225, 70), n=30)
stroke(right_dot, (4, 8))

# ---------- 冖 LID ----------
# tiny left 点 tick above lid start
left_tick = bez((55, 80), (58, 88), (60, 93), (62, 96), n=20)
stroke(left_tick, (5, 3))

# top horizontal
h_top = bez((62, 100), (110, 98), (180, 98), (240, 100), n=60)
stroke(h_top, (6, 6))

# shoulder dab at right 折 joint
dab(240, 100, r=5)

# right side of lid: 折 descending
lid_right = bez((240, 100), (241, 112), (242, 122), (243, 130), n=25)
stroke(lid_right, (6, 5))

# ---------- 口 middle small rectangle ----------
# left vertical
kou_l = bez((110, 118), (110, 132), (110, 145), (110, 155), n=25)
stroke(kou_l, (5, 5))

# top horizontal (already covered by lid, add a slight seg)
kou_t = bez((110, 118), (140, 117), (170, 117), (198, 118), n=30)
stroke(kou_t, (5, 5))
dab(198, 118, r=5)

# right side with 折
kou_r = bez((198, 118), (198, 132), (198, 145), (198, 155), n=25)
stroke(kou_r, (5, 5))

# bottom horizontal
kou_b = bez((110, 155), (140, 156), (170, 156), (198, 155), n=30)
stroke(kou_b, (5, 5))

# ---------- 巾 BOTTOM ----------
# 冂 top horizontal (spans wider than 口, tucking under it)
jin_top = bez((80, 172), (130, 170), (185, 170), (225, 172), n=60)
stroke(jin_top, (6, 6))

# left 竖/撇 of 冂 (slight lean)
jin_left = bez((82, 172), (81, 200), (80, 230), (78, 260), n=50)
stroke(jin_left, (7, 4))

# right side with 折 shoulder then 竖钩
dab(225, 172, r=5)
jin_right = bez((225, 172), (226, 200), (226, 230), (226, 258), n=50)
stroke(jin_right, (7, 7))
# hook UP-and-LEFT
jin_hook = bez((226, 258), (218, 253), (210, 247), (202, 240), n=25)
stroke(jin_hook, (7, 3))

# center 竖 of 巾 — starts inside 口 (touches) and extends far below
center_v = bez((151, 152), (151, 210), (151, 250), (151, 285), n=60)
stroke(center_v, (8, 6))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0577_常/01_常.png")
