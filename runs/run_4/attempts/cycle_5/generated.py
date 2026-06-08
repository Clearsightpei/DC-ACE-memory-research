"""Cycle 5 — 提 (ti, upward flick). Single-phase brushwork.

Tapered-tip stroke (same family as 撇), but:
  - Direction: lower-left BASE → upper-right TIP (reversed from 撇).
  - Length ~250 px (shorter than 撇).
  - Peak 14 (smaller than 撇's 18) — 提 is a lighter, smaller stroke.
  - Gentle bow upward (concave-up) — the centerline lifts slightly
    above the straight base→tip line, mirroring 撇's gentle arc.

Width profile (s=0 at base, s=1 at tip):
  - Base dunbi (0–10%):   14 → 11   (heavy weighted base).
  - Shaft   (10–88%):     11 →  9   (solid).
  - Tail taper (88–100%):  9 →  3   (fine point; max(3, …) floor).
"""

# ── Task 01 | 提 | ti
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code'))
from heng import brushed_bezier


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset_turtle(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black"); t.pensize(3)
    t.penup(); t.goto(0, 0); t.setheading(90)


def _w_ti(s: float) -> float:
    """提 width profile (s=0 at base, s=1 at tip).

    - Base dunbi (0–12%):   14 → 11   (firm weighted base, matches the
                                       c3 lesson — wider dunbi window
                                       reads more "pressed" than a 10%
                                       window).
    - Shaft   (12–88%):     11 →  9.
    - Tail taper (88–100%):  9 →  3   (floor enforced by brushed_bezier;
                                       12% window matches the c3 finding
                                       that smoother > abrupt).
    """
    if s < 0.12:
        return 14.0 - (s / 0.12) * 3.0
    if s < 0.88:
        return 11.0 - ((s - 0.12) / 0.76) * 2.0
    return 9.0 - ((s - 0.88) / 0.12) * 6.0


def draw_ti(t, ox: float = 0.0, oy: float = 0.0, scale: float = 1.0):
    """Draw 提.

    Endpoints (before transform):
        P0 base = (-100, -80)   heavy, lower-left
        P3 tip  = (+150, +60)   fine point, upper-right
    Straight midpoint: (+25, -10). Controls lift the centerline
    above the straight line for a gentle concave-up arc (bow upward
    along the stroke direction).
    """
    P0 = (-100.0 * scale + ox,  -80.0 * scale + oy)
    P3 = ( 150.0 * scale + ox,   60.0 * scale + oy)
    # Bow ~18 px above the straight midpoint — a very gentle concave-up
    # arc (smaller curvature than 撇, but enough to read as a brush
    # flick rather than a straight diagonal).
    P1 = ( -20.0 * scale + ox,  -20.0 * scale + oy)
    P2 = (  75.0 * scale + ox,   30.0 * scale + oy)
    brushed_bezier(t, P0, P1, P2, P3, _w_ti, samples=220)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle(); reset_turtle(t)
    draw_ti(t)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_提.png"))
    try:
        turtle.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
