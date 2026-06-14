"""Auto-composed: 半 — c52. Joint-snap + corner-by-type."""
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
    draw_dian(t, ('TL', 0.604, 0.716), ('C', 0.012, 0.108))
    draw_pie(t, ('TR', 0.308, 0.368), ('TC', 0.908, 0.956))
    draw_heng(t, ('ML', 0.712, 0.528), ('MR', 0.256, 0.38))
    draw_heng(t, ('BL', -0.144, 0.26), ('BR', 1.192, 0.116))
    draw_shu(t, ('TC', 0.264, 0.228), ('BC', 0.48, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_半.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
