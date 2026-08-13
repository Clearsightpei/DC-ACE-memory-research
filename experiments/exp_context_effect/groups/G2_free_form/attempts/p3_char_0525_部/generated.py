"""
Render 部 (bu4) at 300x300.
Compound left-right: 咅 (left) + 阝 (right ear, 邑).

Left 咅 (x ~ 25-165):
  立 top: 点 + 横(short) + 两点(八) + 横(long base)
  口 bottom: 竖 + 横折 + 横(bottom base)

Right 阝 (x ~ 175-275):
  横撇弯钩 forming double-loop ear-shape
  竖 long descending vertical (extends below main body)

# SIGNATURE CHECK:
# - components must TOUCH (H rule): 咅's right-edge horizontals reach to ~165,
#   right ear starts ~175 with kiss overlap; no big gap.
# - Hook flicks UP-and-LEFT (B rule).
# - Variable width, bezier curves, shoulder dabs at 折 joints (F rule).
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

def shoulder(x, y, r=5):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")

# ============= LEFT: 咅 =============
# --- 立 top ---
# 1. top 点 (short dot, slanting down-right)
top_dot = bez((85, 30), (90, 38), (94, 46), (98, 55), n=30)
stroke(top_dot, (3, 8))

# 2. short 横 (upper horizontal of 立)
h_up = bez((55, 68), (85, 66), (115, 66), (145, 70), n=40)
stroke(h_up, (6, 6))

# 3. 两点 (八-like: left 点 sweeping down-left, right 点 sweeping down-right)
left_pt = bez((78, 82), (72, 90), (66, 98), (58, 108), n=30)
stroke(left_pt, (7, 3))
right_pt = bez((120, 82), (128, 92), (135, 100), (144, 108), n=30)
stroke(right_pt, (3, 7))

# 4. long 横 (base of 立)
h_base = bez((30, 122), (75, 120), (120, 120), (168, 124), n=50)
stroke(h_base, (7, 7))

# --- 口 bottom ---
# left 竖
sh_l = bez((55, 155), (55, 180), (55, 210), (55, 240), n=40)
stroke(sh_l, (6, 6))
# 横折 (top + right vertical)
h_top_kou = bez((55, 155), (90, 153), (125, 153), (150, 158), n=40)
stroke(h_top_kou, (6, 6))
shoulder(150, 158, r=4)
r_v = bez((150, 158), (150, 185), (150, 215), (150, 240), n=40)
stroke(r_v, (6, 6))
# bottom 横
h_bot_kou = bez((55, 240), (90, 238), (125, 238), (150, 240), n=40)
stroke(h_bot_kou, (6, 6))

# ============= RIGHT: 阝 (right ear) =============
# 横撇弯钩 — starts top, goes right, folds down, curves left, forms two lobes ear
# Upper lobe: from apex, right, down, and back-left forming small "P"-like head
ear_top = bez((180, 60), (230, 58), (255, 78), (240, 105), n=60)
stroke(ear_top, (6, 6))
shoulder(240, 105, r=5)
ear_top_close = bez((240, 105), (215, 112), (195, 112), (178, 108), n=40)
stroke(ear_top_close, (6, 5))

# Lower lobe (larger)
ear_bot = bez((178, 108), (220, 108), (255, 130), (240, 165), n=60)
stroke(ear_bot, (6, 6))
shoulder(240, 165, r=5)
ear_bot_close = bez((240, 165), (215, 175), (195, 175), (178, 172), n=40)
stroke(ear_bot_close, (6, 5))

# Long 竖 descending (right ear's tail — extends well below the body)
tail = bez((178, 60), (178, 130), (178, 200), (178, 275), n=80)
stroke(tail, (7, 7))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0525_部/01_部.png")
