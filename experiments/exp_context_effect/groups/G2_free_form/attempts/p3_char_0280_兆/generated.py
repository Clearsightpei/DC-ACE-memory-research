"""兆 — 6 strokes. Left half: short 撇 + 点 + long 竖撇.
Right half: short 撇 + 点 + 竖弯钩 (big sweep ending in UP-LEFT hook flick).
Consulted memory_index TIER-0: not a sibling-risk target. Hook flick
on the 竖弯钩 must go UP-and-LEFT (~-115°), not down/outward.
Rendered with PIL Bezier brush-dabs at 300x300.
Revision 1: bolder strokes, taller left 撇, clearer hook.
"""
from PIL import Image, ImageDraw

W = H = 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

def bezier(p0, p1, p2, p3, n=100):
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u**3*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t**3*p3[0]
        y = u**3*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t**3*p3[1]
        pts.append((x, y))
    return pts

def brush(pts, w_start, w_end):
    n = len(pts)
    for i, (x, y) in enumerate(pts):
        t = i / max(1, n - 1)
        r = (w_start * (1 - t) + w_end * t) / 2
        draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

# --- LEFT HALF ---
# Stroke 1: short 撇 at top-left, slanting steeply down-left
s1 = bezier((115, 70), (100, 90), (85, 110), (68, 135), n=70)
brush(s1, 9, 4)

# Stroke 2: 点 / short right-down stroke (mid-left, connects toward the 竖撇)
s2 = bezier((105, 150), (118, 155), (128, 160), (138, 165), n=40)
brush(s2, 5, 8)

# Stroke 3: long 竖撇 (starts upper-mid-left area, curves down and out to bottom-left)
s3 = bezier((130, 70), (125, 135), (110, 200), (72, 268), n=110)
brush(s3, 12, 5)

# --- RIGHT HALF ---
# Stroke 4: short 撇 upper-right, slanting down-left
s4 = bezier((210, 100), (198, 118), (185, 138), (170, 158), n=60)
brush(s4, 8, 4)

# Stroke 5: 点 lower on right (short down-right stroke)
s5 = bezier((193, 175), (205, 180), (215, 185), (225, 192), n=40)
brush(s5, 5, 8)

# Stroke 6: 竖弯钩 - long vertical curving into a sweep-right, then hook up-left
body = bezier((222, 78), (225, 155), (228, 230), (250, 262), n=110)
brush(body, 11, 9)
# Sweep-right continuation (bottom horizontal-ish extension)
sweep = bezier((250, 262), (263, 268), (272, 264), (270, 250), n=60)
brush(sweep, 9, 8)
# Hook flick UP-and-LEFT (~-115°)
hk = bezier((270, 250), (263, 245), (255, 238), (247, 228), n=40)
brush(hk, 8, 2)

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0280_兆/01_兆.png")
print("saved")
