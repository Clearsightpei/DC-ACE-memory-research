# yi.py — 一 (yi, "one") radical, 1 stroke.
# Bootstrap batch (position 37) — human PASSed.
#
# Per TR5: inlined 横 with a soft head-顿 / thin mid / small tail-顿 profile.
# Length 176 px (vs primitive's 200), variable width. Recorded verbatim.

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def draw_yi(t, ox=0.0, oy=-45.0, scale=1.0, length_px=176, samples=140):
    """一 radical: subtly tapered horizontal centered at (ox, oy).

    Default placement mirrors the passing render (oy=-45 in math coords
    → PIL y=195). Width profile: 9 (soft entry) → 6 (mid, ~65% of stroke)
    → 8 (tail 顿) → 5 (tail exit).
    """
    half = length_px / 2.0

    for i in range(samples + 1):
        u = i / samples
        cx_math = ox - half + u * length_px
        cy_math = oy

        if u < 0.05:
            w = 9.0 - (9.0 - 6.5) * (u / 0.05)
        elif u < 0.20:
            w = 6.5 - (6.5 - 6.0) * ((u - 0.05) / 0.15)
        elif u < 0.85:
            w = 6.0
        elif u < 0.95:
            w = 6.0 + (8.0 - 6.0) * ((u - 0.85) / 0.10)
        else:
            w = 8.0 - (8.0 - 5.0) * ((u - 0.95) / 0.05)

        w = max(2.0, w * scale)
        r = w / 2.0
        px, py = _to_pixel(cx_math, cy_math)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
