# BANK_DEVIATION
# skipped: bing_ren.py (left half 仌)
# reason: bing_ren is calibrated for FULL-canvas 仌 in math-coords; 俎's left
#   column occupies only ~45% of canvas width and needs to sit alongside 且 at
#   right — inlining thin pixel-coord 人 pair is cleaner than shrinking bank's
#   calligraphic weights and re-mapping coord conventions.
# fresh_component: zu_left_bing_thin (compressed thin 仌 for L-R char)
#
# Also inlines a fresh right-side 且 (no bank entry for 且; ri.py is 4-stroke
# 日, not 5-stroke 且 with extending bottom heng).
# Character 俎 = 仌 (left) + 且 (right), 9 strokes.

from PIL import Image, ImageDraw
import math
import os

CANVAS = 300


def _line(t, p0, p1, w):
    t.line([p0, p1], fill=(0, 0, 0), width=max(1, int(round(w))))


def _bezier_taper(t, x0, y0, x1, y1, bow_perp, w_head, w_tail):
    """Quadratic bezier from (x0,y0) to (x1,y1), bowed perp by bow_perp,
    linearly tapered from w_head to w_tail. Pixel coords directly."""
    mx0 = (x0 + x1) / 2.0
    my0 = (y0 + y1) / 2.0
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    perp_x, perp_y = -dy / L, dx / L
    mx = mx0 + perp_x * bow_perp
    my = my0 + perp_y * bow_perp
    n = 40
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * x0 + 2 * (1 - u) * u * mx + u ** 2 * x1
        by = (1 - u) ** 2 * y0 + 2 * (1 - u) * u * my + u ** 2 * y1
        w = w_head + (w_tail - w_head) * u
        wi = max(1, int(round(w)))
        if prev is not None:
            t.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            t.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def _ren(t, apex, pie_tail, na_tail, w_head=5.0):
    """Small 人: pie bowed left, na bowed right, meeting at apex."""
    _bezier_taper(t, apex[0], apex[1], pie_tail[0], pie_tail[1],
                  bow_perp=-4.0, w_head=w_head, w_tail=1.5)
    _bezier_taper(t, apex[0], apex[1], na_tail[0], na_tail[1],
                  bow_perp=+4.0, w_head=2.5, w_tail=1.5)


def draw_zu(img):
    t = ImageDraw.Draw(img)

    # ==== LEFT: 仌 (two pie+dian pairs stacked, thin, left column) ====
    # Upper pair: long pie down-left + short dian to right
    _bezier_taper(t, 95, 55, 50, 135, bow_perp=-6.0, w_head=6.0, w_tail=1.5)
    _bezier_taper(t, 85, 90, 120, 130, bow_perp=+3.0, w_head=2.5, w_tail=6.0)

    # Lower pair: same pattern, slightly larger
    _bezier_taper(t, 95, 155, 40, 240, bow_perp=-7.0, w_head=6.0, w_tail=1.5)
    _bezier_taper(t, 85, 195, 125, 235, bow_perp=+3.0, w_head=2.5, w_tail=6.5)

    # ==== RIGHT: 且 (5 strokes; bottom heng extends wide) ====
    x_left = 155
    x_right = 265
    y_top = 55
    y_bot = 245
    y_mid1 = 118
    y_mid2 = 182
    w = 6
    w_mid = 5

    # Stroke 1: left 竖
    _line(t, (x_left, y_top), (x_left, y_bot), w)
    # Stroke 2: 横折 (top heng + right shu)
    _line(t, (x_left, y_top), (x_right, y_top), w)
    _line(t, (x_right, y_top), (x_right, y_bot), w)
    # Stroke 3: interior 横 upper
    _line(t, (x_left + 3, y_mid1), (x_right - 3, y_mid1), w_mid)
    # Stroke 4: interior 横 lower
    _line(t, (x_left + 3, y_mid2), (x_right - 3, y_mid2), w_mid)
    # Stroke 5: bottom 横 — wide, extends past box on both sides
    y_bottom_heng = 258
    _line(t, (35, y_bottom_heng), (280, y_bottom_heng), w + 1)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), (255, 255, 255))
    draw_zu(img)
    out_path = os.path.join(os.path.dirname(__file__), "01_俎.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
