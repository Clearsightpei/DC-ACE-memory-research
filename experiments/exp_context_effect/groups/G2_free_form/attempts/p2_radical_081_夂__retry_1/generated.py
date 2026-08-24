"""
夂 (zhǐ) — 3-stroke radical.  RETRY #1.

Prior attempt (retry_0) failed because strokes were far TOO THICK
(especially the 捺) and the 横撇 was drawn as an overly complex
separate 横 + 撇 tail. The GT shows uniformly LIGHT thin strokes
with only mild taper; the 横撇 top is a small angular shoulder,
not a long 横 segment.

Fix ideas for this retry:
1. Uniform light stroke radius ~2.5 baseline (was 4-8.5).
2. The 横撇 (stroke 2) becomes a small tight angular hook at the
   top-center followed by a long sweeping 撇 down-left — the 横
   part is just a short flick, not a big horizontal bar.
3. The 捺 (stroke 3) starts from ~same top area, sweeps down-right,
   ends with modest terminal press (~5px, not 8.5).
4. Whole glyph tighter — compact square silhouette per
   radical_position_rules "square" family.

Stroke breakdown:
  1. 撇 (short flick top-left of shoulder).
  2. 横撇: small horizontal shoulder at top-center → long 撇 tail
     sweeping down-left.
  3. 捺: from shoulder-area, sweeps down-right to broad foot.
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
        steps = max(60, int(dist * 3))
    for i in range(steps + 1):
        t = i / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        r = r_start + (r_end - r_start) * t
        dab(x, y, r)


def bezier_dab(p0, p1, p2, r_start, r_end, steps=220, ease=1.0):
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


# ------------- Stroke 1: short 撇 flick at top -------------------------
# Small down-left flick just above and left of the shoulder.
s1_start = (145, 78)
s1_end = (118, 108)
dab(s1_start[0], s1_start[1], 3.0)
bezier_dab(s1_start, (132, 90), s1_end, r_start=2.8, r_end=1.0, ease=1.3)


# ------------- Stroke 2: 横撇 (small shoulder + long sweeping 撇) --------
# 横 part: very short horizontal shoulder at top-center
heng_start = (135, 100)
heng_corner = (178, 96)
line_dab(heng_start, heng_corner, r_start=2.5, r_end=2.5, steps=90)
dab(heng_start[0], heng_start[1], 3.0)
# small angular shoulder dab
dab(heng_corner[0], heng_corner[1], 3.5)

# 撇 tail: long sweeping arc down-left from corner
pie_p0 = heng_corner
pie_p2 = (85, 235)
pie_ctrl = (165, 175)   # gentle rightward bow
bezier_dab(pie_p0, pie_ctrl, pie_p2, r_start=3.0, r_end=0.8, ease=1.4)


# ------------- Stroke 3: 捺 (right-leg sweep) ---------------------------
# Starts near the shoulder area (crossing through 撇 body), sweeps
# down-and-right ending in a modest broad foot. Lighter than r0 —
# GT foot is only slightly thicker than the shaft.
na_p0 = (150, 155)
na_p2 = (240, 232)
na_ctrl = (185, 180)
bezier_dab(na_p0, na_ctrl, na_p2, r_start=1.2, r_end=3.5, ease=1.25)
# small terminal foot press extending slightly right (lighter)
foot_start = na_p2
foot_end = (255, 236)
line_dab(foot_start, foot_end, r_start=3.5, r_end=1.8, steps=55)


img.save(
    "<REPO_ROOT>/experiments/exp_context_effect/"
    "groups/G2_free_form/attempts/p2_radical_081_夂__retry_1/01_夂.png"
)
