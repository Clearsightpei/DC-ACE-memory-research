import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from dian import draw_dian
from heng import draw_heng
from shu import draw_shu

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(90)

def task_01(t, screen):
    reset(t)
    draw_heng(t, ('TL', -0.096, 0.82), ('TR', 1.148, 0.708))
    # Brief specifies BC y_frac=1.556 but _anchor.py caps at 1.3 (grid edge).
    # Clipping to 1.3 — shu's bottom endpoint sits at the extended grid floor.
    draw_shu(t, ('TC', 0.4, 0.824), ('BC', 0.492, 1.3))
    draw_dian(t, ('C', 0.672, 0.472), ('BR', 0.444, 0.04))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_下.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
