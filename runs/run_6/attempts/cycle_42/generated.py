"""目 — c42 (restart of c40 after 3-attempt freeze).
Geometric L-corner heuristic: heng_zhe corner = (to_x, from_y)."""
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from shu import draw_shu


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
    draw_shu(t, ('TL', 0.576, 0.656), ('BL', 0.684, 1.244))
    draw_heng_zhe(t, ('TL', 0.804, 0.704), ('TC', 0.872, 0.704), ('BC', 0.872, 1.020))
    draw_heng(t, ('ML', 0.844, 0.556), ('C', 0.764, 0.420))
    draw_heng(t, ('BL', 0.836, 0.180), ('BC', 0.776, 0.072))
    draw_heng(t, ('BL', 0.792, 1.064), ('BC', 0.956, 0.948))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_目.png"))


def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()


if __name__ == "__main__":
    main()
