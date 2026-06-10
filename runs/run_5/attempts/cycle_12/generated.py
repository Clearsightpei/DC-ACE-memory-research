"""Cycle 12 — 上 / 下 / 七.

Renders three Chinese characters by reusing Success Bank primitives and
saves three PNGs alongside this script. Same turtle + postscript pattern
that worked in c11.
"""

import io
import os
import sys
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, '..', '..', 'success_bank', 'code')
sys.path.insert(0, SB)

from heng import draw as draw_heng
from shu import draw as draw_shu
from dian import draw as draw_dian
from shu_wan_gou import draw as draw_swg


def _setup_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.screensize(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    return screen


def _save_postscript_as_png(screen, png_path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode='color',
                            width=WIDTH, height=HEIGHT,
                            pagewidth=WIDTH - 1, pageheight=HEIGHT - 1)
    img = Image.open(io.BytesIO(ps.encode('utf-8')))
    img = img.convert("RGB")
    # Normalize to exact size for the judge
    if img.size != (WIDTH, HEIGHT):
        img = img.resize((WIDTH, HEIGHT), Image.LANCZOS)
    img.save(png_path)


def draw_shang(t):
    """上 — 竖 (left, upper half) + short 横 + long bottom 横."""
    # 竖: centerline x≈-6 turtle. GT top y=+106, bottom y=-156, length 262.
    # shu canonical length = 400, scale = 262/400 ≈ 0.66, center oy=(106-156)/2=-25
    draw_shu(t, ox=-6, oy=-25, scale=0.66)
    # short 横: center turtle (+56, -17), width ~99, scale = 99/400 ≈ 0.25
    draw_heng(t, ox=56, oy=-17, scale=0.25)
    # long bottom 横: center turtle (+11, -167), width 324, scale = 324/400 ≈ 0.81
    draw_heng(t, ox=11, oy=-167, scale=0.81)


def draw_xia(t):
    """下 — long top 横 + 竖 (under, near center) + 点 to its right."""
    # top 横: center turtle (+5, +75), width 328, scale = 0.82
    draw_heng(t, ox=5, oy=75, scale=0.82)
    # 竖: center turtle (+3, -72), top y=+66, bottom y=-211, length 277.
    # shu canonical length 400, scale = 277/400 ≈ 0.69
    draw_shu(t, ox=3, oy=-72, scale=0.69)
    # 点: center turtle (+60, -27), width ~81, dian canonical width ~55 → scale 1.45
    draw_dian(t, ox=60, oy=-27, scale=1.45)


def draw_qi(t):
    """七 — slanted 横 + 竖弯钩 (vertical drop, curve right, up-right hook)."""
    # 竖弯钩 (drawn first so the heng crosses on top):
    #   A0 top at turtle ≈ (-37, +90), A3 bottom corner at turtle ≈ (-37, -150),
    #   so oy + 150s = 90 and oy - 100s = -150 → s=0.96, oy=-54, ox=-37
    draw_swg(t, ox=-37, oy=-54, scale=0.96)
    # 横 (slanted): centerline crosses around turtle (-9, -45), width 307,
    # scale = 307/400 ≈ 0.77. Heng's gentle tilt won't match the strong slant
    # exactly, but the bar placement and length are correct.
    draw_heng(t, ox=-9, oy=-45, scale=0.77)


def render_one(char_name, draw_fn, out_png):
    screen = _setup_screen()
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.reset()
    t.hideturtle()
    draw_fn(t)
    screen.update()
    _save_postscript_as_png(screen, out_png)
    print(f"wrote {out_png}")
    # bye the screen so the next render starts clean
    try:
        screen.clear()
    except Exception:
        pass


def main():
    out1 = os.path.join(OUT_DIR, "01_shang.png")
    out2 = os.path.join(OUT_DIR, "02_xia.png")
    out3 = os.path.join(OUT_DIR, "03_qi.png")

    screen = _setup_screen()
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # 上
    t.reset(); t.hideturtle()
    draw_shang(t)
    screen.update()
    _save_postscript_as_png(screen, out1)
    print(f"wrote {out1}")

    # 下
    t.reset(); t.hideturtle()
    draw_xia(t)
    screen.update()
    _save_postscript_as_png(screen, out2)
    print(f"wrote {out2}")

    # 七
    t.reset(); t.hideturtle()
    draw_qi(t)
    screen.update()
    _save_postscript_as_png(screen, out3)
    print(f"wrote {out3}")

    try:
        turtle.bye()
    except Exception:
        pass


if __name__ == "__main__":
    main()
