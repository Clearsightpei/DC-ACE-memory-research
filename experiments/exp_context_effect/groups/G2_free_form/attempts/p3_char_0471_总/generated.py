"""
Render 总 (zǒng) at 300x300, black ink on white. 9 strokes.

Structural read from GT:
  Top:    丷 — left 点 (slants down-left), right 点 (slants down-right or short flick).
  Middle: 口 — small squarish box (3 strokes: 竖 left, 横折 top+right, 横 bottom).
  Bottom: 心 — 4 strokes: left 点, 卧钩 (bowl with UP-LEFT hook), middle 点, right 点.

Applying the calligraphic-weight 4-move (TIER-0 F):
  1. Teardrop taper on all 点/撇.
  2. Shoulder dab at 口's 横折 corner.
  3. Bezier for the 卧钩 sweeping arc.
  4. Hook flicks UP-and-LEFT (卧钩 ~-145°).

Revision 1: shrunk 口 (was too wide), pulled top dots closer, deepened
心 bowl curve, made hook flick clearer.
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

# --- 丷 top (two dots) ---
# left 点: short flick from upper-right down-left, teardrop thick→thin
left_pt = bez((140, 50), (128, 62), (118, 75), (108, 88), n=40)
stroke(left_pt, (9, 3))

# right 点: short flick from upper-left down-right (mirror), teardrop thin→thick
right_pt = bez((175, 50), (183, 62), (189, 75), (195, 88), n=40)
stroke(right_pt, (3, 8))

# --- 口 middle box (smaller, more square, centered) ---
# 竖 (left vertical)
zuo = bez((115, 112), (115, 130), (115, 150), (115, 170), n=40)
stroke(zuo, (6, 6))

# 横折 (top horizontal into right vertical)
top_h = bez((115, 112), (140, 110), (165, 110), (188, 112), n=40)
stroke(top_h, (6, 6))
# shoulder dab at the 折 corner
dab(188, 112, 4.5)
you = bez((188, 112), (188, 130), (188, 150), (188, 170), n=40)
stroke(you, (6, 6))

# 横 (bottom of 口)
bot_h = bez((115, 170), (140, 170), (165, 170), (188, 170), n=40)
stroke(bot_h, (6, 6))

# --- 心 bottom (heart) ---
# left 点 (outer left of the bowl, slants down-left with teardrop)
h_left = bez((72, 208), (68, 222), (65, 235), (60, 248), n=30)
stroke(h_left, (4, 8))

# 卧钩 (lying-hook bowl): starts from upper-left, sweeps down and around to the
# right, then flicks UP-and-LEFT at the terminal (~-145°).
wo_gou = bez((85, 215), (100, 285), (185, 290), (245, 240), n=90)
stroke(wo_gou, (7, 6))
# hook flick UP-and-LEFT from the arc's terminal
hook = bez((245, 240), (236, 232), (225, 222), (212, 212), n=30)
stroke(hook, (7, 3))

# middle 点 (inside the bowl, small teardrop pointing down-right slightly)
mid_pt = bez((150, 220), (152, 232), (154, 244), (156, 254), n=25)
stroke(mid_pt, (3, 7))

# right 点 (outer right of bowl, slants down-right)
right_dot = bez((198, 205), (206, 215), (213, 226), (220, 238), n=30)
stroke(right_dot, (3, 8))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0471_总/01_总.png")
