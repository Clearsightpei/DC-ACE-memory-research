"""Cycle 20 (run_5) — 末 / 未 / 五 carry-over fixes.

末 / 未 built from primitives directly (NOT draw_mu), because the 木
component in 末/未 is shifted DOWN and its heng is REPLACED by the
middle heng of the composite — so reusing draw_mu wholesale leaves an
extra heng. Stroke positions measured directly from the MMH GT PNGs.

五: 4 strokes per MMH order — top heng, left slanting shu, middle heng,
heng_zhe (right side wrap), and a closing left dot/diagonal omitted (五
is canonically 4 strokes).
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
from heng_zhe import draw as draw_hz         # noqa: E402


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
# 末 — top heng (long) above, middle heng (shorter), long shu, pie + na from
# the middle-heng crossing.
# Measured GT (800x600, origin TL, y down):
#   shu: x≈398, y=173..533 → turtle ox≈-2, oy=-53, scale=0.90
#   top heng: y≈257, x=274..521, width=247 → turtle ox=-3, oy=+43, scale=0.62
#   mid heng: y≈330, x=310..491, width=181 → turtle ox=0,  oy=-30, scale=0.45
#   pie head ≈ (392, 338) → turtle (-8, -38) — scale 0.40
#   na  head ≈ (408, 338) → turtle (+8, -38) — scale 0.45
# ---------------------------------------------------------------------------
def draw_mo(t):
    # 1. Top heng (the diagnostic LONG bar on top — this is what makes 末 = 末)
    draw_heng(t, ox=-3, oy=43, scale=0.62)
    # 2. Shu (long spine through both heng)
    draw_shu(t, ox=-2, oy=-53, scale=0.90)
    # 3. Middle heng (shorter than the top — this is the differentiator)
    draw_heng(t, ox=0, oy=-30, scale=0.45)
    # 4. Pie (left diagonal from mid-heng crossing)
    # pie default head at (150,200); at scale 0.40 → (60, 80). Want head at (-8,-38).
    s_pie = 0.40
    draw_pie(t, ox=-8 - 150 * s_pie, oy=-38 - 200 * s_pie, scale=s_pie)
    # 5. Na (right diagonal)
    # na default head at (-150, 200); at scale 0.45 → (-67.5, 90). Want head at (+8, -38).
    s_na = 0.45
    draw_na(t, ox=8 - (-150) * s_na, oy=-38 - 200 * s_na, scale=s_na)


# ---------------------------------------------------------------------------
# 未 — top heng SHORT (under the mid heng), middle heng longer.
# Measured GT:
#   shu: x≈397, y=171..532 → ox=-3, oy=-52, scale=0.90
#   top heng: y≈253, x=326..471, width=145 → ox=-2, oy=+47, scale=0.36
#   mid heng: y≈330, x=272..515, width=243 → ox=+22 (slight right bias), oy=-30, scale=0.60
#   pie/na heads ≈ (388, 336)/(404, 333) → turtle (-12, -36)/(+4, -33)
# ---------------------------------------------------------------------------
def draw_wei(t):
    # 1. Top heng (SHORT — the differentiator from 末)
    draw_heng(t, ox=-2, oy=47, scale=0.36)
    # 2. Shu
    draw_shu(t, ox=-3, oy=-52, scale=0.90)
    # 3. Middle heng (LONG — longer than top)
    draw_heng(t, ox=22, oy=-30, scale=0.60)
    # 4. Pie
    s_pie = 0.40
    draw_pie(t, ox=-12 - 150 * s_pie, oy=-36 - 200 * s_pie, scale=s_pie)
    # 5. Na
    s_na = 0.45
    draw_na(t, ox=4 - (-150) * s_na, oy=-33 - 200 * s_na, scale=s_na)


# ---------------------------------------------------------------------------
# 五 — 4 strokes (MMH order):
#   1. top heng:   y≈225, x=317..501, w=184 → ox=+9, oy=+75, scale=0.46
#   2. left shu (slanting left as it descends, but use straight shu — small slant lost):
#        head ≈ (390, 241) → (-10, +59); tail ≈ (341, 440) → (-59, -140).
#        Length ≈ 205; default shu length 400 → scale 0.50. Place mid at midpoint.
#        mid turtle = (-34, -40). Default mid (0,0) at scale 0.5.
#        So ox = -34, oy = -40, scale 0.50.
#   3. middle heng: y≈336, x=305..460, w=155 → ox=+82-400=... wait recompute.
#        cx = (305+460)/2 = 383 → turtle ox = -17. oy = 300-336 = -36. scale=155/400=0.39.
#   4. heng_zhe: arm corner≈(465,320), arm-start≈(378,320), vertical-end≈(445,440).
#        Default heng_zhe: arm (-100,+120)→(+100,+120); shu (+100,+120)→(+100,-80).
#        Horizontal span 200, vertical span 200. Measured: horizontal 87, vertical 120.
#        Use scale 0.50. At scale 0.50, default corner at (+50,+60), arm-start (-50,+60), shu-end (+50,-40).
#        Target corner = (65, -20) → ox = 65-50 = +15, oy = -20-60 = -80.
#        At those offsets: arm-start = (-35, -20) — close enough to (-22, -20).
#        Shu-end = (65, -120) — close to target (45, -140).
# ---------------------------------------------------------------------------
def draw_wu(t):
    # 1. Top heng
    draw_heng(t, ox=9, oy=75, scale=0.46)
    # 2. Left slanting shu (use straight shu — minor slant is acceptable)
    draw_shu(t, ox=-34, oy=-40, scale=0.50)
    # 3. Middle heng
    draw_heng(t, ox=-17, oy=-36, scale=0.39)
    # 4. Heng_zhe (right side wrap)
    draw_hz(t, ox=15, oy=-80, scale=0.50)
    # 5. Bottom heng (CLOSING the box) — the long bottom bar
    # bottom heng: y≈453, x=221..586, w=365, cx=403 → ox=+3, oy=-153, scale=0.91
    draw_heng(t, ox=3, oy=-153, scale=0.91)


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
        # Already configured. Just clear strokes.
        for tt in screen.turtles():
            tt.reset()
        screen.clear()
        # clear() resets world coords — re-establish them.
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
    render_one("02_未.png", draw_wei)
    render_one("03_五.png", draw_wu)


if __name__ == "__main__":
    main()
