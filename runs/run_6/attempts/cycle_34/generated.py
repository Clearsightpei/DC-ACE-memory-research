"""Auto-composed: 又 — c34. MMH-derived anchors + bend corners."""
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng_pie import draw_heng_pie
from na import draw_na

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
    draw_heng_pie(t, ('ML', 0.516, 0.048), ('TR', 0.044, 0.936), ('BL', 0.032, 1.22))
    draw_na(t, ('ML', 0.536, 0.36), ('BR', 1.3, 1.26))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_又.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
