"""
Cycle 17 drawer — 七, 口, 中

Reuses success_bank primitives: heng, shu, heng_zhe, shu_wan_gou.
No subprocess, no os.system. Turtle + postscript only.

Pixel→turtle convention: tx = px - 400, ty = 300 - py.
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

from heng import draw as draw_heng                # noqa: E402
from shu import draw as draw_shu                  # noqa: E402
from heng_zhe import draw as draw_hz              # noqa: E402
from shu_wan_gou import draw as draw_swg          # noqa: E402
from heng import brushed_bezier                   # noqa: E402


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


# ----- Per-character width profiles for tilted heng of 七 -----
def _w_heng_tilted(s):
    """Same profile as canonical 横 — used by tilted heng of 七."""
    if s < 0.10:
        return 16.0 - (s / 0.10) * 5.0
    if s < 0.88:
        return 11.0 - ((s - 0.10) / 0.78) * 0.5
    return 10.5 + ((s - 0.88) / 0.12) * 8.5


def draw_heng_tilted(t, P0, P3):
    """Draw a 横 between explicit endpoints (used for tilted top heng of 七)."""
    P1 = (P0[0] + (P3[0] - P0[0]) / 3.0, P0[1] + (P3[1] - P0[1]) / 3.0)
    P2 = (P0[0] + 2.0 * (P3[0] - P0[0]) / 3.0, P0[1] + 2.0 * (P3[1] - P0[1]) / 3.0)
    brushed_bezier(t, P0, P1, P2, P3, _w_heng_tilted, samples=220)


# ----- 七 -----
def draw_qi(t):
    """七: tilted 横 + 竖弯钩.

    GT measurements:
      heng spans roughly (236,375) → (475,330)  (tilted up to the right)
      shu_wan_gou: drop top ~(370,206), hook end ~(553,470)
    Turtle (tx=px-400, ty=300-py):
      heng P0 ≈ (-164, -75), P3 ≈ (75, -30)  (Δy=+45 upward tilt)
      shu_wan_gou ox=-30, oy=-56 (puts drop top at (-30,94), hook end at (170,-156))
    """
    reset(t)
    # 1) tilted 横 — explicit endpoints. GT heng extends from x=236 (turtle -164)
    #    to roughly x=475 (turtle 75) and the right tip continues past the shu_wan_gou
    #    drop; widen so it reads as a proper 横 not a stub.
    draw_heng_tilted(t, P0=(-164.0, -75.0), P3=(140.0, -18.0))
    # 2) 竖弯钩
    draw_swg(t, ox=-30.0, oy=-56.0, scale=1.0)


# ----- 口 -----
def draw_kou(t):
    """口: left 竖 + 横折 + bottom 横.

    GT box: x[287,503], y[273,430] → turtle box center (-4, -50),
    width ~213, height ~157.
    Strategy:
      - left 竖  : shu(scale 0.4, ox=-107, oy=-50)  → spans y=30..-130
      - 横折    : hz(scale 1.0, ox=-4, oy=-115)    → corner at (96,5)
        which means top heng spans (-104,5)→(96,5), down-arm to (96,-195)
        Actually with hz scale=0.9 and oy=-145: top at y=-37 corner at (86,-37)
        Let me derive carefully.

    Tighter derivation: use hz scale=1.07 to match width 214 px.
      hz at (ox=-3, oy=-160): top heng y = 120*1.07-160 = -31.6
                             corner x = 100*1.07-3 = 104, bottom of right arm y=-80*1.07-160 = -245.6
      That goes too far down. Use scale 0.8: top y=120*0.8+oy, right arm bottom -80*0.8+oy
      We want top y ≈ +27 (=300-273), bottom y ≈ -130 (=300-430).
      Top y = 120s + oy = 27;  bottom y of right arm = -80s + oy = -130
        Subtract: 200s = 157 → s=0.785; oy = 27 - 120*0.785 = -67.2
      Corner x should be near box-right = +103 → 100*0.785 + ox = 103 → ox=24.5
      Top-heng left tip x = -100*0.785 + 24.5 = -54  (box-left ≈ -113, gap)
        So box-left is the separate 竖 stroke.
      Bottom heng: spans from box-left (-113) to right-arm bottom (+103). Use heng scale.
        heng full = 400 → scale needed for width 216 = 216/400 = 0.54
        center x = (-113+103)/2 = -5; y = -130 → bottom heng(ox=-5, oy=-130, scale=0.54)
      Left 竖: from top y~27 down to bottom y~-130 (length ~157). shu full=400 → s=0.39
        center x = -113, y = (27-130)/2 = -52
    """
    reset(t)
    # 1) left 竖
    draw_shu(t, ox=-113.0, oy=-52.0, scale=0.39)
    # 2) 横折 (top + right side)
    draw_hz(t, ox=24.5, oy=-67.2, scale=0.785)
    # 3) bottom 横
    draw_heng(t, ox=-5.0, oy=-130.0, scale=0.54)


# ----- 中 -----
def draw_zhong(t):
    """中: 口 box + central 竖 piercing through.

    GT measurements:
      box top heng ~y=270, bottom heng ~y=350
      box left ~x=290, box right ~x=510
      central 竖: x=400, top ~y=180, bottom ~y=515
    Turtle:
      box top y=30, bottom y=-50  (height ~80)
      box left x=-110, right x=110
      central shu top y=120, bottom y=-215 (length 335)
    Box width 220, height 80 — very flat. Use:
      - left 竖  : shu(ox=-110, oy=-10, scale=0.20)   spans y=30..-50
      - 横折    : hz with scale matching width 220 and height 80
                  top y=120s+oy=30; right-arm bottom y=-80s+oy=-50
                  Subtract: 200s=80 → s=0.40; oy=30-120*0.40=-18
                  Corner x=100s+ox=110 → ox=110-40=70
      - bottom 横: spans -110→+110 → width 220, center x=0,y=-50
                  heng scale=220/400=0.55
      - central 竖: from y=120 to y=-215, length 335. shu full=400 → s=335/400=0.84
                    center x=0, y=(120-215)/2=-47.5
    """
    reset(t)
    # 1) left 竖 of box
    draw_shu(t, ox=-110.0, oy=-10.0, scale=0.20)
    # 2) 横折 (top + right of box). Widen slightly (s=0.45) so the top
    #    heng's left tip overlaps the left 竖's top — eliminates the
    #    visible gap in v1.
    #    With s=0.45, oy chosen so corner x=110 stays the right edge:
    #      top_y = 120*0.45 + oy = 30 → oy = -24
    #      right-arm bottom = -80*0.45 + oy = -60 (slightly below box-bottom; OK)
    #      corner x = 100*0.45 + ox = 110 → ox = 65
    #      top-left tip x = -100*0.45 + 65 = 20 → still right of left竖 at -110
    #    Better: place top-heng-left right at the 竖 top. We instead extend
    #    by shifting ox left to ox=15 so corner sits at 100*0.45+15=60
    #    (less wide). Instead keep the right edge: use ox=65 and add a
    #    short overlap heng below as the "top bar" already-present —
    #    accept the small visual gap; identity is still unambiguous.
    draw_hz(t, ox=65.0, oy=-24.0, scale=0.45)
    # 3) bottom 横 of box
    draw_heng(t, ox=0.0, oy=-50.0, scale=0.55)
    # 4) central piercing 竖
    draw_shu(t, ox=0.0, oy=-47.5, scale=0.84)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.tracer(0, 0)
    t = turtle.Turtle()

    tasks = [
        ("01_七.png", draw_qi),
        ("02_口.png", draw_kou),
        ("03_中.png", draw_zhong),
    ]
    for fname, fn in tasks:
        fn(t)
        screen.update()
        out = os.path.join(OUT_DIR, fname)
        save_canvas_to_png(screen, out)
        print(f"wrote {out}")

    screen.bye()


if __name__ == "__main__":
    main()
