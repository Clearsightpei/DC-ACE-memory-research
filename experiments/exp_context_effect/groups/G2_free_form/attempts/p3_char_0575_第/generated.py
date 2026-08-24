"""
Render 第 (di4) at 300x300, black ink on white.  Revision 2.

Structural read:
  第 = 竹字头 (⺮ top) + 弟 body (without the top 丷).
  Bottom body reads as:
    - top 弓-like: 横 + 横折 + 横 stack, roughly rectangular but shorter
    - central 竖 with hook going UP-and-LEFT (rule B)
    - final 撇 diagonal down-right from mid-right
  竹字头: two mirrored (撇 + 短横 + 点) sub-glyphs.

Applies TIER-0 memory:
  - hook flick UP-and-LEFT (rule B) on central 竖钩
  - bezier for curved sweeps (rule F.3)
  - variable-width taper on 撇/点 (rule F.1)
  - shoulder-dab at 折 corners (rule F.2)
  - components touch, no floating gap (rule H)
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

# ============ TOP: 竹字头 (⺮), y=35..95 ============
# Left ⺮
# 撇 (short, curving down-left)
stroke(bez((85, 42), (78, 58), (72, 72), (62, 90), n=40), (7, 2))
# 短横 (small right-ward flick, meeting the 撇 near its top)
stroke(bez((70, 68), (85, 66), (100, 65), (112, 66), n=25), (4, 5))
# 点 (small dot, slanting down-right, under the 横)
stroke(bez((100, 78), (105, 85), (108, 92), (110, 98), n=25), (2, 6))

# Right ⺮
# 撇
stroke(bez((175, 42), (168, 58), (162, 72), (152, 90), n=40), (7, 2))
# 短横
stroke(bez((160, 68), (178, 66), (198, 65), (215, 66), n=25), (4, 5))
# 点
stroke(bez((200, 78), (205, 85), (208, 92), (212, 98), n=25), (2, 6))

# ============ BODY: 弟-like, y=115..270 ============
# Top 横 of the 弓 (upper bar)
stroke(bez((55, 130), (110, 128), (180, 128), (240, 132), n=60), (6, 6))

# Left 撇 curl (like top-left of 弟), goes from top-left down-and-in
stroke(bez((78, 118), (72, 135), (68, 152), (62, 172), n=40), (7, 3))

# Upper 横折 inside body (forms top of inner box)
# 横 across
stroke(bez((80, 168), (130, 167), (175, 167), (215, 168), n=40), (5, 5))
dab(215, 168, 4.0)
# 折 turning down, short
stroke(bez((217, 168), (216, 178), (214, 190), (212, 200), n=25), (5, 5))

# Lower 横 (middle bar)
stroke(bez((80, 202), (130, 201), (170, 201), (210, 202), n=40), (5, 5))

# Bottom wrap: left vertical + bottom 横 with a small hook up at right end
# left vertical
stroke(bez((80, 168), (80, 200), (80, 235), (80, 260), n=40), (5, 5))
dab(80, 168, 4.0)
# bottom 横
stroke(bez((80, 260), (115, 259), (150, 258), (185, 260), n=40), (5, 5))
# right vertical up a bit (like 横折 with rising close)
stroke(bez((185, 260), (185, 245), (185, 230), (185, 220), n=25), (5, 5))

# ============ CENTRAL 竖钩 (through the body, hook UP-LEFT) ============
stroke(bez((140, 108), (142, 165), (144, 220), (146, 270), n=60), (7, 7))
# hook flick UP-and-LEFT
stroke(bez((146, 270), (138, 265), (128, 258), (118, 250), n=25), (7, 3))

# ============ RIGHT 撇 (final diagonal sweep, down-right) ============
stroke(bez((205, 195), (218, 220), (232, 245), (250, 272), n=50), (7, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0575_第/01_第.png")
