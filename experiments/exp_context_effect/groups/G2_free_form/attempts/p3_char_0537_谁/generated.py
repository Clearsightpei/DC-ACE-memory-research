"""
Render 谁 (shui2/shei2) at 300x300, black ink on white.

谁 = 讠 (left, simplified 2-stroke) + 隹 (right, 8 strokes)

Frozen-cohort recipe for 讠 (5x failed): dot + coiled curve as
smooth stroke, widths=(3,5), one continuous polyline.

隹 structure: 亻 (撇 + 竖) on left, then top 撇, four horizontals,
central 竖 threading through the horizontals.

TIER-0 rule H: components must touch — 讠 tail and 亻 stem should
sit close enough (~5px) to not float.
Calligraphic 4-move: taper on 撇/捺/点, shoulder dab optional at
折 joints, bezier for all curved sweeps, hook flicks UP-LEFT.
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


# ============================================================
# LEFT: 讠  (2 strokes, occupies x ~30..95)
# ============================================================
# Stroke 1: 点 (dot) — small angled tick top-left of the radical
dot = bez((55, 55), (60, 60), (65, 66), (68, 72), n=15)
stroke(dot, (3, 8))

# Stroke 2: long coiled curve — starts as a leftward 撇 near the
# dot, sweeps down-left, then curls right at the bottom into a
# small up-tick (the vestigial 折/提 of the old 言 radical).
curve_top = bez((45, 90), (55, 130), (52, 170), (48, 210), n=60)
stroke(curve_top, (4, 6))
curve_tail = bez((48, 210), (55, 235), (68, 248), (85, 250), n=30)
stroke(curve_tail, (6, 4))

# ============================================================
# RIGHT: 隹  (8 strokes, occupies x ~110..270)
# ============================================================
# Stroke 1: 亻 撇 — starts top, curves down-left with taper
ren_pie = bez((140, 55), (128, 95), (118, 130), (108, 165), n=60)
stroke(ren_pie, (10, 4))

# Stroke 2: 亻 竖 — long vertical stem, starts where 撇 joins
ren_shu = bez((138, 105), (138, 160), (138, 210), (138, 260), n=60)
stroke(ren_shu, (7, 6))

# Stroke 3: small 撇 top of right structure (the "head" of 隹) —
# starts higher/more-left as a short flick above the top 横
top_pie = bez((178, 65), (172, 82), (165, 95), (156, 108), n=40)
stroke(top_pie, (8, 3))

# Stroke 4: top 横 (starts at 亻 stem, crosses under 撇)
h1 = bez((150, 112), (180, 110), (215, 110), (245, 114), n=40)
stroke(h1, (5, 6))

# Stroke 5: second 横
h2 = bez((155, 155), (185, 153), (215, 153), (245, 156), n=40)
stroke(h2, (5, 6))

# Stroke 6: third 横
h3 = bez((155, 195), (185, 193), (215, 193), (245, 196), n=40)
stroke(h3, (5, 6))

# Stroke 7: bottom 横 (longest, slightly bowed) — lowest
h4 = bez((145, 245), (185, 242), (225, 242), (260, 246), n=50)
stroke(h4, (6, 8))

# Stroke 8: central 竖 threading from top 横 through h4
zhong_shu = bez((205, 112), (205, 160), (205, 210), (205, 248), n=60)
stroke(zhong_shu, (7, 7))

img.save("/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p3_char_0537_谁/01_谁.png")
