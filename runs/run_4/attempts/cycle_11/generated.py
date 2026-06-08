"""Cycle 11 — 横撇 (heng_pie) brushwork.

Two-segment compound stroke per §1.5:
  Seg A short heng: (-100,+100) → (+30,+100), w 16→11→15 (corner build).
  Seg B 撇 tail:    (+30,+100) → (-150,-130), concave-down arc,
                    w 15→11→3 (taper to fine point).

§1.5 tangency: A's A2 nudged slightly below y=100 so the heng exits
pointing down-and-left into B's direction; B0 == A3; B1 and B2 are
placed ABOVE the straight chord (same family as 撇 from c3) to bow
the centerline concave-down. Width is continuous across the junction
(A ends 13, B starts 13). Final taper to pensize-3 follows the
tapered-tip family established by 撇/提.
"""

import sys
import os
import turtle

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "success_bank", "code"))
from heng import brushed_bezier  # noqa: E402


# ── Task 01 | 横撇 | heng_pie


def _w_A(s: float) -> float:
    """Seg A short heng width profile: 16 → 11 → 15 (corner build).

    Entry dunbi 16 → shaft 11 over first 12%, hold 11 through middle,
    rebuild to 15 over final 20% (corner 顿笔, matches heng_zhe pattern).
    """
    if s < 0.12:
        return 16.0 - (s / 0.12) * 5.0
    if s < 0.80:
        return 11.0
    return 11.0 + ((s - 0.80) / 0.20) * 4.0


def _w_B(s: float) -> float:
    """Seg B 撇 tail width profile: 15 → 11 → 3 (tapered tip).

    Inherits A's corner width 15 (continuous), drops to shaft 11 over
    first 18%, holds 11 through middle ~70%, then tapers 11 → 3 over
    final 12%. Same tapered-tip family as 撇 (c3) and 提 (c5) per §1.3.
    """
    if s < 0.18:
        return 15.0 - (s / 0.18) * 4.0
    if s < 0.88:
        return 11.0
    return 11.0 - ((s - 0.88) / 0.12) * 8.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    # Seg A: short horizontal arm (-100,+100) → (+30,+100).
    A0 = (-100.0 * scale + ox, 100.0 * scale + oy)
    A3 = (30.0 * scale + ox, 100.0 * scale + oy)
    # A1 at 1/3 along, A2 at 2/3 along — nudge A2 slightly below to make
    # the heng exit point down-and-left toward B (§1.5 tangency).
    A1 = (A0[0] + (A3[0] - A0[0]) / 3.0, A0[1])
    A2 = (A0[0] + 2.0 * (A3[0] - A0[0]) / 3.0, A0[1] - 10.0 * scale)
    brushed_bezier(t, A0, A1, A2, A3, _w_A, samples=200)

    # Seg B: 撇 tail (+30,+100) → (-150,-130). Concave-down arc.
    # Chord midpoint ≈ (-60, -15); control points placed ABOVE the chord
    # so the centerline bows upward in the middle (concave-down family).
    B0 = (30.0 * scale + ox, 100.0 * scale + oy)
    B3 = (-150.0 * scale + ox, -130.0 * scale + oy)
    B1 = (-10.0 * scale + ox, 60.0 * scale + oy)
    B2 = (-100.0 * scale + ox, -30.0 * scale + oy)
    brushed_bezier(t, B0, B1, B2, B3, _w_B, samples=220)


def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("white")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("black")
    t.pensize(3)

    draw(t)

    screen.update()

    # Save canvas to PNG (via PostScript + Pillow).
    out_dir = os.path.dirname(os.path.abspath(__file__))
    png_path = os.path.join(out_dir, "01_横撇.png")
    ps_path = os.path.join(out_dir, "01_横撇.ps")
    canvas = screen.getcanvas()
    canvas.postscript(file=ps_path, colormode="color")
    try:
        from PIL import Image
        img = Image.open(ps_path)
        img.load(scale=2)
        img.save(png_path, "PNG")
    except Exception as e:
        print(f"PNG conversion failed: {e}")
    finally:
        try:
            os.remove(ps_path)
        except OSError:
            pass

    screen.bye()


if __name__ == "__main__":
    main()
