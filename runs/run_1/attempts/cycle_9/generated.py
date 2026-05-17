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


def heng(t, x, y, length, tilt=3):
    """Horizontal stroke starting at left end (x, y), faint upward tilt."""
    t.penup(); t.goto(x, y); t.setheading(tilt)
    t.pendown(); t.forward(length); t.penup()


def shu(t, x, y, length):
    """Vertical stroke starting at top (x, y), going straight down."""
    t.penup(); t.goto(x, y); t.setheading(270)
    t.pendown(); t.forward(length); t.penup()


def pie(t, x, y, length, total_rot=60):
    """Left-falling sweep: start (x, y) heading ~260, curve CW total_rot deg."""
    t.penup(); t.goto(x, y); t.setheading(260)
    t.pendown()
    steps = 60
    for _ in range(steps):
        t.forward(length / steps)
        t.right(total_rot / steps)
    t.penup()


def na(t, x, y, length):
    """Right-falling press: down-right, gentle bow, front-loaded curve."""
    t.penup(); t.goto(x, y); t.setheading(300)
    t.pendown()
    steps = 60
    for i in range(steps):
        t.forward(length / steps)
        t.left(0.45 if i < 35 else 0.12)
    t.penup()


# ── Task 01 | 天 | tian
def task_01(t):
    # Like 大 but with an EXTRA bar ON TOP, and pie/na must NOT rise
    # above the top bar. Stacking order: top short heng is the
    # highest element; lower (longer) heng below; pie+na hang BELOW
    # the lower heng, their tops at/below the lower bar.
    t.pensize(11)
    # Top bar: short, highest point of the character
    heng(t, -90, 150, 180, tilt=2)
    # Lower bar: longer, below the top bar
    heng(t, -150, 40, 300, tilt=2)
    # Pie: starts just BELOW the lower bar (NOT above the top bar),
    # sweeps down-left
    pie(t, 20, 30, 200, total_rot=55)
    # Na: starts just below the lower bar near centre, sweeps down-right
    na(t, -10, 30, 210)


# ── Task 02 | 本 | ben
def task_02(t):
    # 木 = heng crossed by a shu that pierces it from above; pie + na
    # branch down-outward from the crossing. Then one extra short
    # horizontal near the BOTTOM of the vertical = 本.
    t.pensize(11)
    # Main horizontal bar (the heng of 木)
    heng(t, -160, 70, 320, tilt=2)
    # Vertical shu pierces the heng from above (top above the bar)
    shu(t, 0, 170, 330)
    # Pie branches down-left from the crossing region
    pie(t, 10, 60, 175, total_rot=55)
    # Na branches down-right from the crossing region
    na(t, -5, 60, 185)
    # Extra short horizontal near the bottom of the vertical
    heng(t, -55, -120, 110, tilt=2)


# ── Task 03 | 口 | kou
def task_03(t):
    # Closed box: left vertical (shu), top + right side as one
    # horizontal-then-fold stroke, bottom horizontal closing it.
    t.pensize(11)
    half = 130          # half-width / half-height of the box
    left_x = -half
    right_x = half
    top_y = half
    bot_y = -half
    # Stroke 1: left vertical (shu) — top-left down to bottom-left
    shu(t, left_x, top_y, top_y - bot_y)
    # Stroke 2: heng-zhe — across the top then fold straight down
    # the right side (box top-right corner shape).
    t.penup(); t.goto(left_x, top_y); t.setheading(0)
    t.pendown()
    t.forward(right_x - left_x)      # top edge, left -> right
    t.right(90)
    t.forward(top_y - bot_y)         # right edge, top -> bottom
    t.penup()
    # Stroke 3: bottom horizontal closing the box
    heng(t, left_x, bot_y, right_x - left_x, tilt=0)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT); screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("天", task_01),
        ("本", task_02),
        ("口", task_03),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))


if __name__ == "__main__":
    main()
