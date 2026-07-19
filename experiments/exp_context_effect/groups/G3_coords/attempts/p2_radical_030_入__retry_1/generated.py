# p2_radical_030_入 — retry #1 (inline-fresh per errata fix).
#
# Errata fix idea (from sandbox.md):
#   "Same as 人 but with na starting mid-shaft on pie. Primitive can't
#    express 'head on another stroke's u=0.3'. Inline both as fresh
#    beziers."
#
# So this attempt does NOT call draw_pie / draw_na from the Success
# Bank. Both strokes are inlined as fresh quadratic-bezier polylines
# with tapered widths (顿笔 blobs at ends). Coordinates are chosen
# from GT observation, not from primitive defaults.
#
# GT reading (PIL coords, canvas 300x300):
#   pie:  head near (150, 88), gently bowed left through (~110, 175),
#         tail at (~78, 253). Uniform-ish width, slight taper at both
#         ends.
#   na:   head sits ON the pie shaft at roughly PIL (147, 128) — this
#         is ~28% down the pie shaft from its head. From there it
#         sweeps down-right through (~200, 215) to tail at (~245, 258).
#         Na is the "fat" stroke — thin at head, swelling to broad
#         near the tail with a slight lift-off (捺's tail 顿笔).
#
# Widths chosen to match brush-pen feel at 300x300:
#   pie: 6px at head, 5px along shaft, 3px at tail (thins to a point).
#   na:  3px at head, growing to ~9px near tail, then quick taper to
#        4px at tail (捺-style swell + tail 顿笔).

import os
from PIL import Image, ImageDraw


def _quad_bezier_points(p0, p1, p2, n=60):
    """Return n+1 sample points along quadratic bezier."""
    pts = []
    for i in range(n + 1):
        u = i / n
        x = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0]
        y = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1]
        pts.append((x, y))
    return pts


def _draw_tapered_stroke(draw, points, widths):
    """Draw a polyline with per-segment interpolated width.

    widths: list of (u_fraction, width_px) tuples, u in [0,1].
    """
    n = len(points) - 1
    for i in range(n):
        u0 = i / n
        u1 = (i + 1) / n
        u_mid = (u0 + u1) / 2
        # interpolate width at u_mid
        w = widths[0][1]
        for j in range(len(widths) - 1):
            ua, wa = widths[j]
            ub, wb = widths[j + 1]
            if ua <= u_mid <= ub:
                t_ = (u_mid - ua) / (ub - ua) if ub > ua else 0
                w = wa + t_ * (wb - wa)
                break
        else:
            if u_mid > widths[-1][0]:
                w = widths[-1][1]
        w = max(1, int(round(w)))
        draw.line([points[i], points[i + 1]], fill="black", width=w)
        # round joint
        r = w / 2
        x, y = points[i + 1]
        draw.ellipse([x - r, y - r, x + r, y + r], fill="black")


def main():
    img = Image.new("RGB", (300, 300), "white")
    d = ImageDraw.Draw(img)

    # REVISION (pass 2):
    # - Pie was too straight. Push control point further left to add
    #   more visible bow (GT clearly bows left in the middle).
    # - Na tail sweeps more toward horizontal in GT — lower the control
    #   point so the curve levels off before the tail 顿笔.

    # --- 撇 (pie) — dominant sweeping stroke, bowed left ---
    pie_head = (152, 86)
    pie_ctrl = (92, 172)   # further left for more visible bow
    pie_tail = (74, 256)
    pie_pts = _quad_bezier_points(pie_head, pie_ctrl, pie_tail, n=80)
    # widths: 顿笔 at head (6), body (5), taper to 2 at tail
    pie_widths = [(0.0, 6), (0.08, 6), (0.5, 5), (0.85, 3), (1.0, 2)]
    _draw_tapered_stroke(d, pie_pts, pie_widths)

    # --- 捺 (na) — starts ON pie shaft (~28% down) ---
    na_head = _quad_bezier_points(pie_head, pie_ctrl, pie_tail, n=100)[28]
    # nudge slightly right so the head reads as "kissing" the pie interior
    na_head = (na_head[0] + 1, na_head[1] - 2)
    # control point lower & further right → tail levels off more before
    # hitting the terminal 顿笔
    na_ctrl = (205, 225)
    na_tail = (252, 258)
    na_pts = _quad_bezier_points(na_head, na_ctrl, na_tail, n=80)
    # widths: thin at head (3), swell to 9 near u=0.85, taper to 4 at tail
    na_widths = [(0.0, 3), (0.15, 4), (0.55, 7), (0.85, 9), (1.0, 4)]
    _draw_tapered_stroke(d, na_pts, na_widths)

    out = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_入.png"
    )
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
