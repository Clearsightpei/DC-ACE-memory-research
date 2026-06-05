"""Cycle 19 drawer — 也, 巴, 寸, 万, 几, 公 (new).

All strokes rendered as smooth Bézier with per-sample pensize
(brushed_bezier). Width floors enforced (peak >= 14, middle >= 7).
"""

import io
import os
import turtle
from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


# ---------- I/O ----------

def save_canvas_to_png(screen, path):
    canvas = screen.getcanvas()
    ps = canvas.postscript(colormode="color")
    img = Image.open(io.BytesIO(ps.encode("utf-8")))
    img.load(scale=1)
    img.convert("RGBA").save(path, "PNG")


def reset_turtle(t):
    t.reset()
    t.hideturtle()
    t.speed(0)
    t.pencolor("black")
    t.pensize(3)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)


# ---------- Brush primitive ----------

def brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=160):
    """Cubic Bézier rendered as a continuous brushed line.

    Per-sample pensize. NEVER below 3 anywhere.
    """
    t.penup()
    t.goto(P0)
    t.pendown()
    for i in range(samples + 1):
        s = i / samples
        x = (1 - s) ** 3 * P0[0] + 3 * (1 - s) ** 2 * s * P1[0] + 3 * (1 - s) * s * s * P2[0] + s ** 3 * P3[0]
        y = (1 - s) ** 3 * P0[1] + 3 * (1 - s) ** 2 * s * P1[1] + 3 * (1 - s) * s * s * P2[1] + s ** 3 * P3[1]
        t.pensize(max(3, w_profile(s)))
        t.goto(x, y)
    t.penup()


# ---------- Width profiles (peak/middle/tip floors) ----------

def w_heng(s):
    # 横: heavy both ends, middle >=10, peak 16
    # bell-ish with raised ends
    end_weight = (1 - s) ** 2 + s ** 2  # 1 at ends, 0.5 at middle
    return 10 + 6 * end_weight  # 10..16


def w_shu(s):
    # 竖: heavy both ends, peak 16, middle 10
    end_weight = (1 - s) ** 2 + s ** 2
    return 10 + 6 * end_weight


def w_pie(s):
    # 撇: heavy head (17), tapers; shaft 11; only the very last 5% tapers to 2
    if s < 0.95:
        # 17 at s=0 -> 11 by s=0.95
        return 17 - (17 - 11) * (s / 0.95)
    # very tail tapers
    k = (s - 0.95) / 0.05
    return max(3, 11 - 8 * k)  # 11 -> 3


def w_na(s):
    # 捺: heavy tail (peak 18), shaft 10, head 4
    if s < 0.7:
        # head 4 -> shaft 10 over first 70%
        return 4 + (10 - 4) * (s / 0.7)
    # 70-100%: shaft 10 -> peak 18
    k = (s - 0.7) / 0.3
    return 10 + 8 * k


def w_ti(s):
    # 提: heavy base (14), shaft 9, very last 5% tapers to 2
    if s < 0.95:
        return 14 - (14 - 9) * (s / 0.95)
    k = (s - 0.95) / 0.05
    return max(3, 9 - 6 * k)


def w_dian(s):
    # 点: peak belly 14, tip 3, teardrop shape (heavy at start belly, tapers)
    if s < 0.3:
        return 14
    k = (s - 0.3) / 0.7
    return max(3, 14 - 11 * k)


def w_hook(s):
    # Generic hook arm: keep shaft 10, head 12. Compact.
    end_weight = (1 - s) ** 2 + s ** 2
    return 10 + 4 * end_weight


# ---------- Compound stroke helpers ----------

def draw_heng(t, x0, y0, x1, y1, samples=160):
    """Horizontal stroke as gentle bezier."""
    P0 = (x0, y0)
    P3 = (x1, y1)
    P1 = (x0 + (x1 - x0) * 0.33, y0 + 2)
    P2 = (x0 + (x1 - x0) * 0.66, y1 + 2)
    brushed_bezier(t, P0, P1, P2, P3, w_heng, samples)


def draw_shu(t, x0, y0, x1, y1, samples=160):
    P0 = (x0, y0)
    P3 = (x1, y1)
    P1 = (x0 + 2, y0 + (y1 - y0) * 0.33)
    P2 = (x1 + 2, y0 + (y1 - y0) * 0.66)
    brushed_bezier(t, P0, P1, P2, P3, w_shu, samples)


def draw_pie(t, P0, P3, curve=40, samples=180):
    """撇: from heavy head P0 down-left to tapered tail P3."""
    mid_x = (P0[0] + P3[0]) / 2
    mid_y = (P0[1] + P3[1]) / 2
    # bow leftward
    P1 = (P0[0] - curve * 0.3, P0[1] - (P0[1] - P3[1]) * 0.3)
    P2 = (mid_x - curve, mid_y - 10)
    brushed_bezier(t, P0, P1, P2, P3, w_pie, samples)


