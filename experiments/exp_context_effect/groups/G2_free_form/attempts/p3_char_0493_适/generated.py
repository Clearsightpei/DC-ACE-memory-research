"""
Render 适 (shi4) at 300x300, black ink on white.

Structural read from GT:
  Wrapper: 辶 (walking radical) — 点 (top-left), 横折折撇 (curved middle),
           long 平捺 (bottom horizontal sweep with slight belly rising to right).
  Inner (upper-right): 舌 = 千 over 口.
    千: 撇 (top short sweep left), 横 (top horizontal), 竖 (vertical spine).
    口: rectangle (横折 + 横 close) at the bottom of 舌.

TIER-0 applied:
  - Bezier for all curves (撇, 折, 平捺).
  - Teardrop taper on 撇/点/捺 (variable width).
  - Components MUST touch: 舌 sits inside 辶's wrap, 平捺 undercuts 舌.
  - No sibling-signature-row targets in 适 (适's components 千,口 aren't
    in the sibling checklist family).
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

def dab(cx, cy, r):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="black")

# =====================================================================
# 舌 (upper-right inner component) — 千 + 口
# occupies approx x=125..255, y=45..205
# =====================================================================

# 千's 撇 — longer, more visible top-left flick
pie = bez((188, 50), (175, 65), (155, 82), (132, 100), n=60)
stroke(pie, (11, 3))

# 千's 横 (top horizontal) — spans across the head, slight rise
h_top = bez((128, 105), (170, 100), (220, 100), (258, 103), n=60)
stroke(h_top, (7, 7))

# 千's 竖 (vertical spine of 舌) — through center-right, into 口
v_spine = bez((185, 103), (185, 140), (185, 175), (185, 210), n=60)
stroke(v_spine, (9, 9))

# 舌's wider middle 横 (this is 口's top 横 / 舌 belly line)
h_mid = bez((138, 155), (180, 152), (225, 152), (260, 155), n=60)
stroke(h_mid, (8, 8))

# 口 — rectangle at bottom of 舌
box_left = bez((150, 155), (150, 180), (150, 200), (150, 215), n=40)
stroke(box_left, (7, 7))
box_right = bez((252, 155), (252, 180), (252, 200), (252, 215), n=40)
stroke(box_right, (7, 7))
box_bot = bez((150, 213), (185, 216), (225, 216), (253, 213), n=50)
stroke(box_bot, (8, 8))
# shoulder dabs at 口 corners
dab(150, 155, 5)
dab(252, 155, 5)
dab(150, 215, 5)
dab(252, 215, 5)

# =====================================================================
# 辶 (walking radical, bottom-left wrapper)
# =====================================================================

# Top 点 (small dot upper-left of the character)
dot_top = bez((78, 55), (74, 63), (70, 72), (68, 82), n=30)
stroke(dot_top, (4, 10))

# 横折折撇 — curved zigzag: goes right, folds down, folds left again
# In 辶 this is a compressed S-curve on the left side
# segment 1: short 横 pointing right-down
s1 = bez((70, 105), (85, 108), (100, 112), (110, 118), n=40)
stroke(s1, (6, 6))
# segment 2: fold down-left (short 撇-ish)
s2 = bez((110, 118), (100, 135), (85, 155), (72, 175), n=50)
stroke(s2, (7, 4))
# shoulder dab at the fold
dab(110, 118, 5)

# 平捺 — the long horizontal sweep at the bottom, with a rising foot at right
# starts up-left, dips down through center, rises to a wide foot at the right
pn1 = bez((45, 205), (75, 235), (140, 260), (215, 255), n=100)
stroke(pn1, (5, 12))
# foot flare at the end
foot = bez((215, 255), (235, 250), (255, 245), (275, 238), n=40)
stroke(foot, (12, 4))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0493_适/01_适.png")
