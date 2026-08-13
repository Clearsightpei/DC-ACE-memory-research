"""
Render 乾 (qian2) at 300x300, black ink on white.

Structural read from GT:
  Left (龺 component, ~10 strokes): top 十 (short horizontal + short vertical),
    middle 日 box (with mid bar), bottom base with long horizontal and long
    vertical descending through — reads as a stacked stem.
  Right (乞 component, 3 strokes): short 撇 top-right; horizontal 一;
    then 乙 = 横折弯钩 sweeping right, curving down, arcing right, hook
    flicking UP-and-LEFT at the terminal (TIER-0 rule B).

# SIGNATURE CHECK: components 龺 (left) + 乞 (right) MUST TOUCH along
# the vertical midline (H rule pos 650). Draw 乙's opening at x~155
# so it overlaps left component's right edge by ~5 px.
# HOOK: 乙's terminal flicks UP-and-LEFT (~-115°), not down/right.
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

def line(p0, p1, w=6, n=40):
    pts = [(p0[0] + (p1[0]-p0[0])*i/n, p0[1] + (p1[1]-p0[1])*i/n) for i in range(n+1)]
    stroke(pts, w)

# =========================================================
# LEFT COMPONENT — 龺 (stacked stem: 十 + 日 + base 十)
# =========================================================

# --- top 十 ---
# short horizontal (top bar)
line((40, 50), (125, 50), w=6, n=40)
# short vertical descending through it
line((82, 30), (82, 78), w=6, n=30)

# --- middle 日 (box + mid bar) ---
# top of box
line((45, 82), (125, 82), w=6, n=40)
# left vertical
line((48, 82), (48, 150), w=6, n=30)
# right vertical (with slight折 shoulder dab)
d.ellipse((118, 78, 128, 88), fill="black")  # shoulder dab
line((123, 82), (123, 150), w=6, n=30)
# mid bar
line((48, 116), (123, 116), w=5, n=40)
# bottom of box
line((48, 148), (123, 148), w=6, n=40)

# --- bottom base 十 ---
# long horizontal base
line((30, 185), (150, 185), w=7, n=50)
# long vertical descending through
line((85, 152), (85, 275), w=7, n=50)

# =========================================================
# RIGHT COMPONENT — 乞 (3 strokes)
# =========================================================

# --- 撇 (short pie, top-right, slanted down-left) ---
pie = bez((225, 60), (215, 78), (200, 92), (185, 105), n=60)
stroke(pie, (8, 3))

# --- 一 (horizontal), slightly rising ---
line((170, 128), (270, 122), w=7, n=60)

# --- 乙 (横折弯钩) — one flowing shape ---
# top segment going right, small drop
seg1 = bez((170, 158), (200, 155), (235, 155), (258, 162), n=60)
stroke(seg1, (7, 7))
# shoulder dab at the 折 corner
d.ellipse((252, 155, 265, 168), fill="black")
# descending arc curving left as it drops (the belly of 乙)
arc = bez((258, 162), (255, 210), (215, 255), (170, 262), n=80)
stroke(arc, (7, 8))
# bottom sweep right along the base (平弯)
belly = bez((170, 262), (215, 275), (255, 275), (285, 268), n=60)
stroke(belly, (8, 8))
# --- 钩 flick UP-and-LEFT (TIER-0 rule B) ---
hook = bez((285, 268), (278, 258), (270, 250), (262, 240), n=30)
stroke(hook, (8, 3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0576_乾/01_乾.png")
