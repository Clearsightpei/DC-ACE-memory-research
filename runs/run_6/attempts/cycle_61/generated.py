"""米 (mi) — c61. Raw MMH + corner-by-type."""
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from dian import draw_dian
from heng import draw_heng
from na import draw_na
from pie import draw_pie
from shu import draw_shu

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(0)

def task_01(t, screen):
    reset(t)
    draw_dian(t, ('TL', 0.528, 0.896), ('ML', 0.964, 0.292))
    draw_pie(t, ('TR', 0.228, 0.544), ('C', 0.812, 0.212))
    draw_heng(t, ('ML', 0.108, 0.808), ('MR', 0.744, 0.608))
    draw_shu(t, ('TC', 0.264, 0.232), ('BC', 0.384, 1.3))
    draw_pie(t, ('C', 0.336, 0.848), ('BL', -0.06, 1.232))
    draw_na(t, ('C', 0.548, 0.824), ('BR', 1.268, 1.08))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_米.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
