"""
Render 热 (re4) at 300x300, black ink on white.

Structural read from GT:
  Top-left  (扌): 横 + 竖钩(hook UP-LEFT) + 提
  Top-right (丸): 丿(sweeping 撇) + 横斜钩(diagonal hook, up-left flick) + 丶(dot)
  Bottom    (灬): four dots along the base, left one flicks down-left,
                  right three flick down-right.

Applies TIER-0 F: 4-move (taper, shoulder dab, bezier, correct hook).
Components must touch (TIER-0 H): 扌 and 丸 overlap along the vertical
midline; the 灬 base sits directly under the top with a small gap.
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

# ============= TOP-LEFT: 扌 =============
# 横 (short horizontal, slightly rising)
h1 = bez((30, 95), (55, 92), (85, 91), (115, 90), n=40)
stroke(h1, (5, 6))

# 竖钩: vertical from (75, 55) down to (75, 175), then hook UP-LEFT
sg = bez((75, 55), (75, 100), (75, 145), (75, 178), n=60)
stroke(sg, (7, 7))
dab(75, 178, 4.5)  # shoulder dab before hook
hook = bez((75, 178), (70, 174), (63, 170), (55, 165), n=25)
stroke(hook, (7, 3))

# 提 (rising stroke, from lower-left to upper-right)
ti = bez((40, 165), (65, 158), (90, 150), (120, 140), n=40)
stroke(ti, (8, 3))

# ============= TOP-RIGHT: 丸 =============
# 丿 (long 撇 sweep, starts upper-right, curves down-left)
pie = bez((205, 50), (185, 90), (165, 130), (135, 178), n=80)
stroke(pie, (10, 4))

# 横斜钩 (horizontal then diagonal curve with hook UP-LEFT):
# top horizontal from (170, 75) to (245, 75), then bends down-right
# then curves back with a hook flicking up-left
h_top = bez((170, 75), (195, 74), (225, 74), (248, 75), n=40)
stroke(h_top, (5, 6))
dab(248, 75, 4.5)  # shoulder dab at fold

# diagonal descending arc (斜钩-like) from fold down-right then back
arc = bez((248, 75), (250, 115), (240, 155), (215, 180), n=70)
stroke(arc, (7, 6))
dab(215, 180, 4.5)
# hook UP-and-LEFT
hook2 = bez((215, 180), (210, 173), (205, 165), (198, 158), n=25)
stroke(hook2, (7, 3))

# 丶 (dot inside 丸, upper-center-right area)
dot_pts = bez((175, 115), (180, 122), (184, 128), (188, 133), n=15)
stroke(dot_pts, (4, 9))

# ============= BOTTOM: 灬 =============
# Four dots along y ~ 225-260
# leftmost: flicks DOWN-LEFT
d1 = bez((70, 215), (65, 230), (60, 245), (55, 258), n=25)
stroke(d1, (4, 9))

# second: flicks DOWN-RIGHT
d2 = bez((115, 215), (120, 230), (124, 245), (128, 258), n=25)
stroke(d2, (4, 9))

# third: flicks DOWN-RIGHT
d3 = bez((170, 215), (175, 230), (179, 245), (183, 258), n=25)
stroke(d3, (4, 9))

# rightmost: flicks DOWN-RIGHT
d4 = bez((225, 215), (232, 230), (238, 245), (245, 258), n=25)
stroke(d4, (4, 9))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0529_热/01_热.png")