def draw_na(t, P0, P3, curve=30, samples=180):
    """捺: head P0 (fine) sweeping to tail P3 (heavy)."""
    mid_x = (P0[0] + P3[0]) / 2
    mid_y = (P0[1] + P3[1]) / 2
    P1 = (P0[0] + (P3[0] - P0[0]) * 0.3, P0[1] - (P0[1] - P3[1]) * 0.3)
    P2 = (mid_x + curve, mid_y - 10)
    brushed_bezier(t, P0, P1, P2, P3, w_na, samples)


def draw_dian(t, P0, P3, samples=80):
    """点: short stroke from belly to tail."""
    P1 = (P0[0] + (P3[0] - P0[0]) * 0.33, P0[1] + (P3[1] - P0[1]) * 0.33 + 4)
    P2 = (P0[0] + (P3[0] - P0[0]) * 0.66, P0[1] + (P3[1] - P0[1]) * 0.66 + 2)
    brushed_bezier(t, P0, P1, P2, P3, w_dian, samples)


# ---------- Characters ----------

def draw_ye(t):
    """也 — upper 横折钩 inset + middle 竖 + dominating 竖弯钩.

    Composition:
      - upper 横折钩 inset top-left: heng (-150,+120)->(0,+120), then 折 down to (0,+30), hook up-left.
      - middle 竖: at x≈-40 from y=+80 down to y=-60.
      - 竖弯钩: dominates bottom half. Starts at upper-middle (x=+30,y=+100),
        sweeps DOWN to (x=+30,y=-100), then BENDS RIGHT to (x=+150,y=-100),
        with a 50px up-hook tip at (x=+150,y=-50).
    """
    # Top-left 横折钩
    # heng part
    draw_heng(t, -180, 120, 10, 120)
    # 折 down (vertical) from (10,120) to (10,30)
    draw_shu(t, 10, 120, 10, 30)
    # small hook up-left from (10,30) to (-25,55)
    brushed_bezier(
        t,
        (10, 30), (5, 38), (-12, 48), (-30, 58),
        lambda s: max(3, 10 - 5 * s), samples=60,
    )

    # Middle short 竖
    draw_shu(t, -70, 80, -70, -40)

    # Dominating 竖弯钩
    # vertical part (y=+100 -> y=-100) at x=+40
    P0 = (40, 100)
    Pmid_v = (40, -100)
    # vertical segment with width floors
    brushed_bezier(
        t,
        P0, (42, 50), (42, -20), Pmid_v,
        w_shu, samples=160,
    )
    # bend right (y=-100 from x=+40 to x=+160), wide curve
    brushed_bezier(
        t,
        (40, -100), (60, -120), (120, -120), (180, -100),
        w_hook, samples=140,
    )
    # up-hook tip from (180,-100) to (180,-50)
    brushed_bezier(
        t,
        (180, -100), (185, -90), (185, -70), (180, -50),
        lambda s: max(3, 12 - 6 * s), samples=80,
    )


def draw_ba(t):
    """巴 — frame on top (wider than tall), 竖弯钩 BIG below.

    Frame: top heng (-120,+120)->(120,+120); left 竖 (-120,+120)->(-120,-30);
    right 竖 (120,+120)->(120,-30); inner heng (-120,+50)->(120,+50);
    bottom heng of frame (-120,-30)->(120,-30); plus small heng inside frame.
    竖弯钩: starts inside frame at top (x=-40,y=+60), drops down THROUGH frame
    bottom to y=-280, bends right to (x=+200,y=-280), hook tip at (+200,-260).
    """
    # Top frame
    draw_heng(t, -130, 130, 130, 130)            # top heng
    draw_shu(t, -130, 130, -130, -20)            # left 竖
    draw_shu(t, 130, 130, 130, -20)              # right 竖
    draw_heng(t, -130, 50, 130, 50)              # inner heng (mouth divider)
    draw_heng(t, -130, -20, 130, -20)            # frame bottom heng

    # 竖弯钩 — dominating BIG below
    # vertical part: (60, +130) -> (60, -280)   (starts at top inside frame, goes WAY down)
    brushed_bezier(
        t,
        (60, 130), (62, 50), (62, -100), (60, -280),
        w_shu, samples=200,
    )
    # bend right (y=-280, x=60 -> x=200)
    brushed_bezier(
        t,
        (60, -280), (90, -300), (150, -300), (200, -280),
        w_hook, samples=140,
    )
    # up-hook tip at (200,-280) -> (200,-240)
    brushed_bezier(
        t,
        (200, -280), (205, -270), (205, -255), (200, -240),
        lambda s: max(3, 12 - 6 * s), samples=80,
    )


