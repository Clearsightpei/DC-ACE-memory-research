"""p3_char_0033_刀 (dao) — G3 coord attempt (revised against clean GT).

刀 has 2 strokes:
  1) 横折钩 — thin 横 head at top, curving smoothly down on the right
     (not a sharp right angle in this GT — more of a rounded arc),
     ending with a small hook at the bottom that curls up-left.
  2) 撇 — long sweeping left-falling stroke starting near the LEFT
     end of the 横 (around x=-70..-60), passing through the top bar,
     and extending down-left well below the base.

Key GT observations after regen:
  - Envelope right side is a smooth CURVE, not a hard 90° corner.
  - 撇 starts near the LEFT of 横 and sweeps out below-left of
    the whole envelope.
  - Character is compact upper-right of center.

G3 constraint: numeric (ox, oy, scale) coords only, no anchors/joints.
"""

from PIL import Image, ImageDraw
import os
import sys

# Make sibling success_bank/code importable so we can reuse the frozen 撇 primitive.
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE, "success_bank", "code"))

from pie import draw_pie  # noqa: E402


CANVAS = 300


def _to_pixel(ox, oy):
    """Math coord -> PIL pixel (center origin, +y up)."""
    return CANVAS / 2 + ox, CANVAS / 2 - oy


def _tapered_curve(draw, pts, widths, ox=0, oy=0, n=48):
    """Interpolate a Catmull-Rom-ish smooth curve through pts with widths per waypoint."""
    # For simplicity use quadratic Bezier chained through midpoints.
    if len(pts) < 2:
        return
    # Build sequence: p0, m01, p1, m12, p2, ...
    # Use midpoints as endpoints of quadratics with pts[i] as control.
    endpoints = [pts[0]]
    for i in range(len(pts) - 1):
        mx = (pts[i][0] + pts[i + 1][0]) / 2
        my = (pts[i][1] + pts[i + 1][1]) / 2
        endpoints.append((mx, my))
    endpoints.append(pts[-1])
    # widths at endpoints: derived by mirror
    w_end = [widths[0]]
    for i in range(len(widths) - 1):
        w_end.append((widths[i] + widths[i + 1]) / 2)
    w_end.append(widths[-1])

    # Now for each segment, draw a quadratic with control = pts[i].
    # segments: (endpoints[0], pts[0], endpoints[1]), (endpoints[1], pts[1], endpoints[2]), ...
    seg_count = len(pts)
    total_len_prev = None
    for si in range(seg_count):
        a = endpoints[si]
        c = pts[si]
        b = endpoints[si + 1]
        w_a = w_end[si]
        w_b = w_end[si + 1]
        prev = None
        for k in range(n + 1):
            u = k / n
            bx = (1 - u) ** 2 * a[0] + 2 * (1 - u) * u * c[0] + u ** 2 * b[0]
            by = (1 - u) ** 2 * a[1] + 2 * (1 - u) * u * c[1] + u ** 2 * b[1]
            w = w_a + (w_b - w_a) * u
            w_int = max(1, int(round(w)))
            px, py = _to_pixel(ox + bx, oy + by)
            if prev is not None:
                draw.line([prev, (px, py)], fill=(0, 0, 0), width=w_int)
                r = w / 2.0
                draw.ellipse([px - r, py - r, px + r, py + r], fill=(0, 0, 0))
            prev = (px, py)


