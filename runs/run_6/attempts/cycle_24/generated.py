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
    draw_dian(t, ('TC', 0.24, 0.288), ('TC', 0.744, 0.708))
    draw_heng(t, ('ML', 0.568, 0.38), ('MR', 0.456, 0.148))
    draw_heng(t, ('BL', 0.664, 0.32), ('BR', 0.236, 0.132))
    draw_shu(t, ('C', 0.38, 0.436), ('BC', 0.42, 1.08))
    draw_heng(t, ('BL', -0.076, 1.276), ('BR', 1.26, 1.216))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_主.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
