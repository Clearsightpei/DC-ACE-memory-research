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
    draw_shu(t, ('TL', 0.588, 0.812), ('BL', 0.66, 1.268))
    # Brief specified ('BR', 0.204, 1.4); clamped y_frac to 1.3 (max of anchor extension).
    draw_heng_zhe(t, ('TL', 0.888, 0.908), ('TR', 0.212, 0.888), ('BR', 0.204, 1.3))
    draw_heng(t, ('ML', 0.88, 0.896), ('C', 0.776, 0.824))
    draw_heng(t, ('BL', 0.812, 1.124), ('BC', 0.98, 0.976))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_日.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
