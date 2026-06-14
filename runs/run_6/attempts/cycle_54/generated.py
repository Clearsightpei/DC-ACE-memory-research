"""人 — c54 (apex_share verification).
Pie + na with shared apex y (na.head.y lifted to pie.head.y).
"""
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from pie import draw_pie
from na import draw_na


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")


def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0, 0); t.setheading(0)


def task_01(t, screen):
    reset(t)
    # apex_share applied: na.head.y lifted from -14.0 to 89.6 to match pie.head.y
    draw_pie(t, ('TC', 0.384, 0.604), ('BL', -0.26, 1.168))
    draw_na(t,  ('TC', 0.348, 0.604), ('BR', 1.3, 1.188))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_人.png"))


def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
