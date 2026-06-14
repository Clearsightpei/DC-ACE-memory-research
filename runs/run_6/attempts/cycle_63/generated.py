"""出 (chu) — c63 fix. raw MMH."""
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import draw_heng
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
    draw_heng(t, ('ML', 0.476, 0.156), ('MR', 0.38, 0.576))
    draw_shu(t, ('TR', 0.512, 0.94), ('MR', 0.472, 0.956))
    draw_shu(t, ('TC', 0.344, 0.26), ('BC', 0.456, 1.024))
    draw_heng(t, ('BL', 0.488, 0.444), ('BR', 0.524, 1.02))
    draw_shu(t, ('BR', 0.488, 0.408), ('BR', 0.72, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_出.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
