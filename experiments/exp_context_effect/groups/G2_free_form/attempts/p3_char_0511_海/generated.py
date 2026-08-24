"""
Render 海 (hai3) at 300x300, black ink on white.

Structure: 氵 (left, 3 strokes) + 每 (right, 7 strokes)
  氵: dot, dot, 提 (rising dot)
  每: 撇 (top-left short), 横 (lid), 竖折 (left of 母),
       横折钩 (top-right of 母 with hook), 横 (crossing 母 mid),
       点 (upper), 点 (lower)

Applies TIER-0 4-move (taper, shoulder dab, bezier, hook flick UP-LEFT).
Components touch (TIER-0 H): 母's mid-横 extends past both verticals;
氵 提's flick reaches toward 每.
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

# --- 氵 (three-drops water) on the left ---
# dot 1: upper, small teardrop slanting down-left
d1 = bez((55, 70), (52, 82), (48, 92), (44, 100), n=30)
stroke(d1, (4, 9))

# dot 2: middle, similar teardrop
d2 = bez((42, 115), (40, 128), (38, 140), (36, 150), n=30)
stroke(d2, (4, 9))

# 提 (rising dot): starts thick lower-left, flicks UP-and-RIGHT toward 每
tirise = bez((38, 200), (48, 192), (60, 185), (75, 178), n=40)
stroke(tirise, (10, 3))

# --- 每 on the right ---
# stroke 1: 撇 (top short, angled down-left) — crosses through the lid
pie1 = bez((175, 40), (163, 55), (150, 72), (130, 92), n=60)
stroke(pie1, (10, 4))

# stroke 2: 横 (lid) — extends across the full width of 每, crossing the 撇
h_lid = bez((105, 78), (150, 76), (210, 76), (262, 80), n=60)
stroke(h_lid, (6, 6))

# --- 母 body ---
# stroke 3: 竖折 (left vertical then bottom horizontal)
#   vertical part
sz_v = bez((118, 92), (117, 140), (117, 190), (117, 240), n=60)
stroke(sz_v, (7, 7))
#   bottom horizontal (part of 竖折)
sz_h = bez((117, 240), (150, 242), (200, 242), (240, 240), n=60)
stroke(sz_h, (7, 6))
# shoulder dab at the fold
dab(118, 240, 5)

# stroke 4: 横折钩 (top horizontal short + right vertical + hook UP-LEFT)
#   short top horizontal (a slight inner cap — the 母 top is really the lid, but 母 itself has an inner top segment)
hzg_top = bez((122, 108), (160, 106), (210, 106), (240, 108), n=50)
stroke(hzg_top, (6, 6))
#   right vertical down
hzg_v = bez((240, 108), (241, 160), (240, 210), (238, 240), n=60)
stroke(hzg_v, (7, 6))
# shoulder dab at top-right fold
dab(240, 108, 5)
#   hook flick UP-and-LEFT at the bottom-right terminal (into the body)
hook = bez((238, 240), (230, 234), (222, 228), (214, 222), n=25)
stroke(hook, (7, 3))

# stroke 5: 横 (middle) — crosses 母, EXTENDS PAST both verticals
h_mid = bez((100, 175), (150, 173), (210, 173), (258, 176), n=60)
stroke(h_mid, (6, 6))

# stroke 6: 点 (left inner dot in 母) — short vertical mark, upper cell
p1 = bez((160, 130), (162, 140), (163, 150), (163, 160), n=30)
stroke(p1, (4, 7))

# stroke 7: 点 (right inner dot in 母) — short vertical mark, upper cell
p2 = bez((200, 130), (199, 140), (198, 150), (198, 160), n=30)
stroke(p2, (4, 7))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0511_海/01_海.png")
