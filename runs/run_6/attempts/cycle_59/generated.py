"""牛 (niu) — c59. Raw MMH + corner-by-type."""
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import draw_heng
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
    draw_pie(t, ('TL', 0.708, 0.772), ('ML', 0.28, 0.756))
    draw_heng(t, ('ML', 0.816, 0.328), ('MR', 0.392, 0.1))
    draw_heng(t, ('BL', -0.084, 0.288), ('BR', 1.14, 0.048))
    draw_shu(t, ('TC', 0.36, 0.236), ('BC', 0.544, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_牛.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
