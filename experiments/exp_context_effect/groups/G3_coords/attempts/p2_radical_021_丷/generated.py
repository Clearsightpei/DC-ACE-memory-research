# 丷 (p2_radical_021) — 2画 radical, two dots at top (like inverted 八 / small).
#
# GT observation: LEFT dot slants down-LEFT (head at upper-right, thick tail
# at lower-left — a "反点"/left-dian, mirror of the bank's standard 点).
# RIGHT dot slants down-RIGHT (head at upper-left, tail at lower-right —
# similar to a short right-leaning 点 or 撇). Both are small, roughly
# centered horizontally, roughly middle-vertical.
#
# The bank's dian.py is right-slanting only. There is no left-dian primitive,
# and calling draw_dian would produce two identical right-slanting dots —
# wrong for 丷 which needs mirrored slants. Per TR5, INLINE both dots as
# small tapered beziers with hand-picked endpoints. Structure is copied from
# dian.py's bezier + width-ramp idiom (P4: 点 thin head -> heavy tail).
#
# Coord math: math-convention (center origin, +y up); _to_pixel flips y.

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _draw_bezier_dot(draw, x0, y0, x1, y1, mx_off, my_off, w_head, w_tail, n=40):
    """Draw one tapered dot as a quadratic bezier from (x0,y0) to (x1,y1).
    Control point is chord midpoint + (mx_off, my_off). Thickness ramps from
    w_head at u=0 to w_tail at u=1.
    """
    mx = (x0 + x1) / 2.0 + mx_off
    my = (y0 + y1) / 2.0 + my_off
    prev_pt = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(bx, by)
        w = w_head * (1 - u) + w_tail * u
        w_int = max(1, int(round(w)))
        if prev_pt is not None:
            draw.line([prev_pt, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev_pt = (px, py)


def render():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), "white")
    draw = ImageDraw.Draw(img)

    # LEFT dot (反点): head at upper-right, tail at lower-left.
    # Center around math coord (-30, 0) roughly, size ~30 px span.
    # Head (thin) at ( -15, +8 ), tail (heavy) at ( -42, -14 ).
    _draw_bezier_dot(
        draw,
        x0=-15.0, y0=8.0,       # thin upper-right head
        x1=-42.0, y1=-14.0,     # heavy lower-left tail
        mx_off=+2.0, my_off=-3.0,  # slight bow to lower-right of chord
        w_head=3.0, w_tail=11.0,
        n=40,
    )

    # RIGHT dot (right-slanting, standard-dian-like but small).
    # Head at upper-left, tail at lower-right. Center around (+30, 0).
    # Head (thin) at ( +15, +12 ), tail (thin needle) at ( +42, -18 ).
    # This right mark reads a touch more like a mini-pie than a heavy dot
    # in the GT — head slightly thicker, tail tapered.
    _draw_bezier_dot(
        draw,
        x0=+15.0, y0=12.0,      # thin upper-left head
        x1=+42.0, y1=-18.0,     # tapered lower-right tail
        mx_off=-2.0, my_off=+3.0,  # slight bow to upper-left of chord
        w_head=8.0, w_tail=2.5,
        n=40,
    )

    return img


if __name__ == "__main__":
    out = render()
    out.save(
        "/Users/peilinwu/Documents/AI memory research/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_021_丷/01_丷.png"
    )