def draw_cun(t):
    """寸 — heng + 竖钩 (with LONG hook) + 点 in upper-right.

    heng: (-180,+100)->(180,+100).
    竖钩: vertical at x=0 from y=+150 down to y=-160, then HOOK LEFT
          with arm 70 px long to (-70,-140).
    点: in upper-right above heng's right tip. Belly at (+150,+165),
        tail to (+170,+135) -- placed above heng, not beside 竖钩.
    """
    # heng
    draw_heng(t, -200, 100, 200, 100)
    # 竖钩 vertical
    brushed_bezier(
        t,
        (0, 170), (2, 80), (2, -50), (0, -160),
        w_shu, samples=200,
    )
    # LONG leftward hook arm from (0,-160) to (-75,-135)
    brushed_bezier(
        t,
        (0, -160), (-20, -160), (-50, -150), (-78, -130),
        lambda s: max(3, 13 - 7 * s), samples=120,
    )
    # 点 upper-right above heng tip
    draw_dian(t, (130, 165), (175, 130))


def draw_wan(t):
    """万 — heng + 撇 (head ABOVE heng) + 横折钩.

    heng: (-180,+100)->(160,+100). heng_y = 100.
    撇: head at (+60, +180) — y = heng_y + 80; sweeps DOWN through heng,
        exiting lower-left at (-180,-180).
    横折钩: starts at (+160,+100) [right end of heng], short heng to
        (+160,+100) then 折 down to (+120,-150), then hook left to (+60,-130).
    """
    # heng
    draw_heng(t, -200, 100, 180, 100)

    # 撇 — head ABOVE heng (y=+180), tail lower-left
    draw_pie(t, (60, 180), (-200, -180), curve=80, samples=200)

    # 横折钩 — from right end of heng going down then hook
    # vertical drop from (160,+100) to (120,-150)
    brushed_bezier(
        t,
        (160, 100), (155, 30), (140, -50), (120, -150),
        w_shu, samples=180,
    )
    # hook left from (120,-150) to (50,-130)
    brushed_bezier(
        t,
        (120, -150), (100, -150), (70, -140), (50, -130),
        lambda s: max(3, 12 - 6 * s), samples=100,
    )


def draw_ji(t):
    """几 — left 撇 + right 横折弯钩 with PROMINENT 钩.

    Left 撇: head (-90,+150) -> tail (-160,-150). Long sweep.
    Right 横折弯钩:
       - heng from (-90,+150) to (140,+150)
       - 折 down/curve to (140,-120) (slight inward)
       - 弯 right to (180,-150)
       - 钩 prominent UP-AND-LEFT: arm 70px to (130,-200).
    """
    # left 撇
    draw_pie(t, (-90, 150), (-170, -150), curve=70, samples=200)

    # heng top
    draw_heng(t, -90, 150, 140, 150)

    # right vertical / 弯 down: from (140,+150) curving inward to (130,-120)
    brushed_bezier(
        t,
        (140, 150), (140, 60), (135, -30), (130, -120),
        w_shu, samples=180,
    )

    # 弯 right at bottom: (130,-120) -> (180,-150)
    brushed_bezier(
        t,
        (130, -120), (150, -135), (165, -148), (180, -150),
        w_hook, samples=80,
    )

    # PROMINENT up-hook: arm 70+ px, tip up-and-left
    brushed_bezier(
        t,
        (180, -150), (175, -180), (155, -210), (115, -220),
        lambda s: max(3, 14 - 8 * s), samples=120,
    )


def draw_gong(t):
    """公 — top 八 (撇+捺) + 厶 below.

    八:
      - 撇: head (+5,+200) -> tail (-150,+30)
      - 捺: head (-10,+200) -> tail (+150,+30)
    厶:
      - 横撇: from (-80,-30) short heng to (+30,-30), then 撇 down-left
              to (-90,-180).
      - 点: closing dot on right side: belly (+30,-100), tail (+70,-150).
    """
    # 撇 (top-left limb of 八)
    draw_pie(t, (10, 200), (-150, 30), curve=50, samples=180)

    # 捺 (top-right limb of 八)
    draw_na(t, (-10, 200), (160, 30), curve=50, samples=180)

    # 厶 horizontal-stroke + descending 撇 (combined 横撇)
    # short heng (-80,-30) -> (+40,-30)
    draw_heng(t, -90, -30, 40, -30)
    # 撇 from (+40,-30) down-left to (-110,-190)
    draw_pie(t, (40, -30), (-110, -190), curve=60, samples=180)

    # 点 closing dot, right side of 厶
    draw_dian(t, (30, -90), (80, -150))


# ---------- Main ----------

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(3)

    tasks = [
        ("01_也.png", draw_ye),
        ("02_巴.png", draw_ba),
        ("03_寸.png", draw_cun),
        ("04_万.png", draw_wan),
        ("05_几.png", draw_ji),
        ("06_公.png", draw_gong),
    ]

    for filename, fn in tasks:
        reset_turtle(t)
        fn(t)
        screen.update()
        save_canvas_to_png(screen, os.path.join(OUT_DIR, filename))


if __name__ == "__main__":
    main()
