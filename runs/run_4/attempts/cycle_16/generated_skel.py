"""Cycle 16 skeleton phase — 三 (san).

Three stacked hengs, SHORT-MEDIUM-LONG (top to bottom). Bottom is longest.
Uniform pensize 3 thin lines at the brief's skeleton targets.

Targets (from task brief):
  Top    heng: (-90, +90)   → (+50, +90)   length ~140 px
  Middle heng: (-100, -10)  → (+50, -10)   length ~150 px
  Bottom heng: (-130, -120) → (+150, -120) length ~280 px
Vertical gaps: ~100 (top→mid), ~110 (mid→bot).
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

    # ── Task 01 | 三 | san ──
    # Top heng (short)
    t.penup(); t.goto(-90, 90); t.pendown()
    t.goto(50, 90)
    t.penup()

    # Middle heng (slightly longer)
    t.penup(); t.goto(-100, -10); t.pendown()
    t.goto(50, -10)
    t.penup()

    # Bottom heng (longest)
    t.penup(); t.goto(-130, -120); t.pendown()
    t.goto(150, -120)
    t.penup()

    screen.update()
    canvas = screen.getcanvas()
    canvas.postscript(file="01_三_skel.eps")

    # Convert EPS to PNG via PIL
    try:
        from PIL import Image
        img = Image.open("01_三_skel.eps")
        img.load(scale=2)
        img.save("01_三_skel.png", "PNG")
    except Exception as e:
        print(f"PNG conversion fallback: {e}")

    screen.bye()


if __name__ == "__main__":
    main()
