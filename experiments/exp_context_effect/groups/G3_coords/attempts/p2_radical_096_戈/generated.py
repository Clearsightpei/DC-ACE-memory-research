# p2_radical_096_戈 (gē) — G3 coord-bank Drawer, first attempt.
#
# INLINE-FRESH decision (per TR8/TR9):
# 戈 has 4 strokes: 短横, 斜钩, 撇, 点.
# - 短横: short and slightly rising; heng primitive is a straight 200px
#   uniform stroke — could reuse at ~0.35 scale but the GT has a slight
#   upward tilt on the left end. I'll inline as a tapered short segment
#   with a slight upward slope, ending with a small 顿笔 blob so it
#   welds to the 斜钩 (斜钩 starts near heng's right end).
# - 斜钩: no bank primitive exists (no xie_gou). Must inline fresh as
#   the character's dominant stroke — long shallow-C diagonal from upper
#   area sweeping down-right with a hook flicking UP at the tail (P1).
# - 撇: pie primitive is tuned as a wide diagonal sweep for standalone;
#   in 戈 the 撇 starts near the intersection of heng and xie_gou and
#   sweeps down-left with less curvature — inline as a tapered curve
#   from a chosen head down-left to a needle tail.
# - 点: bank dian is fine, but at this size (small dot upper right) I
#   inline as one heavy tapered stub for accuracy.
#
# Coord system: math coords, +y up, origin at canvas center (150, 150),
# converted to PIL pixel via _to_pixel().
# Canvas: 300x300, white bg, black ink.

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _lerp(a, b, t):
    return a + (b - a) * t


def _bezier(p0, p1, p2, t):
    """Quadratic bezier interpolation."""
    x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t ** 2 * p2[0]
    y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t ** 2 * p2[1]
    return x, y


def _stamp_taper_bezier(draw, p0_math, p1_math, p2_math, w_start, w_end,
                        w_belly=None, belly_u=0.5, steps=80):
    """Draw a tapered bezier by stamping circles along the curve.
    p0, p1, p2 in math coords; w_* in pixels."""
    p0 = _to_pixel(*p0_math)
    p1 = _to_pixel(*p1_math)
    p2 = _to_pixel(*p2_math)
    for i in range(steps + 1):
        u = i / steps
        x, y = _bezier(p0, p1, p2, u)
        # Width profile: if belly given, ramp start->belly->end; else linear.
        if w_belly is not None:
            if u <= belly_u:
                w = _lerp(w_start, w_belly, u / belly_u)
            else:
                w = _lerp(w_belly, w_end, (u - belly_u) / (1 - belly_u))
        else:
            w = _lerp(w_start, w_end, u)
        r = max(0.5, w / 2)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _stamp_taper_line(draw, p0_math, p1_math, w_start, w_end, steps=40):
    """Straight tapered line via stamped circles."""
    p0 = _to_pixel(*p0_math)
    p1 = _to_pixel(*p1_math)
    for i in range(steps + 1):
        u = i / steps
        x = _lerp(p0[0], p1[0], u)
        y = _lerp(p0[1], p1[1], u)
        w = _lerp(w_start, w_end, u)
        r = max(0.5, w / 2)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _dun_bi(draw, p_math, r):
    """Small filled blob for the 顿笔 (corner press)."""
    x, y = _to_pixel(*p_math)
    draw.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def draw_ge(draw):
    # Revision-1 notes vs first pass:
    # - 斜钩 was too straight/vertical; needed a strong RIGHTWARD belly.
    #   Move control point further right (+70, -20).
    # - Hook flick barely visible; make it longer and more distinct.
    # - Pie was too straight; needs to start from within the character
    #   body (near heng intersection) and curve gracefully down-left.
    # - Character was compressed vertically; spread strokes more.

    # --- Stroke 1: 短横 (short heng), slightly rising toward the right.
    # From (-65, +45) to (+10, +52). Short and thin, ends at the pivot
    # where both 斜钩 and 撇 originate.
    _stamp_taper_line(draw, (-65, 45), (+10, 52), w_start=9, w_end=9)
    _dun_bi(draw, (+10, 52), r=5)

    # --- Stroke 2: 斜钩 (xie gou), the character's dominant stroke.
    # Starts at (-15, +80) high on the left, curves through a STRONGLY
    # RIGHTWARD belly (+75, -10), ends at tail (+95, -105).
    # Then hook flicks UP-and-slightly-left per P1.
    _stamp_taper_bezier(
        draw,
        p0_math=(-15, 80),
        p1_math=(+75, -20),   # deep rightward belly — this is the C
        p2_math=(+95, -105),
        w_start=6, w_belly=13, w_end=7, belly_u=0.5,
    )
    # Hook: from tail up-and-leftward, tapered to needle.
    _stamp_taper_line(draw, (+95, -105), (+75, -78), w_start=8, w_end=1)

    # --- Stroke 3: 撇 (pie). Starts at the heng/xie_gou intersection
    # (roughly (+5, +60)) and sweeps with real curvature down-left to
    # (-100, -105). Belly control (-50, -20) gives the arched
    # calligraphic sweep.
    _stamp_taper_bezier(
        draw,
        p0_math=(+5, 60),
        p1_math=(-55, -10),
        p2_math=(-100, -105),
        w_start=11, w_belly=7, w_end=1, belly_u=0.35,
    )

    # --- Stroke 4: 点 (dian) — small dot upper right area.
    # Thin head at (+70, +100), heavy tail at (+88, +78).
    _stamp_taper_line(draw, (+70, 100), (+88, 78), w_start=3, w_end=11)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_ge(draw)
    out = (
        "/Users/peilinwu/Documents/AI memory research/experiments/"
        "exp_context_effect/groups/G3_coords/attempts/p2_radical_096_戈/"
        "01_戈.png"
    )
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
