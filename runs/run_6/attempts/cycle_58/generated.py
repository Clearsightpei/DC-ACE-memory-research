"""个 (ge) — c58. Raw MMH + corner-by-type + apex_share_pie_na."""
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
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
    t.penup(); t.goto(0,0); t.setheading(0)

def task_01(t, screen):
    reset(t)
    draw_pie(t, ('TC', 0.364, 0.348), ('BL', -0.084, 0.296))
    draw_na(t, ('TC', 0.54, 0.348), ('MR', 1.3, 0.996))
    draw_shu(t, ('C', 0.368, 0.572), ('BC', 0.512, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_个.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
