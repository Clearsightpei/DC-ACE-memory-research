# ── Task 01 | 捺 | na
"""Cycle 4 — atomic stroke 捺 (na), the right-diagonal sweep with flat kick.

Width profile is REVERSED vs 撇:
  - Main sweep:  THIN head (5) at upper-left → HEAVY (18) at lower-right
                 just before the kick base.
  - Flat kick:   HEAVY (18) → fine release (3), short horizontal segment.

Two Bézier segments stitched at the kick base (+170, -180):
  Seg A (main sweep):  P0=(-150,+200) → P3=(+170,-180), w: 5→18
  Seg B (flat kick):   P0=(+170,-180) → P3=(+220,-170), w: 18→3

The curvature is gentle concave-up (centerline bows down-right slightly
relative to the straight head-to-tail line).
"""

import io
import os
import sys
import turtle

from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code'))
from heng import brushed_bezier  # noqa: E402


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset_turtle(t):
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.pensize(3)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


# ---------- 捺 width profiles ----------

def _w_na_main(s: float) -> float:
    """Main sweep width: THIN head → HEAVY just-before-kick.

    s ∈ [0, 1] from head (upper-left) to kick base (lower-right).
      - Entry (0–10%):    5 → 8  (thin, almost from a point — opposite of 撇)
      - Shaft (10–80%):   8 → 14 (progressive thickening)
      - Pre-kick (80–100%): 14 → 18 (heaviest right before the kick base)
    """
    if s < 0.10:
        return 5.0 + (s / 0.10) * 3.0
    if s < 0.80:
        return 8.0 + ((s - 0.10) / 0.70) * 6.0
    return 14.0 + ((s - 0.80) / 0.20) * 4.0


def _w_na_kick(s: float) -> float:
    """Flat-kick width: heavy press → fine release.

    s ∈ [0, 1] over the short horizontal kick segment.
      - Press hold (0–25%): 18 → 16  (the 顿笔 — brush plants heavily)
      - Release (25–100%):  16 → 3   (the 出锋 — brush lifts away)
    The brushed_bezier max(3, ...) floor enforces the minimum.
    """
    if s < 0.25:
        return 18.0 - (s / 0.25) * 2.0
    return 16.0 - ((s - 0.25) / 0.75) * 13.0


def draw_na(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    """Draw 捺 as two stitched cubic Béziers.

    Main sweep endpoints (before transform):
        P0 head     = (-150, +200)   thin, upper-left
        P3 kick-base= (+170, -180)   heavy, lower-right
    Control points place the centerline below the straight head-to-tail
    line so the arc is concave-UP (opposite of 撇's concave-down).

    Flat kick endpoints:
        P0 = (+170, -180)
        P3 = (+220, -170)   ~50 px right + tiny lift
    """
    # Segment A — main sweep, thin → heavy
    A0 = (-150.0 * scale + ox, 200.0 * scale + oy)
    A3 = (170.0 * scale + ox, -180.0 * scale + oy)
    # Control points: bow centerline DOWN-right (concave-up arc).
    # A2 pulled toward horizontal-right so the sweep arrives at the
    # kick base tangentially (not pointing steeply down) — otherwise
    # the seg-A/seg-B junction reads as an angular notch.
    A1 = (-60.0 * scale + ox, 80.0 * scale + oy)
    A2 = (90.0 * scale + ox, -150.0 * scale + oy)
    brushed_bezier(t, A0, A1, A2, A3, _w_na_main, samples=240)

    # Segment B — flat kick, heavy → fine release (nearly horizontal).
    # Lengthened to ~70 px so the kick reads as a deliberate flat
    # release (出锋) rather than a notch. End point lifts ~8 px
    # (a small 出锋 lift, not a hook).
    B0 = (170.0 * scale + ox, -180.0 * scale + oy)
    B3 = (240.0 * scale + ox, -172.0 * scale + oy)
    # Controls bias the kick centerline almost perfectly horizontal,
    # tangentially continuing from seg A's horizontal-ish arrival.
    B1 = (195.0 * scale + ox, -180.0 * scale + oy)
    B2 = (220.0 * scale + ox, -175.0 * scale + oy)
    brushed_bezier(t, B0, B1, B2, B3, _w_na_kick, samples=160)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    reset_turtle(t)

    draw_na(t)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_捺.png"))


if __name__ == "__main__":
    main()
