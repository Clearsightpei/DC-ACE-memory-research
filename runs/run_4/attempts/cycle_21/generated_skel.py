# ── Task 01 | 大 | da
"""
Skeleton phase for 大 (da, big), cycle 21, run_4.

大 = 横 (heng) + 撇 (pie) + 捺 (na).
The 撇 and 捺 apex sits ABOVE the heng; the heng cuts horizontally
through both limbs ~30-40% down from the apex. Limbs extend WIDER
than the heng's endpoints (±200 vs ±130).

Skeleton from GT (per task brief):
  Heng: (-130, +40) -> (+130, +40)
  撇:   head (+15, +130) -> tail (-200, -120)
  捺:   head (+15, +130) -> kick base (+220, -90), kick -> (+260, -75)

Uniform pensize 3 (skeleton convention, §5.2).
"""

import turtle


def setup():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(3)
    t.color("black")
    return screen, t


def draw_line(t, p0, p1):
    t.penup()
    t.goto(p0)
    t.pendown()
    t.goto(p1)
    t.penup()


def draw_da_skeleton(t):
    # Heng: horizontal bar through both limbs.
    draw_line(t, (-130, 40), (130, 40))

    # 撇: from apex above heng down-left to tail well outside heng's left end.
    draw_line(t, (15, 130), (-200, -120))

    # 捺: main sweep from apex down-right to kick base.
    draw_line(t, (15, 130), (220, -90))
    # 捺: flat kick out to tip.
    draw_line(t, (220, -90), (260, -75))


def main():
    screen, t = setup()
    draw_da_skeleton(t)
    screen.update()

    canvas = screen.getcanvas()
    canvas.postscript(file="01_大_skel.ps", colormode="color")
    try:
        from PIL import Image
        img = Image.open("01_大_skel.ps")
        img.save("01_大_skel.png", "png")
    except Exception as e:
        print(f"PNG conversion failed: {e}")

    screen.bye()


if __name__ == "__main__":
    main()
