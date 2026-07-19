"""p2_radical_102_耂 (lao3, "old" radical, 4 strokes).

Stroke order (canonical):
1. 横 (short top horizontal) — upper region
2. 竖 (short vertical) — crosses stroke 1 near its middle-left
3. 横 (long lower horizontal) — spans wider, slight upward tilt
4. 撇 (long diagonal sweep) — starts upper-right, sweeps down-left,
   crossing the long horizontal and exiting bottom-left of canvas.

Approach: inline-fresh per TR8/TR9. The heng primitive at scale ~0.35
would work for the two horizontals, but the SHORT top heng and TILTED
long heng below need slight per-item tuning (short heng is stubby, long
heng has an upward-right tilt). The 竖 is only ~40 px tall — well below
the scale=0.4 threshold, so inline. The 撇 needs a much LONGER, more
sweeping shape than pie.py's canonical (which is designed to fit inside
the canvas center) — inline as a fresh bezier from ~(+80,+70) to
~(-100,-100).

Math-coord convention: center origin, +y up. Converted to PIL pixels
via _to_pixel.
"""

from PIL import Image, ImageDraw
import sys, os

# Make bank importable for reference (we don't call primitives here per
# TR8 inline-fresh rationale — but keep math convention identical).
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "success_bank", "code")))

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def draw_short_heng(t, cx, cy, half_len, thickness):
    """Simple flat horizontal, centered at math-coord (cx, cy)."""
    x0, y0 = _to_pixel(cx - half_len, cy)
    x1, y1 = _to_pixel(cx + half_len, cy)
    t.line([(x0, y0), (x1, y1)], fill=(0, 0, 0), width=thickness)


def draw_tilted_heng(t, x_left, y_left, x_right, y_right, thickness):
    """Slightly tilted horizontal from left-end to right-end (math coords)."""
    p0 = _to_pixel(x_left, y_left)
    p1 = _to_pixel(x_right, y_right)
    t.line([p0, p1], fill=(0, 0, 0), width=thickness)


def draw_short_shu(t, cx, y_top, y_bot, thickness):
    """Short vertical from (cx, y_top) down to (cx, y_bot) in math coords."""
    p0 = _to_pixel(cx, y_top)
    p1 = _to_pixel(cx, y_bot)
    t.line([p0, p1], fill=(0, 0, 0), width=thickness)


def draw_long_pie(t, x0, y0, x1, y1, ctrl_dx=-15.0, ctrl_dy=5.0,
                  w_head=9.0, w_tail=1.0, n=80):
    """Fresh long tapered bezier from head (x0,y0) to tip (x1,y1).

    Math coords. ctrl_dx/ctrl_dy offset the chord midpoint to bow the
    sweep leftward-downward.
    """
    mx = (x0 + x1) / 2.0 + ctrl_dx
    my = (y0 + y1) / 2.0 + ctrl_dy

    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)

    # --- Stroke 1: short top 横 ---
    # Slightly LEFT of center, at math-y ~ +50.
    # Half-length ~30. Thickness ~7.
    draw_short_heng(t, cx=-15.0, cy=50.0, half_len=32.0, thickness=7)

    # --- Stroke 2: short 竖 crossing stroke 1 ---
    # In GT the vertical protrudes above the top heng (like a small hat)
    # and crosses down through it. From y=+80 down to y=+30, at x=-5.
    draw_short_shu(t, cx=-5.0, y_top=80.0, y_bot=30.0, thickness=7)

    # --- Stroke 3: long lower 横 (nearly flat, very slight slope) ---
    # From (-110, +8) to (+110, +5). Wide sweep, ~220 px. Thickness ~8.
    draw_tilted_heng(t, x_left=-110.0, y_left=8.0,
                     x_right=110.0, y_right=5.0, thickness=8)

    # --- Stroke 4: long 撇 sweeping from RIGHT of the long heng down-left,
    # crossing everything and exiting bottom-left of canvas.
    # Head at (+90, +55), tail at (-115, -120).
    draw_long_pie(t, x0=90.0, y0=55.0, x1=-115.0, y1=-120.0,
                  ctrl_dx=-30.0, ctrl_dy=-20.0,
                  w_head=9.0, w_tail=1.0, n=100)

    out_path = os.path.join(os.path.dirname(__file__), "01_耂.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
