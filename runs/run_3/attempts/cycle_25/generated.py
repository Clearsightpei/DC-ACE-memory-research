"""Cycle 25 drawer — 5 carry (也 寸 万 公 为) + 1 new (东).

Composition-precision push. Coords from task brief exactly. Width
floors enforced via t.pensize(max(3, w_profile(s))) inside the
Bezier inner loop.
"""

import io
import os
import turtle

from PIL import Image

WIDTH, HEIGHT = 800, 600
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


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


def brushed_bezier(t, P0, P1, P2, P3, w_profile, samples=160):
    """Cubic Bezier with per-sample width. Width floor=3."""
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


# ---- width profiles -----------------------------------------------------

def w_heng(s):
    # 横: heavy both ends, middle ~10, peaks 16
    if s < 0.1:
        return 16 - 60 * (0.1 - s)  # taper into start
    if s > 0.9:
        return 16 - 60 * (s - 0.9)
    if s < 0.25:
        return 16 - 30 * (s - 0.1)
    if s > 0.75:
        return 10 + 30 * (s - 0.75)
    return 10  # shaft


def w_shu(s):
    # 竖: heavy both ends, middle 10, peaks 16
    if s < 0.1:
        return 16 - 60 * (0.1 - s)
    if s > 0.9:
        return 16 - 60 * (s - 0.9)
    if s < 0.25:
        return 16 - 30 * (s - 0.1)
    if s > 0.75:
        return 10 + 30 * (s - 0.75)
    return 10


def w_pie(s):
    # 撇: heavy head (17), thin tail (2 only at very end), shaft 11
    if s < 0.15:
        return 17 - 30 * s  # 17 -> 12.5
    if s < 0.85:
        return 11
    if s < 0.95:
        return 11 - 60 * (s - 0.85)  # 11 -> 5
    return max(3, 5 - 40 * (s - 0.95))


def w_na(s):
    # 捺: thin head (4), shaft 10, heavy tail (18 belly near s~0.85)
    if s < 0.15:
        return 4 + 40 * s  # 4 -> 10
    if s < 0.7:
        return 10
    if s < 0.9:
        return 10 + 40 * (s - 0.7)  # 10 -> 18
    return 18 - 60 * (s - 0.9)  # taper kick


def w_dian(s):
    # 点: thin head, belly heavy (14), thin tail
    if s < 0.3:
        return 4 + (10 / 0.3) * s  # 4 -> 14
    if s < 0.6:
        return 14
    return max(3, 14 - 30 * (s - 0.6))


def w_gou(s):
    # 钩/复合 compound — keep middle thick, mild taper at ends
    if s < 0.1:
        return 14 - 30 * (0.1 - s)
    if s > 0.9:
        return max(4, 14 - 60 * (s - 0.9))
    return 12


