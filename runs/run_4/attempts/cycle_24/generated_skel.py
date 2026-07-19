"""Cycle 24 — 万 (wan) skeleton.

3 strokes:
  1. Top heng (long): (-130, +100) → (+170, +100)
  2. 横折钩 (right frame): corner (+170, +90) → drop to (+150, -130) → hook left to (+90, -110)
  3. 撇: head (+30, +130) [ABOVE heng] → tail (-130, -130)

The 撇 head must be visibly ABOVE the top heng — this is the distinguishing
feature of 万 vs 力.
"""

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
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.pensize(3)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


# ── Task 01 | 万 | wan
def draw_wan_skel(t):
    """Skeleton phase: uniform pensize 3, three strokes."""
    t.pensize(3)

    # Stroke 1: top heng (long)
    t.penup()
    t.goto(-130, 100)
    t.pendown()
    t.goto(170, 100)
    t.penup()

    # Stroke 2: 横折钩 (right frame) — corner at top-right just below heng's right end
    # Topology: short heng arm at top → 折 down → hook left at bottom
    t.penup()
    t.goto(40, 90)         # short top arm of the 横折钩
    t.pendown()
    t.goto(170, 90)        # corner top-right
    t.goto(150, -130)      # 折 down to bottom-right
    t.goto(90, -110)       # hook curls back up-left
    t.penup()

    # Stroke 3: 撇 — head ABOVE heng, sweeps down-left through heng and across the body
    t.penup()
    t.goto(30, 130)        # head (y=+130) is above heng (y=+100)
    t.pendown()
    t.goto(-130, -130)     # tail bottom-left
    t.penup()


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)
    t = turtle.Turtle()
    reset_turtle(t)
    draw_wan_skel(t)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_万_skel.png"))


if __name__ == "__main__":
    main()
