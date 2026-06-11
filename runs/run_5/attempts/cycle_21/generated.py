"""Cycle 21 (run_5) — 末 retry + 本 + 卞.

末: top heng scale 0.80 vs middle 0.45 (unambiguous diff, per c20 lesson).
本: 木 (draw_mu) + short bottom heng crossing the shu's lower portion.
卞: 下 (draw_xia) shifted down + small dian above its heng.

All rendered via turtle + postscript, no subprocess.
"""

import io
import os
import sys
import turtle

from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(OUT_DIR, "..", "..", "success_bank", "code")
sys.path.insert(0, SB)

from heng import draw as draw_heng           # noqa: E402
from shu import draw as draw_shu             # noqa: E402
from pie import draw as draw_pie             # noqa: E402
from na import draw as draw_na               # noqa: E402
from dian import draw as draw_dian           # noqa: E402
from mu import draw as draw_mu               # noqa: E402
from xia import draw as draw_xia             # noqa: E402


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


# ---------------------------------------------------------------------------
# 末 — top heng (LONG, scale 0.80) above, middle heng (SHORT, scale 0.45),
# long shu, pie + na fanning out from the middle-heng crossing.
#
# c20 had top scale 0.62 vs mid 0.45 — only 38% wider, panel said
# indistinguishable. Bumping top to 0.80 → ~78% wider than mid (0.45).
# Geometry inherited from c20 except for top heng scale:
#   shu: ox=-2, oy=-53, scale=0.90
#   top heng: ox=-3, oy=+43, scale=0.80  (was 0.62)
#   mid heng: ox=0,  oy=-30, scale=0.45
#   pie: scale 0.40, head at (-8, -38)
#   na : scale 0.45, head at (+8, -38)
# ---------------------------------------------------------------------------
def draw_mo(t):
    # 1. Top heng — the LONG diagnostic bar (scale 0.80, was 0.62 in c20)
    draw_heng(t, ox=-3, oy=43, scale=0.80)
    # 2. Shu (long spine through both heng)
    draw_shu(t, ox=-2, oy=-53, scale=0.90)
    # 3. Middle heng (SHORT — 0.45 vs top 0.80 ⇒ 78% wider top)
    draw_heng(t, ox=0, oy=-30, scale=0.45)
    # 4. Pie (left diagonal from mid-heng crossing)
    s_pie = 0.40
    draw_pie(t, ox=-8 - 150 * s_pie, oy=-38 - 200 * s_pie, scale=s_pie)
    # 5. Na (right diagonal)
    s_na = 0.45
    draw_na(t, ox=8 - (-150) * s_na, oy=-38 - 200 * s_na, scale=s_na)


# ---------------------------------------------------------------------------
# 本 — 木 + a short heng crossing the shu near its lower-middle.
#
# Use draw_mu(t) as base (heng + shu + pie + na). Add a short bottom heng.
# In mu: shu is at ox=-2, oy=-49, scale=0.87. Default shu length is 400, so
# scaled length ≈ 348, runs from y≈+125 down to y≈-225 (turtle coords).
# Mid heng of mu is at oy=+13. Add a small heng around y≈-65 (crossing the
# shu about 1/3 from the bottom — matches the GT placement).
# ---------------------------------------------------------------------------
def draw_ben(t):
    draw_mu(t)
    # Short bottom heng — sits below the upper heng but above the pie/na heads.
    # Centered on the shu (ox≈-2), oy≈-65, scale 0.30 (short dash).
    draw_heng(t, ox=-2, oy=-65, scale=0.30)


# ---------------------------------------------------------------------------
# 卞 — small top dian + 下 (heng + shu + dian) below.
#
# Reuse draw_xia(t) for the bottom 下. Shift xia down ~20 to leave room
# for the top dian. Place a small dian above the heng (oy ≈ +150 in xia
# frame ⇒ in turtle world after shift, oy ≈ +130).
# GT inspection: the top "stroke" is a short ribbon going down-right —
# matches a dian shape well.
# ---------------------------------------------------------------------------
def draw_bian(t):
    # 下 component, shifted down a bit
    draw_xia(t, ox=0, oy=-20, scale=1.0)
    # Top dot/pie above the heng of 下
    # xia's heng is at world oy = -20 + 75 = +55. Place dian above it.
    # Slightly left of center to match GT.
    draw_dian(t, ox=-15, oy=130, scale=1.4)


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
_SCREEN_INIT = False


def render_one(name, draw_fn):
    global _SCREEN_INIT
    screen = turtle.Screen()
    if not _SCREEN_INIT:
        screen.setup(WIDTH, HEIGHT)
        screen.setworldcoordinates(-WIDTH / 2, -HEIGHT / 2, WIDTH / 2, HEIGHT / 2)
        _SCREEN_INIT = True
    else:
        for tt in screen.turtles():
            tt.reset()
        screen.clear()
        screen.setworldcoordinates(-WIDTH / 2, -HEIGHT / 2, WIDTH / 2, HEIGHT / 2)
    screen.tracer(0, 0)
    t = turtle.Turtle()
    reset(t)
    draw_fn(t)
    screen.update()
    out_path = os.path.join(OUT_DIR, name)
    save_canvas_to_png(screen, out_path)
    return out_path


def main():
    render_one("01_末.png", draw_mo)
    render_one("02_本.png", draw_ben)
    render_one("03_卞.png", draw_bian)


if __name__ == "__main__":
    main()
