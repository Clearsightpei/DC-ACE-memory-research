"""Auto-composed: 七 — c35. MMH-derived anchors + bend corners."""
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import draw_heng
from shu_wan_gou import draw_shu_wan_gou

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
    draw_heng(t, ('BL', -0.144, 0.188), ('MR', 0.98, 0.704))
    draw_shu_wan_gou(t, ('TL', 0.908, 0.548), ('BC', 0.628, 1.184), ('BR', 0.588, 1.1))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_七.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
