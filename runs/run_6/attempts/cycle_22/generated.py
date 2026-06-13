import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import draw_heng
from na import draw_na
from pie import draw_pie
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
    draw_heng(t, ('ML', 0.364, 0.412), ('MR', 0.516, 0.252))
    # Brief anchor BC y_frac=1.664 exceeds helper limit [-0.3, 1.3]; clamped to 1.3.
    draw_shu(t, ('TC', 0.264, 0.248), ('BC', 0.396, 1.3))
    draw_pie(t, ('C', 0.348, 0.472), ('BL', -0.028, 1.052))
    draw_na(t, ('C', 0.564, 0.496), ('BR', 1.256, 0.912))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_木.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
