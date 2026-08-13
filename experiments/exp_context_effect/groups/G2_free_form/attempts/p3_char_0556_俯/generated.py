"""
俯 (fǔ) — 10 strokes total. Left-right compound: 亻 (left) + 府 (right).
  府 = 广 (canopy: 点+横+撇) + 付 (inside/lower-right: 亻+寸).

Applying TIER-0 rules:
  - H: Components MUST touch — 亻 竖 tucks close to 广 撇.
  - F: Calligraphic-weight 4-move (bez + variable-width stroke,
       shoulder dabs at 折, correct hook flick UP-LEFT).
  - B: Hook flick UP-and-LEFT for 竖钩 in 寸.

Stroke plan:
  1. 亻 撇          (left radical)
  2. 亻 竖          (left radical)
  3. 广 点          (canopy top)
  4. 广 横          (canopy horizontal)
  5. 广 撇          (canopy sweeping left leg)
  6. inner 亻 撇    (付 left)
  7. inner 亻 竖    (付 left)
  8. 寸 横          (付 right)
  9. 寸 竖钩        (付 right, hook UP-LEFT)
 10. 寸 点          (付 right dot)
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


# ============ 亻 (LEFT radical, ~x=15..75) ============
# 1. 撇 — starts upper, sweeps down-left, teardrop taper thin at tail
pie_left = bez((70, 55), (55, 95), (40, 130), (18, 165), n=60)
stroke(pie_left, (10, 4))

# 2. 竖 — long vertical from where 撇 crosses down to bottom
stroke(bez((60, 80), (60, 145), (60, 210), (60, 265), n=60), (8, 8))


# ============ 广 canopy of 府 (right, spans x=95..270 top) ============
# 3. 点 — small dot at top-center of canopy
dot_top = bez((165, 40), (170, 48), (175, 56), (178, 65), n=25)
stroke(dot_top, (4, 9))

# 4. 横 — horizontal bar of 广
h_guang = bez((110, 82), (160, 78), (220, 78), (265, 82), n=50)
stroke(h_guang, (6, 6))
# shoulder dab at right end where hook-in would be
dab(265, 82, 5)

# 5. 广 撇 — long sweeping left leg, from left end of 横, down-left, curved
pie_guang = bez((115, 82), (105, 130), (95, 190), (78, 265), n=80)
stroke(pie_guang, (10, 5))


# ============ 付 (亻 + 寸) tucked INSIDE 广, right side ============
# 6. inner 亻 撇 — short flick down-left
inner_pie = bez((155, 115), (145, 140), (135, 165), (125, 190), n=50)
stroke(inner_pie, (8, 3))

# 7. inner 亻 竖 — vertical
stroke(bez((150, 135), (150, 180), (150, 225), (150, 265), n=60), (7, 7))


# ============ 寸 (right of inner 亻) ============
# 8. 寸 横 — horizontal
h_cun = bez((170, 165), (200, 163), (240, 163), (275, 166), n=50)
stroke(h_cun, (6, 6))

# 9. 寸 竖钩 — vertical with hook flicking UP-and-LEFT (TIER-0 rule B)
sg = bez((225, 140), (225, 185), (225, 225), (225, 258), n=60)
stroke(sg, (8, 8))
# hook: UP-and-LEFT
hook = bez((225, 258), (215, 252), (205, 244), (196, 235), n=25)
stroke(hook, (8, 3))
# shoulder dab at hook joint
dab(225, 258, 5)

# 10. 寸 点 — small dot on left side of 竖钩, upper-mid
inner_dot = bez((205, 180), (212, 190), (218, 200), (222, 210), n=25)
stroke(inner_dot, (4, 8))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0556_俯/01_俯.png")
