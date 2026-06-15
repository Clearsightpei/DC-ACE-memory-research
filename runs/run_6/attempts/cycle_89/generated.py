import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from _anchor import anchor_to_xy
from shu import draw_shu
from heng import draw_heng
from pie import draw_pie
from dian import draw_dian


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0, 0); t.setheading(90)


def task_01(t, screen):
    reset(t)
    # 黑 — 12 strokes (里-like top 8 + 灬 4 dots)
    draw_shu(t,  ("TL", 0.404, 0.58),  ("ML", 0.808, 0.696))
    draw_heng(t, ("TL", 0.592, 0.58),  ("MR", 0.104, 0.552))
    draw_pie(t,  ("TL", 0.912, 0.948), ("C",  0.132, 0.216))
    draw_shu(t,  ("TC", 0.876, 0.772), ("C",  0.708, 0.192))
    draw_heng(t, ("ML", 0.896, 0.628), ("MR", 0.016, 0.512))
    draw_shu(t,  ("TC", 0.308, 0.628), ("BC", 0.376, 0.38))
    draw_heng(t, ("BL", 0.84, 0.072),  ("MR", 0.032, 0.964))
    draw_heng(t, ("BL", 0.528, 0.556), ("BR", 0.464, 0.46))
    draw_dian(t, ("BL", 0.2, 0.908),   ("BL", -0.016, 1.3))
    draw_dian(t, ("BL", 0.796, 0.972), ("BC", 0.064, 1.3))
    draw_dian(t, ("BC", 0.512, 0.852), ("BC", 0.832, 1.232))
    draw_dian(t, ("BR", 0.384, 0.796), ("BR", 0.996, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_黑.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
