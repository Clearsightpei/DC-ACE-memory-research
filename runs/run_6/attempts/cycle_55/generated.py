"""力 (li) — c55 attempt-2-or-3. pie.from.y lowered to heng_zhe_gou heng-y"""
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas(); ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(0)

def task_01(t, screen):
    reset(t)
    draw_heng_zhe_gou(t, ('ML', 0.364, 0.464), ('C', 0.444, 0.464), ('BC', 0.444, 0.996))
    draw_pie(t, ('C', 0.364, 0.414), ('BL', -0.04, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_力.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
