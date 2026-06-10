"""Cycle 11 drawer — 十 / 干 / 工 (horizontal+vertical compositions).

Reuses heng.py and shu.py from success_bank. All positions measured
directly from GT PNGs (pixel→turtle: tx = px-400, ty = 300-py).
"""
import io
import os
import sys
import turtle
from PIL import Image

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from heng import draw as draw_heng  # noqa: E402
from shu import draw as draw_shu    # noqa: E402

WIDTH, HEIGHT = 800, 600


def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset(t):
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


# --- Recipes ----------------------------------------------------------------

def draw_shi(t):
    """十 — one heng + one shu crossing at center.
    GT measurements: H cx=406 cy=322 w=334; V cx=403 cy=357 h=333.
    """
    # heng centerline at (tx=6, ty=-22), span 334 → scale 0.835
    draw_heng(t, ox=6, oy=-22, scale=0.835)
    # shu centerline midpoint (tx=3, ty=-57), half-h 166.5 → scale 0.833
    draw_shu(t, ox=3, oy=-57, scale=0.833)


def draw_gan(t):
    """干 — top short heng + bottom long heng + shu through both.
    Top H: cx=408 cy=203 w=173. Bottom H: cx=405 cy=320 w=336.
    V: cx=402 cy=364 h=322.
    """
    # Top short heng: scale 0.43, at (8, 97)
    draw_heng(t, ox=8, oy=97, scale=0.43)
    # Bottom long heng: scale 0.84, at (5, -20)
    draw_heng(t, ox=5, oy=-20, scale=0.84)
    # Shu midpoint (2, -64), scale 0.805
    draw_shu(t, ox=2, oy=-64, scale=0.805)


def draw_gong(t):
    """工 — top short heng + bottom long heng + shu between them.
    Top H: cx=410 cy=248 w=193. Bottom H: cx=408 cy=436 w=341.
    V: cx=406 cy=342 h=188 (between the two heng).
    """
    # Top heng at (10, 52), scale 0.48
    draw_heng(t, ox=10, oy=52, scale=0.48)
    # Bottom heng at (8, -136), scale 0.853
    draw_heng(t, ox=8, oy=-136, scale=0.853)
    # Shu midpoint (6, -42), scale 0.47 (short — connects the two heng)
    draw_shu(t, ox=6, oy=-42, scale=0.47)


# --- Main -------------------------------------------------------------------

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.setworldcoordinates(-WIDTH/2, -HEIGHT/2, WIDTH/2, HEIGHT/2)
    screen.tracer(0, 0)
    screen.bgcolor("white")
    t = turtle.Turtle()

    for fname, fn in [("01_十.png", draw_shi),
                      ("02_干.png", draw_gan),
                      ("03_工.png", draw_gong)]:
        reset(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, fname))

    try:
        screen.bye()
    except Exception:
        pass


if __name__ == "__main__":
    main()
