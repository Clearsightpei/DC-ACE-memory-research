"""
Render 乘 (chéng) at 300x300, black ink on white. Revision 2.

Structural read from GT:
  Top: short 撇 flick top-center + horizontal + tiny hook piece top-right
  Middle-upper: main long horizontal
  Middle: 北-like body — two short horizontals on left, matching stub + 竖弯钩 on right, central vertical stem
  Bottom: 撇 sweeping to bottom-left, 捺 sweeping to bottom-right

Applies 4-move: tapered strokes, Bezier curves, UP-LEFT hook flicks,
shoulder dabs at 折 joints. Components touch.
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

# --- 1) top 撇 (short) coming down-left from apex ---
pie_top = bez((155, 40), (148, 52), (138, 60), (125, 68), n=40)
stroke(pie_top, (4, 8))

# --- 2) top horizontal (short, top-right) ---
top_horiz = bez((150, 68), (180, 65), (205, 65), (225, 68), n=40)
stroke(top_horiz, (6, 6))
# shoulder dab at corner
dab(225, 70, 4)

# --- 3) short vertical + hook flick at top-right (like 折钩) ---
top_hook_v = bez((228, 68), (230, 82), (232, 95), (230, 105), n=30)
stroke(top_hook_v, (6, 5))
# flick UP-LEFT
top_hook_flick = bez((230, 105), (224, 100), (218, 96), (212, 95), n=20)
stroke(top_hook_flick, (5, 2))

# --- 4) main long horizontal across upper-middle ---
main_h = bez((50, 128), (110, 125), (200, 125), (255, 130), n=60)
stroke(main_h, (6, 7))

# --- 5) two short horizontals on left (北 left half top row) ---
h_left1 = bez((65, 158), (95, 156), (120, 156), (140, 158), n=30)
stroke(h_left1, (5, 5))
h_left2 = bez((65, 188), (95, 186), (120, 186), (140, 188), n=30)
stroke(h_left2, (5, 5))

# --- 6) matching short horizontals on right (北 right half top row) ---
h_right1 = bez((165, 158), (190, 156), (215, 156), (240, 160), n=30)
stroke(h_right1, (5, 5))

# --- 7) center vertical (long descending stem from top) ---
center_v = bez((150, 70), (150, 130), (150, 195), (150, 250), n=60)
stroke(center_v, (7, 7))

# --- 8) right side: short vertical + 竖弯钩 wrapping ---
right_v = bez((215, 165), (218, 195), (220, 220), (218, 240), n=50)
stroke(right_v, (6, 6))
# curve back leftward + up-left hook
right_curve = bez((218, 240), (205, 252), (188, 258), (172, 258), n=40)
stroke(right_curve, (6, 6))
right_flick = bez((172, 258), (170, 252), (168, 246), (166, 240), n=20)
stroke(right_flick, (6, 2))

# --- 9) 撇 bottom-left: long sweep from mid-center down to bottom-left ---
pie_bot = bez((150, 145), (120, 190), (85, 230), (40, 270), n=80)
stroke(pie_bot, (9, 3))

# --- 10) 捺 bottom-right: short S-curve to bottom-right ---
na_bot = bez((150, 195), (175, 220), (200, 245), (230, 265), n=60)
stroke(na_bot, (4, 11))
# foot flare at end
foot = bez((230, 265), (238, 266), (245, 268), (250, 268), n=20)
stroke(foot, (11, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0514_乘/01_乘.png")
