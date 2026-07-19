# p2_radical_113_犬 (quǎn, "dog") — G3 coord-bank drawer
#
# 4-stroke radical: 大 (heng + pie + na) with a 丶 (dian) in upper-right.
# Order: 横 → 撇 → 捺 → 丶
#
# TR8/TR9 rationale — INLINE-FRESH for 大:
# 大 is documented in sandbox.md B1 as a G3-unique FAIL when built from
# bank primitives (heng + pie + na force-fit; heads didn't converge).
# The pie/na primitives have canonical head/tail chords tuned for
# STANDALONE strokes — their apex geometry doesn't naturally produce
# the "pie head and na head meet above heng" convergence 大 requires.
# Per TR8 rule of thumb ("if reaching for TWO primitives at scale<0.55
# to build one radical, STOP — inline"), all three 大-strokes are
# inlined here as tapered beziers with hand-picked apex/crossing pixels.
# The 丶 in upper-right is a small dot — bank `dian` at scale ~0.5
# would nominally fit but for consistency with the fresh-inlined body
# and to tune the exact dot orientation (down-left slant, GT shows
# short right-leaning dot), it is also inlined.
#
# Coord convention: math coords (center origin, +y up), converted to
# PIL pixels via _to_pixel.

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _stamp_seg(draw, prev_pt, pt, w):
    w_int = max(1, int(round(w)))
    draw.line([prev_pt, pt], fill=(0, 0, 0), width=w_int)
    r = w / 2.0
    draw.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))


def draw_heng_inline(draw, x0, y0, x1, y1, width):
    """Uniform-width heng, tapered slightly at both ends."""
    n = 30
    prev_pt = None
    for i in range(n + 1):
        u = i / n
        x = x0 + (x1 - x0) * u
        y = y0 + (y1 - y0) * u
        # Slight taper at ends (~85% width at extremes, full width in middle)
        taper = 0.85 + 0.15 * (1 - abs(2 * u - 1))
        w = width * taper
        pt = _to_pixel(x, y)
        if prev_pt is not None:
            _stamp_seg(draw, prev_pt, pt, w)
        prev_pt = pt


def draw_pie_inline(draw, x0, y0, mx, my, x1, y1, w_head, w_tail):
    """Quadratic-bezier 撇: thick head → thin needle tail."""
    n = 60
    prev_pt = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        w = w_head + (w_tail - w_head) * u
        pt = _to_pixel(bx, by)
        if prev_pt is not None:
            _stamp_seg(draw, prev_pt, pt, w)
        prev_pt = pt


def draw_na_inline(draw, x0, y0, mx, my, x1, y1, w_head, w_belly, w_tail, t_belly=0.7):
    """Quadratic-bezier 捺: thin head → swelling belly → tapered foot."""
    n = 60
    prev_pt = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        if u <= t_belly:
            w = w_head + (w_belly - w_head) * (u / t_belly)
        else:
            w = w_belly + (w_tail - w_belly) * ((u - t_belly) / (1 - t_belly))
        pt = _to_pixel(bx, by)
        if prev_pt is not None:
            _stamp_seg(draw, prev_pt, pt, w)
        prev_pt = pt


def draw_dian_inline(draw, x0, y0, mx, my, x1, y1, w_head, w_tail):
    """Small 点: thin head → heavier rounded tail."""
    n = 40
    prev_pt = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        w = w_head * (1 - u) + w_tail * u
        pt = _to_pixel(bx, by)
        if prev_pt is not None:
            _stamp_seg(draw, prev_pt, pt, w)
        prev_pt = pt


def draw_quan_radical(draw):
    # === REVISION NOTES ===
    # First render: na belly was 15px wide → became a black wedge. Pie
    # head 10px was also too heavy vs GT's thin, uniform-feeling strokes.
    # GT renders every stroke as a thin (~4-6 px) tapered line — the
    # calligraphic profile is subtle at this scale. Reduced all widths
    # by ~50%, kept the composition geometry (apex, heng, crossings).

    # === Stroke 1: 横 (heng) — mid horizontal ===
    # GT shows a heng at roughly canvas mid-height, spanning most of width,
    # slightly rising to the right (calligraphic convention).
    draw_heng_inline(draw, x0=-95, y0=8, x1=95, y1=18, width=5)

    # === Stroke 2: 撇 (pie) — from apex above heng down-left ===
    # Head at ~(-5, +88): the apex of 大, above the heng crossing point.
    # Tail at ~(-105, -115): far lower-left corner.
    # Control pulled slightly left of chord to bow the sweep.
    draw_pie_inline(
        draw,
        x0=-5, y0=88,      # apex head (upper)
        mx=-60, my=-15,    # bow slightly left of chord midpoint
        x1=-105, y1=-115,  # lower-left tail
        w_head=6, w_tail=1,
    )

    # === Stroke 3: 捺 (na) — from apex-area down-right ===
    # Head near apex, sweeps down-right with a subtle belly. GT belly is
    # slight — not a heavy wedge. Cut w_belly from 15 → 7.
    draw_na_inline(
        draw,
        x0=8, y0=75,       # thin head near apex
        mx=60, my=-10,     # control pulled slightly up-right of chord midpoint
        x1=115, y1=-110,   # foot at lower-right
        w_head=2, w_belly=7, w_tail=2,
    )

    # === Stroke 4: 丶 (dian) — upper-right dot, distinguishes 犬 from 大 ===
    # Short right-tilted dot sitting to the right of the apex, above heng.
    draw_dian_inline(
        draw,
        x0=40, y0=70,      # thin upper-left head
        mx=50, my=55,      # slight bow
        x1=68, y1=48,      # heavier lower-right tail
        w_head=2, w_tail=6,
    )


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_quan_radical(draw)
    out_path = __file__.rsplit("/", 1)[0] + "/01_犬.png"
    img.save(out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
