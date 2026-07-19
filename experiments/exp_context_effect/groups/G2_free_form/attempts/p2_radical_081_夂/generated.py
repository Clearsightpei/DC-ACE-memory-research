"""
夂 (zhǐ) — 3-stroke radical.

Stroke breakdown (per canonical MMH order):
  1. 撇 (short): top-right → down-left, small pie at top.
  2. 横撇 (heng-pie): short 横 leftward-going-right then bowed 撇 down-left.
     Together with stroke 1, these form the top "hat" and the descending left leg.
     In 夂, stroke 2 is a 横撇 whose 横 sits at the top-right and whose 撇 tail
     runs down-left crossing under stroke 1's tip and continuing to the lower-left.
  3. 捺 (na): starts on the descending leg near mid-height, sweeps down-and-right
     to a broad flat foot in the lower-right quadrant.

Reference: shared_rules v6; drawer_memory principles 5 (hook = signature) and
2 (compound radicals: shared joints). No hook here — 夂 has NO钩, all
terminals are taper tips or broad foot.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)


def dab(x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def line_dab(p0, p1, r_start, r_end, steps=None):
    x0, y0 = p0
    x1, y1 = p1
    dist = math.hypot(x1 - x0, y1 - y0)
    if steps is None:
        steps = max(60, int(dist * 2.5))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dab(p0, p1, p2, r_start, r_end, steps=200, ease=1.0):
    x0, y0 = p0
    xc, yc = p1
    x2, y2 = p2
    for i in range(steps + 1):
        t = i / steps
        tt = t ** ease
        u = 1 - t
        x = u * u * x0 + 2 * u * t * xc + t * t * x2
        y = u * u * y0 + 2 * u * t * yc + t * t * y2
        r = r_start + (r_end - r_start) * tt
        dab(x, y, r)


# Revision 1: GT strokes are LIGHTER and 横 is SHORTER; the top 撇 crosses
# through the 横撇's shoulder area. Reduce all stroke radii ~35% and shorten
# the 横 segment. Keep the 捺 as the dominant sweeping element.

# ---------------- Stroke 1: short 撇 at top ---------------------------------
# Small pie throw from upper-right toward lower-left. Its tail dives across
# the 横 of stroke 2 (crossing signature — see principle 3).
s1_start = (155, 68)
s1_end = (115, 112)
# small 顿笔 at start (standalone-scale: use r=5, not r=7 balloon)
dab(s1_start[0], s1_start[1], 5)
bezier_dab(s1_start, (142, 82), s1_end, r_start=4.5, r_end=1.2, ease=1.3)


# ---------------- Stroke 2: 横撇, the "hat + leg" ---------------------------
# The 横 is SHORT and sits at the top; then the 撇 tail bows down-and-left
# forming the long descending leg. Shoulder shared with the top 撇's
# crossing point.

# 横 segment — short, slight up-tilt
heng_start = (128, 100)
heng_end = (198, 92)
line_dab(heng_start, heng_end, r_start=4, r_end=4, steps=140)
# small 顿 at start
dab(heng_start[0], heng_start[1], 5)
# shoulder dab at corner (modest, not a big ball)
dab(heng_end[0], heng_end[1], 6)

# 撇 tail (bowed Bezier from shoulder down-and-left, long and sweeping)
pie_p0 = heng_end
pie_p2 = (75, 235)
pie_ctrl = (178, 165)   # control pulled toward interior/right → gentle rightward bow
bezier_dab(pie_p0, pie_ctrl, pie_p2, r_start=5.5, r_end=1.2, ease=1.35)


# ---------------- Stroke 3: 捺 (na), the sweeping right leg -----------------
# Starts on stroke 2's descending 撇 near mid-height, sweeps down-and-right.
# Thin→thick, ending in a broad flat foot. This is the widest-swinging
# element of 夂.
na_p0 = (140, 158)     # sits on the 撇 body
na_p2 = (250, 235)     # broad foot in lower right
na_ctrl = (180, 178)   # gentle downward bow
bezier_dab(na_p0, na_ctrl, na_p2, r_start=1.8, r_end=8.5, ease=1.2)
# broad terminal press (flat foot, extends slightly right)
foot_start = na_p2
foot_end = (272, 240)
line_dab(foot_start, foot_end, r_start=8.5, r_end=4.5, steps=70)


img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_081_夂/01_夂.png"
)
