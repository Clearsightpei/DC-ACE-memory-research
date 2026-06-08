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
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.pensize(3)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


# ── Task 01 | 力 | li
def draw_li_skel(t):
    """Skeleton phase: 力 = 横折钩 (frame) + 撇 (cuts through heng from
    upper-middle, sweeping down-left).

    From brief:
      横折钩: heng (-90, +95) → corner (+85, +95);
              shu corner (+85, +95) → (+85, -130);
              hook (+85, -130) → (+30, -90).
      撇: head (0, +120) ABOVE the heng → tail (-130, -150).
        — 撇 head visibly above heng (y=120 > y=95) so it crosses
          through the heng, distinguishing 力 from 刀 (which has no
          upper extension above the heng).
    """
    t.pensize(3)  # uniform thin — skeleton phase only

    # 横折钩 — three-segment L-with-hook frame
    # Seg A: heng (-90, +95) → corner (+85, +95)
    t.penup()
    t.goto(-90, 95)
    t.pendown()
    t.goto(85, 95)
    # Seg B: shu corner (+85, +95) → (+85, -130)
    t.goto(85, -130)
    # Seg C: hook (+85, -130) → (+30, -90)
    t.goto(30, -90)
    t.penup()

    # 撇 — head ABOVE the heng (y=+120 above heng's y=+95), sweeps down-left
    t.penup()
    t.goto(0, 120)
    t.pendown()
    t.goto(-130, -150)
    t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    reset_turtle(t)
    draw_li_skel(t)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_力_skel.png"))


if __name__ == "__main__":
    main()
