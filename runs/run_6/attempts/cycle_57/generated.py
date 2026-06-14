"""自 (zi) — c57 attempt-2-or-3. pie.tail snapped to box-TL; internal hengs extended to box right wall"""
import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import draw_heng
from heng_zhe import draw_heng_zhe
from pie import draw_pie
from shu import draw_shu

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas(); ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(0)

def task_01(t, screen):
    reset(t)
    draw_pie(t, ('TC', 0.308, 0.224), ('ML', 0.664, 0.016))
    draw_shu(t, ('ML', 0.664, 0.016), ('BL', 0.764, 1.252))
    draw_heng_zhe(t, ('ML', 0.92, 0.112), ('C', 0.96, 0.112), ('BC', 0.96, 1.132))
    draw_heng(t, ('ML', 0.912, 0.864), ('C', 0.96, 0.704))
    draw_heng(t, ('BL', 0.912, 0.46), ('BC', 0.96, 0.332))
    draw_heng(t, ('BL', 0.868, 1.176), ('BR', 0.048, 1.048))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_自.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
