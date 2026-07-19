# 尸 (shi) radical — 3 strokes.
# Structural decomposition (from GT PNG at gt/phase2/尸.png):
#   1) 横折 (top): a horizontal top-bar that turns 90° down at the right,
#      forming the top and right side of a small rectangle in the upper canvas.
#   2) 横 (middle): a short horizontal crossing left-to-right at mid-height,
#      meeting the descended tail of stroke 1.
#   3) 撇 (long pie): starts at the top-LEFT corner (weld to stroke 1's head),
#      sweeps down-and-left in a long soft curve, tail near bottom-left.
#
# The bank has heng_zhe, heng, and pie — but this radical needs
# custom placements and a much LONGER pie than the standalone primitive,
# so I inline all three strokes (TR5: avoid extreme scale stretching).
# Coord math: center-origin, +y UP, converted to PIL by _to_pixel.

import sys, os
from PIL import Image, ImageDraw

CANVAS_SIZE = 300

def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def draw_heng_zhe_shi(t):
    """Stroke 1: 横折 forming top + right side of 尸's upper box.
    Top horizontal: from (-55, +85) to (+45, +85).
    Fold-down: from (+45, +85) to (+40, +10) (slight leftward lean, typical of 尸)."""
    ink_w = 8
    a = _to_pixel(-55, 90)
    b = _to_pixel(50, 90)
    c = _to_pixel(45, 5)
    # Top horizontal
    t.line([a, b], fill=(0, 0, 0), width=ink_w)
    # Right vertical (slightly leaning inward)
    t.line([b, c], fill=(0, 0, 0), width=ink_w)
    # Corner 顿笔 blob
    r = ink_w / 2 + 1
    for pt in (a, b, c):
        t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))


def draw_heng_middle(t):
    """Stroke 2: middle 横 crossing at y ≈ +15, from x=-45 to x=+40.
    Meets the tail of stroke 1's fold-down at the right."""
    ink_w = 7
    a = _to_pixel(-48, 10)
    b = _to_pixel(48, 10)
    t.line([a, b], fill=(0, 0, 0), width=ink_w)
    r = ink_w / 2
    for pt in (a, b):
        t.ellipse([pt[0] - r, pt[1] - r, pt[0] + r, pt[1] + r], fill=(0, 0, 0))


def draw_long_pie(t):
    """Stroke 3: long 撇 starting at the top-LEFT corner of stroke 1
    (weld point ≈ (-55, +85)) sweeping down-left with a soft bow to
    lower-left tail (≈ -95, -110). Tapered brush profile: thick head,
    needle tail."""
    x0, y0 = -55.0, 90.0    # head (welded to heng_zhe top-left)
    x1, y1 = -100.0, -125.0  # tail (lower-left, extends to bottom)
    # Bow the sweep slightly to the left of the chord for calligraphic feel.
    mx = (x0 + x1) / 2 - 15.0
    my = (y0 + y1) / 2 + 5.0

    n_segments = 60
    w_head = 10.0
    w_tail = 1.0

    prev = None
    for i in range(n_segments + 1):
        u = i / n_segments
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
    d = ImageDraw.Draw(img)

    draw_heng_zhe_shi(d)
    draw_heng_middle(d)
    draw_long_pie(d)

    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "01_尸.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
