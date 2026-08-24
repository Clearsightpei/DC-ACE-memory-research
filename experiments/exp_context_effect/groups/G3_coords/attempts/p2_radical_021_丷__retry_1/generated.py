# 丷 (p2_radical_021) retry_1 — 2画 radical, two small dots at top.
#
# GT observation: two SMALL delicate dots. LEFT slants down-LEFT (like a
# small mirrored dian / short pie), RIGHT slants down-RIGHT (like a standard
# small dian). Together they form the "top of 八/兰/羊" element.
#
# Retry fix (per sandbox.md): use bank `dian` at scale 0.5 for the RIGHT dot
# (rotated 0°, standard orientation). Inline a MIRRORED dian at scale 0.5 for
# the LEFT dot, sharing dian's width profile (3 -> 14). Prior attempt drew
# the LEFT dot with tail-heavy 反点 (heavy lower-left blob) and RIGHT as a
# thin needle — both too big and mis-shaped. Retry: both small, symmetric,
# mirror-pair around x=0. Slight inward tilt so they open like a small V.
#
# Coord math: math-convention (center origin, +y up); _to_pixel flips y.

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _draw_dian_std(draw, ox, oy, scale):
    """Standard dian: thin upper-left head -> heavy lower-right tail.
    Copy of bank dian.py logic, small-scale friendly."""
    x0, y0 = -15.0 * scale, 25.0 * scale
    x1, y1 = 18.0 * scale, -20.0 * scale
    mx = (x0 + x1) / 2.0 - 4.0 * scale
    my = (y0 + y1) / 2.0 - 4.0 * scale
    w_head = max(1.5, 3.0 * scale)
    w_tail = max(2.0, 14.0 * scale)
    _stroke_bezier(draw, ox, oy, x0, y0, mx, my, x1, y1, w_head, w_tail)


def _draw_dian_mirrored(draw, ox, oy, scale):
    """Mirrored dian for LEFT dot: thin upper-RIGHT head -> heavy lower-LEFT
    tail. Same width profile as dian (3 -> 14). Just x-flipped endpoints."""
    x0, y0 = 15.0 * scale, 25.0 * scale     # thin upper-right head
    x1, y1 = -18.0 * scale, -20.0 * scale   # heavy lower-left tail
    mx = (x0 + x1) / 2.0 + 4.0 * scale       # mirror bow direction
    my = (y0 + y1) / 2.0 - 4.0 * scale
    w_head = max(1.5, 3.0 * scale)
    w_tail = max(2.0, 14.0 * scale)
    _stroke_bezier(draw, ox, oy, x0, y0, mx, my, x1, y1, w_head, w_tail)


def _stroke_bezier(draw, ox, oy, x0, y0, mx, my, x1, y1, w_head, w_tail, n=40):
    prev_pt = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        px, py = _to_pixel(ox + bx, oy + by)
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

    # SCALE 0.5 for both — 丷 is small/delicate.
    # LEFT dot centered around (ox=-30, oy=0); mirrored dian.
    _draw_dian_mirrored(draw, ox=-30.0, oy=0.0, scale=0.5)
    # RIGHT dot centered around (ox=+30, oy=0); standard dian.
    _draw_dian_std(draw, ox=+30.0, oy=0.0, scale=0.5)

    return img


if __name__ == "__main__":
    out = render()
    out.save(
        "<REPO_ROOT>/experiments/exp_context_effect/groups/G3_coords/attempts/p2_radical_021_丷__retry_1/01_丷.png"
    )
