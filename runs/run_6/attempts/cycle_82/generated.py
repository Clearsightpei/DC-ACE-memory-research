"""Cycle 82 — 法 (fǎ). 8 strokes: 氵 + 去."""
import io, os, sys, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy  # noqa
from dian import draw_dian
from heng import draw_heng
from shu import draw_shu
from pie import draw_pie


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
    # 氵 water radical (3 strokes)
    draw_dian(t, ("TL", 0.436, 0.608), ("ML", 0.896, 0.004))
    draw_dian(t, ("ML", 0.064, 0.332), ("ML", 0.424, 0.664))
    draw_dian(t, ("BL", 0.224, 1.292), ("ML", 0.764, 0.888))
    # 去 right (5 strokes)
    draw_heng(t, ("C", 0.2, 0.304), ("MR", 0.604, 0.096))
    draw_shu(t, ("TC", 0.668, 0.332), ("C", 0.756, 0.928))
    draw_heng(t, ("BL", 0.836, 0.156), ("MR", 1.088, 0.92))
    draw_pie(t, ("BC", 0.896, 0.208), ("BR", 0.368, 0.908))
    draw_shu(t, ("BR", 0.22, 0.52), ("BR", 0.752, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_法.png"))


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle()
    task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
