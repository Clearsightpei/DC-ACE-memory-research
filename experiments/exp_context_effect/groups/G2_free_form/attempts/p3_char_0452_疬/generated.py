"""
Render 疬 (li4) at 300x300, black ink on white.

疬 = 疒 (top-left wrap) + 力 (inside bottom-right).

疒 (5 strokes):
  1. 点     — small dot near top-center of the radical
  2. 横     — horizontal below the dot
  3. 撇     — long sweep from upper-right end of 横 down to lower-left
  4. 点     — small dot inside the fork (upper-left area)
  5. 提     — short rising stroke below the inner dot

力 (2 strokes), inside bottom-right of 疒:
  6. 横折钩 — horizontal then bends down, hook UP-LEFT at the base
  7. 撇     — sweeps from top of the 力 down-left

TIER-0 F applied: bez curves + variable widths + hook UP-LEFT.
Revision 1: enlarged inner 点+提 for visibility, tightened top dot,
shifted 力 up/right to match GT proportions.
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

# ============ 疒 radical ============

# 1. Top 点 — small diagonal dot near top-center, thick→thin, thin end pointing down-right
dot_top = bez((118, 42), (126, 50), (133, 58), (140, 66), n=25)
stroke(dot_top, (4, 8))

# 2. 横 — horizontal, starts under the dot, spans right
heng = bez((70, 88), (130, 84), (190, 84), (232, 88), n=60)
stroke(heng, (6, 7))
# Right-end shoulder dab (where 横 turns implicit into radical body)
d.ellipse((225, 82, 241, 97), fill="black")

# 3. Long 撇 — sweeps from top-left area (just under 横's left end) down to lower-left
pie = bez((98, 92), (85, 155), (72, 215), (48, 275), n=90)
stroke(pie, (10, 4))

# 4. Inner 点 — clearly to the right of the 撇, upper-left inside the fork
inner_dot = bez((95, 130), (103, 138), (110, 146), (117, 154), n=25)
stroke(inner_dot, (4, 8))

# 5. Inner 提 — rises from the 撇's midsection into the fork interior
ti = bez((72, 185), (100, 178), (128, 170), (152, 162), n=35)
stroke(ti, (8, 3))

# ============ 力 (inside, bottom-right of the wrap) ============

# 6. 横折钩
# horizontal top
hz = bez((150, 145), (185, 142), (215, 142), (240, 145), n=50)
stroke(hz, (6, 7))
# corner shoulder dab
d.ellipse((232, 138, 248, 154), fill="black")
# vertical/curved down (slight leftward drift like GT)
vert = bez((240, 148), (238, 195), (222, 240), (198, 275), n=60)
stroke(vert, (7, 5))
# hook flick UP-and-LEFT
hook = bez((198, 275), (192, 268), (185, 262), (176, 258), n=20)
stroke(hook, (6, 3))

# 7. 力's 撇 — starts on the top horizontal, sweeps down-left into a curve
pie2 = bez((175, 155), (162, 200), (145, 240), (120, 278), n=70)
stroke(pie2, (9, 3))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0452_疬/01_疬.png")
