# p2_radical_059_门 — G3 coord-bank RETRY_1.
#
# 门 (mén) — 3-stroke radical. Prior attempt failed:
#   - Hook on 横折钩 read as a small down-pointing arrowhead (base blob
#     + short taper). Needed a longer, thinner UP-LEFT flick with no
#     terminal blob. (P1: hook = tapered short line pointing up-left.)
#   - Dot rendered as a bezier-comma that read as ambiguous; GT shows
#     a short pie-like flick, thin at top-right, thicker at bottom-left.
#   - Bank primitive heng_zhe_gou is symmetric around center; 门 has
#     asymmetric placement (horizontal starts near mid, ends far right).
#     Continue inlining per TR5.
#
# Composition plan (300x300 canvas, math coords, center = (150,150), +y up):
#   - Dot (short pie): from (-38, +82) down-left to (-58, +62).
#     Thin head at upper-right, tapering slightly thicker toward tail.
#   - Left 竖: from (-52, +55) down to (-52, -100). Straight vertical.
#     Deliberate gap between dot's tail and 竖's head (as in GT).
#   - Right 横折钩: horizontal from (-20, +82) to (+72, +82),
#     descending vertical to (+72, -95), then hook UP-and-LEFT to
#     (+48, -70). Long, thin, needle-tipped hook. No terminal blob.

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    """Math-coord (center origin, +y up) -> PIL pixel (top-left, +y down)."""
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _tapered_segment(draw, p0, p1, w0, w1, steps=28, ox=0, oy=0):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, w0 + (w1 - w0) * u0)
        w_int = max(1, int(round(w)))
        pa = _to_pixel(ox + xa, oy + ya)
        pb = _to_pixel(ox + xb, oy + yb)
        draw.line([pa, pb], fill=(0, 0, 0), width=w_int)


def draw_dot_pie(draw, ox=0, oy=0):
    """门's top-left dot: short pie flick, thin upper-right -> thicker
    lower-left. Length ~28px, thickness 3 -> 8."""
    p_head = (-38, 82)  # upper-right start (thin)
    p_tail = (-58, 62)  # lower-left end (thicker)
    _tapered_segment(draw, p_head, p_tail, 3, 8, steps=24, ox=ox, oy=oy)
    # Small rounded cap at tail so it doesn't look sliced.
    tx, ty = _to_pixel(ox + p_tail[0], oy + p_tail[1])
    r = 4
    draw.ellipse([tx - r, ty - r, tx + r, ty + r], fill=(0, 0, 0))


def draw_left_shu(draw, ox=0, oy=0):
    """门's left vertical. Straight 竖 with slight taper (10 -> 11)."""
    p_top = (-52, 55)
    p_bot = (-52, -100)
    _tapered_segment(draw, p_top, p_bot, 10, 11, steps=32, ox=ox, oy=oy)
    # Small head cap so top doesn't look chopped.
    tx, ty = _to_pixel(ox + p_top[0], oy + p_top[1])
    r = 5
    draw.ellipse([tx - r, ty - r, tx + r, ty + r], fill=(0, 0, 0))


def draw_heng_zhe_gou_inline(draw, ox=0, oy=0):
    """门's right 横折钩. Horizontal + vertical + up-left hook."""
    p_h_start = (-20, 82)
    p_corner = (72, 82)
    p_v_end = (72, -95)

    # Horizontal top — uniform-ish.
    _tapered_segment(draw, p_h_start, p_corner, 10, 11, steps=30, ox=ox, oy=oy)

    # Small head cap at horizontal start (顿笔).
    hx, hy = _to_pixel(ox + p_h_start[0], oy + p_h_start[1])
    r_h = 5
    draw.ellipse([hx - r_h, hy - r_h, hx + r_h, hy + r_h], fill=(0, 0, 0))

    # Corner blob (顿笔) — moderate size.
    r_corner = 6
    cx, cy = _to_pixel(ox + p_corner[0], oy + p_corner[1])
    draw.ellipse([cx - r_corner, cy - r_corner, cx + r_corner, cy + r_corner], fill=(0, 0, 0))

    # Vertical descent (right shaft).
    _tapered_segment(draw, p_corner, p_v_end, 11, 10, steps=34, ox=ox, oy=oy)

    # Hook: UP-and-LEFT from base of vertical. Long, thin, needle tip.
    # In math coords, tip.y > base.y means tip is HIGHER (up). Good.
    # Prior mistake: base blob + short taper => arrowhead. Fix: longer
    # (30 px chord), thinner (start 9 taper to 1), no terminal blob,
    # start hook base slightly ABOVE vertical's bottom so shaft and
    # hook merge without extra blob.
    h_base = (72, -92)
    h_tip = (44, -64)
    _tapered_segment(draw, h_base, h_tip, 9, 1, steps=26, ox=ox, oy=oy)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    draw_dot_pie(draw)
    draw_left_shu(draw)
    draw_heng_zhe_gou_inline(draw)

    import os
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "01_门.png")
    img.save(out_path)
    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
