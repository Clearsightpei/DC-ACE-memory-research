import io, os, sys, turtle
from PIL import Image
WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)
from _anchor import anchor_to_xy
from heng import brushed_bezier

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1); img.convert("RGBA").save(path, "PNG")

def reset(t):
    t.reset(); t.hideturtle(); t.speed(0); t.pencolor("black")
    t.penup(); t.goto(0,0); t.setheading(90)

def w_main(s):
    if s < 0.10: return 14.0 - (s/0.10) * 3.0
    if s < 0.85: return 11.0
    return 11.0 + ((s-0.85)/0.15) * 2.0

def w_tail(s): return 13.0 - s * 9.0

def draw_heng_zhe_wan_gou(t, fa, c1a, c2a, ta):
    p0 = anchor_to_xy(fa); pc1 = anchor_to_xy(c1a); pc2 = anchor_to_xy(c2a); p3 = anchor_to_xy(ta)
    # Seg A: head→C1
    a1 = (p0[0] + (pc1[0]-p0[0])*0.33, p0[1] + (pc1[1]-p0[1])*0.33 + 4)
    a2 = (p0[0] + (pc1[0]-p0[0])*0.67, p0[1] + (pc1[1]-p0[1])*0.67 + 4)
    brushed_bezier(t, p0, a1, a2, pc1, w_main, samples=120)
    # Seg B: C1→C2 (long sweep, slight outward bow)
    b1 = (pc1[0] + (pc2[0]-pc1[0])*0.33 + 20, pc1[1] + (pc2[1]-pc1[1])*0.33)
    b2 = (pc1[0] + (pc2[0]-pc1[0])*0.67 + 10, pc1[1] + (pc2[1]-pc1[1])*0.67)
    brushed_bezier(t, pc1, b1, b2, pc2, w_main, samples=180)
    # Seg C: C2→tail (right sweep with slight upward arc)
    c1 = (pc2[0] + (p3[0]-pc2[0])*0.33, pc2[1] + (p3[1]-pc2[1])*0.33 + 10)
    c2 = (pc2[0] + (p3[0]-pc2[0])*0.67, pc2[1] + (p3[1]-pc2[1])*0.67 + 10)
    brushed_bezier(t, pc2, c1, c2, p3, w_tail, samples=120)

def task_01(t, screen):
    reset(t)
    draw_heng_zhe_wan_gou(t, ("TL", 0.43, 0.76), ("TC", 0.79, 0.69), ("BL", 0.5, 1.04), ("BR", 0.85, 0.30))
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_乙.png"))

def main():
    screen = turtle.Screen(); screen.setup(WIDTH, HEIGHT); screen.bgcolor("white"); screen.tracer(0)
    t = turtle.Turtle(); task_01(t, screen); screen.update()

if __name__ == "__main__":
    main()
