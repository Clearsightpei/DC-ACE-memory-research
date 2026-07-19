# p2_radical_116_礻 (shi radical, "spirit/altar", 4 strokes)
# Composition analysis from GT PNG:
#   Stroke 1: top 点 — small tick, points down-right, sits high on canvas near
#             top-center (slightly left of vertical shaft).
#   Stroke 2: 横撇 — short horizontal (small), then a downward-left pie,
#             starting to the LEFT of the shaft top, meeting the shaft area.
#   Stroke 3: 竖 — long vertical shaft descending through the character's
#             center, going from just below the 横撇 down near the bottom.
#   Stroke 4: right 点 — small tick on the RIGHT of the shaft, mid-height.
#
# TR8/TR9 applied: this is a compact 4-stroke radical with idiosyncratic
# stroke placements. Force-fitting bank primitives (dian at scale 0.4,
# heng_pie compressed) would misplace ink. INLINE FRESH via PIL tapered
# beziers/lines for each stroke, tuned to the GT's specific geometry.
# No bank imports.

from PIL import Image, ImageDraw

CANVAS = 300
CX, CY = CANVAS // 2, CANVAS // 2  # center of canvas


def _mp(mx, my):
    """math-coord (center origin, +y up) -> PIL pixel."""
    return (CX + mx, CY - my)


def _tapered_bezier(t, p0, p1, p2, w_head, w_tail, n=30):
    """Quadratic bezier drawn as a series of tapered line segments + caps."""
    prev = None
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        pt = (x, y)
        if prev is not None:
            w = w_head * (1 - u) + w_tail * u
            w_int = max(1, int(round(w)))
            t.line([prev, pt], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r],
                      fill=(0, 0, 0))
        prev = pt


def _tapered_line(t, p0, p1, w_head, w_tail, n=25):
    """Straight tapered stroke via stamped segments."""
    prev = None
    for i in range(n + 1):
        u = i / n
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        pt = (x, y)
        if prev is not None:
            w = w_head * (1 - u) + w_tail * u
            w_int = max(1, int(round(w)))
            t.line([prev, pt], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r],
                      fill=(0, 0, 0))
        prev = pt


def draw():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # --- Stroke 1: top 点 (small dot, points down-right) ---
    # In GT the top dot is near top-center, slightly to the RIGHT.
    _tapered_bezier(
        t,
        _mp(8, 90),     # thin head upper-left
        _mp(15, 82),    # control
        _mp(24, 68),    # heavy tail lower-right
        w_head=2, w_tail=7,
        n=25,
    )

    # --- Stroke 2: 横撇 (short heng turning into a pie) ---
    # In GT the heng portion is short and starts LEFT of center, ending
    # at/near the shaft's top. The pie then sweeps down-left from that
    # corner. Thinner strokes to match GT's skinny brushwork.
    heng_left = _mp(-45, 45)
    heng_right = _mp(15, 50)   # very slight upward tilt
    _tapered_line(t, heng_left, heng_right, w_head=5, w_tail=8, n=20)
    # small 顿笔 blob at the corner:
    bx, by = heng_right
    t.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=(0, 0, 0))
    # Pie part: from the corner down-left tapering to a point.
    pie_head = heng_right
    pie_tail = _mp(-45, -20)
    _tapered_bezier(
        t,
        pie_head,
        _mp(-15, 20),       # control point pulls curve down-left
        pie_tail,
        w_head=8, w_tail=2,
        n=30,
    )

    # --- Stroke 3: 竖 (long vertical shaft) ---
    # The shaft passes near canvas center vertical, slightly RIGHT of
    # center in GT. Long, uniform, thin.
    shu_top = _mp(2, 30)
    shu_bot = _mp(0, -115)
    _tapered_line(t, shu_top, shu_bot, w_head=7, w_tail=7, n=30)

    # --- Stroke 4: right 点 (small dot on right of shaft, mid-height) ---
    _tapered_bezier(
        t,
        _mp(15, 15),    # thin head upper-left
        _mp(25, 5),     # control
        _mp(38, -15),   # heavy tail lower-right
        w_head=2, w_tail=7,
        n=25,
    )

    out = ("/Users/peilinwu/Documents/AI memory research/"
           "experiments/exp_context_effect/groups/G3_coords/"
           "attempts/p2_radical_116_礻/01_礻.png")
    img.save(out)
    print("saved", out)


if __name__ == "__main__":
    draw()
