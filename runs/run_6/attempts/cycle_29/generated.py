import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import draw_heng
from heng_zhe import draw_heng_zhe
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
    draw_shu(t, ('ML', 0.124, 0.028), ('BL', 0.592, 1.052))
    draw_heng_zhe(t, ('ML', 0.388, 0.076), ('MR', 0.744, 0.012), ('BR', 0.348, 1.116))
    draw_heng(t, ('ML', 0.836, 0.98), ('MR', 0.112, 0.856))
    draw_shu(t, ('C', 0.324, 0.116), ('BC', 0.388, 0.636))
    draw_heng(t, ('BL', 0.672, 0.864), ('BR', 0.236, 0.68))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_田.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
