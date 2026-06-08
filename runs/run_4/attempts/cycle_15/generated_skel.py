"""Cycle 15 skeleton phase — 二 (er).

SHORT top heng + LONG bottom heng.
Uniform pensize 3 thin lines at the brief's skeleton targets.

Targets (from task brief):
  Top    heng: (-90, +50)  → (+50, +50)   length ~140 px
  Bottom heng: (-130, -100) → (+130, -100) length ~260 px
"""

import turtle


def main():
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("white")
    screen.tracer(0, 0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(3)
    t.color("black")

    # ── Task 01 | 二 | er ──
    # Top heng (short)
    t.penup(); t.goto(-90, 50); t.pendown()
    t.goto(50, 50)
    t.penup()

    # Bottom heng (long)
    t.penup(); t.goto(-130, -100); t.pendown()
    t.goto(130, -100)
    t.penup()

    screen.update()
    canvas = screen.getcanvas()
    canvas.postscript(file="01_二_skel.eps")

    # Convert EPS to PNG via PIL
    try:
        from PIL import Image
        img = Image.open("01_二_skel.eps")
        img.load(scale=2)
        img.save("01_二_skel.png", "PNG")
    except Exception as e:
        print(f"PNG conversion fallback: {e}")

    screen.bye()


if __name__ == "__main__":
    main()
