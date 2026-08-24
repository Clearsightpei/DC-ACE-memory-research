"""
Render 亳 (bo2) at 300x300, black ink on white.

Structural read from GT (top-to-bottom):
  1. 亠 top:  dot + long horizontal
  2. 口:      small mouth box (3 strokes)
  3. 冖:      long horizontal cover below 口
  4. 乇 bot:  撇 slash + 短横 + 竖弯钩 (vertical, arc right, hook UP-LEFT)

4-move applied:
  - teardrop taper on all 撇/点/捺
  - shoulder dab at every 折
  - bezier for curves
  - hook flick UP-and-LEFT into the character body
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


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# === 亠 top ===
# top dot (点) — teardrop tapered
dot_top = bez((148, 22), (152, 28), (155, 34), (158, 42), n=25)
stroke(dot_top, (3, 9))

# long top horizontal
h_top = bez((60, 60), (110, 58), (180, 58), (235, 62), n=60)
stroke(h_top, (6, 7))

# === 口 (small mouth) ===
# left 竖
box_L = bez((110, 82), (110, 95), (110, 110), (110, 122), n=30)
stroke(box_L, (6, 6))
# top+right (横折) — one path with shoulder dab
box_top = bez((108, 78), (140, 76), (170, 76), (192, 78), n=40)
stroke(box_top, (6, 6))
dab(192, 80, 4.5)  # shoulder dab at 折
box_R = bez((192, 82), (192, 95), (192, 108), (192, 120), n=30)
stroke(box_R, (6, 6))
# bottom 横 of 口
box_bot = bez((108, 122), (140, 121), (170, 121), (194, 123), n=40)
stroke(box_bot, (5, 5))

# === 冖 wide horizontal below 口 ===
h_mid = bez((55, 148), (120, 145), (185, 145), (240, 150), n=60)
stroke(h_mid, (6, 7))

# === 乇 bottom ===
# 撇 slash — starts upper-right of the 冖 area, sweeps to lower-left
pie = bez((178, 158), (155, 178), (125, 195), (85, 218), n=70)
stroke(pie, (10, 4))

# 短横 crossing the 撇
h_short = bez((100, 200), (140, 198), (185, 198), (218, 202), n=45)
stroke(h_short, (6, 6))

# 竖弯钩 — vertical from top-right of the 短横, curves right at bottom, hooks UP-LEFT
# vertical segment
v_seg = bez((178, 202), (178, 230), (178, 250), (180, 262), n=40)
stroke(v_seg, (7, 7))
# arc segment (bends right)
arc = bez((180, 262), (185, 272), (198, 278), (220, 278), n=40)
stroke(arc, (7, 6))
dab(220, 278, 4.5)  # dab at arc end before hook
# hook flick UP-and-LEFT
hook = bez((220, 278), (219, 270), (215, 260), (210, 250), n=25)
stroke(hook, (6, 2))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0532_亳/01_亳.png")
