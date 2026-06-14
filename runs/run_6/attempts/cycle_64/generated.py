"""头 (tou) — c64 fix. raw MMH."""
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from dian import draw_dian
from heng import draw_heng
from pie import draw_pie

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
    draw_dian(t, ('TL', 0.768, 0.748), ('C', 0.196, 0.052))
    draw_dian(t, ('ML', 0.5, 0.328), ('C', 0.004, 0.724))
    draw_heng(t, ('BL', -0.052, 0.26), ('BR', 1.044, 0.092))
    draw_pie(t, ('TC', 0.508, 0.468), ('BL', 0.148, 1.3))
    draw_dian(t, ('BC', 0.88, 0.612), ('BR', 0.684, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_头.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
