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
    t.penup(); t.goto(0,0); t.setheading(90)

def task_01(t, screen):
    reset(t)
    draw_heng(t, ('TL', 0.2, 0.88), ('TR', 0.968, 0.756))
    draw_pie(t, ('TC', 0.724, 0.84), ('BL', -0.088, 0.904))
    # Brief's shu to-anchor was ('BC', 0.464, 1.6); y_frac=1.6 exceeds
    # _anchor.py's [-0.3, 1.3] cap. Clamped to 1.3 to preserve direction.
    draw_shu(t, ('C', 0.288, 0.356), ('BC', 0.464, 1.3))
    draw_dian(t, ('C', 0.98, 0.88), ('BR', 0.988, 0.748))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_不.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
