"""
Render 俎 (zǔ) at 300x300.

Structural read from GT:
  Left component: a stacked pair of 夕-like flicks — two 撇 (short down-left
    curves) alternating with two short 提-like right-going flicks.
    Upper unit sits near top, lower unit tucks below-left of it.
  Right component: 且 — a narrow rectangle with two internal horizontals,
    the bottom horizontal extends OUTWARD to the left as a base bar under
    the whole character.
Applies TIER-0 F: bez + variable-width stroke helpers, hook-less character.
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

# =========================================================================
# LEFT COMPONENT — two stacked 夕-like flick pairs
# =========================================================================

# Upper flick unit (near top-center-left)
# 撇 upper: down-left curve
p1 = bez((100, 55), (90, 90), (75, 120), (55, 155), n=70)
stroke(p1, (10, 4))
# short right flick attached to upper 撇 (mid of 撇, going down-right)
r1 = bez((90, 90), (105, 105), (120, 115), (135, 122), n=40)
stroke(r1, (5, 8))

# Lower flick unit (tucked below upper, shifted left)
# 撇 lower: another down-left curve, starting from where r1 tail is
p2 = bez((80, 145), (68, 180), (55, 215), (35, 255), n=70)
stroke(p2, (10, 4))
# short right flick attached to lower 撇
r2 = bez((70, 180), (85, 195), (100, 205), (115, 213), n=40)
stroke(r2, (5, 8))

# =========================================================================
# RIGHT COMPONENT — 且 (narrow rectangle w/ 2 internal horizontals + base)
# =========================================================================
# Top: 竖 (left vertical of 且) + 横折 (top+right)
# Left vertical (竖)
lv = bez((155, 55), (155, 140), (155, 220), (155, 260), n=80)
stroke(lv, (8, 8))

# Top horizontal + right vertical (横折) — draw as one L
top_h = bez((155, 55), (185, 55), (215, 55), (240, 55), n=50)
stroke(top_h, (7, 7))
# shoulder dab at top-right corner
d.ellipse((240-6, 55-6, 240+6, 55+6), fill="black")
right_v = bez((240, 55), (240, 130), (240, 200), (240, 255), n=80)
stroke(right_v, (8, 8))

# Two internal horizontals
h_mid1 = bez((155, 115), (185, 115), (215, 115), (240, 115), n=40)
stroke(h_mid1, (6, 6))
h_mid2 = bez((155, 175), (185, 175), (215, 175), (240, 175), n=40)
stroke(h_mid2, (6, 6))

# Bottom horizontal — extends OUTWARD to left as base of the whole char
base = bez((30, 260), (100, 258), (180, 258), (260, 258), n=80)
stroke(base, (8, 8))

img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0482_俎/01_俎.png")
