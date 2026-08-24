"""
Render 疵 (ci1, blemish) at 300x300, black ink on white.

Composition: 疒 (canopy, 5 strokes) + 此 (bottom-inside, 6 strokes) = 11 strokes.

Frozen-cohort 疒 recipe (from frozen_cohort.md, applied but unverified):
  (1) 点 top-left of 一
  (2) 横 long top spanning canopy width
  (3) LONG curved 撇 from right end of 横 to bottom-left (dominant)
  (4) inner 点 below 横, right of 撇 stem
  (5) 提 rising short flick BELOW the inner 点

此 = 止 (left, 4 strokes: 竖 + 短横/提 + 竖 + 横) + 匕 (right, 2 strokes: 撇 + 竖弯钩).

TIER-0 H rule: 此 must be tucked INSIDE the canopy's 撇 sweep, touching along boundary.
TIER-0 F rule: taper via bez+stroke, shoulder-dab at 折 corners, hook UP-and-LEFT.
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


def shoulder_dab(x, y, r=6):
    d.ellipse((x - r, y - r, x + r, y + r), fill="black")


# ============ 疒 canopy (5 strokes) ============

# (1) 点 top-left dot
p1 = bez((62, 42), (68, 52), (72, 62), (76, 72), n=25)
stroke(p1, (3, 8))

# (2) 横 top spanning canopy width
h_top = bez((78, 78), (130, 76), (185, 76), (225, 80), n=50)
stroke(h_top, (5, 6))
shoulder_dab(225, 80, r=6)

# (3) LONG dominant 撇 from right end of 横 curving down-left (moderated so it exits left of body)
pie = bez((225, 80), (170, 130), (110, 190), (58, 268), n=100)
stroke(pie, (11, 4))

# (4) inner 点 below 横, right of 撇 stem (nested inside canopy triangle)
inner_dot = bez((105, 105), (110, 115), (115, 122), (120, 132), n=20)
stroke(inner_dot, (3, 8))

# (5) 提 rising flick BELOW the inner 点 (goes up-right)
ti = bez((92, 155), (110, 148), (128, 142), (146, 138), n=30)
stroke(ti, (7, 3))


# ============ 此 body (6 strokes) — tucked inside canopy, bottom-right ============
# Layout: 止 on left-of-body (x ~ 130-195), 匕 on right (x ~ 200-270), baseline ~ y=255

# --- 止 (4 strokes) — order: 竖 + 横 + 竖(taller) + 横(long) ---
# (6) short left 竖 of 止 (top-left corner)
zh1 = bez((140, 175), (140, 200), (140, 220), (140, 240), n=40)
stroke(zh1, (7, 6))

# (7) short 横 branching right from mid-竖 (technically a 提 shape)
ti2 = bez((140, 215), (155, 213), (170, 212), (182, 213), n=25)
stroke(ti2, (6, 5))

# (8) tall 竖 (center-right of 止) — taller, defines 止's spine
zh2 = bez((172, 165), (172, 195), (172, 225), (172, 250), n=50)
stroke(zh2, (7, 7))

# (9) long 横 base of 止 (wide, spans under whole 止)
h_bot_zhi = bez((122, 253), (150, 251), (178, 251), (200, 253), n=40)
stroke(h_bot_zhi, (5, 6))

# --- 匕 (2 strokes) — right of 止, hook prominent ---
# (10) 撇 from upper-right of 匕, sweeping down-left
pie2 = bez((240, 168), (225, 192), (215, 215), (208, 240), n=60)
stroke(pie2, (8, 4))

# (11) 竖弯钩: starts higher-right, goes down, curves right, hook UP-and-LEFT
zwg_v = bez((222, 175), (222, 205), (222, 232), (228, 255), n=50)
stroke(zwg_v, (7, 7))
zwg_arc = bez((228, 255), (245, 260), (258, 258), (268, 248), n=40)
stroke(zwg_arc, (7, 6))
shoulder_dab(268, 248, r=6)
# hook flick UP-and-LEFT (~-110°)
hook = bez((268, 248), (263, 238), (258, 228), (253, 220), n=25)
stroke(hook, (6, 3))


img.save("<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0580_疵/01_疵.png")
