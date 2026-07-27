# p2_radical_117_手 (shǒu, "hand") — retry_1, 4 strokes.
#
# Diagnosis of retry_0 (from prior attempt PNG vs GT):
#  - Bank primitives (heng width 12, shu_gou width 12, arrow-blob hook)
#    produced ink far too heavy for GT's thin hand-drawn look.
#  - Top 撇 was too short and did NOT visibly cross the 短横; GT shows a
#    clear diagonal that starts above and passes THROUGH the 短横.
#  - Hook rendered as a solid downward-pointing arrow blob; GT hook is
#    a subtle short up-left curl.
#  - 长横 not clearly longer than 短横 (they nearly matched in width).
#
# Retry fix (per errata + form_catalog):
#  - INLINE FRESH everything at thinner widths (~5-6 px). Bank
#    primitives at 12 px thickness dominate the visual mass and cannot
#    be thinned without abandoning them (which per TR8 we are doing).
#  - 撇 as a tapered bezier from (+35, +90) DOWN-LEFT to (-35, +30) —
#    the tail must land BELOW the 短横 so it visibly crosses it.
#  - 短横 short: length ~70 px, y=+55, x centered around +5. Thin.
#  - 长横 clearly longer: length ~150 px, y=+5. Thin.
#  - 竖 shaft: from y=+40 down to y=-75 (centered x≈+8, right of 长横
#    midpoint per GT which has shaft slightly right of center).
#  - 钩: SHORT thin flick from shaft base up-and-LEFT, tapered to a
#    point (not a blob).

import os

from PIL import Image, ImageDraw

CANVAS_SIZE = 300
_HERE = os.path.dirname(os.path.abspath(__file__))


def _to_pixel(ox, oy):
    """math coords (center origin, +y up) -> PIL pixel."""
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _tapered_bezier(t, p0, p1, p2, w_head, w_tail, n=48):
    """Quadratic bezier stamp-line, math coords in, tapering width."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        r = max(0.5, w / 2.0)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        if prev is not None:
            wi = max(1, int(round(w)))
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
        prev = (px, py)


def _tapered_line(t, head_math, tail_math, w_head, w_tail, n=32):
    """Straight tapered stamp-line."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = head_math[0] + u * (tail_math[0] - head_math[0])
        by = head_math[1] + u * (tail_math[1] - head_math[1])
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        r = max(0.5, w / 2.0)
        t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        if prev is not None:
            wi = max(1, int(round(w)))
            t.line([prev, (px, py)], fill=(0, 0, 0), width=wi)
        prev = (px, py)


def draw_shou(t, ox=0.0, oy=0.0, scale=1.0):
    """手 (shǒu): 撇 + 短横 + 长横 + 竖钩."""

    s = scale

    # Stroke 1: 撇 — top diagonal starting upper-right, sweeping down-left,
    # crossing the 短横. Slight curl (bow to the left).
    _tapered_bezier(
        t,
        p0=(ox + 40 * s, oy + 92 * s),                     # head (upper-right)
        p1=(ox - 5 * s, oy + 68 * s),                      # control (slight left bow)
        p2=(ox - 40 * s, oy + 38 * s),                     # tail (below 短横 line)
        w_head=6.0 * s,
        w_tail=1.0,
    )

    # Stroke 2: 短横 — short horizontal at y=+55, x ∈ [-30, +40] (length 70).
    _tapered_line(
        t,
        head_math=(ox - 30 * s, oy + 55 * s),
        tail_math=(ox + 40 * s, oy + 55 * s),
        w_head=5.0 * s,
        w_tail=5.0 * s,
    )

    # Stroke 3: 长横 — long horizontal at y=+5, x ∈ [-75, +75] (length 150).
    _tapered_line(
        t,
        head_math=(ox - 75 * s, oy + 5 * s),
        tail_math=(ox + 75 * s, oy + 5 * s),
        w_head=5.5 * s,
        w_tail=5.5 * s,
    )

    # Stroke 4: 竖钩 — vertical shaft from y=+40 down to y=-75, slight
    # right of center (x≈+8). Ends with a SHORT up-left hook.
    shaft_x = ox + 8 * s
    shaft_top_y = oy + 40 * s
    shaft_bot_y = oy - 75 * s
    _tapered_line(
        t,
        head_math=(shaft_x, shaft_top_y),
        tail_math=(shaft_x, shaft_bot_y),
        w_head=5.0 * s,
        w_tail=4.0 * s,
    )

    # Hook: SMOOTH curved flick — bezier from shaft base curling up-and-left.
    # +y is up so hook_tip.y is HIGHER than hook_base.y — direction up-left.
    _tapered_bezier(
        t,
        p0=(shaft_x, shaft_bot_y),
        p1=(shaft_x - 6 * s, shaft_bot_y + 4 * s),
        p2=(shaft_x - 20 * s, shaft_bot_y + 16 * s),
        w_head=4.0 * s,
        w_tail=0.8,
        n=24,
    )


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_shou(t)
    out = os.path.join(_HERE, "01_手.png")
    img.save(out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
