"""Cycle 12 — 竖折 (shu-zhe) compound stroke.

Phase 2 (compound strokes), single-phase (eval=vision).

Mirror of 横折's L-frame: a vertical arm comes DOWN, turns 90° to the
RIGHT, and runs as a horizontal arm. It is the bottom-left "L" frame
of 山, 凶, 区, 匹, ….

Two-Bézier-segment stitched stroke per §1.5 (established by 捺 in c4,
and applied to the corner case by 横折 in c7):
  Segment A (shu arm, vertical):    (-80, +100) → (-80, -80)
    w_profile: 16 (entry dunbi) → 11 (shaft) → 14 (corner build)
  Segment B (heng arm, horizontal): (-80, -80) → (+80, -80)
    w_profile: 14 (corner inherit) → 11 (shaft) → 14 (slight closing weight)

Width is continuous across the lower-left corner (A ends 14, B starts
14). The corner-顿笔 thickening is what makes the turn read as a
single stroke rather than two glued lines (heng_zhe c7 lesson).

Both control points within each segment are colinear with the
endpoints, so the segments themselves are straight; only the width
varies along the arc-length.
"""

import os
import sys
import turtle

# Path to Success Bank code for the brushed_bezier helper.
_SUCCESS_BANK = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "success_bank", "code")
)
sys.path.insert(0, _SUCCESS_BANK)
from heng import brushed_bezier  # noqa: E402


# ── Task 01 | 竖折 | shu_zhe ──────────────────────────────────────────────


def _w_shuzhe_A(s: float) -> float:
    """Shu-arm (vertical) width profile.

    s ∈ [0, 1] along the vertical arm (top → bottom corner).
      - Entry dunbi (0–10%):     16 → 11  (canonical 起笔 press)
      - Shaft       (10–80%):    11        (steady vertical)
      - Corner build (80–100%):  11 → 14   (顿笔 thickening into the turn)
    """
    if s < 0.10:
        return 16.0 - (s / 0.10) * 5.0
    if s < 0.80:
        return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 3.0


def _w_shuzhe_B(s: float) -> float:
    """Heng-arm (horizontal) width profile.

    s ∈ [0, 1] along the horizontal arm (left corner → right end).
      - Corner inherit (0–15%):  14 → 11  (carry corner 顿笔 weight forward)
      - Shaft         (15–85%):  11        (steady horizontal)
      - Closing       (85–100%): 11 → 14   (slight 收笔 weight at the right end)
    """
    if s < 0.15:
        return 14.0 - (s / 0.15) * 3.0
    if s < 0.85:
        return 11.0
    return 11.0 + ((s - 0.85) / 0.15) * 3.0


def draw_shu_zhe(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    """Draw 竖折 as two stitched cubic Béziers.

    Segment A (shu arm):  (-80, +100) → (-80, -80), vertical.
    Segment B (heng arm): (-80, -80)  → (+80, -80), horizontal.

    A3 == B0 at the lower-left corner. Width continuous across the
    junction (A ends 14, B starts 14). Each segment's control points
    are colinear with its endpoints, so the segments are straight.
    """
    # Segment A: vertical arm (top → bottom-left corner).
    A0 = (-80.0 * scale + ox, 100.0 * scale + oy)
    A3 = (-80.0 * scale + ox, -80.0 * scale + oy)
    A1 = (A0[0] + (A3[0] - A0[0]) / 3.0, A0[1] + (A3[1] - A0[1]) / 3.0)
    A2 = (A0[0] + 2.0 * (A3[0] - A0[0]) / 3.0, A0[1] + 2.0 * (A3[1] - A0[1]) / 3.0)
    brushed_bezier(t, A0, A1, A2, A3, _w_shuzhe_A, samples=200)

    # Segment B: horizontal arm — starts at A's endpoint (sharp 90° corner).
    B0 = (-80.0 * scale + ox, -80.0 * scale + oy)
    B3 = (80.0 * scale + ox, -80.0 * scale + oy)
    B1 = (B0[0] + (B3[0] - B0[0]) / 3.0, B0[1] + (B3[1] - B0[1]) / 3.0)
    B2 = (B0[0] + 2.0 * (B3[0] - B0[0]) / 3.0, B0[1] + 2.0 * (B3[1] - B0[1]) / 3.0)
    brushed_bezier(t, B0, B1, B2, B3, _w_shuzhe_B, samples=200)


def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("black")

    draw_shu_zhe(t)

    screen.update()

    # Save canvas as PNG via PostScript → PIL.
    out_dir = os.path.dirname(os.path.abspath(__file__))
    ps_path = os.path.join(out_dir, "_01_竖折.ps")
    png_path = os.path.join(out_dir, "01_竖折.png")
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
