"""
Cycle 17 — 十 (shi, ten) — SKELETON phase.

Phase A: uniform pensize 3, endpoints only. No brushwork.
GT-derived skeleton:
  - Heng: (-150, +20) → (+150, +20).
  - Shu : (+15, +160) → (+15, -180).
"""

import turtle


def setup():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(3)
    t.color("black")
    return screen, t


def draw_line(t, p0, p1):
    t.penup()
    t.goto(p0)
    t.pendown()
    t.goto(p1)
    t.penup()


def main():
    screen, t = setup()

    # ── Task 01 | 十 | shi
    # Heng
    draw_line(t, (-150, 20), (150, 20))
    # Shu
    draw_line(t, (15, 160), (15, -180))

    screen.update()

    # Save canvas to PostScript then PNG via PIL
    canvas = screen.getcanvas()
    ps_path = "01_shi_skel.ps"
    canvas.postscript(file=ps_path, colormode="color")

    try:
        from PIL import Image
        img = Image.open(ps_path)
        img.save("01_十_skel.png", "png")
    except Exception as e:
        print(f"PIL conversion failed: {e}")

    screen.bye()


if __name__ == "__main__":
    main()
