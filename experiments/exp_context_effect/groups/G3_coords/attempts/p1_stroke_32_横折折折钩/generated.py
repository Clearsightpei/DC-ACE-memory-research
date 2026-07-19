# p1_stroke_32_横折折折钩 — attempt using G3 coord format (PIL, math coords).
#
# 横折折折钩 (heng zhe zhe zhe gou): horizontal + THREE folds + hook.
# Canonical example: the last stroke of 仍 / 奶 / 扔 (right-hand component 乃).
# Shape sequence:
#   1) short 横      — rightward
#   2) 折 down-left  — diagonal drop (like a short 撇)
#   3) 折 down-right — diagonal descent (belly of 乃)
#   4) 折 down       — short vertical drop (very short; sometimes rolled into #3)
#   5) 钩 up-left    — tapered hook flick (P1 rule)
#
# Coord convention: origin at canvas center, +y up (math). _to_pixel converts.
# Following principle_bank P2 (PIL over turtle), P3 (tapered spine),
# P4 (width profiles), P5 (math coords), P6 (concatenated tapered segments
# + corner blob).

import os
from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    px = CANVAS_SIZE / 2 + ox
    py = CANVAS_SIZE / 2 - oy
    return px, py


def _stroke_line(t, p0, p1, w0, w1, steps=60):
    """Tapered spine: stamp circles along p0->p1 with width ramp w0->w1."""
    for i in range(steps + 1):
        u = i / steps
        x = p0[0] + (p1[0] - p0[0]) * u
        y = p0[1] + (p1[1] - p0[1]) * u
        r = (w0 + (w1 - w0) * u) / 2.0
        t.ellipse([x - r, y - r, x + r, y + r], fill=(0, 0, 0))


def _dun_blob(t, pt, r):
    """顿笔 corner blob to hide miter (P6)."""
    t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))


def draw_heng_zhe_zhe_zhe_gou(t, ox=0, oy=0, scale=1.0):
    """横折折折钩 — 4 tapered segments joined at 3 corners, + hook flick."""
    # --- Segment 1: 横 (short horizontal, slight rise) ---
    # top-left area of canvas.
    p1a_m = (-70 * scale,  95 * scale)
    p1b_m = ( 30 * scale, 100 * scale)
    p1a = _to_pixel(ox + p1a_m[0], oy + p1a_m[1])
    p1b = _to_pixel(ox + p1b_m[0], oy + p1b_m[1])
    _stroke_line(t, p1a, p1b, 9 * scale, 11 * scale, steps=60)
    _dun_blob(t, p1b, 8 * scale)

    # --- Segment 2: 折 diagonal down-LEFT (like a short 撇) ---
    # From the top-right corner of #1, sweep down-left.
    p2a_m = ( 30 * scale, 100 * scale)   # coincident with p1b for continuity
    p2b_m = (-55 * scale,  20 * scale)
    p2a = _to_pixel(ox + p2a_m[0], oy + p2a_m[1])
    p2b = _to_pixel(ox + p2b_m[0], oy + p2b_m[1])
    _stroke_line(t, p2a, p2b, 11 * scale, 8 * scale, steps=70)
    _dun_blob(t, p2b, 7 * scale)

    # --- Segment 3: 折 diagonal down-RIGHT (belly) ---
    # From the bottom of #2, sweep down-right — the long belly of 乃.
    p3a_m = (-55 * scale,  20 * scale)   # coincident with p2b
    p3b_m = ( 60 * scale, -60 * scale)
    p3a = _to_pixel(ox + p3a_m[0], oy + p3a_m[1])
    p3b = _to_pixel(ox + p3b_m[0], oy + p3b_m[1])
    _stroke_line(t, p3a, p3b, 9 * scale, 12 * scale, steps=80)
    _dun_blob(t, p3b, 8 * scale)

    # --- Segment 4: 折 short vertical drop ---
    # From the bottom of #3, short drop straight down.
    p4a_m = ( 60 * scale, -60 * scale)   # coincident with p3b
    p4b_m = ( 55 * scale, -95 * scale)
    p4a = _to_pixel(ox + p4a_m[0], oy + p4a_m[1])
    p4b = _to_pixel(ox + p4b_m[0], oy + p4b_m[1])
    _stroke_line(t, p4a, p4b, 12 * scale, 9 * scale, steps=40)

    # --- Segment 5: 钩 up-and-LEFT flick (P1 hook rule) ---
    p5a_m = ( 55 * scale, -95 * scale)   # coincident with p4b
    p5b_m = ( 15 * scale, -70 * scale)   # tip up-left
    p5a = _to_pixel(ox + p5a_m[0], oy + p5a_m[1])
    p5b = _to_pixel(ox + p5b_m[0], oy + p5b_m[1])
    _stroke_line(t, p5a, p5b, 9 * scale, 2 * scale, steps=40)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_heng_zhe_zhe_zhe_gou(t, ox=0, oy=0, scale=1.0)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "01_横折折折钩.png")
    img.save(out_path)
    print("wrote", out_path)


if __name__ == "__main__":
    main()
