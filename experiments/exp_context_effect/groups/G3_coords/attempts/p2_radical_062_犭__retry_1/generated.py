# p2_radical_062_犭 — quan-pang (dog radical), 3 strokes. RETRY_1.
#
# Prior attempt (attempts/p2_radical_062_犭/) failed:
#   - The upper "X" (strokes 1+2) was too small / too high, disconnected
#     from the spine.
#   - Spine 弯钩 (stroke 3) was too far right, too vertical, no visible
#     crossing with the X, and the bottom hook was nearly invisible.
#
# Fix for retry_1 (per sandbox/errata "inline as one continuous curl"):
#   - Enlarge and center the upper X so strokes 1 and 2 clearly cross.
#   - The spine (stroke 3) is a big 弯钩: starts near the crossing point,
#     bulges rightward, sweeps left at bottom, and terminates in a
#     visible up-left hook.
#   - Move the entire radical slightly LEFT (radical position) so it
#     reads as a tall narrow column.
#
# GT structure (3 strokes, top-down, MMH order):
#   1) Short 撇 (upper) — top-right head, sweeps down-left
#   2) Medium 撇 — starts higher-right than #1, sweeps deeper down-left
#      crossing #1 to form the classic 犭 "X" at the top
#   3) Long 弯钩 — begins BELOW the X (near the crossing endpoint of #2),
#      curves down and right into a belly, then sweeps back to the left
#      into a tail that hooks UP-LEFT.
#
# Bank fit: pie.py and wan_gou.py are designed for standalone use at
# canvas scale and cannot match the specific placements/curvatures the
# radical needs. INLINE all three strokes per TR5.
#
# PIL, 300×300, math coords (center origin, +y up).

import os
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


def _cbez(p0, p1, p2, p3, steps):
    pts = []
    for i in range(steps + 1):
        u = i / steps
        b = (1 - u)
        x = b**3 * p0[0] + 3 * b*b * u * p1[0] + 3 * b * u*u * p2[0] + u**3 * p3[0]
        y = b**3 * p0[1] + 3 * b*b * u * p1[1] + 3 * b * u*u * p2[1] + u**3 * p3[1]
        pts.append((x, y))
    return pts


def _draw_tapered(d, pts, w_head, w_tail):
    n = len(pts)
    for i in range(n - 1):
        u = i / (n - 1)
        w = w_head + (w_tail - w_head) * u
        w_int = max(1, int(round(w)))
        p1 = _to_pixel(pts[i][0], pts[i][1])
        p2 = _to_pixel(pts[i + 1][0], pts[i + 1][1])
        d.line([p1, p2], fill=(0, 0, 0), width=w_int)
        r = w_int / 2.0
        d.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r], fill=(0, 0, 0))


def draw_quan_pang(d):
    # Radical column center around x ≈ -20 (left-radical position),
    # spanning y from about +100 (top) down to -95 (bottom hook).

    # ---- Stroke 1: short upper 撇 ----
    # High and short, tail already down-left.  Its midpoint sits at
    # ~(-13, +72). We want stroke 2 to cross THROUGH that midpoint.
    s1_p0 = (+5, +95)
    s1_ctrl = (-5, +82)
    s1_p1 = (-30, +55)
    pts1 = _qbez(s1_p0, s1_ctrl, s1_p1, 30)
    _draw_tapered(d, pts1, w_head=6, w_tail=2)

    # ---- Stroke 2: medium 撇 that CROSSES stroke 1 ----
    # To make an X, stroke 2 must start to the LEFT of stroke 1's head
    # (or higher) and its trajectory must intersect stroke 1's segment.
    # Trick: start at UPPER-LEFT of stroke 1's head, sweep down-RIGHT
    # first through stroke 1's midpoint, then continue down-LEFT below.
    # Actually GT 犭 form: stroke 2 head is roughly at same x as stroke1
    # head, but starts LOWER and travels a much LONGER path down-left,
    # its trajectory begins from ABOVE-RIGHT and ends BELOW-LEFT of the
    # crossing point. So p0 stays high-right, tail goes far-lower-left.
    # For visible crossing, put s2 through (-13, +72), which is s1's mid.
    s2_p0 = (+22, +88)
    s2_ctrl = (-13, +72)   # forces path through this crossing point
    s2_p1 = (-50, +15)
    pts2 = _qbez(s2_p0, s2_ctrl, s2_p1, 60)
    _draw_tapered(d, pts2, w_head=8, w_tail=2)

    # ---- Stroke 3: long 弯钩 spine ----
    # Starts near stroke-2's mid-upper region (attached to the X body),
    # bulges rightward, dips down-and-around, and terminates in a
    # crisp UP-LEFT hook. Use a cubic bezier for the belly.
    #
    # Anchors:
    #   A: (-8, +40)  — origin just below the X crossing
    #   ctrl1: (+35, +5)  — pull right (belly)
    #   ctrl2: (+30, -50) — continue right then curve back
    #   B: (-8, -80)  — bottom, before the hook
    A = (-8, +40)
    C1 = (+35, +5)
    C2 = (+30, -50)
    B = (-8, -80)
    body = _cbez(A, C1, C2, B, 80)

    # Tapered spine: thin head, thick belly, thinner into the hook root
    n = len(body)
    for i in range(n - 1):
        u = i / (n - 1)
        # belly at u ≈ 0.5
        if u < 0.5:
            w = 3 + (10 - 3) * (u / 0.5)
        else:
            w = 10 - (10 - 5) * ((u - 0.5) / 0.5)
        w_int = max(3, int(round(w)))
        p1 = _to_pixel(body[i][0], body[i][1])
        p2 = _to_pixel(body[i + 1][0], body[i + 1][1])
        d.line([p1, p2], fill=(0, 0, 0), width=w_int)
        r = w_int / 2.0
        d.ellipse([p2[0] - r, p2[1] - r, p2[0] + r, p2[1] + r], fill=(0, 0, 0))

    # ---- Hook (钩): visible up-left flick from B ----
    # Continue from spine tail, curve LEFT and clearly UP.  Bigger hook.
    H_ctrl = (-35, -78)
    H_tip = (-50, -60)
    hook = _qbez(B, H_ctrl, H_tip, 30)
    _draw_tapered(d, hook, w_head=6, w_tail=2)


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
