"""立 (li2) — c62. Raw MMH + corner-by-type."""
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
    draw_dian(t, ('TC', 0.148, 0.46), ('TC', 0.708, 0.792))
    draw_heng(t, ('ML', 0.552, 0.552), ('MR', 0.456, 0.292))
    draw_dian(t, ('BL', 0.732, 0.008), ('BC', 0.068, 0.556))
    draw_pie(t, ('C', 0.864, 0.704), ('BC', 0.584, 0.912))
    draw_heng(t, ('BL', -0.092, 1.184), ('BR', 1.152, 1.16))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_立.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
