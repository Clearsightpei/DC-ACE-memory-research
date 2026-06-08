"""Cycle 21 — 大 brushwork (iter 2: WIDER limbs per run_3 c12 finding)."""

import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code'))
from heng import draw as draw_heng
from pie import draw as draw_pie
from na import draw as draw_na


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


# ── Task 01 | 大 | da
def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)

    t = turtle.Turtle()
    reset_turtle(t)

    # Heng — slightly LONGER (scale 0.70, 280 px) so it's a clear horizontal bar
    draw_heng(t, ox=0, oy=+40, scale=0.70)

    # 撇 — scale 0.85 so tail reaches x≈-153 BEYOND heng's -140
    # Canonical head (+150,+200) at scale 0.85 = (+127.5, +170).
    # Want apex (+10, +130): ox=10-127.5=-117.5, oy=130-170=-40.
    # Tail at scale 0.85: (-153,-153). After offset: (-270.5, -193). Reaches WIDE.
    draw_pie(t, ox=-117.5, oy=-40, scale=0.85)

    # 捺 — scale 0.75 so kick tip reaches x≈+180+ BEYOND heng's +140
    # Canonical head (-150,+200) at scale 0.75 = (-112.5, +150).
    # Want apex (+10, +130): ox=10-(-112.5)=122.5, oy=130-150=-20.
    # Kick tip canonical (+240,-172) at scale 0.75 = (+180, -129). Offset: (+302.5, -149). WIDE.
    draw_na(t, ox=122.5, oy=-20, scale=0.75)

    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_大.png"))


if __name__ == "__main__":
    main()
