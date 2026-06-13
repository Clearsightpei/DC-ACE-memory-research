import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import draw_heng
from heng_zhe_gou import draw_heng_zhe_gou
from pie import draw_pie

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
    # Brief specified ('BL', 0.032, 1.48) but y_frac=1.48 exceeds anchor validator's [-0.3, 1.3] range.
    # Clamping y_frac to 1.3 (max allowed); preserves direction.
    draw_pie(t, ('TL', 0.808, 0.456), ('BL', 0.032, 1.3))
    draw_heng_zhe_gou(t, ('TC', 0.112, 0.492), ('TR', 0.176, 0.516), ('BC', 0.604, 1.132))
    draw_heng(t, ('C', 0.12, 0.38), ('C', 0.804, 0.292))
    draw_heng(t, ('BC', 0.048, 0.076), ('C', 0.804, 0.98))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_月.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
