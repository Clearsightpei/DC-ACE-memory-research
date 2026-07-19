# p2_radical_005_一 — G3 (coord-bank)  [REVISION 1]
#
# Target: 一 (yi, "one"), 1画部首.
# Per P7 (radicals ARE strokes when shape matches): 一 ↔ heng primitive.
#
# First pass used draw_heng(ox=0, oy=-45, scale=0.88) which produced a
# uniform-thickness blunt-ended slab. GT shows subtly tapered ends and a
# thinner mid-body (~6-7 px) with a soft entry-顿笔 hint and slight
# downward curl at the right end.
#
# TR5 rationale: rather than shrink the primitive further (scale<0.4 broke
# the primitive's tuning), INLINE a width-profile version of 横. Keep the
# same centerline geometry the primitive uses (200 px unit, math-coord
# center origin), but stamp a series of small circles with a per-u width
# profile: thicker at head (~9), thin mid (~6), a small 顿 at tail (~8),
# matching P4's 横 width guideline adjusted for the softer radical form.

from pathlib import Path
from PIL import Image, ImageDraw

CANVAS = 300


def _to_pixel(ox, oy):
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def draw_yi_inline(draw, ox=0.0, oy=0.0, scale=1.0, length_px=176, samples=140):
    """Inlined 一 with a soft head-顿 / thin mid / small tail-顿 profile."""
    half = length_px / 2.0

    for i in range(samples + 1):
        u = i / samples
        # centerline: horizontal, no curvature
        cx_math = ox - half + u * length_px
        cy_math = oy

        # width profile (in px):
        # u=0.00: 9 (soft entry 顿笔)
        # u=0.05-0.20: taper to ~6.5
        # u=0.20-0.85: uniform ~6.0
        # u=0.85-0.95: swell to 8 (tail 顿)
        # u=0.95-1.00: taper to 5
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
        draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Inlined 一 (see TR5): centerline at math (0, -45) i.e. PIL y=195,
    # length 176 px → spans PIL x ∈ [62, 238]. Matches GT position/length.
    draw_yi_inline(draw, ox=0, oy=-45, scale=1.0, length_px=176)

    out = Path(__file__).parent / "01_一.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