# ---- main ---------------------------------------------------------------

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # ── Task 01 | 也 | yě ────────────────────────────────────────────
    # NO top heng — just (a) short heng, (b) short shu, (c) BIG 竖弯钩
    reset_turtle(t)
    # short heng (-100,+150)->(+30,+150)
    brushed_bezier(
        t,
        (-100, 150),
        (-60, 152),
        (-10, 152),
        (30, 150),
        w_heng,
    )
    # short shu (0,+130)->(0,+20)
    brushed_bezier(
        t,
        (0, 130),
        (0, 100),
        (0, 60),
        (0, 20),
        w_shu,
    )
    # BIG 竖弯钩 (-80,+50)->(-80,-150)->(+180,-150)->(+200,-90)
    # break into two Beziers: vertical drop with curve into horizontal sweep,
    # then horizontal sweep into upward hook.
    brushed_bezier(
        t,
        (-80, 50),
        (-80, -70),
        (-50, -150),
        (60, -150),
        w_gou,
    )
    brushed_bezier(
        t,
        (60, -150),
        (140, -150),
        (190, -150),
        (200, -90),
        w_gou,
    )
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_也.png"))

    # ── Task 02 | 寸 | cùn ───────────────────────────────────────────
    # heng top, 竖钩 with CURLED hook, 点 upper-right
    reset_turtle(t)
    # heng (-160,+100)->(+160,+100)
    brushed_bezier(
        t,
        (-160, 100),
        (-60, 105),
        (60, 105),
        (160, 100),
        w_heng,
    )
    # 竖钩 (0,+180)->(0,-160), then sharp curling hook up to (-90,-100)
    brushed_bezier(
        t,
        (0, 180),
        (0, 80),
        (0, -40),
        (0, -160),
        w_shu,
    )
    # curling hook — sharp curl up, not linear: control pts pull DOWN-LEFT then UP
    brushed_bezier(
        t,
        (0, -160),
        (-30, -180),
        (-80, -160),
        (-90, -100),
        w_gou,
    )
    # 点 upper-right above the heng
    brushed_bezier(
        t,
        (110, 160),
        (135, 145),
        (155, 130),
        (170, 110),
        w_dian,
    )
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_寸.png"))

    # ── Task 03 | 万 | wàn ───────────────────────────────────────────
    # heng top, 横折钩 right side, 撇 dramatic head HIGH at (+90,+260)
    reset_turtle(t)
    # heng (-160,+150)->(+160,+150)
    brushed_bezier(
        t,
        (-160, 150),
        (-60, 153),
        (60, 153),
        (160, 150),
        w_heng,
    )
    # 横折钩: starts at (-30,+150) along heng — actually a separate stroke
    # rendered as 横 segment then 折 down then 钩.
    # vertical part from (+160,+150) down to (+120,-150) with hook to (+60,-100)
    brushed_bezier(
        t,
        (160, 150),
        (155, 50),
        (140, -50),
        (120, -150),
        w_shu,
    )
    # hook
    brushed_bezier(
        t,
        (120, -150),
        (100, -140),
        (75, -115),
        (60, -100),
        w_gou,
    )
    # 撇 head DRAMATICALLY high (+90,+260), tail (-220,-180)
    # sweep from upper-right ABOVE heng down through to lower-left
    brushed_bezier(
        t,
        (90, 260),
        (40, 150),
        (-100, 30),
        (-220, -180),
        w_pie,
    )
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_万.png"))

    # ── Task 04 | 公 | gōng ──────────────────────────────────────────
    # 八 top (撇 + 捺), then 厶 small open-triangle below
    reset_turtle(t)
    # 八 撇: head (-30,+180) -> tail (-160,+30)
    brushed_bezier(
        t,
        (-30, 180),
        (-70, 130),
        (-115, 80),
        (-160, 30),
        w_pie,
    )
    # 八 捺: head (+30,+180) -> tail (+170,+30)
    brushed_bezier(
        t,
        (30, 180),
        (70, 130),
        (120, 80),
        (170, 30),
        w_na,
    )
    # 厶 small open triangle:
    # small 撇 (-20,-20)->(-100,-130)
    brushed_bezier(
        t,
        (-20, -20),
        (-50, -50),
        (-80, -90),
        (-100, -130),
        w_pie,
    )
    # 横折 (-100,-130)->(+40,-130)->(+40,-180)
    brushed_bezier(
        t,
        (-100, -130),
        (-40, -128),
        (20, -128),
        (40, -130),
        w_heng,
    )
    brushed_bezier(
        t,
        (40, -130),
        (40, -145),
        (40, -165),
        (40, -180),
        w_shu,
    )
    # closing 点 (+30,-170)->(+80,-200)
    brushed_bezier(
        t,
        (30, -170),
        (45, -180),
        (62, -190),
        (80, -200),
        w_dian,
    )
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "04_公.png"))

    # ── Task 05 | 为 | wèi ──────────────────────────────────────────
    # top 点 prominent slanted (+50,+220)->(+120,+170)
    # 撇 sweep down-left
    # 横折钩 with rounded turn
    # interior 点
    reset_turtle(t)
    # top 点 prominent slanted
    brushed_bezier(
        t,
        (50, 220),
        (72, 205),
        (98, 188),
        (120, 170),
        w_dian,
    )
    # 撇 from upper area sweeping down-left (head +20,+170, tail -180,-60)
    brushed_bezier(
        t,
        (20, 170),
        (-30, 110),
        (-100, 30),
        (-180, -60),
        w_pie,
    )
    # 横折钩: horizontal at top (-100,+100)->(+150,+100), then down to (+120,-100),
    # rounded turn, then hook at (+60,-80)
    brushed_bezier(
        t,
        (-100, 100),
        (-20, 103),
        (70, 103),
        (150, 100),
        w_heng,
    )
    # rounded folding turn down — soft curve, not sharp corner
    brushed_bezier(
        t,
        (150, 100),
        (155, 40),
        (140, -40),
        (120, -100),
        w_shu,
    )
    # hook at base curling left
    brushed_bezier(
        t,
        (120, -100),
        (100, -95),
        (75, -85),
        (60, -80),
        w_gou,
    )
    # interior 点 (lower-mid, the central dot of 为)
    brushed_bezier(
        t,
        (-40, 30),
        (-25, 18),
        (-8, 5),
        (10, -10),
        w_dian,
    )
    # bottom 点 (right of center, base of 为)
    brushed_bezier(
        t,
        (40, -30),
        (55, -45),
        (70, -60),
        (85, -75),
        w_dian,
    )
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "05_为.png"))

    # ── Task 06 | 东 | dōng ─────────────────────────────────────────
    # heng top, 竖钩 center w/ hook, 撇, 点, heng bottom
    reset_turtle(t)
    # heng top (-180,+150)->(+180,+150)
    brushed_bezier(
        t,
        (-180, 150),
        (-60, 153),
        (60, 153),
        (180, 150),
        w_heng,
    )
    # 竖钩 center (0,+90)->(0,-160) with hook to (-60,-130)
    brushed_bezier(
        t,
        (0, 90),
        (0, 10),
        (0, -80),
        (0, -160),
        w_shu,
    )
    brushed_bezier(
        t,
        (0, -160),
        (-20, -155),
        (-45, -140),
        (-60, -130),
        w_gou,
    )
    # 撇 (-30,+60)->(-180,-40)
    brushed_bezier(
        t,
        (-30, 60),
        (-80, 30),
        (-130, 0),
        (-180, -40),
        w_pie,
    )
    # 点 (+30,+60)->(+90,+20)
    brushed_bezier(
        t,
        (30, 60),
        (50, 47),
        (70, 33),
        (90, 20),
        w_dian,
    )
    # heng bottom (-180,-90)->(+180,-90)
    brushed_bezier(
        t,
        (-180, -90),
        (-60, -88),
        (60, -88),
        (180, -90),
        w_heng,
    )
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "06_东.png"))


if __name__ == "__main__":
    main()
