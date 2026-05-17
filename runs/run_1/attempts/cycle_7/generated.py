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


# Helper strokes scaled to character size (~320px glyphs).
# Recipes carried verbatim from drawer_memory.md, scaled ~4.5x.

def stroke_heng(t, cx, cy, length, tilt=0):
    """Horizontal stroke centered at (cx, cy)."""
    t.penup()
    t.goto(cx - length / 2, cy)
    t.setheading(tilt)
    t.pendown()
    t.forward(length)
    t.penup()


def stroke_shu(t, top_x, top_y, length):
    """Vertical stroke from (top_x, top_y) going due south."""
    t.penup()
    t.goto(top_x, top_y)
    t.setheading(270)
    t.pendown()
    t.forward(length)
    t.penup()


def stroke_pie(t, start_x, start_y, length, total_rot=60, heading=260):
    """Left-falling sweep: ~60deg clockwise curve (memory recipe)."""
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(heading)
    t.pendown()
    steps = 60
    for _ in range(steps):
        t.forward(length / steps)
        t.right(total_rot / steps)
    t.penup()


def stroke_na(t, start_x, start_y, length, heading=300):
    """Right-falling press: front-loaded curve, flattening tail."""
    t.penup()
    t.goto(start_x, start_y)
    t.setheading(heading)
    t.pendown()
    steps = 60
    for i in range(steps):
        t.forward(length / steps)
        t.left(0.45 if i < 35 else 0.12)
    t.penup()


# ── Task 01 | 一 | yi
def task_01(t):
    # Memory hypothesis: 一 is an OCR blind spot; keep it NEAR-FLAT
    # (~0deg tilt, not 4deg) and use a THICKER pen so it reads as a
    # bold bar, not a hairline. Scale ~340px wide, centered.
    t.pensize(12)
    stroke_heng(t, 0, 0, 340, tilt=0)


# ── Task 02 | 大 | da
def task_02(t):
    # 大 = heng near top + pie and na crossing like arms/legs.
    t.pensize(9)
    # Top horizontal, ~300px, near-flat, sitting in upper region.
    stroke_heng(t, 0, 110, 300, tilt=0)
    # Pie: left-falling sweep starting from middle of the heng,
    # going down-left. Scaled-up 60deg-curve recipe (~300px).
    stroke_pie(t, 25, 110, 300, total_rot=55, heading=255)
    # Na: right-falling press starting near the same crossing point,
    # going down-right. Scaled-up na recipe (~300px).
    stroke_na(t, -5, 95, 300, heading=300)


# ── Task 03 | 木 | mu
def task_03(t):
    # 木 = heng crossed by shu; pie and na branch downward-outward
    # from the crossing.
    t.pensize(9)
    # Horizontal bar, ~300px, near top-middle.
    stroke_heng(t, 0, 90, 300, tilt=0)
    # Vertical down the center through the heng.
    stroke_shu(t, 0, 150, 320)
    # Pie branching down-left from the crossing (where heng meets shu).
    stroke_pie(t, 0, 70, 230, total_rot=55, heading=250)
    # Na branching down-right from the crossing.
    stroke_na(t, 0, 70, 230, heading=305)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT); screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("一", task_01),
        ("大", task_02),
        ("木", task_03),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))


if __name__ == "__main__":
    main()
