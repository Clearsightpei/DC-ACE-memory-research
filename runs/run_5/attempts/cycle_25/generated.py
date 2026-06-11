"""Cycle 25 (run_5): 里 (c24 carry), 本 (c21+c22 carry), 天 (new).

Reuses Success Bank turtle primitives. Canvas 800x600.
Turtle → pixel: tx = px - 400, ty = 300 - py.

Fix notes:
  - 里 c24 1/3: panel said middle heng of 土 missing. Add a clearly
    visible short middle heng below the 日 and above the bottom long heng.
    Also lengthen the central 竖 from c24's scale 0.44 (length 175) up to
    0.64 (length 256) to match GT — c24 had the shu too short.
  - 本 c21/c22 v=0.76: try draw_mu(scale=0.92) + smaller bottom dash
    (scale=0.20 at oy=-58) to drop pixel surplus while keeping crossbar.
  - 天 (new): heng + heng + pie + na. Top heng short (scale~0.32 at
    ty=85), middle heng longer (scale~0.69 at ty=-30), pie + na heads
    meeting at middle heng center with scale 0.45 (木 lesson — small
    diagonals).
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

from heng import draw as draw_heng           # noqa: E402
from shu  import draw as draw_shu            # noqa: E402
from pie  import draw as draw_pie            # noqa: E402
from na   import draw as draw_na             # noqa: E402
from mu   import draw as draw_mu             # noqa: E402


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


# ============================================================
# 里 — 日 (4 strokes) + 土 (3 strokes), with middle-土-heng fix.
# GT measurements (px → turtle, ty = 300 - py):
#   - top heng of 日:   ty=78..72,  tx=[-108,+104], w=208, center=-2  → scale 0.52, oy=78
#   - internal heng of 日: ty=30..16, tx=[-81,+91], w=170, center=+5 → scale 0.43, oy=22
#   - bottom heng of 日 (= top of 土): ty=-26..-40, tx=[-70,+72], w=140 → scale 0.35, oy=-32
#   - central shu (through 土): tx=-2, ty=84..-172, length 256, center=-44 → scale 0.64
#   - left  竖 of 日: tx=-78..-68 (column band), ty=80..-180 (the LEFT side runs
#                     all the way down — actually it stops near ty=-50 in the
#                     character; the lower part is overlap with bottom heng).
#                     Use ty=78..-44, center=17, length ~120 → scale 0.30
#   - right 竖 of 日: tx=+88..+98, similar vertical extent → scale 0.30 at ox=+90
#   - middle 土 heng: short, around tx=-37, ty=-100, width ~80 → scale 0.22
#                     (GT shows this offset slightly left of shu center)
#   - bottom long heng: tx=+10, ty=-172, width 335 → scale 0.84
# ============================================================
def draw_li(t):
    # 1. Left 竖 of 日.
    draw_shu(t, ox=-78, oy=17, scale=0.30)
    # 2. Top heng of 日 (long).
    draw_heng(t, ox=-2, oy=78, scale=0.52)
    # 3. Right 竖 of 日.
    draw_shu(t, ox=90, oy=17, scale=0.30)
    # 4. Internal middle heng of 日.
    draw_heng(t, ox=5, oy=22, scale=0.43)
    # 5. Bottom heng of 日 (doubles as top heng of 土).
    draw_heng(t, ox=1, oy=-32, scale=0.35)
    # 6. Central 竖 through 土 (long: from just below top heng to bottom long heng).
    draw_shu(t, ox=-2, oy=-44, scale=0.64)
    # 7. Middle heng of 土 — short, slightly LEFT of shu center.
    #    THIS is the one c24 was missing/too-small. Place clearly between
    #    bottom-of-日 (ty=-32) and bottom-long-heng (ty=-172).
    #    Center ty ≈ -100. Width ~85 px → scale 0.21 (deliberately short, like GT).
    draw_heng(t, ox=-35, oy=-100, scale=0.22)
    # 8. Bottom long heng of 土.
    draw_heng(t, ox=10, oy=-172, scale=0.84)


# ============================================================
# 本 — draw_mu (slightly shrunk) + small bottom dash.
# Brief recipe: draw_mu(scale=0.92), draw_heng(ox=-2, oy=-58, scale=0.20).
# ============================================================
def draw_ben(t):
    draw_mu(t, scale=0.92)
    draw_heng(t, ox=-2, oy=-58, scale=0.20)


# ============================================================
# 天 — 2 heng + pie + na.
# GT measurements (turtle coords):
#   - top heng:     ty≈85, tx_center≈+10, width ~125 → scale 0.31
#   - middle heng:  ty≈-30, tx_center≈0,  width ~275 → scale 0.69
#   - pie head ≈ middle-heng center (0,-30), descending lower-left
#   - na  head ≈ middle-heng center (0,-30), descending lower-right
#
# Pie canonical head=(+150,+200). For head at (0,-30) with scale s:
#   ox = 0 - 150s, oy = -30 - 200s. s=0.45 → ox=-67.5, oy=-120.
#   Tail at (-180s+ox, -180s+oy) = (-148.5, -201). Within bbox.
#
# Na canonical head=(-150,+200). For head at (0,-30) with scale s:
#   ox = 0 + 150s, oy = -30 - 200s. s=0.45 → ox=+67.5, oy=-120.
#   Kick tip at (240s+ox, -172s+oy) = (175.5, -197.4). Within bbox.
#
# Use scale 0.45 — matches mu.py's mastered diagonal scale (木 c14 lesson:
# pie/na at 0.45 keep visual > 0.8; larger scales overshoot brushwork).
# ============================================================
def draw_tian(t):
    # 1. Top heng (short cap).
    draw_heng(t, ox=10, oy=85, scale=0.32)
    # 2. Middle heng (longer).
    draw_heng(t, ox=0, oy=-30, scale=0.69)
    # 3. 撇 — head at middle heng center, descending lower-left.
    draw_pie(t, ox=-67.5, oy=-120.0, scale=0.45)
    # 4. 捺 — head at middle heng center, descending lower-right.
    draw_na(t, ox=67.5, oy=-120.0, scale=0.45)


# ============================================================
# Driver
# ============================================================
_SCREEN_INIT = False


def render_one(name, draw_fn):
    global _SCREEN_INIT
    screen = turtle.Screen()
    if not _SCREEN_INIT:
        screen.setup(WIDTH, HEIGHT)
        screen.setworldcoordinates(-WIDTH / 2, -HEIGHT / 2, WIDTH / 2, HEIGHT / 2)
        screen.bgcolor("white")
        _SCREEN_INIT = True
    else:
        for tt in screen.turtles():
            tt.reset()
        screen.clear()
        screen.setworldcoordinates(-WIDTH / 2, -HEIGHT / 2, WIDTH / 2, HEIGHT / 2)
        screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    reset(t)
    draw_fn(t)
    screen.update()
    out_path = os.path.join(OUT_DIR, name)
    save_canvas_to_png(screen, out_path)
    print(f"wrote {name}")
    return out_path


def main():
    render_one("01_里.png", draw_li)
    render_one("02_本.png", draw_ben)
    render_one("03_天.png", draw_tian)
    try:
        turtle.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
