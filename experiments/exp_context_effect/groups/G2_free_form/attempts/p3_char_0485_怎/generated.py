"""
p3_char_0485_怎 — 9 strokes: 乍 (top, 5 strokes) over 心 (bottom, 4 strokes).

Memory consulted:
- memory_index.md TIER-0 F: apply calligraphic-weight 4-move (taper,
  shoulder dab, Bezier for sweeps, correct hook flick). No uniform
  polylines.
- memory_index.md TIER-0 B: 卧钩 (心) flicks UP-and-LEFT (~-145°)
  from bowl's right end.
- memory_index.md TIER-0 H: components MUST touch — 乍's bottom横
  must sit close above 心's bowl top, no visible gap.
- attempts/p3_char_0112_心/generated.py: taper_line + bezier_taper
  helper pattern (copied here).
- attempts/p3_char_0165_乍/generated.py: 乍 stroke layout (撇 sweep,
  short top-横, long 竖, two crossing 横).

Layout: top-bottom compound. 乍 occupies top ~y 20-155, 心 occupies
bottom ~y 165-278. 乍's bottom横 ends near y=150; 心's bowl-belly
starts around y=210 with entry dots above (~y=175). Components
touch/overlap through the middle band.

Stroke order: 乍 first (撇 → top横 → 竖 → mid横 → bot横), then 心
(left dot → 卧钩 with hook → center dot → right dot).
"""
from PIL import Image, ImageDraw

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


def heng(x0, y0, x1, y1, r0=3.0, r1=4.2):
    # slight taper thin->thick with a small final shoulder dab
    taper_line(x0, y0, x1, y1, r0, r1, steps=180)
    dab(x1, y1, r1 + 0.6)


def shu(x0, y0, x1, y1, r0=4.5, r1=3.8):
    # vertical, mildly tapered
    taper_line(x0, y0, x1, y1, r0, r1, steps=200)


# ============ 乍 (top block) ============

# Stroke 1: 撇 — long sweeping pie from upper-right of block down-and-left
# Bezier bow (control pulled slightly right of the chord) — thick→thin
# End around (60, 155)
p0, p1, p2, p3 = (155, 25), (140, 75), (105, 115), (55, 155)
for i in range(261):
    t = i / 260
    u = 1 - t
    x = (u**3)*p0[0] + 3*(u**2)*t*p1[0] + 3*u*(t**2)*p2[0] + (t**3)*p3[0]
    y = (u**3)*p0[1] + 3*(u**2)*t*p1[1] + 3*u*(t**2)*p2[1] + (t**3)*p3[1]
    r = 5.2 + (1.4 - 5.2) * t
    dab(x, y, r)

# Stroke 2: 短横 at top of right side
heng(138, 55, 205, 52, r0=3.0, r1=4.0)

# Stroke 3: 竖 — long vertical from top-横 down through the block
shu(150, 55, 150, 158, r0=4.3, r1=3.6)

# Stroke 4: 中横 — middle horizontal, crosses the 竖 and extends right
heng(128, 105, 218, 103, r0=3.0, r1=4.2)

# Stroke 5: 底横 — bottom horizontal of 乍 (base). Slightly longer.
heng(122, 152, 222, 150, r0=3.2, r1=4.5)


# ============ 心 (bottom block) ============
# Compact — placed touching just under 乍's bottom横.

# Stroke 6: left dot — down-and-LEFT slanting, thin→thick
taper_line(92, 190, 75, 232, 2.3, 5.4, steps=140)
dab(75, 232, 5.6)

# Stroke 7: 卧钩 — shallow smile bowl, then UP-LEFT flick from right end
bezier_taper(
    (110, 220),      # left entry
    (135, 268),      # control 1 — belly down
    (198, 268),      # control 2
    (222, 218),      # right end (before hook)
    r0=3.0,
    r1=7.2,          # press before hook
    steps=260,
)
# Hook flick: UP-and-LEFT from (222, 218) — TIER-0 B compliant
hx0, hy0 = 222, 218
hx1, hy1 = hx0 - 22, hy0 - 17
taper_line(hx0, hy0, hx1, hy1, 7.2, 1.2, steps=100)

# Stroke 8: center dot — upper-middle above/inside bowl, LEFT-slanting
taper_line(160, 178, 145, 210, 2.4, 5.6, steps=140)
dab(145, 210, 5.8)

# Stroke 9: right dot — upper-right, RIGHT-slanting (down-right), thin→thick
taper_line(210, 182, 235, 218, 2.4, 5.8, steps=140)
dab(235, 218, 6.0)


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0485_怎/01_怎.png")
print("saved")
