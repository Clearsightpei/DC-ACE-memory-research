"""
p3_char_0555_般 — 般 (bān)
Compound: 舟 (left) + 殳 (right).

# SIGNATURE CHECK: neither component in the strict sibling table,
# but 殳 top = 几-like arch; make sure 几's right leg is 竖弯钩-ish
# hooking UP-LEFT into body, not straight down; 又 below = 横撇 + 捺
# with S-curve. Apply the 4-move recipe (taper, shoulder dab, bez,
# hook flick UP-LEFT).
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def bez(p0, p1, p2, p3, n=60):
    out = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        out.append((x, y))
    return out


def stroke(pts, widths=(6, 6)):
    """Draw variable-width stroke by dabbing ellipses densely along polyline."""
    n = len(pts)
    if n < 2:
        return
    w0, w1 = widths
    # densify: sample every ~1 px along each segment
    dense = []
    total = 0.0
    seg_lens = []
    for i in range(n - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        L = math.hypot(x1 - x0, y1 - y0)
        seg_lens.append(L)
        total += L
    if total == 0:
        return
    acc = 0.0
    for i in range(n - 1):
        x0, y0 = pts[i]
        x1, y1 = pts[i + 1]
        L = seg_lens[i]
        steps = max(2, int(L) + 1)
        for s in range(steps):
            u = s / steps
            x = x0 + (x1 - x0) * u
            y = y0 + (y1 - y0) * u
            t = (acc + u * L) / total
            r = (w0 * (1 - t) + w1 * t) / 2
            d.ellipse((x - r, y - r, x + r, y + r), fill="black")
        acc += L
    # end point
    x1, y1 = pts[-1]
    r = w1 / 2
    d.ellipse((x1 - r, y1 - r, x1 + r, y1 + r), fill="black")


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# =============== LEFT: 舟 ===============
# stroke 1: 撇 (top-left diagonal) — from top-right of 舟 to lower-left
p_pie = bez((85, 55), (75, 80), (60, 105), (45, 140))
stroke(p_pie, widths=(9, 3))

# stroke 2: 竖 (vertical left side of the boat body)
stroke([(60, 105), (60, 115), (60, 130), (60, 150), (60, 175), (60, 200)], widths=(6, 6))
dab(60, 105, 4)  # shoulder dab

# stroke 3: 横折钩 (top-right corner: goes right then down with hook UP-LEFT)
# horizontal segment
stroke([(60, 105), (75, 103), (95, 101), (115, 100)], widths=(6, 6))
# shoulder dab at corner
dab(115, 100, 5)
# vertical segment
stroke([(115, 100), (117, 130), (119, 160), (120, 195)], widths=(6, 6))
# hook flick UP-LEFT
hook = bez((120, 195), (115, 200), (105, 200), (95, 190))
stroke(hook, widths=(6, 3))

# stroke 4: 点 (dot inside upper) — small teardrop
dot = bez((78, 135), (85, 140), (92, 145), (95, 150))
stroke(dot, widths=(3, 7))

# stroke 5: 横 (middle horizontal crossing the boat body)
stroke([(52, 155), (75, 154), (100, 153), (125, 152)], widths=(6, 6))

# stroke 6: 横 (lower horizontal, bottom of boat)
stroke([(50, 200), (75, 198), (100, 196), (125, 195)], widths=(7, 6))


# =============== RIGHT: 殳 ===============
# top part: 几-like (short 撇 + 横折弯钩)
# stroke 7: 撇 (top-left short pie of 几)
p2 = bez((175, 60), (170, 75), (163, 90), (155, 105))
stroke(p2, widths=(8, 3))

# stroke 8: 横折弯钩 — horizontal, then arc down and hook UP-LEFT
# horizontal top
stroke([(175, 60), (200, 58), (225, 56), (250, 55)], widths=(6, 6))
dab(250, 55, 5)
# vertical/arc down
stroke([(250, 55), (252, 75), (253, 95), (250, 115)], widths=(6, 6))
# sweeping arc to bottom-right then hook
arc = bez((250, 115), (245, 130), (240, 138), (225, 140))
stroke(arc, widths=(6, 5))
# hook flick UP-LEFT
hk2 = bez((225, 140), (222, 135), (218, 130), (212, 128))
stroke(hk2, widths=(5, 2))

# bottom part: 又 (横撇 + 捺)
# stroke 9: 横撇 — short horizontal then diagonal pie down-left
# horizontal
stroke([(170, 160), (185, 158), (200, 156), (215, 155)], widths=(6, 6))
dab(215, 155, 5)
# pie down-left
pie3 = bez((215, 155), (200, 190), (180, 220), (155, 250))
stroke(pie3, widths=(8, 3))

# stroke 10: 捺 (S-curve down-right)
na = bez((190, 175), (210, 210), (235, 235), (270, 255))
stroke(na, widths=(3, 12))
# flat foot flare
stroke([(265, 253), (270, 255), (275, 254)], widths=(10, 3))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0555_般/01_般.png")
print("saved")
