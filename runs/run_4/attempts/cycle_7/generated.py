"""Cycle 7 — 横折 (heng-zhe) compound stroke.

Phase 2 (compound strokes), single-phase (eval=vision).

Two-Bézier-segment stitched stroke per §1.5 (established by 捺 in c4):
  Segment A (heng arm): (-100, +120) → (+100, +120)
    w_profile: 16 (entry dunbi) → 11 (shaft) → 15 (corner 顿笔)
  Segment B (shu arm):  (+100, +120) → (+100, -80)
    w_profile: 15 (inherit corner) → 11 (shaft) → 13 (slight closing weight)

The corner thickening to width 15 at the A→B junction is the visual
signature of 横折. Width is continuous across the junction (A ends 15,
B starts 15), giving a clean L-corner with a 顿笔, not two separate
strokes glued together.

Both control points within each segment are colinear with endpoints
(no arc), so the segments are essentially straight.
"""

import os
import sys
import turtle

# Path to Success Bank code for brushed_bezier helper.
_SUCCESS_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
sys.path.insert(0, _SUCCESS_BANK)
from heng import brushed_bezier  # noqa: E402


# ── Task 01 | 横折 | heng_zhe ──────────────────────────────────────────────


def _w_hengzhe_A(s: float) -> float:
    """Heng-arm width profile.

    s ∈ [0, 1] along the horizontal arm.
      - Entry dunbi (0–10%):  16 → 11  (canonical heng entry press)
      - Shaft     (10–80%):   11        (steady)
      - Corner build (80–100%): 11 → 15  (顿笔 thickening at the turn)
    """
    if s < 0.10:
        return 16.0 - (s / 0.10) * 5.0
    if s < 0.80:
        return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 4.0


def _w_hengzhe_B(s: float) -> float:
    """Shu-arm width profile.

    s ∈ [0, 1] along the vertical arm.
      - Corner inherit (0–15%): 15 → 11  (carry the 顿笔 thickness down)
      - Shaft        (15–85%):  11        (steady vertical)
      - Closing       (85–100%): 11 → 13  (slight 收笔 weight,垂露-ish, not needle)
    """
    if s < 0.15:
        return 15.0 - (s / 0.15) * 4.0
    if s < 0.85:
        return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 2.0


def draw_heng_zhe(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    """Draw 横折 as two stitched cubic Béziers.

    Segment A (heng arm): (-100, +120) → (+100, +120), horizontal.
    Segment B (shu arm):  (+100, +120) → (+100, -80), vertical.

    A3 == B0 at the corner. Width continuous (A ends 15, B starts 15).
    Within each segment, control points are colinear with endpoints
    (no curvature), so the segments look straight.
    """
    # Segment A: horizontal arm.
    A0 = (-100.0 * scale + ox, 120.0 * scale + oy)
    A3 = (100.0 * scale + ox, 120.0 * scale + oy)
    A1 = (A0[0] + (A3[0] - A0[0]) / 3.0, A0[1] + (A3[1] - A0[1]) / 3.0)
    A2 = (A0[0] + 2.0 * (A3[0] - A0[0]) / 3.0, A0[1] + 2.0 * (A3[1] - A0[1]) / 3.0)
    brushed_bezier(t, A0, A1, A2, A3, _w_hengzhe_A, samples=200)

    # Segment B: vertical arm — starts where A ended (sharp 90° corner).
    B0 = (100.0 * scale + ox, 120.0 * scale + oy)
    B3 = (100.0 * scale + ox, -80.0 * scale + oy)
    B1 = (B0[0] + (B3[0] - B0[0]) / 3.0, B0[1] + (B3[1] - B0[1]) / 3.0)
    B2 = (B0[0] + 2.0 * (B3[0] - B0[0]) / 3.0, B0[1] + 2.0 * (B3[1] - B0[1]) / 3.0)
    brushed_bezier(t, B0, B1, B2, B3, _w_hengzhe_B, samples=200)


def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("black")

    draw_heng_zhe(t)

    screen.update()

    # Save canvas as PNG via PostScript → PIL.
    out_dir = os.path.dirname(os.path.abspath(__file__))
    ps_path = os.path.join(out_dir, "_01_横折.ps")
    png_path = os.path.join(out_dir, "01_横折.png")
    canvas = screen.getcanvas()
    canvas.postscript(file=ps_path, colormode="color")
    try:
        from PIL import Image
        img = Image.open(ps_path)
        img.load(scale=2)
        img.save(png_path, "PNG")
    finally:
        if os.path.exists(ps_path):
            os.remove(ps_path)

    screen.bye()


if __name__ == "__main__":
    main()
