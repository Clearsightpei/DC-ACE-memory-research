import io, os, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset_turtle(t):
    t.reset(); t.hideturtle(); t.speed(0)
    t.pencolor("black"); t.pensize(3)
    t.penup(); t.goto(0, 0); t.setheading(90)


def brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=200):
    t.penup(); t.goto(P0); t.pendown()
    for i in range(samples + 1):
        s = i / samples
        x = (1 - s) ** 3 * P0[0] + 3 * (1 - s) ** 2 * s * P1[0] + 3 * (1 - s) * s * s * P2[0] + s ** 3 * P3[0]
        y = (1 - s) ** 3 * P0[1] + 3 * (1 - s) ** 2 * s * P1[1] + 3 * (1 - s) * s * s * P2[1] + s ** 3 * P3[1]
        t.pensize(max(3, w_profile(s)))
        t.goto(x, y)
    t.penup()


# ── Task 01 | 横 | heng
def task_01_heng(t):
    """Draw a canonical 楷书 horizontal stroke (heng).

    Brushwork profile:
      - Entry (dunbi): pensize ~17 at s=0, easing down to ~12 by s=0.10.
      - Shaft: ~12 → ~11 from s=0.10 → s=0.82 (>= 50% of peak).
      - Closing press (收笔): ~11 → ~18 from s=0.82 → s=1.0 (right end heaviest).
    Gentle upward tilt: end y rises ~6 px above start.
    Essentially straight (control points colinear with start/end line).
    """
    # Endpoints: left to right, slight upward tilt for canonical 楷书 feel.
    P0 = (-200.0, -3.0)
    P3 = (200.0, 3.0)
    # Control points on the same line (so curve is essentially straight,
    # not bowed). Place them at 1/3 and 2/3 along the segment.
    P1 = (P0[0] + (P3[0] - P0[0]) / 3.0, P0[1] + (P3[1] - P0[1]) / 3.0)
    P2 = (P0[0] + 2.0 * (P3[0] - P0[0]) / 3.0, P0[1] + 2.0 * (P3[1] - P0[1]) / 3.0)

    def w_heng(s):
        # Entry press (dunbi): 16 -> 11 over the first 10%.
        if s < 0.10:
            return 16.0 - (s / 0.10) * 5.0
        # Shaft: 11 -> 11 over the middle ~78% (steady medium, ~65% of peak).
        if s < 0.88:
            return 11.0 - ((s - 0.10) / 0.78) * 0.5
        # Closing press (收笔): 10.5 -> 19 over the final 12% — right end heaviest (sharper press).
        return 10.5 + ((s - 0.88) / 0.12) * 8.5

    brushed_bezier(t, P0, P1, P2, P3, w_heng, samples=220)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    reset_turtle(t)

    task_01_heng(t)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_横.png"))


if __name__ == "__main__":
    main()
