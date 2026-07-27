"""
p3_char_0112_心 — heart character, 4 strokes.

Memory consulted:
- form_catalog.md "卧钩 as 心-bowl base": shallow smile-arc bowl (concave-up),
  belly at bottom-middle. Hook flicks up-and-left (~145°) from right end.
  Three dots: left dot OUTSIDE bowl far-left, center dot upper-middle inside
  bowl, right dot upper-right (short rightward flick).
- sibling_signature_checklist.md: 卧钩 hook UP-and-LEFT from bowl's right end
  (~-145°). Never flick down or straight up.
- drawer_memory.md: PIL brush-dabs for tapered strokes; Bezier for arcs.

Stroke order (traditional): 1) left dot, 2) 卧钩 bowl, 3) center dot, 4) right dot.
"""

from PIL import Image, ImageDraw
import math

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)


def dab(x, y, r):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


def taper_line(x0, y0, x1, y1, r0, r1, steps=200):
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


def bezier_taper(p0, p1, p2, p3, r0, r1, steps=250):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = (u**3) * p0[0] + 3 * (u**2) * t * p1[0] + 3 * u * (t**2) * p2[0] + (t**3) * p3[0]
        y = (u**3) * p0[1] + 3 * (u**2) * t * p1[1] + 3 * u * (t**2) * p2[1] + (t**3) * p3[1]
        r = r0 + (r1 - r0) * t
        dab(x, y, r)


# ---- Stroke 1: left dot (点) — LEFT-slanting dot outside bowl on far left ----
# Per GT: slants down-and-LEFT (top-right → bottom-left), thin→thick.
taper_line(75, 145, 58, 195, 2.5, 5.5, steps=140)
dab(58, 195, 5.8)

# ---- Stroke 2: 卧钩 (lying hook) — shallow smile arc + up-left flick ----
# Belly at bottom-middle (~y=225). Left entry ~ (100, 195), right end ~ (220, 195).
bezier_taper(
    (100, 195),     # left entry — start thin
    (125, 245),     # control 1 — pulls belly down
    (195, 245),     # control 2
    (220, 195),     # right end (before hook)
    r0=3.0,
    r1=7.5,         # thickens toward right (press before hook)
    steps=260,
)
# Hook flick: up-and-left from (220, 195). In image coords (y-down),
# "up-left" = dx<0, dy<0. ~30 px long, ~35° above horizontal.
hx0, hy0 = 220, 195
dx, dy = -22, -18   # up-left
hx1, hy1 = hx0 + dx, hy0 + dy
taper_line(hx0, hy0, hx1, hy1, 7.5, 1.2, steps=100)

# ---- Stroke 3: center dot — upper-middle above/inside bowl, LEFT-slanting ----
# GT shows this dot slanting down-and-LEFT (top-right → bottom-left).
taper_line(155, 115, 138, 155, 2.5, 6.0, steps=140)
dab(138, 155, 6.2)

# ---- Stroke 4: right dot — upper-right, RIGHT-slanting (down-right) ----
# GT shows right dot as short 点 slanting down-and-RIGHT.
taper_line(215, 125, 240, 165, 2.5, 6.0, steps=140)
dab(240, 165, 6.2)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0112_心/01_心.png"
)
print("saved")
