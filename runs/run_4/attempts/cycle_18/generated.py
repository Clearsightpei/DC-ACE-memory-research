import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code'))

from pie import draw as draw_pie
from na import draw as draw_na


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


# ── Task 01 | 八 | ba
def draw_ba(t):
    """Brushwork phase: 八 composed from mastered 撇 (c3) + 捺 (c4) primitives.

    Skeleton targets (per task brief, matching the approved generated_skel.py):
      撇:     head (-30, +75)  → tail (-100, -110)
      捺 main: head (+50, +100) → kick base (+150, -110)
      Kick:   (+150, -110) → (+200, -100)

    Canonical pie head (+150, +200) with scale=0.55, ox=-115, oy=-25:
        head → (150*0.55-115, 200*0.55-25) = (-32.5, +85)   vs target (-30, +75)
    Canonical na head (-150, +200) with scale=0.55, ox=130, oy=-20:
        head → (-150*0.55+130, 200*0.55-20) = (+47.5, +90)  vs target (+50, +100)

    Heads are within ~10 px of brief targets — well under the "near each other
    with ~80 px gap" spec (here pie head at -32.5 and na head at +47.5 give
    a horizontal gap of 80 px). The mastered brushwork (width profiles, taper,
    flat kick) is inherited verbatim from c3/c4 — no endpoint changes.
    """
    draw_pie(t, ox=-115, oy=-25, scale=0.55)
    draw_na(t, ox=130, oy=-20, scale=0.55)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    reset_turtle(t)
    draw_ba(t)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_八.png"))


if __name__ == "__main__":
    main()
