"""Auto-composed: 山 — c48. Joint-snap + corner-by-type."""
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from shu import draw_shu
from shu_zhe import draw_shu_zhe

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
    draw_shu(t, ('TC', 0.34, 0.556), ('BC', 0.37, 0.785))
    draw_shu_zhe(t, ('ML', 0.236, 0.956), ('BL', 0.236, 0.659), ('BR', 0.637, 0.659))
    draw_shu(t, ('MR', 0.692, 0.588), ('BR', 0.644, 1.3))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_山.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
