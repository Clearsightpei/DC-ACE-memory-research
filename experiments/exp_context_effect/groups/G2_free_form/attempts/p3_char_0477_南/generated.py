"""
Render 南 (nan2) at 300x300, black ink on white.

Structural read from GT (9 strokes):
  Top cross 十:
    1. short 横 near the very top
    2. short 竖 crossing it and continuing slightly down (forms 十)
  Body frame 冂 (open at bottom):
    3. 竖 — long left vertical (frame's left wall)
    4. 横折钩 — top of frame goes right then folds sharply down as
       the right wall; terminal hook flicks UP-and-LEFT into the body
  Inner 干-like fill:
    5. 一 — inner top horizontal (short, spans inside of frame near top)
    6. 一 — inner middle horizontal (a bit shorter, mid-height)
    7. 丨 — inner center vertical, drops from the top-inner-一 down
       past the middle-一 toward the bottom of the frame
    (南 total: 9 strokes; the 干 inside gives 5-6-7 = three strokes;
     top 十 = two strokes; frame 冂 = two strokes = 2+2+3 = 7. Two more
     small horizontals inside as 丷 sidebars — total 9)

Applies TIER-0 F: teardrop tapers, bezier for curves, shoulder dab at
折 corner, hook flicks UP-LEFT.
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

# =========================================================
# Stroke 1: top 横 (short horizontal near the top)
# =========================================================
h_top = bez((120, 35), (145, 33), (175, 33), (200, 38), n=40)
stroke(h_top, (6, 7))

# =========================================================
# Stroke 2: top 竖 (short vertical crossing the 横 → 十)
# starts a bit above the 横, ends around y ~ 78 (short stub)
# =========================================================
v_top = bez((162, 20), (162, 40), (162, 60), (162, 80), n=40)
stroke(v_top, (7, 6))

# =========================================================
# Stroke 3: left 竖 (long left wall of 冂 frame)
# starts around y=75, drops to the bottom
# =========================================================
v_left = bez((60, 78), (60, 145), (60, 215), (58, 278), n=60)
stroke(v_left, (9, 7))

# =========================================================
# Stroke 4: 横折钩 (top+right wall of 冂 with hook)
# horizontal segment across the top, then folds down as right wall,
# terminal hook flicks UP-and-LEFT
# =========================================================
# horizontal part (top of frame)
frame_top = bez((60, 80), (110, 76), (180, 76), (240, 82), n=60)
stroke(frame_top, (8, 8))
# shoulder dab at the 折 corner
dab(240, 82, 6)
# vertical drop (right wall)
frame_right = bez((240, 82), (240, 150), (240, 215), (238, 275), n=60)
stroke(frame_right, (8, 7))
# hook flick UP-and-LEFT into the body
hook = bez((238, 275), (232, 271), (224, 265), (216, 258), n=25)
stroke(hook, (7, 3))

# =========================================================
# Stroke 5: inner top 横 (inside frame near top)
# =========================================================
inner_top = bez((90, 115), (135, 113), (185, 113), (215, 117), n=40)
stroke(inner_top, (6, 6))

# =========================================================
# Stroke 6: inner middle 横
# =========================================================
inner_mid = bez((90, 195), (135, 193), (185, 193), (215, 197), n=40)
stroke(inner_mid, (6, 6))

# =========================================================
# Stroke 7: inner 丨 (short vertical stub, top-inner going down through mid)
# In 南 the inner 干 has: short-top-horizontal-dab + a vertical
# We'll draw the vertical from mid area
# =========================================================
inner_vert = bez((150, 118), (150, 165), (150, 210), (150, 250), n=60)
stroke(inner_vert, (7, 7))

# =========================================================
# Stroke 8: left inner short 丨 (the small vertical / dot 丷 left)
# small tick coming down from inner top
# =========================================================
left_tick = bez((115, 130), (113, 145), (112, 160), (110, 178), n=30)
stroke(left_tick, (5, 3))

# =========================================================
# Stroke 9: right inner short 丨 (the small vertical / dot 丷 right)
# =========================================================
right_tick = bez((190, 130), (192, 145), (194, 160), (196, 178), n=30)
stroke(right_tick, (5, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0477_南/01_南.png")
print("saved 南")
