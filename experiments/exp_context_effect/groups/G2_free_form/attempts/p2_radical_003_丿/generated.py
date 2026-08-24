"""
Render 丿 (pie radical, 1画) as a standalone at 300x300, black on white.

丿 is a 撇 stroke: starts upper-right with a 顿笔 press, curves down-and-left
with a gentle bow (belly on the lower-right side), tapers thick->thin to a
sharp tip at the lower-left.

Per memory:
- Standalone scale: pull Bezier control ~45 px off midline for pronounced curve.
- Standalone start-press small: r=6-8 (not r=12 as in compound stroke).
- Endpoint TERMINATES (no shoulder/hook), so end with plain radius, no r+2 ball.
- Sharp tip: r_end near 1.0.

Bezier: sample ~400 points, thick->thin taper via linearly decreasing radius.
"""
from PIL import Image, ImageDraw


def bezier(p0, p1, p2, t):
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return x, y


def dab(draw, x, y, r):
    draw.ellipse((x - r, y - r, x + r, y + r), fill="black")


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # 丿 endpoints matched to GT observation
    # Revised: match GT shape (start ~ (115,85), tip ~ (60,258)), gentler curve.
    # First attempt: start-press was too balloon-like (r+1.5 on r_start=10 is
    # too much for a standalone). Also the curvature was slightly too pronounced.
    # Fixes: r_start=8 (smaller), no separate press dab (just the first ramp dab),
    # and pull control point LESS far off the chord so the bow is gentle.
    P0 = (117, 85)     # upper-right start
    P2 = (58, 258)     # lower-left tip
    # Chord midpoint ~ (87, 172). Pull right ~28 px for a gentle bow.
    P1 = (115, 170)

    steps = 500
    r_start = 8.0
    r_end = 1.0

    for i in range(steps + 1):
        t = i / steps
        x, y = bezier(P0, P1, P2, t)
        r = r_start + (r_end - r_start) * t
        dab(d, x, y, r)

    out = "<REPO_ROOT>/experiments/exp_context_effect/groups/G2_free_form/attempts/p2_radical_003_丿/01_丿.png"
    img.save(out)


if __name__ == "__main__":
    main()