def draw_dao(t, ox=0, oy=0, scale=1.0):
    """Draw 刀: rounded 横折钩 envelope + crossing 撇."""

    # ----- 横折钩: smooth rounded envelope -----
    # Top-left tip of 横 near (-75, +70).
    # Curves right and down through top-right shoulder (+65, +65),
    # then descends on the right side (curving slightly inward),
    # bottom right around (+55, -70), then small hook up-left to (+30, -60).
    envelope_pts = [
        (-75 * scale,  70 * scale),   # left tip of 横 (thin start)
        ( 30 * scale,  72 * scale),   # along the 横 bar
        ( 62 * scale,  65 * scale),   # top-right shoulder (顿笔)
        ( 68 * scale,  20 * scale),   # upper right shaft
        ( 58 * scale, -40 * scale),   # right shaft curving inward
        ( 42 * scale, -72 * scale),   # base of shaft (before hook)
    ]
    envelope_widths = [
        max(1, int(round(4 * scale))),    # very thin head
        max(1, int(round(7 * scale))),    # thicker toward corner
        max(1, int(round(11 * scale))),   # thickest at shoulder (顿笔)
        max(1, int(round(9 * scale))),
        max(1, int(round(8 * scale))),
        max(1, int(round(7 * scale))),    # base
    ]
    _tapered_curve(t, envelope_pts, envelope_widths, ox=ox, oy=oy)

    # Shoulder 顿笔 blob for extra weight at top-right corner.
    sx, sy = _to_pixel(ox + 62 * scale, oy + 65 * scale)
    sr = max(3, int(round(6 * scale)))
    t.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(0, 0, 0))

    # Hook: small curl up-and-left from base of shaft.
    hook_pts = [
        ( 42 * scale, -72 * scale),   # start (continuing from shaft base)
        ( 30 * scale, -75 * scale),   # dip down-left
        ( 18 * scale, -60 * scale),   # curl up-left to fine tip
    ]
    hook_widths = [
        max(1, int(round(7 * scale))),
        max(1, int(round(5 * scale))),
        max(1, int(round(2 * scale))),
    ]
    _tapered_curve(t, hook_pts, hook_widths, ox=ox, oy=oy, n=30)

    # ----- 撇 crossing near LEFT end of 横 -----
    # In GT the 撇 starts up around the left side of the 横 (near where
    # the 横 begins) and sweeps down-left below the base of the envelope.
    # pie primitive head is at (+65*s, +90*s), tail at (-45*s, -85*s).
    # Target head near (-40, +80), tail near (-110, -90).
    # Head math: ox + 65*s = -40, tail: ox - 45*s = -110 → 110*s = 70 → s ≈ 0.64
    # ox = -40 - 65*0.64 = -40 - 41.6 = -81.6
    # Head y: oy + 90*0.64 = 80 → oy = 80 - 57.6 = 22.4
    # Verify tail y: oy - 85*0.64 = 22.4 - 54.4 = -32.0 (need lower, ~-90)
    # Adjust: use larger vertical scale by extending differently. Since pie
    # primitive is uniform-scale, pick scale=0.95 for vertical reach:
    # scale=0.95 → head=(+61.75,+85.5), tail=(-42.75,-80.75)
    # ox: head x=-40 → ox = -40 - 61.75 = -101.75; tail x = -101.75-42.75 = -144.5 (off canvas)
    # Compromise: scale=0.80. head=(52,72). ox=-40-52=-92, tail x = -92-36 = -128 (still off)
    # Use scale=0.72. head=(46.8, 64.8), tail=(-32.4, -61.2).
    # ox = -40 - 46.8 = -86.8, tail x = -86.8 - 32.4 = -119.2 → PIL px = 150-119.2=30.8 (in bounds)
    # oy for head y=+70: oy = 70 - 64.8 = 5.2; tail y = 5.2 - 61.2 = -56 (fine)
    pie_scale = 0.75
    # head after scale: (48.75, 67.5); target head (-45, +72) → ox = -45 - 48.75 = -93.75
    # oy = 72 - 67.5 = 4.5; tail = (-33.75, -63.75); tail world = (-127.5, -59.25)
    draw_pie(t, ox=-93.75, oy=4.5, scale=pie_scale)


def main():
    img = Image.new("RGB", (CANVAS, CANVAS), "white")
    draw = ImageDraw.Draw(img)
    draw_dao(draw, ox=0, oy=0, scale=1.0)
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "01_刀.png")
    img.save(out_path)
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
