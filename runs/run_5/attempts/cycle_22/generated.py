"""Cycle 22 (run_5) — 本 retry + 六 retry + 七 retry.

All three are visual-gate carry-overs from earlier cycles (本 c21 v=0.76,
六 c19 v=0.74, 七 c12/c17 v=0.76/0.79). Strategy: shrink the brushwork
surplus by tuning small diagonals down so total pixel mass approaches GT
skeleton more tightly, while preserving the structural signature OCR needs.

本: draw_mu base + small bottom heng dash, scale 0.22, placed close to the
    pie/na head zone (oy ~ -55).
六: top dian + heng + small 撇 (scale 0.22) + small right dian (scale 1.5).
七: tilted heng + shu_wan_gou shrunk to scale 0.78.

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
from heng import brushed_bezier               # noqa: E402
from shu import draw as draw_shu             # noqa: E402
from pie import draw as draw_pie             # noqa: E402
from dian import draw as draw_dian           # noqa: E402
from shu_wan_gou import draw as draw_swg     # noqa: E402
from mu import draw as draw_mu               # noqa: E402


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
# 本 — 木 (draw_mu) + a small bottom heng dash.
#
# GT measurements (turtle coords):
#   - top heng (middle bar of 木): spans tx[-110, +115], ty ≈ +25, slight up-tilt
#   - shu (long spine): top tx≈-5,ty≈+110 → bottom tx≈-2,ty≈-240
#   - pie head ~(-20,+5), tail ~(-180,-155)
#   - na  head ~(-20,+5), tail ~(+160,-150)
#   - bottom dash: spans tx[-90, +40], ty ≈ -130 (well below pie/na heads)
#
# c21 placed the dash at oy=-65 with scale 0.30 (full brushwork). Visual
# fell to 0.76 — surplus from the broad dash. Try scale 0.22 (matches the
# thin GT dash) at oy ≈ -55 (slightly higher → closer to the pie/na heads).
# ---------------------------------------------------------------------------
def draw_ben(t):
    # draw_mu uses pie scale 0.45, na scale 0.45, heng scale 0.55, shu scale 0.87.
    draw_mu(t)
    # Small bottom dash — slightly left of center, scale 0.22 (skeleton-thin).
    draw_heng(t, ox=-2, oy=-55, scale=0.22)


# ---------------------------------------------------------------------------
# 六 — top dian + heng + small 撇 (left) + small right dian.
#
# GT measurements (turtle coords):
#   - top dian: center tx≈-15, ty≈+115, small (scale ~1.3)
#   - heng: spans tx[-150,+130], ty ≈ +20 (slight up-tilt)
#   - 撇: head tx≈-50, ty≈-50; tail tx≈-110, ty≈-170 (short, steep)
#   - right dian: head tx≈+20, ty≈-50; tail tx≈+85, ty≈-175 (more vertical)
#
# c19 used pie scale 0.28 + right dian scale 2.0 — visual 0.74. The brief's
# fix: shrink pie to 0.22 and right dian to 1.5.
#
# Geometry for pie scale 0.22:
#   pie canonical head=(150,200), tail=(-180,-180), span dx=-330, dy=-380.
#   scale 0.22 → head canonical (33,44), tail canonical (-39.6,-39.6).
#   Want head ≈ (-50,-50). ox = -50 - 33 = -83. oy = -50 - 44 = -94.
#   Then tail = (-39.6 - 83, -39.6 - 94) = (-122.6, -133.6). dy from head
#   is -84 — shorter than GT's -120 but proportionally pie-shaped at 0.22.
#
# Geometry for right dian scale 1.5:
#   dian canonical entry (-25,+20), tail (+30,-25), dx=+55, dy=-45.
#   scale 1.5 → entry (-37.5,+30), tail (+45,-37.5).
#   Want entry ≈ (+20,-50). ox = +20 - (-37.5) = +57.5. oy = -50 - 30 = -80.
#   Then tail = (+45 + 57.5, -37.5 - 80) = (+102.5, -117.5). Approx GT.
# ---------------------------------------------------------------------------
def draw_liu(t):
    # 1) Top dian — small, slightly left of center, high up.
    draw_dian(t, ox=-10, oy=85, scale=1.3)
    # 2) Long heng — centered, slight up-tilt is built into draw_heng.
    draw_heng(t, ox=-10, oy=20, scale=0.70)
    # 3) Small 撇 (left), scale 0.22 (was 0.28 in c19).
    draw_pie(t, ox=-83, oy=-94, scale=0.22)
    # 4) Right dian, scale 1.5 (was 2.0 in c19), more downward-leaning.
    draw_dian(t, ox=57.5, oy=-80, scale=1.5)


# ---------------------------------------------------------------------------
# 七 — tilted heng + 竖弯钩 (smaller).
#
# GT measurements (turtle coords):
#   - heng: P0 (-150, -45) → P3 (+110, -20), tilted up-right
#   - shu_wan_gou: drop top ≈ (-25, +110); hook end ≈ (+180, -170)
#
# c17 used swg scale 1.0 — visual 0.79, just under 0.80. Shrink swg to
# scale 0.78 so its brushwork surplus drops.
#
# At swg scale 0.78:
#   canonical drop top (0,+150) → world (ox, +117+oy)
#   canonical hook end (+200,-100) → world (+156+ox, -78+oy)
#   Want drop top ≈ (-25, +90). ox = -25, oy = -27 → drop top = (-25, +90).
#   Then hook end = (+156-25, -78-27) = (+131, -105). Slightly shorter than
#   the c17 case but matches the GT span better when heng is also retracted.
#
# Heng spans GT tx[-150,+110]; tilted: P0 lower-left → P3 upper-right.
# Use the brushed_bezier directly with custom endpoints (same tilt trick
# as c17 did via draw_heng_tilted helper).
# ---------------------------------------------------------------------------

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


def draw_qi(t):
    # 1) Tilted heng — explicit endpoints, runs lower-left → upper-right.
    draw_heng_tilted(t, P0=(-150.0, -45.0), P3=(110.0, -10.0))
    # 2) 竖弯钩, scale 0.78 (was 1.0 in c17, 0.96 also tried).
    draw_swg(t, ox=-25.0, oy=-27.0, scale=0.78)


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
    render_one("01_本.png", draw_ben)
    render_one("02_六.png", draw_liu)
    render_one("03_七.png", draw_qi)
    try:
        turtle.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
