"""p2_radical_032_厶 (2画部首) — G3 coord-bank attempt.

厶 decomposition:
  Stroke 1: 撇折 (pie-zhe) — a soft diagonal down-left, then a horizontal
    that rises slightly right (the "折" turn). In GT the 撇 head sits
    near center-top-right, tail curls to lower-left, then the horizontal
    sweeps right (with a very shallow upward tilt toward the right end).
  Stroke 2: 点 (dian) — a short diagonal dot at the right end of the
    horizontal, going down-right.

Bank primitives fit here (radical is essentially 撇折 + 点), but the
撇折 primitive is drawn with two rigid straight lines which won't match
GT's curved 撇 and slightly-tilted 折 well. So I INLINE fresh recipes
(TR5) rather than force pie_zhe with extreme transforms.

Canvas: 300x300 PIL. Math coords: center=(150,150), +y up.
"""
from PIL import Image, ImageDraw
import os

CANVAS_SIZE = 300
CX = CY = CANVAS_SIZE / 2


def _to_pixel(mx, my):
    return CX + mx, CY - my


def draw_tapered_curve(t, p0, p1, ctrl, w_head, w_tail, n=50):
    """Quadratic-Bezier curve with linear width taper from w_head to w_tail."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * ctrl[0] + u ** 2 * p1[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * ctrl[1] + u ** 2 * p1[1]
        px, py = _to_pixel(bx, by)
        if prev is not None:
            w = w_head * (1 - u) + w_tail * u
            w_int = max(1, int(round(w)))
            t.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            t.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
        prev = (px, py)


def draw_si(t):
    # Revision: scale up the whole radical (GT occupies a large portion of
    # canvas). Push the 撇 head higher (near math +75) and drop the corner
    # lower to match the more sprawling GT silhouette. Add a small
    # entry-flick (up-then-right) to the 撇 head to mimic GT's cursive
    # opening curl.
    #
    # Stroke 1a — small entry flick at the head of 撇 (short up-hook).
    flick_start = (30.0, 75.0)
    flick_top = (35.0, 85.0)
    t.line([_to_pixel(*flick_start), _to_pixel(*flick_top)],
           fill=(0, 0, 0), width=5)

    # Stroke 1b: 撇 portion — from upper-right head down-left to corner.
    #   Head (30, 75). Corner (-70, -30). Slight left-bow (control pulled
    #   left of chord midpoint).
    p_head = (30.0, 75.0)
    p_corner = (-70.0, -30.0)
    ctrl_pie = ((p_head[0] + p_corner[0]) / 2 - 12,
                (p_head[1] + p_corner[1]) / 2 + 6)
    draw_tapered_curve(t, p_head, p_corner, ctrl_pie,
                       w_head=9.0, w_tail=6.0, n=60)

    # Head 顿笔 blob (calligraphic entry).
    hx, hy = _to_pixel(*p_head)
    t.ellipse([hx - 4, hy - 4, hx + 4, hy + 4], fill=(0, 0, 0))

    # Stroke 1c: 折 (horizontal, slight downward droop then flat) — from
    # corner sweeping right to (+70, -55). Right end lower than left
    # end, matching GT's sagging 折.
    h_left = p_corner
    h_right = (70.0, -55.0)
    ctrl_h = ((h_left[0] + h_right[0]) / 2 + 5,
              (h_left[1] + h_right[1]) / 2 - 6)
    draw_tapered_curve(t, h_left, h_right, ctrl_h,
                       w_head=7.0, w_tail=6.0, n=55)

    # Corner 顿笔 blob at the 撇-折 join.
    cx_p, cy_p = _to_pixel(*p_corner)
    t.ellipse([cx_p - 5, cy_p - 5, cx_p + 5, cy_p + 5], fill=(0, 0, 0))

    # Stroke 2: 点 — short diagonal dot at the right side, below the
    # horizontal's right end. In GT it visibly extends further down-right
    # than the horizontal ends. Head near (+45, -35), tail (+80, -75).
    d_head = (45.0, -35.0)
    d_tail = (80.0, -75.0)
    ctrl_d = ((d_head[0] + d_tail[0]) / 2 - 3,
              (d_head[1] + d_tail[1]) / 2 - 4)
    draw_tapered_curve(t, d_head, d_tail, ctrl_d,
                       w_head=3.0, w_tail=12.0, n=40)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    t = ImageDraw.Draw(img)
    draw_si(t)
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "01_厶.png")
    img.save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
