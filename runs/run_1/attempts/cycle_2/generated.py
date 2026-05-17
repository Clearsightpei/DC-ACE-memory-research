import io, os, turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Phase-1 atomic strokes: memory says aim for ~70 pixels total length
STROKE_LEN = 70


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset_turtle(t):
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.pensize(3)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


# ── Task 01 | 横 | heng
def task_01(t):
    # Horizontal stroke, left-to-right, faint upward tilt.
    # Memory: setheading(3) to setheading(5) — keep this; length ~70 px.
    t.penup()
    # Start slightly left of center so the stroke is centered on canvas.
    t.goto(-STROKE_LEN / 2, 0)
    t.setheading(4)  # very small upward tilt
    t.pendown()
    t.forward(STROKE_LEN)
    t.penup()


# ── Task 02 | 竖 | shu
def task_02(t):
    # Vertical stroke, top-to-bottom, perfectly straight.
    # Memory: setheading(270); forward(...) — approach correct; just shorten.
    t.penup()
    # Start above center so stroke is vertically centered.
    t.goto(0, STROKE_LEN / 2)
    t.setheading(270)  # south
    t.pendown()
    t.forward(STROKE_LEN)
    t.penup()


# ── Task 03 | 撇 | pie
def task_03(t):
    # Pie: starts upper-right, sweeps DOWN-AND-LEFT, convex toward the right.
    # Memory: previously drawn backwards (swept up-right). The fix:
    #   - start high, heading roughly SOUTH (slightly west of south)
    #   - per-step forward(small) + t.right(small_angle) so the path
    #     bows rightward as it descends (heading rotates toward
    #     west-of-south, i.e. heading goes from ~260 down toward ~210).
    t.penup()
    # Start near upper-right region. Total stroke length ~70 px.
    t.goto(STROKE_LEN / 2 * 0.7, STROKE_LEN / 2)
    # Initial heading: slightly west of south so motion begins downward,
    # angled a touch leftward already.
    t.setheading(260)
    t.pendown()
    steps = 35
    step_len = STROKE_LEN / steps
    # Total turning: ~50 degrees clockwise across the stroke.
    # Using t.right(...) (clockwise) rotates heading from 260 toward
    # 260 - 50 = 210, i.e. heading swings further west-of-south.
    # This makes the path curve convex to the right (bows right) while
    # ending lower-left. That matches the GT shape per memory.
    total_turn = 50.0
    turn_per_step = total_turn / steps
    for _ in range(steps):
        t.forward(step_len)
        t.right(turn_per_step)
    t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    for idx, (key, fn) in enumerate([
        ("heng", task_01),
        ("shu",  task_02),
        ("pie",  task_03),
    ], start=1):
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, f"{idx:02d}_{key}.png"))


if __name__ == "__main__":
    main()
