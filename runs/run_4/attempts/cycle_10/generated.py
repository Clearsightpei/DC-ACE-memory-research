"""Cycle 10 — 竖弯钩 (shu_wan_gou) brushwork.

Three-segment compound:
  Seg A vertical drop (0,+150)→(0,-100), w 16→11.
  Seg B quarter-arc (0,-100)→(+150,-150), concave-up; w 11→13.
  Seg C up-hook (+150,-150)→(+200,-100), w 13→3.

§1.5 tangency: A's A2 nudged toward B's first control direction (down)
to avoid an angular notch; B's B2 placed at (+100,-150) so the curve
exit-tangent points up-right into C; C inherits B's exit width.
"""

import sys, os, turtle

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", "..", "success_bank", "code"))
from heng import brushed_bezier  # noqa: E402


# ── Task 01 | 竖弯钩 | shu_wan_gou


def _w_A(s: float) -> float:
    # Entry dunbi 16 → shaft 11 over first 12%, hold 11 to end of shaft.
    if s < 0.12:
        return 16.0 - (s / 0.12) * 5.0
    return 11.0


def _w_B(s: float) -> float:
    # Smooth thicken through the curve: 11 → 13 (slight build into hook).
    return 11.0 + s * 2.0


def _w_C(s: float) -> float:
    # Hook taper: hold 13 briefly (first 15%), then long taper to 3.
    if s < 0.15:
        return 13.0
    return 13.0 - ((s - 0.15) / 0.85) * 10.0


def draw(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    # Seg A: vertical drop
    A0 = (0.0 * scale + ox, 150.0 * scale + oy)
    A3 = (0.0 * scale + ox, -100.0 * scale + oy)
    A1 = (A0[0], A0[1] + (A3[1] - A0[1]) / 3.0)
    # A2 nudged toward B's direction (B1 is straight below B0): keep at x=0.
    A2 = (A0[0], A0[1] + 2.0 * (A3[1] - A0[1]) / 3.0)
    brushed_bezier(t, A0, A1, A2, A3, _w_A, samples=220)

    # Seg B: quarter-circle curve, concave-up
    B0 = (0.0 * scale + ox, -100.0 * scale + oy)
    B3 = (150.0 * scale + ox, -150.0 * scale + oy)
    B1 = (0.0 * scale + ox, -150.0 * scale + oy)
    B2 = (100.0 * scale + ox, -150.0 * scale + oy)
    brushed_bezier(t, B0, B1, B2, B3, _w_B, samples=200)

    # Seg C: up-hook to (+200,-100)
    C0 = (150.0 * scale + ox, -150.0 * scale + oy)
    C3 = (200.0 * scale + ox, -100.0 * scale + oy)
    # Pull control points so tangent at C0 continues B's exit (up-right)
    C1 = (170.0 * scale + ox, -148.0 * scale + oy)
    C2 = (190.0 * scale + ox, -125.0 * scale + oy)
    brushed_bezier(t, C0, C1, C2, C3, _w_C, samples=180)


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

    # Save canvas to PNG (via PostScript + Pillow if available).
    out_dir = os.path.dirname(os.path.abspath(__file__))
    png_path = os.path.join(out_dir, "01_竖弯钩.png")
    ps_path = os.path.join(out_dir, "01_竖弯钩.ps")
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
