"""
Render 选 (xuǎn) at 300x300, black ink on white.

Composition: 先 (upper-right) + 辶 (walk radical, wrapping bottom-left).

先 stroke sequence (6): 丿, 一, 竖, 一, 撇, 竖弯钩.
辶 stroke sequence (3): 点 (top), 横折折撇 (wavy left), 平捺 (long right sweep).

Applying TIER-0 F: bezier + variable-width taper + hook UP-and-LEFT.
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

# ===== 先 (upper-right component) =====
# 1. 丿 short pie at top
pie1 = bez((160, 40), (152, 55), (142, 70), (128, 80), n=40)
stroke(pie1, (7, 3))

# 2. 一 upper long horizontal (crosses through 竖)
h1 = bez((105, 90), (150, 88), (200, 88), (245, 92), n=50)
stroke(h1, (6, 6))
dab(245, 92, 4)  # end dab

# 3. 竖 vertical through both horizontals
v1 = bez((175, 55), (175, 100), (175, 130), (175, 155), n=50)
stroke(v1, (6, 6))

# 4. 一 lower horizontal (the 土 bottom)
h2 = bez((115, 155), (160, 153), (205, 153), (250, 157), n=50)
stroke(h2, (6, 6))
dab(250, 157, 4)

# 5. 撇 left leg from bottom horizontal down-left
pie2 = bez((165, 160), (150, 190), (135, 215), (115, 245), n=60)
stroke(pie2, (8, 3))

# 6. 竖弯钩 right leg — down, then arc right, hook up-left
sg_v = bez((205, 160), (205, 200), (207, 225), (218, 240), n=50)
stroke(sg_v, (7, 6))
sg_arc = bez((218, 240), (232, 250), (248, 252), (262, 250), n=40)
stroke(sg_arc, (6, 5))
# hook flick UP-and-LEFT
hook = bez((262, 250), (258, 242), (254, 232), (250, 222), n=25)
stroke(hook, (6, 2))

# ===== 辶 (walk radical, wraps bottom-left) =====
# a. 点 (top-left dot, above the 辶 body)
dot_pts = bez((70, 55), (72, 62), (74, 68), (75, 74), n=15)
stroke(dot_pts, (3, 8))

# b. 横折折撇 — the wavy S shape on the left
# segment 1: small horizontal-ish at top
w1 = bez((60, 100), (72, 100), (85, 102), (95, 108), n=30)
stroke(w1, (5, 5))
dab(95, 108, 4)  # shoulder
# segment 2: down-left diagonal
w2 = bez((95, 108), (85, 125), (72, 140), (60, 155), n=40)
stroke(w2, (5, 5))
dab(60, 155, 4)  # shoulder
# segment 3: down-right diagonal (the 撇 that curves down to meet 平捺)
w3 = bez((60, 155), (75, 180), (90, 205), (95, 235), n=50)
stroke(w3, (6, 4))

# c. 平捺 — long horizontal sweep at the bottom, thickening to the right, with foot
pn_main = bez((85, 240), (140, 260), (200, 265), (255, 260), n=80)
stroke(pn_main, (5, 12))
# foot flare
foot = bez((255, 260), (263, 258), (270, 256), (275, 252), n=20)
stroke(foot, (12, 3))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0465_选/01_选.png")
