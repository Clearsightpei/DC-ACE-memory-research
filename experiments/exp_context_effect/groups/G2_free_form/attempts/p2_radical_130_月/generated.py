"""
Render 月 (4-stroke radical) at 300x300 using PIL.

Revision 1 notes vs first attempt:
- Extend vertical extent: top ~y=55, bottom hook ~y=275 (was 70..255).
- Make the 撇 sweep more outward: increase leftward drift near the
  bottom so left tail lands around x=45 y=270 (was 55, 265, too vertical).
- Internal 横 strokes should NOT touch the 撇 — their left ends float
  inside the box, joining the 撇's inner curve rather than crossing it.
  So shorten the internal 横 on the left side.
- Slightly larger hook at bottom-right.

Structure (from GT):
- Tall-narrow silhouette, ~55% canvas width, ~90% canvas height.
- Stroke 1: 撇 — start near top ~(100, 55), curves down-left to
  a tapered tail at ~(45, 275). Noticeable outward bow.
- Stroke 2: 横折钩 — top 横 from x=100 y=55 to x=210 y=55,
  shoulder dab, 竖 descends along right wall to about y=265,
  then hook flicking left ~15 px.
- Stroke 3: internal 横 — inside upper region ~y=125, from the
  inner side of the 撇 (~x=88) to right wall (~x=203).
- Stroke 4: internal 横 — inside middle region ~y=195, from the
  inner side of the 撇 (~x=76) to right wall (~x=200).
"""

from PIL import Image, ImageDraw

W, H = 300, 300
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

BLACK = (0, 0, 0)


def dab(x, y, r=5):
    draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


def taper_line(pts, w_start, w_end, steps=None):
    if steps is None:
        steps = 40
    seg_lens = []
    total = 0.0
    for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]):
        L = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
        seg_lens.append(L)
        total += L
    samples = []
    for i in range(steps + 1):
        t = i / steps * total
        acc = 0
        for k, L in enumerate(seg_lens):
            if acc + L >= t or k == len(seg_lens) - 1:
                u = (t - acc) / L if L > 0 else 0
                u = max(0.0, min(1.0, u))
                x0, y0 = pts[k]
                x1, y1 = pts[k + 1]
                samples.append((x0 + u * (x1 - x0), y0 + u * (y1 - y0)))
                break
            acc += L
    for i, (x, y) in enumerate(samples):
        t = i / steps
        w = w_start + (w_end - w_start) * t
        r = w / 2
        draw.ellipse([x - r, y - r, x + r, y + r], fill=BLACK)


# ----- Stroke 1: 撇 (left side, more outward sweep) -----
pie_pts = [
    (100, 55),
    (95, 90),
    (88, 130),
    (78, 175),
    (65, 220),
    (52, 255),
    (45, 275),
]
dab(100, 55, r=5)
taper_line(pie_pts, w_start=9, w_end=2, steps=70)

# ----- Stroke 2: 横折钩 (top 横 + right 竖 + hook) -----
top_heng = [(100, 55), (155, 53), (210, 55)]
taper_line(top_heng, w_start=6, w_end=7, steps=40)
dab(210, 55, r=5)
right_shu = [(210, 55), (208, 120), (206, 185), (204, 240), (203, 265)]
taper_line(right_shu, w_start=6, w_end=6, steps=50)
# Hook flicking left — a bit larger
hook_pts = [(203, 265), (192, 270), (180, 265), (172, 258)]
taper_line(hook_pts, w_start=6, w_end=2, steps=20)

# ----- Stroke 3: internal 横 (upper) -----
# Left end sits just inside the 撇's curve at y=125 (~x=88).
h3 = [(88, 125), (145, 124), (203, 125)]
taper_line(h3, w_start=4, w_end=5, steps=30)

# ----- Stroke 4: internal 横 (lower) -----
# Left end floats inside 撇's curve at y=195 (~x=76).
h4 = [(76, 195), (138, 194), (201, 195)]
taper_line(h4, w_start=4, w_end=5, steps=30)

img.save(
    "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_130_月/01_月.png"
)
