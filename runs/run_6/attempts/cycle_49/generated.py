"""Auto-composed: 五 — c49. Joint-snap + corner-by-type."""
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
    draw_heng(t, ('TL', 0.668, 0.772), ('TR', 0.464, 0.616))
    draw_shu(t, ('TC', 0.237, 0.839), ('BL', 0.893, 0.929))
    draw_heng_zhe(t, ('ML', 0.544, 0.808), ('C', 0.762, 0.808), ('BC', 0.762, 0.877))
    draw_heng(t, ('BL', -0.296, 1.076), ('BR', 1.3, 1.108))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_五.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
