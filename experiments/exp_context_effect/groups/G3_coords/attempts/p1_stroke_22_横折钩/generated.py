# p1_stroke_22_横折钩 — attempt.
# 横折钩 = 横折 (horizontal + 90-deg turn down) + a small up-and-left 钩 at the base.
# Follows principle-bank rules:
#  P1: hook flicks UP-AND-LEFT.
#  P2: PIL ImageDraw (no turtle/postscript).
#  P3: tapered line segments, no polygons.
#  P4: shaft uniform ~10-12px, hook 10 -> 2 taper.
#  P5: math coord convention (+y up), center origin.
#  P6: two straight tapered segments + 顿笔 blob at corner, continuous ink at join.
#
# Layout in math coords (canvas 300x300, origin at center):
#   横 body: (-90, +60) -> (+80, +60)    slight rise, uniform width.
#   竖 body: (+80, +60) -> (+80, -70)    vertical shaft.
#   钩:      base ~ (+80, -70) -> (+55, -50)  short flick up-and-left, tapered.

from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _tapered_segment(draw, p0, p1, w0, w1, steps=20, ox=0, oy=0):
    x0, y0 = p0
    x1, y1 = p1
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = x0 + (x1 - x0) * u0
        ya = y0 + (y1 - y0) * u0
        xb = x0 + (x1 - x0) * u1
        yb = y0 + (y1 - y0) * u1
        w = max(1, int(w0 + (w1 - w0) * u0))
        pa = _to_pixel(ox + xa, oy + ya)
        pb = _to_pixel(ox + xb, oy + yb)
        draw.line([pa, pb], fill=(0, 0, 0), width=w)


def draw_heng_zhe_gou(draw, ox=0, oy=0, scale=1.0):
    # 横 (horizontal, slight taper start->end for calligraphic feel; kept near-uniform).
    p_h_start = (-90 * scale, 60 * scale)
    p_corner = (80 * scale, 60 * scale)
    p_v_end = (80 * scale, -70 * scale)

    # Horizontal shaft — width 10 -> 12 (subtle press).
    _tapered_segment(draw, p_h_start, p_corner, 10 * scale, 12 * scale, steps=24, ox=ox, oy=oy)

    # 顿笔 blob at the corner (hides the miter, calligraphic turn).
    r = int(8 * scale)
    cx, cy = _to_pixel(ox + p_corner[0], oy + p_corner[1])
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # Vertical shaft — width uniform ~12 (slight taper 12 -> 11 to hint at draw pressure).
    _tapered_segment(draw, p_corner, p_v_end, 12 * scale, 11 * scale, steps=24, ox=ox, oy=oy)

    # Hook: up-and-left flick from the base of the shaft.
    # Base point sits slightly above the shaft's actual bottom so ink is continuous.
    h_base = (p_v_end[0] + 1 * scale, p_v_end[1] + 2 * scale)
    h_tip = (p_v_end[0] - 22 * scale, p_v_end[1] + 22 * scale)
    _tapered_segment(draw, h_base, h_tip, 11 * scale, 2 * scale, steps=16, ox=ox, oy=oy)

    # Small rounded cap at the shaft's very bottom so the hook root reads as filled.
    br = int(6 * scale)
    bx, by = _to_pixel(ox + p_v_end[0], oy + p_v_end[1])
    draw.ellipse([bx - br, by - br, bx + br, by + br], fill=(0, 0, 0))


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_heng_zhe_gou(draw, ox=0, oy=0, scale=1.0)
    out = __file__.rsplit("/", 1)[0] + "/01_横折钩.png"
    img.save(out)
    print("saved:", out)


if __name__ == "__main__":
    main()
