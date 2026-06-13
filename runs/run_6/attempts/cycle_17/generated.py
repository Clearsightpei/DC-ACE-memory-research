import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
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
    draw_heng(t, ('TL', 0.712, 0.58), ('TR', 0.408, 0.396))
    draw_heng(t, ('ML', -0.132, 0.76), ('MR', 1.188, 0.62))
    # Brief's BC y_frac=1.688 exceeds _anchor.py extended range [-0.3, 1.3];
    # clamped to 1.3 (the maximum representable extension) to preserve direction.
    draw_shu(t, ('TC', 0.312, 0.712), ('BC', 0.476, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_干.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
