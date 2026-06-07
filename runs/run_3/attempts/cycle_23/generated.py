"""Cycle 23 drawer — 5 carry + 为 (NEW).

Width floors mandatory: pensize never below 3 anywhere, peak >= 14, shaft >= 7.
Smooth Bezier centerline with per-sample pensize (NOT dot stamps).
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


# ----- width profiles -----

def w_heng(s):
    # 横 — heavy ends, shaft middle
    if s < 0.1:
        return 16 - 4 * (s / 0.1)        # 16 -> 12
    if s > 0.9:
        return 12 + 4 * ((s - 0.9) / 0.1)  # 12 -> 16
    return 12  # shaft >= 10 floor


def w_shu(s):
    # 竖 — heavy ends, shaft middle
    if s < 0.1:
        return 16 - 4 * (s / 0.1)
    if s > 0.9:
        return 12 + 4 * ((s - 0.9) / 0.1)
    return 12


def w_pie(s):
    # 撇 — heavy head, tapered tail
    if s < 0.15:
        return 17 - 5 * (s / 0.15)        # 17 -> 12
    if s > 0.92:
        # tip: down to 3 at very end
        return max(3, 11 - 8 * ((s - 0.92) / 0.08))
    return 12  # shaft >= 11


def w_na(s):
    # 捺 — fine head, heavy tail
    if s < 0.1:
        return 6 + 6 * (s / 0.1)          # 6 -> 12
    if s > 0.85:
        return 12 + 6 * ((s - 0.85) / 0.15)  # 12 -> 18
    return 12


def w_dian(s):
    # 点 — heavy belly, tapered tail (peak 18 for "bigger" cases)
    if s < 0.35:
        return 8 + 10 * (s / 0.35)        # 8 -> 18
    if s < 0.7:
        return 18 - 4 * ((s - 0.35) / 0.35)  # 18 -> 14
    return max(3, 14 - 11 * ((s - 0.7) / 0.3))  # 14 -> 3


def w_dian_small(s):
    # 点 — peak 14, used for top 点
    if s < 0.35:
        return 7 + 7 * (s / 0.35)
    if s < 0.7:
        return 14 - 3 * ((s - 0.35) / 0.35)
    return max(3, 11 - 8 * ((s - 0.7) / 0.3))


def w_thick(s):
    # uniform fat profile for hook/sweep segments where we want unmistakable presence
    if s < 0.1:
        return 16 - 4 * (s / 0.1)
    if s > 0.9:
        return max(4, 12 - 8 * ((s - 0.9) / 0.1))
    return 12


def w_hook_short(s):
    # short hook arm — stay heavy
    return max(8, 14 - 6 * s)


# ----------------- main -----------------

def main():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("white")
    screen.tracer(0, 0)
    t = turtle.Turtle()
    reset_turtle(t)

    # ── Task 01 | 也 | yě
    # 3 strokes: 横折钩 (top), middle 竖, BIG 竖弯钩.
    reset_turtle(t)
    # (a) 横折钩 — heng then 折 down then small hook
    # heng (-100,+150) -> (+50,+150)
    brushed_bezier(t, (-100, 150), (-50, 152), (10, 152), (50, 150), w_heng)
    # 折 down (+50,+150) -> (+50,+30)
    brushed_bezier(t, (50, 150), (52, 110), (52, 70), (50, 30), w_shu)
    # small hook to (+15, +50)
    brushed_bezier(t, (50, 30), (40, 35), (28, 42), (15, 50), w_hook_short)
    # (b) middle 竖 (0,+90) -> (0,-20)
    brushed_bezier(t, (0, 90), (1, 60), (1, 20), (0, -20), w_shu)
    # (c) BIG 竖弯钩: down then right then up hook
    # vertical segment (-50,+10) -> (-50,-150)
    brushed_bezier(t, (-50, 10), (-50, -40), (-50, -100), (-50, -150), w_shu)
    # horizontal sweep (-50,-150) -> (+180,-150)
    brushed_bezier(t, (-50, -150), (20, -155), (110, -155), (180, -150), w_thick)
    # up-hook (+180,-150) -> (+180,-95)
    brushed_bezier(t, (180, -150), (182, -130), (182, -110), (180, -95), w_hook_short)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "01_也.png"))

    # ── Task 02 | 寸 | cùn
    # heng (-130,+50)->(+130,+50). 竖钩 (0,+100)->(0,-120) hook (-60,-95). 点 belly(+85,0) tail(+125,-25).
    reset_turtle(t)
    # heng
    brushed_bezier(t, (-130, 50), (-60, 52), (60, 52), (130, 50), w_heng)
    # 竖 (0,+100) -> (0,-120)
    brushed_bezier(t, (0, 100), (1, 50), (1, -40), (0, -120), w_shu)
    # hook arm (0,-120) -> (-60,-95)
    brushed_bezier(t, (0, -120), (-20, -110), (-45, -100), (-60, -95), w_hook_short)
    # 点 bigger — peak 18; belly (+85,0) tail (+125,-25)
    # head a bit up-left from belly
    brushed_bezier(t, (70, 15), (78, 8), (85, 0), (125, -25), w_dian)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "02_寸.png"))

    # ── Task 03 | 万 | wàn
    # heng SHORT (-130,+130) at some y, 撇 head (+50,+200) -> tail (-220,-170),
    # 横折钩 corner (+100,-20) hook to (+50,-5)
    reset_turtle(t)
    # heng — placed near top so 撇 head can be above
    brushed_bezier(t, (-130, 120), (-50, 122), (50, 122), (130, 120), w_heng)
    # 撇 — head HIGH above heng at (+50,+200), tail far lower-left (-220,-170)
    brushed_bezier(t, (50, 200), (0, 100), (-100, 0), (-220, -170), w_pie)
    # 横折钩 — start near heng's right area, go down, hook leftward
    # 折 vertical: from (+130, 120) area down to corner (+100,-20)
    brushed_bezier(t, (130, 120), (122, 80), (108, 30), (100, -20), w_shu)
    # hook (+100,-20) -> (+50,-5)
    brushed_bezier(t, (100, -20), (85, -15), (65, -8), (50, -5), w_hook_short)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "03_万.png"))

    # ── Task 04 | 公 | gōng
    # 八: 撇 (-20,+180)->(-160,0), 捺 (+20,+180)->(+170,0)
    # 厶: 横撇 (-100,-20)->(+60,-20)->(-50,-150), 点 (+60,-20)->(+110,-130)
    reset_turtle(t)
    # 八 — 撇 left
    brushed_bezier(t, (-20, 180), (-60, 130), (-110, 70), (-160, 0), w_pie)
    # 八 — 捺 right
    brushed_bezier(t, (20, 180), (60, 130), (115, 70), (170, 0), w_na)
    # 厶 — 横撇: heng segment then 撇 down-left
    brushed_bezier(t, (-100, -20), (-50, -18), (20, -18), (60, -20), w_heng)
    # 撇 from (+60,-20) down-left to (-50,-150)
    brushed_bezier(t, (60, -20), (30, -60), (-15, -110), (-50, -150), w_pie)
    # closing 点 (right side) from (+60,-20) down-right to (+110,-130)
    brushed_bezier(t, (60, -20), (75, -55), (95, -95), (110, -130), w_dian)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "04_公.png"))

    # ── Task 05 | 夫 | fū
    # upper heng very short (-80,+80) at y=+200; lower heng (-180,+180) at y=+50; gap=150
    # 人 below: 撇 from (+30,+50)->(-160,-180); 捺 from (-30,+50)->(+170,-180)
    # 竖 down through center
    reset_turtle(t)
    # upper heng short at y=+200
    brushed_bezier(t, (-80, 200), (-30, 202), (30, 202), (80, 200), w_heng)
    # lower heng long at y=+50
    brushed_bezier(t, (-180, 50), (-60, 52), (60, 52), (180, 50), w_heng)
    # 竖 through center (0,+220) -> (0,+30)
    brushed_bezier(t, (0, 220), (1, 170), (1, 90), (0, 30), w_shu)
    # 撇 lower-left from just below lower-heng center
    brushed_bezier(t, (20, 50), (-30, 0), (-100, -80), (-180, -180), w_pie)
    # 捺 lower-right
    brushed_bezier(t, (-20, 50), (30, 0), (100, -80), (180, -180), w_na)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "05_夫.png"))

    # ── Task 06 | 为 | wèi
    # top 点 belly(+30,+200) tail(+90,+150)
    # 横折钩: corner (-100,+100), heng across then down, hook
    # 撇 (-50,+80) -> (-200,-150)
    # lower-right 点 belly(+50,-100) tail(+120,-150)
    reset_turtle(t)
    # top 点 — small dian peak 14
    brushed_bezier(t, (10, 215), (20, 210), (30, 200), (90, 150), w_dian_small)
    # 横折钩 — heng from upper-left across, then折 down-right, then small hook left
    # heng segment: (-150,+100) -> (+80,+100)
    brushed_bezier(t, (-150, 100), (-80, 102), (10, 102), (80, 100), w_heng)
    # 折 down: (+80,+100) -> (+60,-80)
    brushed_bezier(t, (80, 100), (75, 50), (68, -20), (60, -80), w_shu)
    # hook (+60,-80) -> (+10,-55)
    brushed_bezier(t, (60, -80), (45, -72), (25, -62), (10, -55), w_hook_short)
    # 撇 (-50,+80) -> (-200,-150)
    brushed_bezier(t, (-50, 80), (-100, 30), (-150, -50), (-200, -150), w_pie)
    # lower-right 点
    brushed_bezier(t, (40, -85), (45, -92), (50, -100), (120, -150), w_dian)
    screen.update()
    save_canvas_to_png(screen, os.path.join(OUT_DIR, "06_为.png"))


if __name__ == "__main__":
    main()
