"""p2_radical_077_忄 — heart-side radical (3 strokes).

Composition (per GT inspection):
  1. Left 点 (dian) — small dot slanting UP-LEFT-to-DOWN-RIGHT, on the
     left flank of the central vertical, in upper-middle region.
  2. Right 点 — mirrored dot (slanting UP-RIGHT-to-DOWN-LEFT), on the
     right flank, slightly HIGHER than the left dot (per GT).
  3. Central 竖 (shu) — long vertical descending from near the top of
     the canvas to near the bottom. GT shows a tiny leftward hook at
     the very top (the brush entry curl) but no bottom hook.

Applying TR8 (INLINE-FRESH TEST):
- draw_dian primitive is diagonal upper-left-to-lower-right; the RIGHT
  dot of 忄 is mirrored — the primitive would need reflection, which is
  not a pure (ox, oy, scale) transform. So the right dot must be
  inlined fresh (mirrored bezier).
- The LEFT dot IS the standard dian shape, but at scale ~0.4 (see TR5:
  scale < 0.4 is a warning; 0.45 acceptable). Bank primitive could
  work but for consistency with the mirrored right dot, I inline the
  left dot too using the SAME width profile — so the two dots visually
  match (P4: width profiles are stroke-specific; keeping both dots
  from ONE recipe guarantees matched inking).
- The central 竖 with a small brush-entry curl at the top does NOT
  match the flat-topped `shu` primitive. Inline as one tapered polyline
  with a small leftward hook at the top.

Coord convention (P5): math coords, center origin (150, 150), +y up.
"""

from PIL import Image, ImageDraw

CANVAS = 300


def _to_pixel(ox, oy):
    return (CANVAS / 2 + ox, CANVAS / 2 - oy)


def draw_dot(t, head_math, tail_math, head_w=3.0, tail_w=13.0, bow=(-3.0, -3.0), n=36):
    """Draw a tapered bezier dot from head (thin) to tail (heavy).

    bow = (dx, dy) offset applied to the chord midpoint to form the
    quadratic bezier control point (math coords).
    """
    x0, y0 = head_math
    x1, y1 = tail_math
    mx = (x0 + x1) / 2.0 + bow[0]
    my = (y0 + y1) / 2.0 + bow[1]
    prev_pt = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        if prev_pt is not None:
            w = head_w * (1 - u) + tail_w * u
            w_int = max(1, int(round(w)))
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def draw_central_shu(t, top_math, bot_math, top_w=11.0, bot_w=13.0, hook_len=10.0, n=60):
    """Draw the long central vertical with a small leftward brush-entry
    curl at the very top.

    Modeled as: a tiny hook segment from (top.x - hook_len, top.y + 4)
    curving down into (top.x, top.y), then a straight tapered vertical
    from top down to bot.
    """
    # Hook/curl segment: bezier starting from HIGHER-LEFT of shaft top,
    # curving DOWN and RIGHT into the shaft top. The GT shows a visible
    # curl about 15-18 px wide, so use a control point that sags below
    # the chord to create a real arc.
    hx0, hy0 = top_math[0] - hook_len, top_math[1] + 12
    hx1, hy1 = top_math[0], top_math[1]
    # Control point pulled RIGHT and DOWN of chord midpoint to bow the
    # curl into a rightward arc.
    hmx = (hx0 + hx1) / 2.0 + 6.0
    hmy = (hy0 + hy1) / 2.0 + 4.0
    prev_pt = None
    n_hook = 24
    for i in range(n_hook + 1):
        u = i / n_hook
        bx = (1 - u) ** 2 * hx0 + 2 * (1 - u) * u * hmx + u ** 2 * hx1
        by = (1 - u) ** 2 * hy0 + 2 * (1 - u) * u * hmy + u ** 2 * hy1
        px, py = _to_pixel(bx, by)
        if prev_pt is not None:
            w = 2.5 * (1 - u) + top_w * u
            w_int = max(1, int(round(w)))
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)

    # Main shaft: tapered vertical from top_math down to bot_math.
    x0, y0 = top_math
    x1, y1 = bot_math
    prev_pt = None
    for i in range(n + 1):
        u = i / n
        bx = x0 + (x1 - x0) * u
        by = y0 + (y1 - y0) * u
        px, py = _to_pixel(bx, by)
        if prev_pt is not None:
            w = top_w * (1 - u) + bot_w * u
            w_int = max(1, int(round(w)))
            t.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def render():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    t = ImageDraw.Draw(img)

    # STROKE 3: Central shu — descends from near top to near bottom
    # with a prominent leftward curl at the very top (per GT: the top
    # visibly curves left-then-down like a brush entry hook, ~15-18 px
    # of curl visible). Shaft sits slightly RIGHT of center.
    shu_top = (10.0, 105.0)
    shu_bot = (10.0, -130.0)
    draw_central_shu(t, shu_top, shu_bot, top_w=10, bot_w=11, hook_len=18)

    # STROKE 1: Left flanker (小撇/dian variant) — a short diagonal
    # sweep on the LEFT of the shaft. Per GT, this reads more like a
    # short 撇 (pie) than a full 点: a slanted line thickening then
    # thinning, positioned in upper-middle vertical zone. Head at
    # upper-right (near shaft), tail toward lower-left. Wait — checking
    # GT again: left dot is HEAD UPPER-LEFT, TAIL LOWER-RIGHT (standard
    # dian direction). Keep dian orientation but make it more compact
    # and less bowed.
    draw_dot(
        t,
        head_math=(-52.0, 55.0),
        tail_math=(-25.0, 30.0),
        head_w=2.5, tail_w=12.0,
        bow=(-1.5, -1.5),
    )

    # STROKE 2: Right flanker (提/short tick pointing up-right).
    # Per GT, the right dot slants from LOWER-LEFT (thin head at
    # shaft-adjacent bottom) to UPPER-RIGHT (heavier tail out and up).
    # This is a mirror of the left dot BUT with slant reversed and
    # positioned slightly higher.
    draw_dot(
        t,
        head_math=(52.0, 68.0),
        tail_math=(25.0, 45.0),
        head_w=2.5, tail_w=12.0,
        bow=(1.5, -1.5),
    )

    out = "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_077_忄/01_忄.png"
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    render()
