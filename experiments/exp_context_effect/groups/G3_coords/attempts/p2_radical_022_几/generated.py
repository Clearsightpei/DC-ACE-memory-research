"""p2_radical_022_几 — G3 (coord-bank) attempt.

几 = 撇 (left) + 横折弯钩 (right, one continuous stroke).

Composition analysis (from GT — compact character occupying ~180x180
of the 300x300 canvas, centered a bit above center):
- Left stroke 撇: starts near the upper-middle where it welds with
  the right stroke's horizontal head, descends nearly-vertically with
  a slight left lean and a soft scoop at the bottom, ending near
  canvas (75, 250).
- Right stroke 横折弯钩 (one continuous stroke):
  * short horizontal from the weld point going right ~55 px
  * turn down (with a slight leftward-bowing vertical descent) to
    near canvas y=245
  * smooth curve sweeping right at the bottom (~15-20 px right)
  * short upward hook flicking up-and-slightly-left

TR6 comments on primitive use:
- No pie primitive call — 撇 in 几 is nearly-vertical, whereas
  pie.py's canonical shape is a wide diagonal sweep (P10 rule about
  丿 vs 撇 applies here too). INLINE a bezier that matches 几's
  scoop-tail 撇 shape.
- No heng_zhe_gou reuse — 几's right stroke has a curved bottom-right
  sweep (弯), which heng_zhe_gou lacks (it goes down + hook, not
  down + right-sweep + hook). INLINE bezier.

TR7 sanity check:
- 撇: head (135, 95), tail (75, 250). Bezier bows through (110, 175).
  All in canvas bounds with ~50 px left margin, ~50 px bottom margin.
- 横折弯钩:
  * horizontal head (135, 95) → (215, 95): 80 px wide top.
  * vertical descent (215, 95) → (205, 245): ~150 px shaft with mild
    leftward bow.
  * 弯 curve (205, 245) → (245, 260): sweeps right-and-down 40 px.
  * hook (245, 260) → (240, 235): flicks up 25 px.
  Right margin ~55 px, bottom margin ~40 px.
- Weld at top: pie head and horizontal start share canvas point
  (135, 95).
"""

from PIL import Image, ImageDraw
import os

CANVAS_SIZE = 300
OUT_PATH = os.path.join(os.path.dirname(__file__), "01_几.png")


def _tapered_bezier(draw, p0, p1, p2, w0, w1, steps=60):
    """Draw a quadratic bezier from p0 to p2 through control p1 with linear width taper.
    p0, p1, p2 are CANVAS pixel coords (top-left origin, +y down)."""
    prev = None
    for i in range(steps + 1):
        u = i / steps
        bx = (1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u ** 2 * p2[0]
        by = (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u ** 2 * p2[1]
        w = w0 + (w1 - w0) * u
        w_int = max(1, int(round(w)))
        if prev is not None:
            draw.line([prev, (bx, by)], fill=(0, 0, 0), width=w_int)
            r = w / 2.0
            draw.ellipse([bx - r, by - r, bx + r, by + r], fill=(0, 0, 0))
        prev = (bx, by)


def _tapered_line(draw, p0, p1, w0, w1, steps=40):
    """Tapered straight line, canvas pixel coords."""
    for i in range(steps):
        u0 = i / steps
        u1 = (i + 1) / steps
        xa = p0[0] + u0 * (p1[0] - p0[0])
        ya = p0[1] + u0 * (p1[1] - p0[1])
        xb = p0[0] + u1 * (p1[0] - p0[0])
        yb = p0[1] + u1 * (p1[1] - p0[1])
        w = max(1, int(round(w0 + (w1 - w0) * ((u0 + u1) / 2))))
        draw.line([(xa, ya), (xb, yb)], fill=(0, 0, 0), width=w)


def draw_pie_ji(draw):
    """Left stroke of 几: nearly-vertical 撇 with a soft scoop at the tail.
    Canvas coords head=(135, 95), tail=(75, 250). Bezier control at
    (108, 180) — slight leftward bow through the middle so the shaft
    reads mostly-vertical with a gentle scoop at the bottom."""
    head = (135.0, 95.0)
    tail = (75.0, 250.0)
    ctrl = (108.0, 180.0)
    _tapered_bezier(draw, head, ctrl, tail, w0=11, w1=2, steps=60)


def draw_heng_zhe_wan_gou(draw):
    """Right stroke of 几: 横折弯钩 as ONE continuous stroke."""
    # A. Horizontal top: from weld point going right ~80 px.
    p_h_start = (135.0, 95.0)
    p_h_end = (215.0, 95.0)
    _tapered_line(draw, p_h_start, p_h_end, w0=10, w1=12, steps=24)

    # 顿笔 blob at top-right corner (P6).
    cx, cy = p_h_end
    r = 6
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(0, 0, 0))

    # B. Vertical descent with slight leftward bow.
    # Canvas y grows DOWN, so p_v_end.y > p_v_start.y.
    p_v_start = (215.0, 95.0)
    p_v_end = (205.0, 245.0)
    p_v_ctrl = (208.0, 170.0)  # slight leftward bow
    _tapered_bezier(draw, p_v_start, p_v_ctrl, p_v_end, w0=12, w1=11, steps=40)

    # C. 弯 — smooth curve at the bottom sweeping right.
    # From bottom of shaft, curves right and slightly down.
    p_c_start = (205.0, 245.0)
    p_c_end = (245.0, 260.0)
    p_c_ctrl = (225.0, 262.0)  # curve bowing down-right
    _tapered_bezier(draw, p_c_start, p_c_ctrl, p_c_end, w0=11, w1=10, steps=30)

    # 顿笔 blob at the hook base for continuity.
    hx, hy = p_c_end
    r = 5
    draw.ellipse([hx - r, hy - r, hx + r, hy + r], fill=(0, 0, 0))

    # D. Upward hook — tapered, flicking up-and-slightly-left.
    p_hk_start = (245.0, 260.0)
    p_hk_end = (240.0, 232.0)
    _tapered_line(draw, p_hk_start, p_hk_end, w0=10, w1=2, steps=16)


def main():
    img = Image.new("RGB", (CANVAS_SIZE, CANVAS_SIZE), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw_pie_ji(draw)
    draw_heng_zhe_wan_gou(draw)
    img.save(OUT_PATH)
    print(f"Saved {OUT_PATH}")


if __name__ == "__main__":
    main()
