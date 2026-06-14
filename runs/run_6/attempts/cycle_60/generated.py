"""古 (gu) — c60. Raw MMH + corner-by-type."""
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
    t.penup(); t.goto(0,0); t.setheading(0)

def task_01(t, screen):
    reset(t)
    draw_heng(t, ('ML', -0.044, 0.56), ('MR', 1.184, 0.472))
    draw_shu(t, ('TC', 0.372, 0.28), ('BC', 0.26, 0.352))
    draw_shu(t, ('BL', 0.6, 0.42), ('BL', 0.968, 1.3))
    draw_heng_zhe(t, ('BL', 0.892, 0.444), ('BC', 0.944, 0.444), ('BC', 0.944, 1.072))
    draw_heng(t, ('BC', 0.048, 1.232), ('BR', 0.22, 1.24))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_古.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
