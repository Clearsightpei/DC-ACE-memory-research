"""Cycle 24 (run_5): 丰, 丘, 里.

Reuses Success Bank turtle primitives. Canvas 800x600.
Turtle → pixel: tx = px - 400, ty = 300 - py.
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


# ----------------------- 丰 -----------------------
# GT bbox x=[252,563] y=[169,535]. 4 strokes: 3 evenly-stacked heng + central shu through all.
# heng centers measured: y=250 (w=191), y=321 (w=192), y=402 (w=311).
# shu spans y=169..535, x-center ~393.
def draw_feng(t):
    # 1. Top heng — y=250 → ty=50, width 191
    draw_heng(t, ox=-3,  oy=50,   scale=0.478)
    # 2. Middle heng — y=321 → ty=-21, width 192
    draw_heng(t, ox=-3,  oy=-21,  scale=0.480)
    # 3. Bottom heng — y=402 → ty=-102, width 311
    draw_heng(t, ox=8,   oy=-102, scale=0.778)
    # 4. Central shu — protrudes above top heng and below bottom heng.
    # GT shu spans y=169..535 → ty 131..-235. center=-52, scale=0.915.
    draw_shu(t, ox=-7, oy=-52, scale=0.915)


# ----------------------- 丘 -----------------------
# GT bbox x=[237,576] y=[214,470]. 5 strokes per brief.
# comp1 (top): contains pie + short top heng (drawn merged in MMH).
# comp2: left shu, x=330, y=[285,446]
# comp3: middle heng y=334, x=[346,526], w=180
# comp4: right shu, x=441, y=[341,441] (small)
# comp5: bottom long heng y=456, x=[237,576] w=339
def draw_qiu(t):
    # 1. Short 撇 (top-left) — descends from upper-right to lower-left at the top of 丘.
    # pie canonical head (+150,+200) → tail (-180,-180). With scale s, head offset (+150s, +200s)+(ox,oy).
    # Want head near (tx=30, ty=80) and tail near (tx=-50, ty=30). s ~ 0.27.
    # head: 150*0.27=40.5 → ox=-10, oy=80-200*0.27=26. tail: (-180*0.27-10, -180*0.27+26) = (-58.6, -22.6). Want tail (-50, 30) -- tail too low.
    # Reduce scale and shift up.
    # s=0.22: head 33+ox, 44+oy; tail -39.6+ox, -39.6+oy. Want head (30, 80) tail (-50, 30).
    # head: ox=-3, oy=36. tail: -42.6, -3.6. tail still too low.
    # The pie has a steep diagonal; for a short top pie we accept some divergence.
    draw_pie(t, ox=-5, oy=46, scale=0.22)
    # 2. Top short heng — y=255 → ty=45, x=[346,455] width 109 → scale 0.27
    draw_heng(t, ox=0,  oy=45,  scale=0.27)
    # 3. Left 竖 — x=330, y=[285,446]. ty 15..-146, center=-66, length 161 → scale 0.40
    draw_shu(t, ox=-70, oy=-66, scale=0.40)
    # 4. Middle heng — y=334 → ty=-34, x=[346,526] center=436, width 180 → scale 0.45
    draw_heng(t, ox=36, oy=-34, scale=0.45)
    # 5. Right small 竖 (between middle and bottom heng) — x=441, y=[341,441]. ty -41..-141 center=-91, length 100 → scale 0.25
    draw_shu(t, ox=41, oy=-91, scale=0.25)
    # 6. Bottom long heng — y=456 → ty=-156, x=[237,576] center=406, width 339 → scale 0.85
    draw_heng(t, ox=6,  oy=-156, scale=0.85)


# ----------------------- 里 -----------------------
# GT bbox x=[242,577] y=[206,488]. 7 strokes: 日 (4) + 土 (3).
# 日: left竖 x=318, top heng y=215 x=[312,490], right竖 x=490, internal heng y~285, bottom heng y~350.
# 土: center 竖 x=400, middle heng y~395, bottom heng y=472 x=[242,577].
def draw_li(t):
    # 1. Left 竖 of 日 — x=318→ox=-82, y=[220,356] ty 80..-56, center 12, length 136 → scale 0.34
    draw_shu(t, ox=-82, oy=12, scale=0.34)
    # 2. Top heng of 日 — y=215→ty=85, x=[312,490] center 1, width 178 → scale 0.445
    draw_heng(t, ox=1, oy=85, scale=0.445)
    # 3. Right 竖 of 日 — x=490→ox=90, y=[215,350] ty 85..-50, center 17.5, length 135 → scale 0.338
    draw_shu(t, ox=90, oy=17, scale=0.338)
    # 4. Internal heng of 日 — y~283 → ty=17, width ~150 → scale 0.375, ox center between left&right verticals
    draw_heng(t, ox=4, oy=17, scale=0.375)
    # 5. Bottom heng of 日 (also top heng of 土) — y~350 → ty=-50, width ~178 → scale 0.445
    draw_heng(t, ox=1, oy=-50, scale=0.445)
    # 6. Center 竖 of 土 (extends from inside 日 down through the 土) — x~400, y=[285,460] ty 15..-160, center -72, len 175 → scale 0.44
    draw_shu(t, ox=0, oy=-72, scale=0.44)
    # 7. Middle heng of 土 — y~395 → ty=-95, x=[346,455] width ~107 → scale 0.27
    draw_heng(t, ox=0, oy=-95, scale=0.27)
    # 8. Bottom long heng — y=472→ty=-172, x=[242,577] center 10, width 335 → scale 0.84
    draw_heng(t, ox=10, oy=-172, scale=0.84)


def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.setworldcoordinates(-WIDTH/2, -HEIGHT/2, WIDTH/2, HEIGHT/2)
    screen.tracer(0, 0)
    screen.bgcolor("white")
    t = turtle.Turtle()

    for fn, draw_fn in [("01_丰.png", draw_feng),
                        ("02_丘.png", draw_qiu),
                        ("03_里.png", draw_li)]:
        reset(t)
        draw_fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, fn))
        print(f"wrote {fn}")

    try:
        screen.bye()
    except turtle.Terminator:
        pass


if __name__ == "__main__":
    main()
