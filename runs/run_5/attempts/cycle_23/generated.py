"""Cycle 23 (run_5) — 升 + 千 + 正.

Three simple characters using small-pie + heng-stack + shu compositions:

升: pie (top-left small) + heng + heng (stacked, tilted) + shu (right, long).
千: small pie (top) + heng + shu through the heng's midpoint.
正: top heng + left shu + middle (short) heng + right shu + bottom long heng.

Apply the 生 (sheng.py) c13 lesson: keep 撇 small (scale ~0.30) to avoid
brushwork-surplus penalising visual_score. Reuse heng/shu/pie from the
success bank only.

Turtle + postscript only — no subprocess, no os.system.
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
from heng import brushed_bezier              # noqa: E402
from shu import draw as draw_shu             # noqa: E402
from pie import draw as draw_pie             # noqa: E402


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


def _w_heng_canonical_local(s: float) -> float:
    if s < 0.10:
        return 16.0 - (s / 0.10) * 5.0
    if s < 0.88:
        return 11.0 - ((s - 0.10) / 0.78) * 0.5
    return 10.5 + ((s - 0.88) / 0.12) * 8.5


def draw_heng_tilted(t, P0, P3):
    P1 = (P0[0] + (P3[0] - P0[0]) / 3.0, P0[1] + (P3[1] - P0[1]) / 3.0)
    P2 = (P0[0] + 2.0 * (P3[0] - P0[0]) / 3.0, P0[1] + 2.0 * (P3[1] - P0[1]) / 3.0)
    brushed_bezier(t, P0, P1, P2, P3, _w_heng_canonical_local, samples=220)


# ---------------------------------------------------------------------------
# 升 — pie (top-left small) + heng + heng + shu (right, long).
#
# GT measurements (turtle coords, est from 800x600 GT):
#   - top-left pie: head ~(-40, +110), tail ~(-110, -30). Short, steep.
#   - upper heng: x[-120, +160], y ≈ +5, slight up-tilt.
#   - lower heng: x[-180, +200], y ≈ -45, slight up-tilt (longer).
#   - right shu: top ~(+90, +130), bottom ~(+100, -210) (long, near-vertical).
#
# Strategy: small pie scale 0.30, two stacked heng (scales 0.70, 0.95),
# right shu scale 0.85.
#
# Pie geometry, scale 0.30:
#   canonical head=(150,200), tail=(-180,-180). scale 0.30 → head (45,60),
#   tail (-54,-54). Want head ≈ (-40, +110). ox = -40 - 45 = -85. oy = +110-60=+50.
#   Then tail = (-54 - 85, -54 + 50) = (-139, -4). Slightly higher tail than
#   GT (-30) — acceptable, structural signature is the small upper-left pie.
# ---------------------------------------------------------------------------
def draw_sheng_char(t):
    # 1) small top-left pie — tail lands at the upper heng's left end so
    #    pie+upper-heng forms a clear left arm.
    #    scale 0.30: head canonical (45,60), tail (-54,-54).
    #    Want tail ≈ (-110, +10) → ox = -110+54 = -56, oy = 10+54 = 64.
    #    Then head = (-56+45, 64+60) = (-11, 124). Reads as small pie top-center
    #    sweeping down to the upper-heng's left.
    draw_pie(t, ox=-56, oy=64, scale=0.30)
    # 2) upper heng — its left end near the pie's tail, around y=+10
    draw_heng(t, ox=15, oy=10, scale=0.62)
    # 3) lower heng — long, around y=-50
    draw_heng(t, ox=5, oy=-50, scale=0.95)
    # 4) right shu — long, the spine going down on the right
    draw_shu(t, ox=110, oy=-30, scale=0.90)


# ---------------------------------------------------------------------------
# 千 — small pie (top) + heng + shu (middle).
#
# GT measurements (turtle coords):
#   - top pie: head ~(+40, +80), tail ~(-120, +30). Short, near-horizontal tilt.
#   - heng: x[-150, +150], y ≈ -20, slight tilt.
#   - shu (through middle of heng): top ~(0, +20), bottom ~(0, -210).
#
# Strategy: small pie scale 0.30, heng scale 0.78, shu scale 0.80.
#
# Pie geometry, scale 0.30:
#   head canonical (45,60), tail (-54,-54). Want head ≈ (+40,+80).
#   ox = +40 - 45 = -5. oy = +80 - 60 = +20.
#   Then tail = (-54 - 5, -54 + 20) = (-59, -34). Steeper than GT but the
#   structural signature is "small top diagonal" — OCR will read.
# ---------------------------------------------------------------------------
def draw_qian(t):
    # 1) small top pie (scale 0.30) — first stroke
    draw_pie(t, ox=-5, oy=20, scale=0.30)
    # 2) heng — long, around y=-20
    draw_heng(t, ox=0, oy=-20, scale=0.78)
    # 3) shu — through middle of heng down to bottom
    draw_shu(t, ox=0, oy=-100, scale=0.78)


# ---------------------------------------------------------------------------
# 正 — top heng + left shu + middle heng + right shu + bottom heng.
#
# GT measurements (turtle coords, 800x600 GT):
#   - top heng: x[-60, +130], y ≈ +95.
#   - left shu: top ~(-50, +90), bottom ~(-55, -120). Short.
#   - middle heng: x[-30, +100], y ≈ -10. Short.
#   - right shu: top ~(+45, -10), bottom ~(+45, -120). Shorter.
#   - bottom heng: x[-130, +180], y ≈ -130. Longest.
#
# Strategy: 5 strokes, all with scaled placements.
#
# Note: GT uses traditional stroke order: 1.top heng 2.left shu 3.middle heng
#       4.right shu 5.bottom heng. Render in same order so overlaps look right.
# ---------------------------------------------------------------------------
def draw_zheng(t):
    # 1) top heng — short-ish, upper portion
    draw_heng(t, ox=35, oy=95, scale=0.48)
    # 2) left shu — descends from JUST BELOW top heng down to bottom heng.
    #    Must NOT protrude above top heng (else reads as 丘). scale 0.52 with
    #    oy=-45 → top (0,+59), bottom (0,-149); with ox=-50 places top at
    #    (-50,+59) (below top-heng y=+95) and bottom at (-50,-149) (just
    #    below bottom-heng y=-130).
    draw_shu(t, ox=-50, oy=-45, scale=0.52)
    # 3) middle heng — short, in the middle, slightly right of center
    draw_heng(t, ox=30, oy=-15, scale=0.33)
    # 4) right shu — descends from middle heng down to near bottom heng
    draw_shu(t, ox=60, oy=-75, scale=0.32)
    # 5) bottom heng — long, the base
    draw_heng(t, ox=25, oy=-130, scale=0.82)


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
    return out_path


def main():
    render_one("01_升.png", draw_sheng_char)
    render_one("02_千.png", draw_qian)
    render_one("03_正.png", draw_zheng)
    try:
        turtle.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
