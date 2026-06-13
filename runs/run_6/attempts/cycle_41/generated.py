"""Auto-composed: 白 — c41. MMH-derived anchors + bend corners."""
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import draw_heng
from heng_zhe import draw_heng_zhe
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
    draw_pie(t, ('TC', 0.248, 0.312), ('ML', 0.7, 0.404))
    draw_shu(t, ('ML', 0.188, 0.412), ('BL', 0.62, 1.196))
    draw_heng_zhe(t, ('ML', 0.392, 0.436), ('MR', 0.588, 0.404), ('BR', 0.232, 1.3))
    draw_heng(t, ('BL', 0.6, 0.208), ('BC', 0.932, 0.128))
    draw_heng(t, ('BL', 0.696, 0.948), ('BR', 0.072, 0.904))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_白.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
