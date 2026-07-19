# p2_radical_062_犭 — quan-pang (dog radical), 3 strokes.
#
# Stroke decomposition (from GT):
#   1) Short 撇 at top (small pie, ~upper-right area, sweeps down-left).
#   2) Long 弯钩 that starts at top-right, curves down through where the
#      first 撇 crosses it, and flicks left at the bottom.
#   3) Medium 撇 starting from the crossing point (mid-body) sweeping
#      down-left to the bottom-left of the radical.
#
# The radical form is a narrow, tall column (typical left-radical shape).
# We inline all three strokes with tuned coords so they meet at the
# expected crossing near y ≈ +30 (canvas center 150, radical top).
#
# Bank fit: primitive pie.py is designed for a full-canvas 撇; radical's
# strokes are much smaller and specifically-placed, so we INLINE (per TR5).
# wan_gou.py is close in idiom to stroke #2 but with different curvature
# and much longer body — inlined too.
#
# PIL, 300×300, math coords (center origin, +y up).

import os
import sys
from PIL import Image, ImageDraw

CANVAS_SIZE = 300


def _to_pixel(ox, oy):
    return CANVAS_SIZE / 2 + ox, CANVAS_SIZE / 2 - oy


def _qbez(p0, p1, p2, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def _draw_tapered(d, pts, w_head, w_tail, profile="linear"):
    """Draw a tapered stroke through pts (math coords)."""
    n = len(pts)
    for i in range(n - 1):
        u = i / (n - 1)
        if profile == "linear":
            w = w_head + (w_tail - w_head) * u
        elif profile == "belly":  # thin - thick(0.5) - thin
            if u < 0.5:
                w = w_head + (w_tail - w_head) * (u / 0.5)
            else:
                w = w_tail + (w_head - w_tail) * ((u - 0.5) / 0.5)
        w_int = max(1, int(round(w)))
        p1 = _to_pixel(pts[i][0], pts[i][1])
        p2 = _to_pixel(pts[i + 1][0], pts[i + 1][1])
        d.line([p1, p2], fill=(0, 0, 0), width=w_int)
        r = w_int / 2.0
        d.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r], fill=(0, 0, 0))


def draw_quan_pang(d):
    # REVISION: previous attempt had strokes not crossing visibly and
    # stroke 2 too vertical.  In GT, strokes 1 and 2 form a clear "X"
    # in the upper half; stroke 3 is a very long 弯钩 that starts high
    # and curves DEEP down and around to a hook near the bottom.
    #
    # Coordinate anchors (math coords, canvas center = origin):
    #   Stroke 1 (short 撇, upper): head (+5, +90) high -> tail (-25, +55).
    #     Goes down-left crossing near (-10, +65).
    #   Stroke 2 (medium 撇, crosses stroke 1): head (+25, +75) top-right
    #     -> tail (-30, +10), passes through the crossing area (~-10, +45).
    #     Together with stroke 1 they make the X-shape.
    #   Stroke 3 (long 弯钩, spine): starts near the top (+30, +60),
    #     curves down through (+20, 0), sweeps to (+10, -80), hook flicks
    #     up-left to (-15, -70).

    # ---- Stroke 1: short 撇 upper ----
    s1_p0 = (5, 90)
    s1_ctrl = (-8, 78)
    s1_p1 = (-25, 55)
    pts1 = _qbez(s1_p0, s1_ctrl, s1_p1, 30)
    _draw_tapered(d, pts1, w_head=7, w_tail=2, profile="linear")

    # ---- Stroke 2: medium 撇 crossing through stroke 1 ----
    s2_p0 = (25, 75)
    s2_ctrl = (5, 50)
    s2_p1 = (-30, 10)
    pts2 = _qbez(s2_p0, s2_ctrl, s2_p1, 50)
    _draw_tapered(d, pts2, w_head=9, w_tail=1, profile="linear")

    # ---- Stroke 3: long 弯钩 (spine) ----
    # A tall arc from top-right, bowing right, curving in at bottom, hooking left.
    s3_p0 = (30, 60)              # top start (thin head)
    s3_ctrl_upper = (35, 15)      # bulges right
    s3_mid = (25, -25)
    upper = _qbez(s3_p0, s3_ctrl_upper, s3_mid, 30)
    s3_ctrl_lower = (18, -70)
    s3_bottom = (5, -90)
    lower = _qbez(s3_mid, s3_ctrl_lower, s3_bottom, 40)
    body = upper + lower[1:]

    n = len(body)
    for i in range(n - 1):
        u = i / (n - 1)
        # thin head -> belly at u≈0.5 -> thinner before hook
        if u < 0.5:
            w = 3 + (8 - 3) * (u / 0.5)
        else:
            w = 8 - (8 - 4) * ((u - 0.5) / 0.5)
        w_int = max(3, int(round(w)))
        p1 = _to_pixel(body[i][0], body[i][1])
        p2 = _to_pixel(body[i + 1][0], body[i + 1][1])
        d.line([p1, p2], fill=(0, 0, 0), width=w_int)
        r = w_int / 2.0
        d.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r], fill=(0, 0, 0))

    # Hook flick up-left from the bottom.
    hook_tip = (-18, -78)
    hook_ctrl = (-5, -88)
    hook = _qbez(s3_bottom, hook_ctrl, hook_tip, 20)
    m = len(hook)
    for i in range(m - 1):
        u = i / (m - 1)
        w = 5 - (5 - 2) * u
        w_int = max(2, int(round(w)))
        p1 = _to_pixel(hook[i][0], hook[i][1])
        p2 = _to_pixel(hook[i + 1][0], hook[i + 1][1])
        d.line([p1, p2], fill=(0, 0, 0), width=w_int)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    d = ImageDraw.Draw(img)
    draw_quan_pang(d)
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "01_犭.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
