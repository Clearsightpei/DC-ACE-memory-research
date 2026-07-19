# p2_radical_028_人 (retry 1) — 人 radical.
#
# Retry fix idea (from sandbox): the bank's pie+na primitives at scale 0.90
# rendered as an over-fat V with na's heavy belly and tails offset from
# each other. Sandbox says: "primitives' diagonal chord + head positions
# couldn't produce the two-strokes-KISS-AT-APEX geometry cleanly."
#
# Following shared_rules "if a bank primitive doesn't fit without extreme
# transformation, draw fresh the way G1 would" — inline both strokes as
# tapered beziers with control points chosen specifically so both HEADS
# land at the same apex point.
#
# GT anatomy (from GT PNG):
#   - Apex near top-center, ~(150, 85) in PIL coords.
#   - 撇 (left-falling): starts at apex, curves left-outward, tail near
#     bottom-left ~(80, 240). Thin head (tapered start), thin tail.
#   - 捺 (right-falling): starts at apex (or just below/right), sweeps
#     down-right with a subtle belly, ends with a slight foot lift near
#     ~(230, 235). Modest belly (not the fat na of standalone 捺).
#   - The two strokes KISS at the apex — the na's head touches the pie
#     just below the pie's head, not perfectly at the same pixel.

import os
from PIL import Image, ImageDraw


CANVAS = 300


def _tapered_bezier(draw, p0, p1, p2, w0, w_mid, w1, n=80):
    """Quadratic bezier with per-segment width interpolated w0->w_mid->w1."""
    prev = None
    for i in range(n + 1):
        u = i / n
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        # width: 0..0.5 lerp w0->w_mid, 0.5..1 lerp w_mid->w1
        if u <= 0.5:
            w = w0 + (w_mid - w0) * (u / 0.5)
        else:
            w = w_mid + (w1 - w_mid) * ((u - 0.5) / 0.5)
        wi = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=wi)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    d = ImageDraw.Draw(img)

    # Revision: pass-1 was too straight (V-shape). Add real curvature.
    # Pie: pull control much further LEFT so stroke bows out convex.
    # Na: pull control DOWN-RIGHT so belly is fuller and reads as a
    # proper 捺 with a foot lift.

    # Apex in PIL coords.
    apex = (150, 78)

    # --- 撇 (pie): apex -> lower-left, strong outward bow.
    pie_start = apex                        # thin head at apex
    pie_end   = (70, 246)                   # thin tail bottom-left
    # control pulled well leftward + high so curve is convex-left.
    pie_ctrl  = (85, 155)
    _tapered_bezier(d, pie_start, pie_ctrl, pie_end,
                    w0=3.5, w_mid=6.0, w1=1.5, n=100)

    # --- 捺 (na): head just under-right of apex, sweeping down-right,
    # ending in a distinct foot lift at bottom-right.
    na_start = (156, 92)                    # head kissing pie just below apex
    na_end   = (238, 235)                   # foot lower-right (slight lift)
    # control pulled RIGHTWARD and slightly UP for a fuller belly.
    na_ctrl  = (215, 155)
    _tapered_bezier(d, na_start, na_ctrl, na_end,
                    w0=1.5, w_mid=8.0, w1=3.0, n=100)

    out = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "01_人.png"
    )
    img.save(out)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
