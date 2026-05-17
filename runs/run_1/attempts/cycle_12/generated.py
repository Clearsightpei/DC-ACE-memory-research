import io, os, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset_turtle(t):
    t.reset(); t.hideturtle(); t.speed(0)
    t.pencolor("black"); t.pensize(3)
    t.penup(); t.goto(0, 0); t.setheading(90)


# ---- sub-character primitives (scaled / positioned) -------------------------
# Each takes the turtle, a center (cx, cy), and a size s (full glyph width).

def draw_mu(t, cx, cy, s):
    """木 (tree): horizontal bar, vertical shu piercing it from ABOVE,
    pie/na splaying down-left/down-right from the crossing point.
    (Phase-2 rule: shu pierces heng from above; pie+na from the crossing.)"""
    half = s / 2.0
    # heng — full-width bar slightly above middle
    bar_y = cy + 0.10 * s
    t.penup(); t.goto(cx - half, bar_y); t.setheading(2)
    t.pendown(); t.forward(s); t.penup()
    # shu — vertical, starts above the bar, pierces down through it
    top_y = cy + half
    bot_y = cy - half
    t.goto(cx, top_y); t.setheading(270)
    t.pendown(); t.forward(top_y - bot_y); t.penup()
    # pie — from the crossing (bar_y) sweeping down-left
    t.goto(cx, bar_y); t.setheading(250)
    t.pendown()
    steps = 40
    for _ in range(steps):
        t.forward((0.55 * s) / steps)
        t.right(1.0)
    t.penup()
    # na — from the crossing sweeping down-right
    t.goto(cx, bar_y); t.setheading(300)
    t.pendown()
    for i in range(steps):
        t.forward((0.55 * s) / steps)
        t.left(0.8 if i < steps * 0.6 else 0.2)
    t.penup()


def draw_shi(t, cx, cy, s):
    """十 (cross): full-width horizontal + full-height vertical, centered."""
    half = s / 2.0
    t.penup(); t.goto(cx - half, cy); t.setheading(2)
    t.pendown(); t.forward(s); t.penup()
    t.goto(cx, cy + half); t.setheading(270)
    t.pendown(); t.forward(s); t.penup()


def draw_kou(t, cx, cy, w, h):
    """口 (box): a closed rectangle centered at (cx, cy)."""
    x0, x1 = cx - w / 2.0, cx + w / 2.0
    y0, y1 = cy - h / 2.0, cy + h / 2.0
    t.penup(); t.goto(x0, y1); t.setheading(0)
    t.pendown()
    t.goto(x1, y1)   # top
    t.goto(x1, y0)   # right
    t.goto(x0, y0)   # bottom
    t.goto(x0, y1)   # left, close
    t.penup()


# ── Task 01 | 林 | lin
def task_01(t):
    t.pensize(10)
    # two 木 side by side; left slightly narrower, same height
    draw_mu(t, cx=-95, cy=0, s=190)   # left, narrower
    draw_mu(t, cx=100, cy=0, s=210)   # right


# ── Task 02 | 古 | gu
def task_02(t):
    t.pensize(10)
    # 十 on top, 口 directly below
    draw_shi(t, cx=0, cy=110, s=210)
    draw_kou(t, cx=0, cy=-105, w=200, h=170)


# ── Task 03 | 困 | kun
def task_03(t):
    t.pensize(10)
    # large 口 enclosing a smaller 木
    draw_kou(t, cx=0, cy=0, w=360, h=360)
    draw_mu(t, cx=0, cy=0, s=210)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT); screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("林", task_01),
        ("古", task_02),
        ("困", task_03),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))


if __name__ == "__main__":
    main()
