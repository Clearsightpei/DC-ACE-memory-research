"""Cycle 13 — 横折弯钩 (heng_zhe_wan_gou) compound stroke.

Phase 2 (compound strokes), single-phase (eval=vision). Most complex
compound so far — FOUR stitched cubic-Bézier segments:

  Seg A (short heng):     (-80, +120) → (+80, +120)     w 16→11→14
  Seg B (vertical drop):  (+80, +120) → (+80,  -60)     w 14→11
  Seg C (quarter-curve):  (+80,  -60) → (+140,-100)     w 11→12  concave-up
  Seg D (up-hook):        (+140,-100) → (+170, -50)     w 12→3   tapered tip

Composes 横折 (A+B from c7) + 竖弯钩's curve+hook (C+D from c10) in one
continuous brushed path.

§1.5 tangency at each junction:
  A→B: A ends going right; B starts going down. Corner-顿笔 thickening
       (A ends 14, B starts 14) makes the right-angle turn read as one
       stroke (heng_zhe c7 lesson).
  B→C: B's tangent at its endpoint is vertical-down. C0=(+80,-60) with
       C1=(+80,-100) → C starts heading straight down. Tangent continuous.
       Then C curves to end horizontal at (+140,-100) (C2=(+120,-100)→
       C3=(+140,-100) → C ends heading right).
  C→D: C ends heading right; D0=(+140,-100) with D1=(+155,-100) → D
       starts heading right. Tangent continuous. D then curves up to
       the hook tip at (+170,-50).

Width: corner-顿笔 14 at A→B junction, smooth thinning to 11 along B's
shaft, a gentle 11→12 build through the C curve (mirrors 竖弯钩's
13 corner thicken in c10), then a 12→3 taper across D for the
sharp hook point.
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


# ── Task 01 | 横折弯钩 | heng_zhe_wan_gou ─────────────────────────────────


def _w_A(s: float) -> float:
    """Heng arm width profile.

      - Entry dunbi (0–10%):     16 → 11
      - Shaft       (10–80%):    11
      - Corner build (80–100%):  11 → 14   (顿笔 into the A→B turn)
    """
    if s < 0.10:
        return 16.0 - (s / 0.10) * 5.0
    if s < 0.80:
        return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 3.0


def _w_B(s: float) -> float:
    """Vertical drop width profile.

      - Corner inherit (0–15%):  14 → 11   (carry corner 顿笔 forward)
      - Shaft         (15–100%): 11        (steady vertical drop)
    """
    if s < 0.15:
        return 14.0 - (s / 0.15) * 3.0
    return 11.0


def _w_C(s: float) -> float:
    """Quarter-curve width profile — gentle 11→12 build through the arc.

    Mirrors 竖弯钩's 11→13 thickening through its curve (c10) but a touch
    lighter since the following hook is shorter here.
    """
    return 11.0 + s * 1.0


def _w_D(s: float) -> float:
    """Up-hook width profile — 12 → 3 taper to a needle tip.

    Standard tapered-tip family (§1.3): hold near full width briefly,
    then a smooth release. A short hook means almost the whole arc is
    the release window.
    """
    if s < 0.15:
        return 12.0 - (s / 0.15) * 1.0   # 12 → 11 brief shoulder
    return 11.0 - ((s - 0.15) / 0.85) * 8.0  # 11 → 3 tapered tip


def draw_heng_zhe_wan_gou(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    """Draw 横折弯钩 as four stitched cubic Béziers."""
    # Segment A: short heng — (-80, +120) → (+80, +120), straight horizontal.
    A0 = (-80.0 * scale + ox, 120.0 * scale + oy)
    A3 = (80.0 * scale + ox, 120.0 * scale + oy)
    A1 = (A0[0] + (A3[0] - A0[0]) / 3.0, A0[1])
    A2 = (A0[0] + 2.0 * (A3[0] - A0[0]) / 3.0, A0[1])
    brushed_bezier(t, A0, A1, A2, A3, _w_A, samples=200)

    # Segment B: vertical drop — (+80, +120) → (+80, -60), straight vertical.
    B0 = (80.0 * scale + ox, 120.0 * scale + oy)
    B3 = (80.0 * scale + ox, -60.0 * scale + oy)
    B1 = (B0[0], B0[1] + (B3[1] - B0[1]) / 3.0)
    B2 = (B0[0], B0[1] + 2.0 * (B3[1] - B0[1]) / 3.0)
    brushed_bezier(t, B0, B1, B2, B3, _w_B, samples=200)

    # Segment C: quarter-curve right, concave-up.
    #   C0=(+80,-60), C3=(+140,-100). Controls per task brief:
    #   C1=(+80,-100) → C starts heading straight DOWN  (tangent to B's end).
    #   C2=(+120,-100) → C ends heading straight RIGHT  (tangent for D).
    C0 = (80.0 * scale + ox, -60.0 * scale + oy)
    C3 = (140.0 * scale + ox, -100.0 * scale + oy)
    C1 = (80.0 * scale + ox, -100.0 * scale + oy)
    C2 = (120.0 * scale + ox, -100.0 * scale + oy)
    brushed_bezier(t, C0, C1, C2, C3, _w_C, samples=180)

    # Segment D: up-hook — (+140,-100) → (+170,-50).
    #   D1=(+155,-100) → D starts heading RIGHT  (tangent to C's end).
    #   D2=(+170,-80)  → D ends heading straight UP (sharp needle tip).
    D0 = (140.0 * scale + ox, -100.0 * scale + oy)
    D3 = (170.0 * scale + ox, -50.0 * scale + oy)
    D1 = (155.0 * scale + ox, -100.0 * scale + oy)
    D2 = (170.0 * scale + ox, -80.0 * scale + oy)
    brushed_bezier(t, D0, D1, D2, D3, _w_D, samples=160)


def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("black")

    draw_heng_zhe_wan_gou(t)

    screen.update()

    # Save canvas as PNG via PostScript → PIL.
    out_dir = os.path.dirname(os.path.abspath(__file__))
    ps_path = os.path.join(out_dir, "_01_横折弯钩.ps")
    png_path = os.path.join(out_dir, "01_横折弯钩.png")
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
